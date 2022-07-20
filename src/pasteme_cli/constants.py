# Language choices

LANGUAGES = {
    'bash': 'Command Language',
    'c': 'C Language',
    'cpp': 'C++ Language',
    'csharp': 'C# Language',
    'css': 'CSS Style Sheet Language',
    'go': 'Go Language',
    'html': 'HTML Language',
    'java': 'Java Language',
    'js': 'JavaScript Language',
    'json': 'JSON Data Format',
    'lua': 'Lua Language',
    'md': 'MarkDown Language',
    'php': 'PHP Language',
    'plaintext': 'PlainText',
    'python': 'Python Language',
    'rb': 'Ruby Language'
}

THEMES = {
    'default': 'Default Light',
    'dark': 'Default Dark',
    'atom-one-light': 'Atom One Light',
    'atom-one-dark': 'Atom One Dark',
    'github': 'Github Light',
    'github-dark': 'Github Dark',
}

# Hint for using the available languages

LANGUAGES_HINT = f'''snippet language (available languages:
{", ".join([_ for _ in LANGUAGES.keys()])})
'''

# Hint for using the available themes

THEMES_HINT = f'''theme (available themes:
{", ".join([_ for _ in THEMES.keys()])})
'''

# Actual service information

PASTEME_SERVICE_URL = 'https://pasteme.pythonanywhere.com'

PASTEME_API_URL = 'https://pasteme.pythonanywhere.com/api/v1/paste/'

# Traceback messages

CONNECTION_ISSUE_HINT = 'Check your network connection. Make sure the PasteMe service is up and running.'

# Information

EPILOG_DESCRIPTION = '''Author -> Sadra Yahyapour (mailto:lnxpylnxpy@gmail.com)
GitHub -> https://github.com/collove/pasteme-cli'''