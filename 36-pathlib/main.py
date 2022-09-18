# class Path
from genericpath import exists
from os import mkdir
from pathlib import Path

#home path
p = Path.home()
print(p)

# current working directory
p2 = Path.cwd()
print(p2)

p.parent

# _________________________________________

# Concatenation of path

p = Path.home()

p / "Documents"
p / "Documents" / "main.py"

p.joinpath("Documents", "main.py")

(p / "Documents" / "main.py").suffix
p.joinpath("Documents", "main.py").suffix

# ______________________________________

from pathlib import Path

p = Path("/home/loic/Documents/Courses/Formation_Python")
print(p.name)
print(p.stem)
print(p.suffix)
print(p.suffixes)
print(p.parts)
print(p.exists())
print(p.is_dir())
print(p.is_file())

print(p.parent.parent)

# _____________________________________

# Create and suppress directories (suppress if the dir is empty)

p = Path.home()

p = p / "DossierTest"

p.mkdir()

p.mkdir(exists_ok=True) # no error if it exist

p = p / "1" / "2" / "3"

p.mkdir() # Impossible if parents doesn't exist

p.mkdir(parents=True)

p = p / "readme.txt"

p.touch()  # create
p.unlink() # suppress

p = p.parent

p.rmdir()

p = p.parent.parent.parent # --> DossierTest

p.rmdir() # --> dir not empty

#suppress dir tree if not empty using shutil
import shutil

shutil.rmtree(p)

mkdir(parents=True, exist_ok=True)

#________________________________________

# read and write in a file

p = Path.home() / " PathLib" / "readme.txt"

p.touch()

p.write_text("Bonjour")

p.read_text()


