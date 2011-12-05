from distutils.core import setup
import os
import py2exe
from glob import *

data_files = []
data_files += glob('icons/*.png')
data_files += glob('dlls/*.dll')
includes = []
excludes = [] #['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
           # 'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
           # 'Tkconstants', 'Tkinter']
packages = []
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll', 'MSVCP90.dll']
 
setup(
    options = {"py2exe": {"compressed": 2,
                          "optimize": 2,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "bundle_files": 3,
                          "dist_dir": "build/",
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                         },
             },
    data_files = data_files,
    windows=['simpleBT.py']
)
