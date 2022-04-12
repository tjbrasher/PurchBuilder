import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [],
                'excludes': ['PyQt5', 'PySide2', 'tornado', 'email',
                            'NoteBook', 'pygments', 'Regex',
                            'soupsieve', 'wcwidth', 'asyncio', 'bs4',
                            'cffi', 'ctypes', 'curses'],
                'include_files':[('Files', 'Files')]}

base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('purchGUI.py', base=base, target_name = 'purchListCreator',
    icon = "ea_logo_bug_Q1V_4.ico")
]

setup(name='PURCH_ListCreator',
      version = '1.0',
      description = 'Purchasing list conversion application',
      options = {'build_exe': build_options},
      executables = executables)
