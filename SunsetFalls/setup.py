import cx_Freeze

base="Win32GUI"

executables = [cx_Freeze.Executable("Sunset Falls.py", base=base, icon="icon.ico")]

cx_Freeze.setup(
	name="FishandChimps",
	options={"build_exe": {"packages":["pygame"], 
	"include_files":["walk", "stand", "fall", "retry", "noise"]}},
	executables=executables
	)