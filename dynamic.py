"""
Created by Adrian Kostoski on 14/08/2020

Python script that strips unnecessary files from a ReactJs production build APP and
renames random generated names of static files to more Dynamics friendly filenames,
ready to be uploaded as Dynamics 365 web resources.

REQUIREMENTS:
    - Python 3.8+

USAGE:
    - build your react app with "npm run build"
    - place "dynamic.py" in the same directory as the "build" directory.
    - run "dynamic.py" by locating the dynamic.py directory in cmd
    - run command: "python dynamic.py".

NOTES:
    - the index.html should remain as index.html before running dynamic.py, you can rename it afterwards
    - the unnecessary files will be stored in the extras directory
    - all remaining files in the build directory should be uploaded to Dynamics as web resources
    - web resource example url: "/WebResources/<SOLUTION_NAME>_react/static/js/2.chunk.js"
    - web resource example url: "/WebResources/<SOLUTION_NAME>_react/index.html"
"""

import os
import shutil
import pathlib
from pathlib import Path

BUILD_FOLDER_NAME = 'build'
EXTRAS_FOLDER_NAME = 'extras'
ROOT_PATH = pathlib.Path(__file__).parent.absolute()
BUILD_PATH = f'{ROOT_PATH}\\{BUILD_FOLDER_NAME}'
EXTRAS_PATH = f'{ROOT_PATH}\\{EXTRAS_FOLDER_NAME}'
EXTRAS = ['favicon', 'logo', 'manifest', 'robots', 'service-worker', 'runtime-main', '.map', '.txt']


def move_extras():
    if not os.path.isfile(EXTRAS_PATH):
        Path(EXTRAS_PATH).mkdir(parents=True, exist_ok=True)

    for path, subdir, files in os.walk(BUILD_PATH):
        for file in files:
            for extra in EXTRAS:
                if extra in file:
                    try:
                        shutil.move(f'{path}\\{file}', f'{EXTRAS_PATH}\\{file}')
                    except FileNotFoundError:
                        continue


def rename_generated_codes():
    to_replace = []
    for path, subdir, files in os.walk(BUILD_PATH):
        for file in files:
            if file.endswith('.css') or file.endswith('.js'):
                renamed = file.split('.')
                to_replace.append(renamed.pop(1))
                renamed = '.'.join(renamed)
                try:
                    os.rename(f'{path}\\{file}', f'{path}\\{renamed}')
                except FileExistsError:
                    pass

    edit_index(to_replace)


def edit_index(to_replace):
    with open(f'{BUILD_PATH}\\index.html', 'r') as index_html:
        code = index_html.read()
        for replace in to_replace:
            code = code.replace(f'.{replace}', '')
    index_html.close()

    with open(f'{BUILD_PATH}\\index.html', 'w') as index_html:
        index_html.write(code)


if __name__ == '__main__':
    move_extras()
    rename_generated_codes()
    print('Converting completed!')
