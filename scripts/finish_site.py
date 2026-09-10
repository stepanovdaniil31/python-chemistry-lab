from pathlib import Path
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
  <meta http-equiv="refresh" content="0;url=lab/index.html?path=01_python_syntax.ipynb">
  <script>location.replace("lab/index.html?path=01_python_syntax.ipynb");</script>
</head>
<body><main><h1>Python для химиков</h1><p><a href="lab/index.html?path=01_python_syntax.ipynb">Открыть блокноты</a></p></main></body>
</html>
''', encoding='utf-8')
(root / '.nojekyll').touch()
print('Site entrypoint and notebook index verified')
