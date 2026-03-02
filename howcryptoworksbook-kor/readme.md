# 암호화폐가 실제로 작동하는 방식: 누락된 매뉴얼

**현재 상태:** 초판 이전 - 공식 초판이 무료 전자책으로 출판되기 전에 커뮤니티 피드백을 위해 열려 있습니다.

**저자:** Larry Cermak ([@lawmaster](https://x.com/lawmaster))

**공동 저자:** Igor Igamberdiev(Wintermute), Bohdan Pavlov(Wintermute)

**검토자:** Wintermute Research, The Block Research

**편집자:** 팀 코플랜드

---

## 이 책에 대하여

*암호화 실제 작동 원리*는 비트코인의 UTXO 모델부터 양자 저항 암호화에 이르기까지 암호화폐가 실제로 어떻게 작동하는지 설명하는 포괄적인 기술 서적입니다. 이 책은 15개 장과 서문에 걸쳐 90,000개 이상의 단어로 구성되어 있으며 암호화폐 생태계의 기본 개념부터 새로운 개발까지 모든 것을 다루고 있습니다.

이 저장소에는 오픈 소스이며 무료로 읽고, 다운로드하고, 공유할 수 있는 책의 전체 텍스트가 포함되어 있습니다. 이 버전은 커뮤니티로부터 피드백을 수집하기 위해 GitHub에 게시되었습니다. 최고의 편집 및 수정 사항은 공식 초판에 통합될 예정이며, 이 초판은 앞으로 몇 달 내에 Amazon 및 기타 플랫폼에서 **무료 전자책**으로 출시될 예정입니다.

최종 버전을 만드는 데 도움을 주고 싶다면 지금이 바로 그때입니다. 아래 [기여](#contributing)를 참조하세요.

## 이 책이 존재하는 이유

후보자들에게 암호화폐 분야의 탄탄한 기반을 제공할 수 있는 단일 리소스를 추천하려고 했을 때 부족함이 있었습니다. 일부 책에서는 하나의 프로토콜만 깊이 다루고 나머지는 무시합니다. YouTube와 X에는 얇게 위장된 광고가 넘쳐납니다. 최고의 연구 결과는 수십 개의 페이월 사이트에 분산되어 있습니다. 학술 논문은 엄격하지만 실제 학습을 하기에는 너무 추상적입니다.

모든 것이 뭔가 부족했습니다. 너무 좁고, 너무 편향되어 있고, 너무 진보하고, 너무 단편적이거나, 가이드 없이는 접근하기가 너무 어렵습니다.

이 책은 그 문제를 해결하려는 나의 시도이다.

## 무엇이 다른가

- **포괄적인 범위:** 비트코인, 이더리움, 솔라나, DeFi, MEV, 스테이블코인, 보관, 시장 구조, 거버넌스, NFT, DePIN, 양자 저항 등을 다루는 15개 장
- **최신 정보:** 암호화폐는 빠르게 움직이며 대부분의 책은 출시되기 전에 오래된 것입니다. 이는 현재 데이터, 프로토콜 및 시장 현실을 바탕으로 적극적으로 유지 관리됩니다.
- **구조화된 학습:** 각 장은 마지막 장을 기반으로 구성되어 점차 복잡성이 증가하는 일관된 스토리를 만듭니다.
- **전문가 검토:** 각 장은 해당 특정 분야에 깊이 관여하는 사람이 검토했습니다.
- **정직한 평가:** 기술적 아이디어를 얕보지 않고 명확하게 설명하고 장점과 한계를 모두 논의합니다.
- **오픈 소스:** 책 전체를 무료로 읽고 공유할 수 있습니다. 기본 교육이 유료화 장벽 뒤에 갇혀 있어서는 안 됩니다.

## 이 책은 누구를 위한 것인가

이 책은 거래자나 투자자뿐만 아니라 기술이 실제로 어떻게 작동하는지 이해하고 싶은 사람들을 위해 쓰여졌습니다. 이는 귀하가 지적 호기심이 있다고 가정하지만 사전 전문 지식을 가정하지는 않습니다.

이 내용을 주의 깊게 읽고 핵심 아이디어를 흡수한다면 오늘날 암호화폐 업계에서 풀타임으로 일하는 대부분의 사람들보다 더 많은 것을 알게 될 것입니다.

## 장

| # | 장 |
|---|---------|
| - | [서문: 이것이 중요한 이유](Chapters/_preface.md) |
| 1 | [비트코인 종합 소개](Chapters/ch01_bitcoin.md) |
| 2 | [이더리움 생태계](Chapters/ch02_ethereum.md) |
| 3 | [솔라나 생태계](Chapters/ch03_solana.md) |
| 4 | [L1 블록체인](Chapters/ch04_l1_blockchains.md) |
| 5 | [보관 기본 사항](Chapters/ch05_custody.md) |
| 6 | [암호화폐 시장 구조 및 거래](Chapters/ch06_market_structure.md) |
| 7 | [디파이](Chapters/ch07_defi.md) |
| 8 | [MEV](Chapters/ch08_mev.md) |
| 9 | [스테이블코인 및 RWA](Chapters/ch09_stablecoins_rwas.md) |
| 10 | [하이퍼액체](Chapters/ch10_hyperliquid.md) |
| 11 | [대체 불가능한 토큰(NFT)](Chapters/ch11_nfts.md) |
| 12 | [거버넌스 및 토큰 경제학](Chapters/ch12_governance.md) |
| 13 | [DePIN](Chapters/ch13_depin.md) |
| 14 | [양자저항](Chapters/ch14_quantum_resistance.md) |
| 15 | [예측시장](Chapters/ch15_prediction_markets.md) |

[머리말](Chapters/_preface.md)부터 시작하거나, 전체 섹션별 분석을 보려면 [목차](table_of_contents.md)를 참조하세요.

## 기여

이것은 **사전 초판** 릴리스입니다. 우리는 공식 초판이 나오기 전에 콘텐츠를 다듬는 데 도움을 줄 전문 리뷰어와 기여자를 적극적으로 찾고 있습니다.

이 책에 기여하려면 [CONTRIBUTING.md](CONTRIBUTING.md)를 참조하세요. 모든 기여는 귀하의 독창적인 작품이어야 하며 CC-BY 라이선스에 따라 기여되어야 합니다.

오류를 발견했거나 의견이 있거나 개선에 기여하고 싶은 경우:

- **사소한 수정 사항이 있는 경우:** 수정 사항이 포함된 풀 요청을 제출하세요.
- **대규모 변경이나 새로운 자료의 경우:** 먼저 작성자와 협의하세요.
- **질문이나 토론:** 이슈 열기

풀 요청을 제출할 때 각 변경 사항에 대해 별도의 커밋을 사용하면 검토가 더 쉬워집니다. 향후 버전에서는 중요한 기여자가 인정될 것입니다.

---

## 특허

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a>

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. Individual contributions are licensed under CC-BY; the compiled book is published under CC-BY-NC-ND.

The decision to make this book freely available is both practical and philosophical: traditional publishing can't keep pace with crypto's evolution, and basic education shouldn't be locked behind paywalls.
