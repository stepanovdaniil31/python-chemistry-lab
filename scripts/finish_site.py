from pathlib import Path
from html.parser import HTMLParser
import json

root = Path('dist')
notebook = root / 'files' / '01_python_syntax.ipynb'
assert notebook.is_file(), 'The published notebook is missing'
assert (root / 'lab' / 'index.html').is_file(), 'JupyterLab was not built'
assert (root / 'api' / 'contents' / 'all.json').is_file(), 'Notebook index is missing'

(root / 'index.html').write_text('''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Python для химиков</title>
  <meta name="description" content="Учебные блокноты Python. Запуск в браузере без регистрации.">
  <script id="jupyter-config-data" type="application/json" data-jupyter-lite-root=".">{}</script>
  <meta http-equiv="refresh" content="0;url=lab/index.html?path=01_python_syntax.ipynb">
  <script>location.replace("lab/index.html?path=01_python_syntax.ipynb");</script>
</head>
<body><main><h1>Python для химиков</h1><p><a href="lab/index.html?path=01_python_syntax.ipynb">Открыть блокноты</a></p></main></body>
</html>
''', encoding='utf-8')
(root / '.nojekyll').touch()


class PageConfigParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_config = False
        self.config = ''
        self.found = False

    def handle_starttag(self, tag, attrs):
        if tag == 'script' and dict(attrs).get('id') == 'jupyter-config-data':
            self.in_config = True
            self.found = True

    def handle_data(self, data):
        if self.in_config:
            self.config += data

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_config = False


# JupyterLite fetches the parent index.html and reads this JSON during startup.
for page in (root / 'index.html', root / 'lab' / 'index.html'):
    parser = PageConfigParser()
    parser.feed(page.read_text(encoding='utf-8'))
    assert parser.found, f'JupyterLite configuration block is missing: {page}'
    assert isinstance(json.loads(parser.config), dict), f'Invalid page config: {page}'

print('Site entrypoint and notebook index verified')
