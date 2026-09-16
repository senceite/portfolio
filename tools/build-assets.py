"""Resize the selected source images into web-ready WebP for the portfolio site."""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageOps

DRIVE = Path(r"G:\My Drive\Documentos Pessoais\07 Família e Relações\Ajuda Rafa")
PDF = Path(sys.argv[1])
OUT = Path(sys.argv[2])

# (slug, [(source path, output name)]) — first entry of each case is its cover.
CASES: dict[str, list[tuple[Path, str]]] = {
    "urbo": [
        (DRIVE / "Urbo Gastrobar" / "10.jpg", "papelaria"),
        (DRIVE / "Urbo Gastrobar" / "1.jpg", "marca"),
        (DRIVE / "Urbo Gastrobar" / "15.jpg", "simbolo"),
        (DRIVE / "Urbo Gastrobar" / "4.jpg", "construcao"),
        (DRIVE / "Urbo Gastrobar" / "5.jpg", "padrao"),
        (DRIVE / "Urbo Gastrobar" / "8.jpg", "tipografia"),
        (DRIVE / "Urbo Gastrobar" / "6.png", "assinatura"),
        (DRIVE / "Urbo Gastrobar" / "11.jpg", "cartoes"),
        (DRIVE / "Urbo Gastrobar" / "12.jpg", "sacola"),
        (DRIVE / "Urbo Gastrobar" / "14.jpg", "fachada"),
        (DRIVE / "Urbo Gastrobar" / "13.jpg", "site"),
        (DRIVE / "Urbo Gastrobar" / "9.jpg", "embalagem"),
    ],
    "reconhecer": [
        (PDF / "reconhecer" / "card-18.jpg", "abertura"),
        (PDF / "reconhecer" / "card-28.jpg", "assinatura"),
        (PDF / "reconhecer" / "card-27.jpg", "tipografia"),
        (PDF / "reconhecer" / "card-31.jpg", "estudos"),
        (PDF / "reconhecer" / "card-01.jpg", "dado-milhoes"),
        (PDF / "reconhecer" / "card-12.jpg", "racismo-agora"),
        (PDF / "reconhecer" / "card-05.jpg", "retratos"),
        (PDF / "reconhecer" / "card-11.jpg", "dado-56"),
        (PDF / "reconhecer" / "card-34.jpg", "ife"),
        (PDF / "reconhecer" / "card-33.jpg", "stories"),
    ],
    "multiplo": [
        (DRIVE / "Múltiplo" / "8a8ad9139301079.622d3e77c6873.jpg", "capa-aberta"),
        (DRIVE / "Múltiplo" / "bcfb4a139301079.622d3e77c7a3a.jpg", "capa"),
        (DRIVE / "Múltiplo" / "5f52d9139301079.622d3e77c39cb.jpg", "obras-e-poemas"),
        (DRIVE / "Múltiplo" / "80f3d1139301079.622d3e77c30cf.jpg", "dobradura"),
        (DRIVE / "Múltiplo" / "939d58139301079.622d3e77c574c.jpg", "cronologia"),
        (DRIVE / "Múltiplo" / "87e7b1139301079.622d3e77c4c2d.jpg", "citacao"),
        (DRIVE / "Múltiplo" / "880deb139301079.622d3e77c51b3.jpg", "retrato"),
        (DRIVE / "Múltiplo" / "926999139301079.622d3e77c289c.jpg", "nao-ha-vagas"),
        (DRIVE / "Múltiplo" / "e99e51139301079.622d3e77c60e7.jpg", "os-mortos"),
    ],
    "n1pt": [
        (DRIVE / "N1PT/Dia da Educação 2024/Institucional/N1PT_Participe-Feed-1.png", "abertura"),
        (DRIVE / "N1PT/Dia da Educação 2024/Institucional/N1PT_Institucional-Feed-4.png", "institucional"),
        (DRIVE / "N1PT/Dia da Educação 2024/Dados/Dado 1/cards-dados-1_feed.png", "dado-1"),
        (DRIVE / "N1PT/Dia da Educação 2024/Dados/Dado 3/cards-dados-2_stories.png", "dado-3"),
        (DRIVE / "N1PT/Dia da Educação 2024/Dados/Dado 4/cards-dados-2_stories.png", "dado-4"),
        (DRIVE / "N1PT/Dia da Educação 2024/Dados/Dado 6/cards-dados-1_stories.png", "dado-6"),
        (DRIVE / "N1PT/Dia da Educação 2024/imagem-n1pt-3.png", "carrossel"),
        (DRIVE / "N1PT/Dia da Educação 2024/Participe/Interno/1/N1PT_Participe-Carrossel-1-FRM.png", "quiz"),
        (DRIVE / "N1PT/Dia da Educação 2024/Participe/Parceiros/2/N1PT_Participe-Feed-2.png", "parceiros"),
        (DRIVE / "N1PT/Dia da Educação 2024/Mailing-Dia-da-Educação.jpg", "mailing"),
    ],
    "aruanda": [
        (PDF / "aruanda" / "spread-1.jpg", "capa"),
        (PDF / "aruanda" / "spread-3.jpg", "expediente"),
        (PDF / "aruanda" / "spread-4.jpg", "principia"),
        (PDF / "aruanda" / "spread-5.jpg", "emicida"),
        (PDF / "aruanda" / "spread-6.jpg", "viola-davis"),
        (PDF / "aruanda" / "spread-7.jpg", "ryane-leao"),
        (PDF / "aruanda" / "spread-8.jpg", "voce-em-aruanda"),
        (PDF / "aruanda" / "apres-5.jpg", "grid"),
        (PDF / "aruanda" / "apres-6.jpg", "edicao-2"),
    ],
    "budapeste": [
        (DRIVE / "Budapeste" / "3e5340135334143.61e650bf07026.jpg", "capa"),
        (DRIVE / "Budapeste" / "b55bff135334143.61e650bf0c5fe.jpg", "capa-e-quarta"),
        (DRIVE / "Budapeste" / "c0875d135334143.61e650bf0841b.jpg", "espelho"),
        (DRIVE / "Budapeste" / "110aa7135334143.61e650bf08f8e.jpg", "cidade-amarela"),
        (DRIVE / "Budapeste" / "861aa7135334143.61e650bf067c1.jpg", "miolo"),
        (DRIVE / "Budapeste" / "c4ec25135334143.61e650bf0d9e8.jpg", "aberto"),
    ],
}

WIDE, THUMB = 1600, 800


def save(img: Image.Image, path: Path, width: int) -> tuple[int, int]:
    out = img if img.width <= width else img.resize(
        (width, round(img.height * width / img.width)), Image.LANCZOS
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    out.save(path, "WEBP", quality=82, method=6)
    return out.size


missing: list[str] = []
for slug, entries in CASES.items():
    for source, name in entries:
        if not source.exists():
            missing.append(str(source))
            continue
        img = ImageOps.exif_transpose(Image.open(source)).convert("RGB")
        w, h = save(img, OUT / slug / f"{name}.webp", WIDE)
        save(img, OUT / slug / f"{name}@sm.webp", THUMB)
        print(f"{slug}/{name}\t{w}x{h}", flush=True)

for path in missing:
    print(f"MISSING\t{path}", flush=True)
