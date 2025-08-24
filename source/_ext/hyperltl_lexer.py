from pygments.lexer import RegexLexer, words
from pygments.token import *

class HyperLTLLexer(RegexLexer):
    """
    Pygments lexer for HyperLTL
    """

    name = 'HyperLTL'
    aliases = ['hyperltl', 'hltl', 'hq']
    filenames = ['*.hltl', '*.hyperltl']
    mimetypes = ['text/x-hyperltl']

    tokens = {
        'root': [
            # Whitespace
            (r'\s+', Text),

            # Path quantifiers (highest precedence keywords)
            (words(('Forall', 'Exists'), suffix=r'\b'), Keyword.Reserved),

            # Trace quantifiers
            (words(('A', 'E'), suffix=r'\b'), Keyword.Type),

            # Temporal operators
            (words(('G', 'F', 'X', 'U', 'R'), suffix=r'\b'), Operator.Word),

            # Boolean constants
            (words(('TRUE', 'FALSE'), suffix=r'\b'), Keyword.Constant),

            # Logical operators
            (r'->', Operator),           # Implication
            (r'=', Operator),            # Equivalence
            (r'&', Operator),            # Conjunction
            (r'\|', Operator),           # Disjunction
            (r'~', Operator),            # Negation

            # Punctuation
            (r'\.', Punctuation),        # Dot after quantifiers
            (r'\[', Punctuation),        # Opening bracket
            (r'\]', Punctuation),        # Closing bracket
            (r'\(', Punctuation),        # Opening parenthesis
            (r'\)', Punctuation),        # Closing parenthesis

            # Numbers
            (r'\d+', Number.Integer),

            # Identifiers (trace variables, propositions)
            (r'[a-zA-Z][a-zA-Z0-9_.]*', Name.Variable),

            # Any other character (fallback)
            (r'.', Text),
        ],
    }

    def analyse_text(text):
        """
        Analyse text to see if it looks like HyperLTL.
        Return a score between 0.0 and 1.0.
        """
        score = 0.0

        if 'Forall' in text or 'Exists' in text:
            score += 0.3

        if any(pattern in text for pattern in ['Forall ', 'Exists ', 'A ', 'E ']):
            if '.' in text:
                score += 0.2

        temporal_ops = ['G', 'F', 'X', 'U', 'R']
        if any(op in text for op in temporal_ops):
            score += 0.1

        if '][' in text:
            score += 0.2

        logical_ops = ['->', '&', '|', '~', '=']
        if any(op in text for op in logical_ops):
            score += 0.1

        return min(score, 1.0)