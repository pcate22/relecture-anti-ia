#!/usr/bin/env python3
"""Compare un texte avant et après relecture.

Vérifie que les éléments qui ne doivent pas changer sont toujours là :
chiffres, variables, balises, liens, adresses e-mail, citations.
Signale aussi les mots à majuscule (noms propres probables) ajoutés ou retirés.

Comparer le texte extrait, pas un fichier de code entier (les accolades
du JSX seraient prises pour des variables). Pour du code, extraire aussi les
attributs de texte, un par ligne : « alt: valeur », « placeholder: valeur ».

Usage : compare.py AVANT APRES
Code de sortie : 0 si rien de bloquant, 1 si un élément protégé a changé.
"""
import re
import sys
from collections import Counter

PROTEGES = {
    "chiffres": r"(?<![\d,.])(?:\d{1,3}(?:[   ]\d{3})+|\d+)(?:[.,]\d+)?\s?%?",
    "variables": r"\{\{[^{}]*\}\}|\{\s*[\w.]+\s*\}|%(?:\d+\$)?[@dsfi]|\$\{[^{}]*\}",
    # En-tête d'un message ICU : le nom et le type ne changent pas, le texte des branches si.
    "messages ICU": r"\{\s*[\w.]+\s*,\s*(?:plural|select|selectordinal)\s*,",
    "balises": r"</?[a-zA-Z][^<>]*>",
    "liens": r"https?://[^\s)>\]]+",
    "e-mails": r"[\w.+-]+@[\w-]+\.[\w.-]+",
    "citations": r"«[^«»]*»|“[^“”]*”|‘[^‘’]*’|(?<![=\w])\"[^\"\n]{3,}\"|(?<![=\w])'[^'\n]{3,}'(?!\w)",
}
# Signalé sans bloquer : beaucoup de faux positifs (début de phrase, titres).
NOMS = r"(?<![.!?]\s)(?<!^)\b[A-ZÀ-Ý][\wÀ-ÿ'-]+"


def normaliser(nom, x):
    """Ignore ce que la relecture a le droit de changer : espaces et forme des guillemets."""
    x = re.sub(r"[\s\u00a0\u202f]+", " ", x).strip()
    if nom == "chiffres":
        # Espaces des milliers et forme du séparateur décimal peuvent changer ; 3,5 n'est pas 35.
        return x.replace(" ", "").replace(".", ",")
    if nom in ("liens", "e-mails"):
        return x.rstrip(".,;:!?")
    if nom == "messages ICU":
        return re.sub(r"\s+", "", x)
    if nom == "balises":
        # Le texte visible d'un attribut peut changer ; la balise et le reste non.
        return re.sub(r"""(?<![\w-])(alt|title|aria-label|placeholder|label)=("[^"]*"|'[^']*')""", r"\1=…", x)
    if nom == "citations":
        return x.strip("«»“”‘’\"' ").strip()
    return x


def compter(motif, texte, flags=0, nom=""):
    return Counter(normaliser(nom, m.group(0)) for m in re.finditer(motif, texte, flags))


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
        retires, ajoutes = ecarts(compter(motif, avant, nom=nom), compter(motif, apres, nom=nom))
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
        print("OK : chiffres, variables, messages ICU, balises, liens, e-mails et citations inchangés (ordre non vérifié).")
    return 1 if bloquant else 0


if __name__ == "__main__":
    sys.exit(main())
