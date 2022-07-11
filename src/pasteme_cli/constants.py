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

LANGUAGES_HINT = f'''snippet language (available languages:
{", ".join([l for l in LANGUAGES.keys()])})
'''

PASTEME_SERVICE_URL = 'https://pasteme.pythonanywhere.com'

PASTEME_API_URL = 'http://localhost:8000/api/v1/paste/'

CONNECTION_ISSUE_HINT = f'Check your network connection. Make sure the PasteMe service ({PASTEME_SERVICE_URL}) is up and running.'

JSON_TEMPLATE = '''~~ {} ~~
{}
'''

EPILOG_DESCRIPTION = '''Author -> Sadra Yahyapour (mailto:lnxpylnxpy@gmail.com)
GitHub -> https://github.com/collove/pasteme-cli'''