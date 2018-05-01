from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "gwconv",
    version = "1.1",
    description = "Geneweb converter",
    executables = [Executable("gwconv.py", base=base), Executable("imheal.py", base=base)]
)