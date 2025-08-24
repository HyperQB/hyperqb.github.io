# hyperqb.github.io

This website is built using [Sphinx](https://www.sphinx-doc.org/), and uses the [Furo](https://github.com/pradyunsg/furo) theme. The content is written in reStructuredText for rich formatting capabilities including tables, code blocks, and mathematical notations.

Note: Sphinx is really finicky with indentation and spaces/newlines between blocks. If something is not being formatted right, it is very likely it has something to do with that.

## Building the Website

To build this website locally:

```bash
# Install Sphinx
pip install sphinx

# Build the HTML files
make html

# Or use sphinx-build directly
sphinx-build -b html source/ build/
```

The built website will be available in the `build/` directory and can be viewed by opening `index.html` in your browser.

Run the following for cleaning, building, and opening the home web page
```bash
 make clean && make html && open build/html/index.html
```

## Continuous Integration and Deployment

The folder `source/case-studies/benchmarks_ui/` is updated automatically when the same folder is updated in [HyperRUSTY](https://github.com/HyperQB/HyperRUSTY)

The workflow `.github/workflows/sphinx.yml` deploys the website in [https://hyperqb.github.io/](https://hyperqb.github.io/)