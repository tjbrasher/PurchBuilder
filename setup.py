import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [],
                'excludes': ['PyQt5', 'PySide2', 'tornado', 'email',
                            'NoteBook', 'pygments', 'Regex',
                            'soupsieve', 'wcwidth', 'asyncio', 'bs4',
                            'cffi', 'ctypes', 'curses', 'backcall', 
                            'colorama', 'black', 'blib2to3', 'idna',
                            'jupyter_client', 'jupyter_core', 'jupyter_pygments', 'lib2to3',
                            'markupsafe', 'matplotlib_inline', 'nbclient',
                            'nbconvert', 'nbformat', 'parso', 'sqlite3', 
                            'test', 'toml', 'traitlets', 'testpath',
                            'zmq' 'pytz'],
                'include_files':[('Files', 'Files')]}

base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('purchGUI.py', base=base, target_name = 'purchListCreator',
    icon = "ea_logo_bug_Q1V_4.ico")
]

setup(name='PURCH_ListCreator',
      version = '1.2',
      description = 'Purchasing list conversion application',
      options = {'build_exe': build_options},
      executables = executables)
