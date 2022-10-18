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
    'rb': 'Ruby Language',
}

LANGUAGES_EXTENSIONS = {
    '.bash': 'bash',
    '.c': 'c',
    '.cpp': 'cpp',
    '.csharp': 'c#',
    '.css': 'css',
    '.go': 'go',
    '.html': 'html',
    '.java': 'java',
    '.js': 'javascript',
    '.json': 'json',
    '.lua': 'lua',
    '.md': 'markdown',
    '.php': 'php',
    '.txt': 'plaintext',
    '':'plaintext',
    '.py': 'python',
    '.rb': 'ruby',
}

THEMES = {
    'default': 'Default Light',
    'dark': 'Default Dark',
    'atom-one-light': 'Atom One Light',
    'atom-one-dark': 'Atom One Dark',
    'github': 'Github Light',
    'github-dark': 'Github Dark',
}

EXPIRY_TIME = {
    '1d': '1 Day',
    '1w': '1 Week',
    '1m': '1 Month',
}

# Hint for using the available languages
LANGUAGES_HINT = f'''snippet language (available languages:
{", ".join(LANGUAGES.keys())})
'''

# Hint for using the available themes
THEMES_HINT = f'''theme (available themes:
{", ".join(THEMES.keys())})
'''

# Hint for using the available expiry times
EXPIRY_TIME_HINT = f'''expiry time (available expiry times:
{", ".join(EXPIRY_TIME.keys())}) (default: 1w/1week)
'''

# Actual service information

PASTEME_SERVICE_URL = 'https://pasteme.pythonanywhere.com'

# Traceback messages

CONNECTION_ISSUE_HINT = 'Check your network connection. Make sure the PasteMe service is up and running.'

# Information

EPILOG_DESCRIPTION = '''Author -> Sadra Yahyapour (mailto:lnxpylnxpy@gmail.com)
GitHub -> https://github.com/collove/pasteme-cli'''
