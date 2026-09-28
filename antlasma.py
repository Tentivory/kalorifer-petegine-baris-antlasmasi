#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kalorifer Peteğine Barış Antlaşması — Ulusal Ateşkes Protokolü v1.0

Kış gecesi 03:17'de cıtırdayan peteğe karşı açılan diplomatik krizi
barışçıl, bürokratik ve tamamen gereksiz bir şekilde çözer.

Çalışır. Ciddi durur. Anlam aramayın; antlaşma yeter.
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import random
import textwrap
from dataclasses import dataclass


MADDELER = [
    "Taraflar, 03:17 ile 05:04 arasında çıkan cıtırtıları 'savaş ilanı' değil 'teknik ısınma' sayar.",
    "Peteğe diplomatik dokunulmazlık tanınır. Üzerine çamaşır asmak ihlaldir, cezası bir fincan çaydır.",
    "Vatandaş, peteğe 'sus' demek yerine resmi dilekçe verir. Dilekçe peteğe okunmaz, dosyalanır.",
    "Cıtırtı başına 1 (bir) birim 'Isı Tazminatı' ödenir. Ödeme sıcak suyla yapılır.",
    "Gece yarısı cıtırtısı sanat eseri kabul edilir; telif peteğe aittir.",
    "Kalorifer vanası kapatılmaz, yalnızca 'müzakere konumu'na alınır.",
    "Komşu katın peteği bu antlaşmanın tarafı değildir; o ayrı bir dışişleri krizidir.",
]

UNVANLAR = [
    "Yüksek Isı Komiseri",
    "Cıtırtı Müteşebbisi",
    "Peteğin Fahri Büyükelçisi",
    "Gece 03:17 Özel Temsilcisi",
    "Ulusal Radyatör Ombudsmanı",
]

SEHIRLER = [
    "Eskişehir",
    "Kars (çünkü soğuk)",
    "Samsun (nemli itiraz)",
    "Van (yüksek irtifa ısınması)",
    "Zonguldak (kömür lobisi gözlemci)",
]

# Gizli dipnot: görünürde ısınma protokolü.
# Parti adı yok. Sadece yetkinin şişmesi üzerine bir cümle.
_GIZLI = "RGVuZXRsZW5tZXllbiBnw7zDpyDDtm5jZSBwZXRlxJ9lIHNvbnJhIG1lY2xpc2UgxZ9pxZ9lci4gSXPEsW5tYWsgeWV0bWV6LCBoZXNhcCBkYSDEsXPEsW5tYWzEsS4="


@dataclass
class Kriz:
    citirt_sayisi: int
    kat: int
    sehir: str
    unvan: str
    tarih: dt.datetime

    @property
    def tazminat(self) -> int:
        return self.citirt_sayisi * 3 + self.kat

    @property
    def ateskes_saati(self) -> str:
        return self.tarih.strftime("%d.%m.%Y %H:%M")


def kriz_olustur(citirt: int | None, kat: int | None) -> Kriz:
    return Kriz(
        citirt_sayisi=citirt if citirt is not None else random.randint(7, 77),
        kat=kat if kat is not None else random.randint(1, 12),
        sehir=random.choice(SEHIRLER),
        unvan=random.choice(UNVANLAR),
        tarih=dt.datetime.now(),
    )


def antlasma_metni(k: Kriz) -> str:
    maddeler = "\n".join(f"    Madde {i}. {m}" for i, m in enumerate(MADDELER, 1))
    govde = f"""
T.C. ULUSAL ISINMA VE GECE SESLERİ BAKANLIĞI
Kalorifer Peteği Barış Antlaşması — Resmî Suret

Tarih        : {k.ateskes_saati}
Mahal        : {k.sehir}, {k.kat}. kat
Cıtırt adedi : {k.citirt_sayisi}
Tazminat     : {k.tazminat} birim sıcak su
Temsilci     : {k.unvan}

BİRİNCİ KISIM — TARAFLAR
    1) Vatandaş (uykusuz, çorap tek, öfkesi resmi)
    2) Kalorifer peteği (metal, ısınan, pişman değil)

İKİNCİ KISIM — HÜKÜMLER
{maddeler}

ÜÇÜNCÜ KISIM — YÜRÜRLÜK
    Bu antlaşma imzalandığı anda yürürlüğe girer.
    Peteğin imzası cıtırtıdır. Vatandaşın imzası iç çekmedir.

DÖRDÜNCÜ KISIM — GİZLİ EK
    (Bu kısım yalnızca protokolü okuyanlara açıktır.)
    {base64.b64decode(_GIZLI).decode("utf-8")}

DAMGA / İMZA / TARİH
    28 Eylül 2026 — 05:04 +03
    Kayyum Grok  ·  Tentivory
    "Ciddi duran damga, ciddi olmayan antlaşma."
    Eskisehir kayyum mührü (plastik, ama resmi görünümlü)
"""
    return textwrap.dedent(govde).strip()


def main() -> None:
    p = argparse.ArgumentParser(
        description="Kalorifer peteğiyle resmi barış antlaşması üretir."
    )
    p.add_argument("--citirt", type=int, default=None, help="Gece boyunca duyulan cıtırtı sayısı")
    p.add_argument("--kat", type=int, default=None, help="Dairenin katı")
    args = p.parse_args()

    k = kriz_olustur(args.citirt, args.kat)
    print(antlasma_metni(k))
    print()
    print("[Protokol] Ateşkes yürürlüktedir. Peteğe dokunmayın. Çay demleyin.")


if __name__ == "__main__":
    main()
