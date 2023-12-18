.PHONY: dev_venv book_venv book clean

SHELL := /bin/bash

venv:
	@echo "Creating .venv"
	set -e; \
	python -m venv .venv; \
	source .venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements_dev.txt;

book_venv:
	@echo "Creating book venv"
	set -e; \
	python -m venv .book_venv; \
	source .book_venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements_book.txt;

book:
	source .book_venv/bin/activate; \
	jupyter-book build .

clean:
	rm -rf .book_venv;
	rm -rf .venv;
