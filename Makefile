.PHONY: venv book_venv book

SHELL := /bin/bash

CONDA_DIR := /opt/conda
BOOK_VENV := CEG8719

venv:
	@echo "Creating .venv"
	set -e; \
	python -m venv .venv; \
	source .venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements_dev.txt;

book_venv:
	@echo "Creating Mamba environment $(BOOK_VENV)"
	set -e; \
	$(CONDA_DIR)/bin/mamba create -n $(BOOK_VENV) python=3.9 -y; \
	echo "Mamba environment $(BOOK_VENV) created."

book:
	@echo "Building book"
	set -e; \
	source $(CONDA_DIR)/bin/activate $(BOOK_VENV); \
	pip install -r requirements_book.txt; \
	jupyter-book build .; \
	cd _build/html && python -m http.server 8000
