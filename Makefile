.PHONY: docs

black:
	black pdfneedocr tests setup.py

flake:
	flake8 pdfneedocr tests setup.py

test:
	pytest

install:
	python -m pip install -e ".[dev]"
	pre-commit install

pypi:
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*

clean:
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ .ipynb_checkpoints .pytest_cache

check: clean black flake test clean

docs:
	cp README.md docs/index.md
	python -m mkdocs serve

deploy-docs:
	cp README.md docs/index.md
	python -m mkdocs gh-deploy
