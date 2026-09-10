from pathlib import Path
import contextlib
import io
import nbformat

for path in sorted(Path('content').glob('*.ipynb')):
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    namespace = {'input': lambda prompt='': '23.5'}
    count = 0
    for cell in notebook.cells:
        if cell.cell_type == 'code':
            with contextlib.redirect_stdout(io.StringIO()):
                exec(compile(cell.source, f'{path.name}:{cell.id}', 'exec'), namespace)
            count += 1
    print(f'{path.name}: {count} code cells passed')
