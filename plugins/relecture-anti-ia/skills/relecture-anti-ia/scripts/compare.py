#!/usr/bin/env python3
"""Compare un texte avant et après relecture.

Vérifie que les éléments qui ne doivent pas changer sont toujours là :
chiffres, variables, balises, liens, adresses e-mail, citations.
Signale aussi les mots à majuscule (noms propres probables) ajoutés ou retirés.

Usage : compare.py AVANT APRES
Code de sortie : 0 si rien de bloquant, 1 si un élément protégé a changé.
"""
import re
import sys
from collections import Counter

PROTEGES = {
    "chiffres": r"\d+(?:[.,   ]\d+)*\s?%?",
    "variables": r"\{\{[^{}]*\}\}|\{[^{}]*\}|%(?:\d+\$)?[@dsfi]|\$\{[^{}]*\}",
    "balises": r"</?[a-zA-Z][^<>]*>",
    "liens": r"https?://[^\s)>\]]+",
    "e-mails": r"[\w.+-]+@[\w-]+\.[\w.-]+",
    "citations": r"«[^«»]*»|“[^“”]*”",
}
# Signalé sans bloquer : beaucoup de faux positifs (début de phrase, titres).
NOMS = r"(?<![.!?]\s)(?<!^)\b[A-ZÀ-Ý][\wÀ-ÿ'-]+"


def compter(motif, texte, flags=0):
    return Counter(m.group(0).strip() for m in re.finditer(motif, texte, flags))


def ecarts(avant, apres):
    return sorted((avant - apres).elements()), sorted((apres - avant).elements())


def main():
    if len(sys.argv) != 3:
        print(__doc__.strip())
        return 2
    avant = open(sys.argv[1], encoding="utf-8").read()
    apres = open(sys.argv[2], encoding="utf-8").read()

    bloquant = False
    for nom, motif in PROTEGES.items():
        retires, ajoutes = ecarts(compter(motif, avant), compter(motif, apres))
        if retires or ajoutes:
            bloquant = True
            print(f"[BLOQUANT] {nom}")
            for x in retires:
                print(f"  retiré : {x}")
            for x in ajoutes:
                print(f"  ajouté : {x}")

    retires, ajoutes = ecarts(compter(NOMS, avant, re.M), compter(NOMS, apres, re.M))
    if retires or ajoutes:
        print("[À VÉRIFIER] mots à majuscule (noms propres probables)")
        for x in retires:
            print(f"  retiré : {x}")
        for x in ajoutes:
            print(f"  ajouté : {x}")

    if not bloquant:
        print("OK : chiffres, variables, balises, liens, e-mails et citations inchangés.")
    return 1 if bloquant else 0


if __name__ == "__main__":
    sys.exit(main())
