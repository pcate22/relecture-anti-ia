# relecture-anti-ia

Un skill Claude Code pour relire les contenus web et pro en français : pages de site, FAQ, posts LinkedIn, e-mails, slides, et les textes d'interface d'une app ou d'un logiciel. Il ne s'applique pas à la fiction.

Le skill lui-même : [SKILL.md](plugins/relecture-anti-ia/skills/relecture-anti-ia/SKILL.md).

## Pourquoi

Quand on rédige avec une IA, le texte prend vite la même voix que tout le monde : « Ce n'est pas X, c'est Y », des triades d'adjectifs, « au cœur de », une question en accroche. Le lecteur le sent, même sans savoir dire pourquoi.

Ce skill aide à retrouver sa propre voix dans un texte écrit avec une IA. Il repère les tournures, explique pourquoi elles sonnent faux et propose des reformulations. Vous décidez, passage par passage : il ne modifie un passage qu'après votre choix. Pour passer un détecteur d'IA, ce n'est pas le bon outil : le score ne dit rien de la provenance (voir Limites).

## Ce qu'il fait

1. Il vous demande si le texte a été rédigé avec une IA. Si oui, il cherche aussi ce qui manque : un exemple vécu, une prise de position, vos expressions.
2. Il donne un score sur 10, le nombre de passages par niveau (fort, moyen, faible) et ce qui bloque (texte encore en brouillon, fait à vérifier).
3. Il vous demande ce que vous voulez traiter, par exemple « forts et moyens, sauf la typographie ».
4. Il présente les passages un par un, dans l'ordre du texte (par écran pour une interface), et attend votre réponse avant de passer au suivant.
5. À la fin, il vous rend la liste de vos décisions au format « avant → après », prête à reporter.

### Deux modes plus rapides

Sur demande seulement :
- **« Corrige le simple »** : le skill applique lui-même la typographie, les accords et le registre (tu ou vous, on ou nous), puis liste chaque changement. Les tournures restent à trancher une à une.
- **« Tout d'un coup »** : toutes les fiches dans un seul tableau, et vous répondez en une ligne (« 1A, 2 garder, 3B »).

### Votre guide de voix

Le skill cherche votre guide de voix avant de relire : d'abord un chemin ou un lien indiqué dans votre `CLAUDE.md` ou dans la conversation, puis un fichier au nom parlant à la racine du projet ou dans `~/.claude/` (`voix.md`, `charte-editoriale.md`, `guide-de-style.md`, `brand-voice.md`, `tone-of-voice.md`…). S'il ne trouve rien, il vous demande une fois si vous en avez un, en fichier, sur Notion ou ailleurs. Un lien Notion ou Google Docs se lit si l'outil est connecté à Claude ; sinon, collez le contenu.

Il s'en sert pour votre registre, les mots qui sont à vous (il ne les relève plus), ceux que vous refusez et vos règles de typographie. Un modèle est dans [exemples/voix.md](exemples/voix.md). Pour qu'il ne pose plus la question, ajoutez à votre `CLAUDE.md` une ligne comme `Guide de voix : ~/Documents/ma-voix.md`.

### Textes d'interface

Pour une app ou un logiciel (boutons, erreurs, états vides, fichiers de traduction), le skill adapte sa relecture : il ne touche jamais aux variables (`{prenom}`, `%d`), ne propose pas de texte plus long (sauf pour rendre un bouton explicite), signale les doublons de vocabulaire (« Supprimer » et « Effacer » pour la même action) et les verbes qui changent de forme, relit les textes alternatifs, et regroupe les fiches par écran. Il suit votre glossaire produit s'il en trouve un.

La grille couvre six familles : structures de phrase, vocabulaire surreprésenté, mise en forme et typographie française, ton, calques de l'anglais, et régularité (des paragraphes tous coulés dans le même moule).

## Exemple de fiche

> **3 sur 8. [FORT, tournure IA] Page d'accueil, section « Qui suis-je »**
> « Consultante en stratégie digitale, j'accompagne les PME. **Mon approche ? Simple et efficace** : **placer l'humain au cœur de** chaque projet. »
> Pourquoi : accroche en question, formule-choc en deux temps, « au cœur de ».
> A. « Consultante en stratégie digitale, j'aide les PME à choisir leurs outils et à former leurs équipes. »
> B. Garder tel quel.
> Question : « l'humain », concrètement, ce sont les équipes, les clients, ou les deux ?
>
> A, B, garder, ou votre réponse.

## Installation

Il faut [Claude Code](https://code.claude.com/docs).

### En plugin

Dans une session Claude Code :

```
/plugin marketplace add pcate22/relecture-anti-ia
/plugin install relecture-anti-ia@cateline-puccetti
```

La seconde commande ouvre un panneau : choisissez où installer, puis validez.

Ou depuis le terminal :

```bash
claude plugin marketplace add pcate22/relecture-anti-ia
```

```bash
claude plugin install relecture-anti-ia@cateline-puccetti
```

Le skill s'appelle alors `/relecture-anti-ia:relecture-anti-ia`.

### En copie simple

```bash
git clone https://github.com/pcate22/relecture-anti-ia.git
```

```bash
cp -r relecture-anti-ia/plugins/relecture-anti-ia/skills/relecture-anti-ia ~/.claude/skills/
```

Si vous avez déjà un dossier `~/.claude/skills/relecture-anti-ia`, cette commande écrase son `SKILL.md` : sauvegardez-le ou renommez-le avant. N'installez pas non plus le plugin et la copie en même temps : les deux répondraient aux mêmes demandes.

Le skill se lance alors avec `/relecture-anti-ia`, ou tout seul quand vous écrivez « ça fait IA » ou « trop ChatGPT ».

## Mises à jour

Claude Code ne met pas à jour ce plugin tout seul. Pour l'activer : `/plugin`, onglet Marketplaces, choisir `cateline-puccetti`, puis « Enable auto-update ». Ou à la main, quand vous voulez :

```bash
claude plugin marketplace update cateline-puccetti
```

```bash
claude plugin update relecture-anti-ia@cateline-puccetti
```

Pour être prévenu des nouvelles versions, suivez les Releases du dépôt sur GitHub (bouton Watch, puis Custom, puis Releases). En copie simple, refaites la copie.

## Limites

- Le score mesure des tournures, pas la provenance. Une IA bien guidée les évite, et un humain en écrit certaines par habitude. Un score bas ne prouve pas qu'un texte est humain, un score haut ne prouve pas qu'il vient d'une IA.
- Un marqueur isolé ne prouve rien : chaque passage reçoit un niveau, et c'est vous qui décidez.
- Il n'existe pas de liste française mesurée statistiquement. Les listes de vocabulaire sont transposées de travaux en anglais.
- Les citations d'autrui (témoignages, avis clients) ne sont jamais relevées : c'est leur texte.

## Sources

- Wikipédia, [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- Kobak et al., vocabulaire en excès dans les résumés PubMed ([arXiv 2406.07016](https://arxiv.org/abs/2406.07016), [liste des mots](https://github.com/berenslab/llm-excess-vocab)).
- Articles de presse française (Siècle Digital, Blog du Modérateur) sur le tiret cadratin et les tournures répétées.
- Des tournures refusées en relecture sur des textes réels.

## Autrice et licence

Cateline Puccetti, [cateline.fr](https://cateline.fr). Licence [MIT](LICENSE).
