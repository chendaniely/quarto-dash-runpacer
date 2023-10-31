@all: all
all:
	echo "hello"

@PHONY: render
render:
	quarto render run_pacer.qmd

@PHONY: preview
preview:
	quarto preview run_pacer.qmd

@PHONY: shiny
shiny:
	make render
	shiny run run_pacer-app.py

@PHONY: deploy_setup
deploy_setup:
	rsconnect add \
		--server https://colorado.posit.co/rsc/ \
		--name colorado \
		--api-key ${CONNECT_API_KEY}

@PHONY: deploy
deploy:
	quarto
	rsconnect deploy shiny . --entrypoint run_pacer-app:app

@PHONY: setup
setup:
	rm -rf venv .venv
	python -m venv venv
	source activate venv/bin/activate

	pip install --upgrade pip wheel
	pip uninstall -y shiny htmltools
	pip install shiny==0.6.0 htmltools==0.4.1

	pip install jupyter pandas pytest seaborn

	pip install shinylive
	pip install rsconnect-python
