# DISC Unconference 2023 - Project outputs
A collection of outputs from the projects created at the DISC Unconference 2023.

## How to build and visualize these documents

This repository sets up a [JupyterBook](https://jupyterbook.org/en/stable/start/your-first-book.html). All content is markdown files stored in the `unconference` folder.

To add a new project page:

1. Add your markdown file to the `unconference` folder;
2. Add the name of your markdown file to the `_toc.yml` file, under the `chapters` heading.
3. Submit a pull request to this repo. Make sure to add your collaborators as co-authors on the pull request.

### Building locally

To build the book locally, you need to have [JupyterBook installed](https://jupyterbook.org/en/stable/install.html). You can use either `pip` or `conda` to install this and other requirements for your book by running

```bash
pip install -r requirements.txt
```

or

```bash
conda create -f environment.yml
conda activate projects
```

Then, run

```bash
jupyter-book build unconference
```

to build the book. You can then open the generated `unconference/_build/html/index.html` file in your browser to view the book.

### GitHub pages

This repository comes with a [pre-defined GitHub pages setup](https://github.com/melissawm/disc-unconference-project/blob/main/.github/workflows/pages.yml).

You can then access this site at `https://numfocus.github.io/disc-unconference-2023-projects/`.

## Contributing to this repository

If you find typos, incomplete or misleading instructions, or have suggestions for improvements to this template, open an issue at the [numfocus/disc-unconference-2023-projects](https://github.com/numfocus/disc-unconference-2023-projects) repo.
