import cx_Freeze

base="Win32GUI"

executables = [cx_Freeze.Executable("ShadowCat.py", base=base, icon="icon.ico")]

cx_Freeze.setup(
	name="Serenity",
	options={"build_exe": {"packages":["tkinter"], 
	"include_files":["client.py", "img"]}},
	executables=executables

	)