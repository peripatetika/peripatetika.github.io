"""
Smanji i pretvori sliku u WebP prije dodavanja na blog (nije obavezno).

CSS već sam izreže svaku naslovnu sliku na isti omjer, pa dimenzije nije
potrebno namještati. Ovaj alat služi samo da velike slike (npr. fotografije
s mobitela od nekoliko MB) ne usporavaju učitavanje.

Upotreba:
    python alati/pripremi_sliku.py slika.jpg                    -> slika.webp
    python alati/pripremi_sliku.py slika.jpg docs/images/naslovne/ime.webp
"""
import sys
from pathlib import Path

from PIL import Image, ImageOps

NAJVECA_SIRINA = 1600   # dovoljno za oštar prikaz i na retina ekranima
KVALITETA = 82

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    ulaz = Path(sys.argv[1])
    izlaz = Path(sys.argv[2]) if len(sys.argv) > 2 else ulaz.with_suffix(".webp")
    slika = ImageOps.exif_transpose(Image.open(ulaz))
    if slika.width > NAJVECA_SIRINA:
        visina = round(slika.height * NAJVECA_SIRINA / slika.width)
        slika = slika.resize((NAJVECA_SIRINA, visina), Image.LANCZOS)
    if slika.mode not in ("RGB", "RGBA"):
        slika = slika.convert("RGBA" if "A" in slika.getbands() else "RGB")
    izlaz.parent.mkdir(parents=True, exist_ok=True)
    slika.save(izlaz, "WEBP", quality=KVALITETA, method=6)
    print(f"{izlaz}  {slika.width}×{slika.height}  {izlaz.stat().st_size // 1024} KB")

if __name__ == "__main__":
    main()
