.PHONY: dev lint serve

dev:
	python3 -m http.server 8000 --bind 127.0.0.1

lint:
	npx html-validate index.html || true

serve:
	python3 -m http.server 8000
