from pathlib import Path

p = Path.home() / "image.png"

p.parent / p.stem

p.parent / (p.stem + "-lowres" + p.suffix)

