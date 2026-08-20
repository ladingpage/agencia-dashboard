#!/usr/bin/env python3
"""Construye el PDF del relevamiento del funnel.

Las capturas de pantalla no se alteran nunca: se incrustan tal cual si existen
en docs/pdf/img/, y si falta alguna se deja un espacio reservado con el nombre
de archivo esperado, para poder regenerar el PDF cuando aparezca.

Uso:  python3 docs/pdf/build.py
"""
import base64
import html
import mimetypes
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "funnel-webinar.html"
IMG_DIR = ROOT / "img"
OUT_DIR = ROOT / "build"
OUT_HTML = OUT_DIR / "funnel-webinar.rendered.html"
OUT_PDF = ROOT / "funnel-webinar-limitless.pdf"

CHROME_CANDIDATES = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium/chrome-linux/chrome",
    "chromium",
    "google-chrome",
]

SLOT_RE = re.compile(
    r'<img\s+data-slot="(?P<slot>[^"]+)"\s+data-caption="(?P<caption>[^"]*)"\s*>',
    re.S,
)


def find_chrome() -> str:
    for candidate in CHROME_CANDIDATES:
        if Path(candidate).exists():
            return candidate
        found = subprocess.run(["which", candidate], capture_output=True, text=True)
        if found.returncode == 0:
            return found.stdout.strip()
    sys.exit("No se encontró un binario de Chromium para renderizar el PDF.")


def embed(slot: str, caption: str) -> str:
    """Devuelve la imagen incrustada, o el espacio reservado si todavía no está."""
    path = IMG_DIR / slot
    if path.exists():
        mime = mimetypes.guess_type(path.name)[0] or "image/png"
        data = base64.b64encode(path.read_bytes()).decode("ascii")
        return (
            f'<img src="data:{mime};base64,{data}" alt="{html.escape(slot)}">'
            f"<figcaption>{caption}</figcaption>"
        )
    plain = re.sub(r"<[^>]+>", "", caption)
    return (
        '<div class="slot">'
        '<div class="slot-l">Captura pendiente</div>'
        f'<div class="slot-f">img/{html.escape(slot)}</div>'
        f'<div class="slot-d">{html.escape(plain)}</div>'
        "</div>"
    )


def main() -> None:
    source = SRC.read_text(encoding="utf-8")
    missing: list[str] = []
    embedded: list[str] = []

    def replace(match: re.Match) -> str:
        slot = match.group("slot")
        (embedded if (IMG_DIR / slot).exists() else missing).append(slot)
        return embed(slot, match.group("caption"))

    rendered = SLOT_RE.sub(replace, source)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_HTML.write_text(rendered, encoding="utf-8")

    subprocess.run(
        [
            find_chrome(),
            "--headless",
            "--no-sandbox",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={OUT_PDF}",
            OUT_HTML.as_uri(),
        ],
        check=True,
        capture_output=True,
    )

    print(f"PDF generado: {OUT_PDF.relative_to(ROOT.parent.parent)}")
    print(f"Capturas incrustadas: {len(embedded)}")
    if missing:
        print(f"Capturas pendientes ({len(missing)}) — dejalas en docs/pdf/img/ y volvé a correr:")
        for slot in missing:
            print(f"  · {slot}")


if __name__ == "__main__":
    main()
