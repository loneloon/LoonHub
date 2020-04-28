import cx_Freeze

base="Win32GUI"

executables = [cx_Freeze.Executable("AmazingRace.py", base=base, icon="icon.ico")]

cx_Freeze.setup(
	name="AmazingRace",
	options={"build_exe": {"packages":["pygame"], 
	"include_files":["img", "names"]}},
	executables=executables

	)