python -m venv venv
source activate venv/bin/activate

pip install --upgrade pip wheel

pip install jupyter pandas shiny
pip install git+https://github.com/posit-dev/py-shiny.git#egg=shiny
pip install pytest

quarto render run_pacer.qmd
