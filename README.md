python -m venv venv
source activate venv/bin/activate

pip install --upgrade pip wheel

pip uninstall -y shiny htmltools
pip install shiny==0.6.0 htmltools==0.4.1

pip install jupyter pandas pytest seaborn


quarto render run_pacer.qmd
shiny run run_pacer-app.py

quarto preview run_pacer.qmd
