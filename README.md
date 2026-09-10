# Python для химиков

JupyterLite с учебными блокнотами. Python работает в браузере; студентам не нужны аккаунты.

**Сайт:** https://stepanovdaniil31.github.io/python-chemistry-lab/

## Материалы

- `content/00_python_syntax.ipynb` — основной синтаксис Python: переменные, типы, ветвления, коллекции, циклы и функции.
- `content/01_kalkulyator.ipynb` — вычисления и переменные.
- `content/02_stroki_vyvod.ipynb` — строки, ввод и вывод.
- `content/03_usloviya.ipynb` — условия.
- `content/04_cikly.ipynb` — циклы.
- `content/05_spiski.ipynb` — списки.
- `content/06_slovari.ipynb` — словари.
- `content/07_funkcii.ipynb` — функции.
- `content/08_faily.ipynb` — файлы.
- `content/09_oshibki_parser.ipynb` — ошибки и разбор формул.
- `content/10_numpy.ipynb` — NumPy.
- `content/11_matplotlib.ipynb` — Matplotlib.
- `content/12_pandas.ipynb` — pandas.
- `content/13_statistika.ipynb` — статистика.
- `content/14_chislennye_metody.ipynb` — численные методы.
- `content/15_miniproekt_kinetika.ipynb` — мини-проект по кинетике.

При сборке проверяется формат всех блокнотов. Демонстрационный блокнот `00` дополнительно выполняется целиком; практические задания `01`–`15` содержат заготовки решений и намеренные ошибки, поэтому автоматически не выполняются.

## Обновление материалов

Добавьте или замените `.ipynb` в папке `content` и сохраните изменения в ветке `main`. GitHub Actions автоматически пересоберёт и опубликует сайт. Новый блокнот появится в файловой панели.

Если нужно изменить блокнот, открывающийся при входе, измените путь в `scripts/finish_site.py`.

## Сохранение и сдача работ

Изменения пользователя сохраняются в хранилище его браузера. Скачивайте готовую работу через контекстное меню файла: **Download / Скачать**. Автоматического сбора работ и общей редактируемой копии нет.

Локальная изменённая копия имеет приоритет над опубликованным оригиналом. Для новой редакции занятия удобно давать файлу новое имя, чтобы не подменять студенческую работу.

## Локальная сборка

```sh
python -m venv .venv
# Активируйте виртуальное окружение.
python -m pip install -r requirements.txt
python scripts/check_notebooks.py
jupyter lite build --contents content --output-dir dist
python scripts/finish_site.py
python -m http.server 8000 --directory dist
```

При первом открытии требуется интернет для загрузки Python/Pyodide и компонентов среды. Установка библиотек внутри ноутбука не требуется.

Основа сайта: [JupyterLite](https://jupyterlite.readthedocs.io/).
