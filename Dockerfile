FROM python:3.13-slim

WORKDIR /app

# Prebuilt static website output
COPY howcryptoworksbook-kor-site/ /app/

ENV PORT=8080
EXPOSE 8080

CMD ["sh", "-c", "python -m http.server ${PORT} --bind 0.0.0.0 --directory /app"]
