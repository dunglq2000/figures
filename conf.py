project = 'TikZ for mathematician and cryptographers'
copyright = '2025, dunglq'
author = 'Lê Quốc Dũng'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_togglebutton', 
    'sphinx_design', 
    'sphinx_book_theme', 
    'sphinx_proof', 
    'sphinxcontrib.bibtex', 
]

proof_minimal_theme = True

bibtex_bibfiles = ["myrefs.bib"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_logo = "Euler_Stamp.jpg"
html_title = "Math Book"

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['mystyles.css']

only_build_toc_files = True

mathjax3_config = {                  
    "tex": {                        
        "macros": {                     
            "bm": ['{\\boldsymbol{#1}}',1] 
            }                       
        }                           
    }

numfig_format = {
    "figure": 'Hình %s',
    "table": 'Bảng %s'
}

numfig = True
pygments_style = "default"

def setup(app):
    # Remove the index node from the doctree before LaTeX processes it
    from sphinx.writers.latex import LaTeXTranslator
    LaTeXTranslator.visit_index = lambda self, node: None  # Skip index nodes

latex_engine = 'lualatex'
latex_elements = {
    'passoptionstopackages': r'''
\PassOptionsToPackage{svgnames}{xcolor}
''',
    'fontpkg': r'''
\setmainfont{CMU Serif}
\setsansfont{CMU Sans Serif}
''',
    'preamble': r'''
\usepackage[titles]{tocloft}
\usepackage{amsmath, amsfonts, amssymb}
\usepackage{bm}
\usepackage{cancel}
\usepackage{float}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
''',
    'sphinxsetup': 'TitleColor=DarkGoldenrod',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'makeindex': '',
    'printindex': '',
    'figure_align': r'H',
}

