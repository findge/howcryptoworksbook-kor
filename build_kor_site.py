from __future__ import annotations

import datetime as dt
import html
import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

import markdown

SOURCE_ROOT = Path("howcryptoworksbook-kor")
OUTPUT_ROOT = Path("howcryptoworksbook-kor-site")


@dataclass
class Doc:
    source_rel: str
    output_name: str
    group: str
    title: str


def normalize_posix_path(base_dir: str, raw_target: str) -> str:
    target_path = PurePosixPath(base_dir).joinpath(raw_target)
    parts: list[str] = []
    for part in target_path.parts:
        if part in ("", "."):
            continue
        if part == "..":
            if parts:
                parts.pop()
            continue
        parts.append(part)
    return "/".join(parts)


def read_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def first_heading(markdown_text: str, fallback: str) -> str:
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return fallback


def parse_chapter_number(filename: str) -> int:
    match = re.match(r"ch(\d+)_", filename)
    if not match:
        return 0
    return int(match.group(1))


def chapter_group(number: int) -> str:
    if 1 <= number <= 5:
        return "Section I. 기초와 인프라"
    if 6 <= number <= 10:
        return "Section II. 시장과 응용"
    return "Section III. 제도와 미래"


def build_docs() -> list[Doc]:
    docs: list[Doc] = []

    seed_docs = [
        ("readme.md", "index.html", "시작하기"),
        ("table_of_contents.md", "table-of-contents.html", "시작하기"),
        ("Chapters/_preface.md", "preface.html", "시작하기"),
    ]

    for rel, output_name, group in seed_docs:
        text = read_markdown(SOURCE_ROOT / rel)
        fallback = Path(rel).stem.replace("_", " ").title()
        docs.append(
            Doc(
                source_rel=rel,
                output_name=output_name,
                group=group,
                title=first_heading(text, fallback),
            )
        )

    chapter_files = sorted((SOURCE_ROOT / "Chapters").glob("ch*.md"), key=lambda p: p.name)
    for path in chapter_files:
        rel = path.relative_to(SOURCE_ROOT).as_posix()
        number = parse_chapter_number(path.name)
        text = read_markdown(path)
        docs.append(
            Doc(
                source_rel=rel,
                output_name=f"{path.stem.replace('_', '-')}.html",
                group=chapter_group(number),
                title=first_heading(text, path.stem),
            )
        )

    contrib_text = read_markdown(SOURCE_ROOT / "CONTRIBUTING.md")
    docs.append(
        Doc(
            source_rel="CONTRIBUTING.md",
            output_name="contributing.html",
            group="부록",
            title=first_heading(contrib_text, "Contributing"),
        )
    )

    return docs


def rewrite_md_links(markdown_text: str, current_rel: str, source_to_output: dict[str, str]) -> str:
    current_dir = str(PurePosixPath(current_rel).parent)

    pattern = re.compile(r"\]\(([^)]+)\)")

    def repl(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        if not target:
            return match.group(0)
        if target.startswith(("http://", "https://", "mailto:", "tel:", "#")):
            return match.group(0)

        path_part, hash_sep, fragment = target.partition("#")
        if not path_part.lower().endswith(".md"):
            return match.group(0)

        normalized = normalize_posix_path(current_dir, path_part)
        mapped = source_to_output.get(normalized)
        if not mapped:
            return match.group(0)

        if hash_sep:
            return f"]({mapped}#{fragment})"
        return f"]({mapped})"

    return pattern.sub(repl, markdown_text)


def group_docs(docs: list[Doc]) -> list[tuple[str, list[Doc]]]:
    grouped: list[tuple[str, list[Doc]]] = []
    seen: dict[str, list[Doc]] = {}
    for doc in docs:
        if doc.group not in seen:
            seen[doc.group] = []
            grouped.append((doc.group, seen[doc.group]))
        seen[doc.group].append(doc)
    return grouped


def build_sidebar(grouped_docs: list[tuple[str, list[Doc]]], active_output: str) -> str:
    chunks: list[str] = []
    for group_name, group_items in grouped_docs:
        chunks.append('<section class="nav-group">')
        chunks.append(f'<h3 class="nav-group-title">{html.escape(group_name)}</h3>')
        chunks.append('<ul class="nav-list">')
        for item in group_items:
            active = " active" if item.output_name == active_output else ""
            title = html.escape(item.title)
            chunks.append(
                f'<li><a class="nav-link{active}" data-title="{title}" href="{item.output_name}">{title}</a></li>'
            )
        chunks.append("</ul>")
        chunks.append("</section>")
    return "\n".join(chunks)


def build_page_jump(label: str, doc: Doc | None, cls: str) -> str:
    if doc is None:
        return '<span class="page-jump" aria-hidden="true"></span>'
    return (
        f'<a class="page-jump {cls}" href="{doc.output_name}">'  # noqa: E501
        f'<span class="jump-kicker">{label}</span>'
        f'<span class="jump-title">{html.escape(doc.title)}</span>'
        "</a>"
    )


def render_template(
    doc: Doc,
    body_html: str,
    sidebar_html: str,
    prev_doc: Doc | None,
    next_doc: Doc | None,
    updated_text: str,
) -> str:
    escaped_title = html.escape(doc.title)
    escaped_group = html.escape(doc.group)
    prev_html = build_page_jump("이전", prev_doc, "prev")
    next_html = build_page_jump("다음", next_doc, "next")

    return f"""<!doctype html>
<html lang=\"ko\">
  <head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>{escaped_title} | How Crypto Worksbook KOR</title>
    <meta name=\"description\" content=\"How Crypto Worksbook 한국어판 읽기 사이트\" />
    <link rel=\"stylesheet\" href=\"assets/styles.css\" />
    <script defer src=\"assets/app.js\"></script>
  </head>
  <body>
    <div class=\"page-progress\"><span></span></div>

    <header class=\"topbar\">
      <button class=\"menu-toggle\" type=\"button\" aria-expanded=\"false\" aria-controls=\"sidebar\">목차</button>
      <a class=\"brand\" href=\"index.html\">
        <span class=\"brand-mark\" aria-hidden=\"true\"></span>
        <span class=\"brand-text\">
          <span class=\"brand-title\">How Crypto Worksbook</span>
          <span class=\"brand-sub\">한국어 백과사전</span>
        </span>
      </a>
      <div class=\"top-actions\">
        <input id=\"navSearch\" class=\"nav-search\" type=\"search\" placeholder=\"목차 검색\" aria-label=\"목차 검색\" />
      </div>
    </header>

    <div class=\"layout\">
      <aside id=\"sidebar\" class=\"sidebar\">
        <div class=\"sidebar-header\">
          <div class=\"sidebar-kicker\">Contents Architecture</div>
          <div class=\"sidebar-note\">원본 문서 구조를 그대로 유지해 탐색할 수 있도록 구성했습니다.</div>
        </div>
        {sidebar_html}
      </aside>

      <main class=\"content-wrap\">
        <article class=\"article\">
          <div class=\"article-meta\">
            <span class=\"meta-tag\">{escaped_group}</span>
            <span class=\"meta-updated\">갱신: {updated_text}</span>
          </div>

          <div class=\"article-body\">
            {body_html}
          </div>

          <footer class=\"article-footer\">
            {prev_html}
            {next_html}
          </footer>
        </article>
      </main>
    </div>
  </body>
</html>
"""


def main() -> None:
    if not SOURCE_ROOT.exists():
        raise SystemExit(f"source folder not found: {SOURCE_ROOT}")

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    docs = build_docs()
    source_to_output = {doc.source_rel: doc.output_name for doc in docs}
    grouped = group_docs(docs)

    for idx, doc in enumerate(docs):
        src_path = SOURCE_ROOT / doc.source_rel
        markdown_text = read_markdown(src_path)
        markdown_text = rewrite_md_links(markdown_text, doc.source_rel, source_to_output)

        md_engine = markdown.Markdown(
            extensions=["extra", "fenced_code", "tables", "sane_lists", "toc"],
            output_format="html5",
        )
        body_html = md_engine.convert(markdown_text)

        sidebar_html = build_sidebar(grouped, doc.output_name)

        prev_doc = docs[idx - 1] if idx > 0 else None
        next_doc = docs[idx + 1] if idx < len(docs) - 1 else None

        updated_at = dt.datetime.fromtimestamp(src_path.stat().st_mtime)
        updated_text = updated_at.strftime("%Y-%m-%d")

        page_html = render_template(
            doc=doc,
            body_html=body_html,
            sidebar_html=sidebar_html,
            prev_doc=prev_doc,
            next_doc=next_doc,
            updated_text=updated_text,
        )

        (OUTPUT_ROOT / doc.output_name).write_text(page_html, encoding="utf-8", newline="")
        print(f"built: {doc.output_name}")

    print(f"done: {len(docs)} pages -> {OUTPUT_ROOT}")


if __name__ == "__main__":
    main()
