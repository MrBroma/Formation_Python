# Scan a dir 

from pathlib import Path

Path.home().iterdir()

# find dir in a path
for f in Path.home().iterdir():
    print(f.name)

[f for f in Path.home().iterdir() if f.is_dir()]

[f for f in Path.home().iterdir() if f.is_file()]

p = Path.home() / "Downloads"

import glob

p.glob("*.png")

for f in p.glob("*.png"):
    print(f.name)

# test
p = Path.home() / "Pictures/Wallpapers"

p.glob("*.jpg")

for f in p.glob("*.jpg"):
    print(f.name)

