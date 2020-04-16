import cx_Freeze

base="Win32GUI"

executables = [cx_Freeze.Executable("Serenity.py", base=base, icon="icon.ico")]

cx_Freeze.setup(
	name="Serenity",
	options={"build_exe": {"packages":["pygame"], 
	"include_files":["green_beret", "room"]}},
	executables=executables

	)