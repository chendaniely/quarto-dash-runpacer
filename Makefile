@PHONY: shiny
shiny:
	make render
	shiny run run_pacer-app.py

@PHONY: render
render:
	quarto render run_pacer.qmd

@PHONY: preview
preview:
	quarto preview run_pacer.qmd --port 9099

@PHONY: deploy_setup
deploy_setup:
	rsconnect add \
		--server https://colorado.posit.co/rsc/ \
		--name colorado \
		--api-key ${CONNECT_API_KEY}

@PHONY: deploy
deploy:
	make render
	pip freeze > requirements.txt
	rsconnect deploy shiny . --entrypoint run_pacer-app:app

@PHONY: setup
setup:
	rm -rf venv .venv
	python -m venv venv
	source venv/bin/activate

@PHONY: install
install:

	pip install --upgrade pip wheel
	pip uninstall -y shiny htmltools
	pip install -y shiny==0.6.0 htmltools==0.4.1

	pip install -y jupyter pandas pytest seaborn plotnine

	pip install -y shinylive
	pip install -y rsconnect-python
