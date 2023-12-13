.PHONY: book_venv book clean

SHELL := /bin/bash

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
