application_title =  "STEGO"
main_python_file = "test.py"

import sys

from cx_Freeze import setup, Executable
 
base =none
if sys.platform=="win32":
	base="Win32GUI"

includes=["atexit","re"]

setup(	
		name=application_title,
		version="0.1",
		description="simple test",
		options={"build_exe":{"includes":includes}},
		executables=[Executable(main_python_file,base=base)])
