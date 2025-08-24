"""
Sphinx extension to add HyperLTL syntax highlighting support.
"""

def setup(app):
    """Register HyperLTL lexer with Sphinx"""

    try:
        from .hyperltl_lexer import HyperLTLLexer
    except ImportError:
        from hyperltl_lexer import HyperLTLLexer

    from sphinx.highlighting import lexers

    # Register under multiple aliases
    lexers['hyperltl'] = HyperLTLLexer()
    lexers['hltl'] = HyperLTLLexer()
    lexers['hq'] = HyperLTLLexer()

    from pygments.lexers import get_lexer_by_name
    import pygments.lexers

    # Add to pygments lexer registry
    pygments.lexers.LEXERS['HyperLTLLexer'] = (
        'hyperltl_lexer', 'HyperLTL', ('hyperltl', 'hltl', 'hq'),
        ('*.hltl', '*.hyperltl'), ('text/x-hyperltl',)
    )

    app.add_config_value('hyperltl_default_style', 'default', 'env')

    return {
        'version': '0.1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }