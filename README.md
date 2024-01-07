# CEG8719: Geospatial Data, Analytics and AI

Welcome to the repository for my coursework submission for CEG8719. This project focuses on the acquisition and pre-processing of a geospatial dataset but also serves and will be actively used as the development environment for collection and integration (initially local files but finally a cloud postgres database) for all open-source datasets used through to the completion of my final MRes research paper in Summer 2024.

## Getting Started

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new/cdrowley/CEG8719?quickstart=1)

Click the button above to open a new GitHub Codespace for this repository. This will create a new Codespace with all the required dependencies installed and ready to go.

You can then start working on the project using the provided make commands in a terminal to either:

- **Making Book Changes**:
	- Following any changes, to rebuild the book use `make book`.

- **Add New Data Collection Notebooks**:
	- To alter or add new collection notebooks, follow these steps:
	- Add any new required packages to `requirements_dev.txt`.
	- Create dev virtual environment using `make venv`.
	- Modify or add a new notebook in the `data_collection/` directory.
	- Save any collected data in `data/<source>/...`.

**Makefile Commands**:
The Makefile provides the following commands that you can execute:

- `venv`: Creates a virtual environment for development notebooks.
- `book`: Builds the Jupyter book for the project (using the `book_venv` environment).
- `book_venv`: Used by `book` to creates a Mamba environment for the book (if not already created).
- `clean`: Removes the `.venv` dev and `book_venv` book environments as well as the `book/_build` directory.


## Acknowledgements

The book/site was created using a [cookiecutter-jupyter-book template](https://github.com/giswqs/cookiecutter-jupyter-book) from [Qiusheng Wu](https://scholar.google.com/citations?user=vmml4_0AAAAJ), which itself builds on the open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).
