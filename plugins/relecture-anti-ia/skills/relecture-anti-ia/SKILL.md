---
name: relecture-anti-ia
description: Relire un texte en français et rendre un rapport détaillé des tournures typiques d'une IA (ChatGPT, Claude, Gemini) : chaque passage cité dans son contexte, niveau estimé, reformulations proposées. La personne qui écrit tranche : rien n'est modifié sans son accord, sauf les modes « Corrige typo, orthographe et registre » et « Corrige tout » quand elle les demande. À utiliser avant de livrer un texte web ou pro destiné à être lu par d'autres (page web, FAQ, post LinkedIn, e-mail, newsletter, slide, textes d'interface d'une app ou d'un logiciel : boutons, messages d'erreur, onboarding, fichiers de traduction), et dès que l'utilisateur dit « ça fait IA », « phrase IA », « trop ChatGPT », « pas naturel », « réécris plus simple », même sans dire « anti-IA ». Ne s'applique pas à la fiction.
---

# Relecture anti-IA (français)

But : aider la personne qui écrit à rendre un texte tel qu'elle l'aurait écrit elle-même. Le skill **montre et propose, il ne corrige pas** : aucune modification du texte ou du fichier sans son accord, passage par passage. Exceptions, à sa demande seulement : les modes « Corrige typo, orthographe et registre » et « Corrige tout » (voir plus bas).

Un marqueur isolé ne prouve rien : beaucoup sont des habitudes humaines légitimes. D'où le niveau estimé pour chaque passage, et la règle : on signale tout ce qu'on voit, on ne décide pas à sa place.

**Hors champ : la fiction** (roman, nouvelle, conte, poème). Ce skill n'y touche pas.

## Guide de voix

Avant de relire, trouver le guide de voix de la personne, s'il existe. Il peut porter un autre nom ou vivre ailleurs (Notion, Google Docs, site de marque). Dans cet ordre, et s'arrêter au premier trouvé :

1. **Une indication déjà donnée** : un chemin ou un lien vers un guide de voix, un « tone of voice », une charte éditoriale ou un guide de style dans le `CLAUDE.md` du projet ou de `~/.claude/`, ou plus tôt dans la conversation.
2. **Un fichier local au nom parlant**, à la racine du projet puis dans `~/.claude/` (sans fouiller le reste du disque) : `voix.md`, `ma-voix.md`, `ton.md`, `charte-editoriale.md`, `guide-de-style.md`, `style.md`, `brand-voice.md`, `tone-of-voice.md`, `tone_of_voice.md`, `voice.md`, `tone.md`. Ignorer la casse, les espaces et l'extension (`.md`, `.txt`) : « Tone of Voice.md » compte.
3. **Sinon, demander une fois** : « As-tu un guide de voix (tone of voice) ou une charte éditoriale (fichier, page Notion, document en ligne) ? Si oui, donne-moi le chemin ou le lien. » Accepter « non » et relire normalement.

Si la réponse est un lien : le lire avec l'outil connecté qui convient (Notion, Google Drive…). Si aucun outil n'y a accès, demander de coller le contenu. Puis proposer d'ajouter une ligne dans le `CLAUDE.md` (« Guide de voix : <chemin ou lien> ») pour ne plus avoir à le demander ; ne l'écrire qu'avec accord.

Une fois trouvé, vérifier que le contenu décrit bien une façon d'écrire (un `style.md` peut être une feuille de style CSS) ; sinon l'ignorer et passer à l'étape suivante. Puis s'en servir pour toute la relecture :
- **registre** (tu ou vous, on ou nous, écriture inclusive ou non) : c'est la référence, ne plus poser la question ;
- **mots et tournures à soi** : ne jamais les relever, même s'ils sont dans la grille ; les préférer dans les reformulations ;
- **mots refusés** : les relever au niveau FORT, quel que soit le contexte, sauf dans une citation d'autrui ;
- **règles typographiques** (tiret cadratin, emojis, insécables) : elles passent avant la grille.

Le guide décrit une voix, il ne contient pas de faits : ne jamais en tirer d'anecdote, de chiffre ou de souvenir pour compléter un texte. Dire en tête du rapport quel guide a servi (ou qu'aucun n'a été trouvé).

S'il n'y en a pas, relire normalement. En fin de relecture, si des décisions se répètent (même registre, même mot refusé trois fois), proposer de les noter dans un `voix.md` et montrer le contenu avant de l'écrire. Ne jamais créer ni modifier ce fichier sans accord.

## Méthode

1. Demander d'abord : « Ce texte a-t-il été rédigé avec une IA ? » (sauf si le texte vient d'être rédigé dans cette conversation : la réponse est oui, ne pas poser la question). Si oui, chercher aussi ce qui manque de la personne (exemples vécus, expressions à elle, aspérités), pas seulement ce qui est en trop.
2. Lire le texte entier une fois : repérer le ton général (promo ? uniforme ? sans opinion ?).
3. Chercher d'abord les restes de chantier (crochets, « à écrire », « brouillon », « TODO », texte d'exemple) : bloquants, en tête du rapport. Tout fait personnel qui semble rédigé par une IA (anecdote, chiffre, délai, résultat client) est « à faire valider » : c'est son vécu, pas celui du modèle.
4. Passer la grille ci-dessous, famille par famille, puis les points hors grille.
5. Rendre le rapport (format ci-dessous). Ne rien réécrire dans le fichier avant les réponses.

**Ce que vaut une réponse** : choisir A ou B sur une fiche vaut accord pour ce passage seulement. Fichier de texte seul (Markdown pur, .txt) : le modifier pour ce passage, rien d'autre. Code (y compris MDX et HTML), fichier de traduction, CMS, design, présentation, document en ligne : ne rien écrire pendant les fiches ; voir « Reporter dans la source », qui demande un accord à part. Texte collé dans la conversation ou fichier hors de portée : noter la décision pour la liste finale.

**Ordre des questions avant le rapport** : chercher le guide de voix (et ne demander que s'il n'est pas trouvé), puis la question « rédigé avec une IA ? », puis le score et le choix des niveaux. Pas d'autre question avant la première fiche. Texte court (moins de 10 fiches) : sauter le choix des niveaux et tout montrer.

**Demande de réécriture explicite** (« réécris plus simple ce paragraphe ») : ne pas dérouler le rapport ni poser les questions ci-dessus ; utiliser le guide de voix s'il est déjà connu ou trouvé sans demander, et ne poser une question que si le registre est indispensable et inconnu. Proposer directement une version réécrite, sans fait ajouté, en gardant intactes les variables et les citations, puis lister en une ligne les marqueurs retirés. Bio ou page « À propos » : réécrire quand même, sans rien retirer du sens (public visé, conviction), et ajouter sous la version une ou deux questions sur les passages ambigus. La personne garde, ajuste ou refuse.

## Format du rapport

Le rapport doit être facile à lire : il se parcourt d'un coup d'œil, l'essentiel en premier, toujours dans le même ordre. Pas d'emoji.

**1. Score global**, en tête : une information par ligne, en liste courte, jamais plusieurs éléments à la suite sur une même ligne :

> **Score de tournures IA : 3/10** (faible)
>
> - 2 passages forts
> - 3 moyens
> - 4 faibles
> - Bloquant : la section « Tarifs » est encore en brouillon
> - Guide de voix : `voix.md` (racine du projet)
> - Temps estimé pour trancher : 10 minutes

Ce score mesure les tournures d'IA, **pas la provenance** : une IA bien guidée (consignes de style) les évite, et son texte peut avoir un score bas. Le dire dans le rapport quand le texte a été rédigé avec une IA.

Barème du score sur 10 :
- **0 à 2** : rien ou presque, quelques habitudes humaines ;
- **3 à 4** : faible, des marqueurs isolés dans un texte à la voix nette ;
- **5 à 6** : moyen, des tournures d'IA dans plusieurs sections ;
- **7 à 8** : fort, la plupart des paragraphes portent un marqueur ;
- **9 à 10** : texte manifestement généré, à reprendre en entier.

Le score juge le texte entier (densité et gravité des marqueurs), pas le nombre brut : un seul passage fort dans une bio courte pèse plus que quatre faibles dans un guide de 40 pages.

**2. Choisir ce qu'on montre.** Après le score, un petit tableau du décompte, par niveau (bloquant, fort, moyen, faible) et par type de problème :
- **brouillon** : reste de chantier, fait personnel à valider ;
- **tournure IA** : un marqueur de la grille (structure, vocabulaire, ton) ;
- **registre** : tu/vous, on/nous, inclusif/masculin ;
- **régularité** : prose au même moule (voir grille §6) ;
- **langue** : accord, titre qui ne correspond pas, graphie, typographie.

Puis demander quels niveaux et quels types traiter (ex. « forts et moyens, sauf langue »), et attendre la réponse.

**3. Le détail, une fiche à la fois, dans l'ordre du texte** (section par section ; pour une interface, voir « Ordre des fiches » dans Textes d'interface) : sans cet ordre, on ne suit plus. Montrer une seule fiche, attendre la réponse, puis passer à la suivante. Annoncer la position (« 3 sur 8 »). La fiche suit toujours cet ordre :

> **3 sur 8. [FORT, tournure IA] Page d'accueil, section « Qui suis-je »**
>
> « Consultante en stratégie digitale, j'accompagne les PME dans le choix de leurs outils. **Mon approche ? Simple et efficace** : **placer l'humain au cœur de** chaque projet. »
>
> **Pourquoi** : accroche en question, formule-choc en deux temps, « au cœur de ».
>
> - **A.** « Consultante en stratégie digitale, j'accompagne les PME dans le choix de leurs outils. »
> - **B.** Garder tel quel.
>
> **Question** : « l'humain », concrètement, ce sont les équipes, les clients, ou les deux ? Si c'est important pour toi, on peut le dire en une phrase.
>
> A, B, garder, ou ta réponse.

Chaque partie de la fiche sur sa propre ligne, séparée par une ligne vide : en Markdown, des lignes de citation qui se suivent se fondent en un seul paragraphe.

- **Contexte** : la phrase entière, plus celle d'avant ou d'après si elle éclaire le choix ; le passage en cause en **gras**. Jamais un fragment isolé : sans contexte, on ne peut pas trancher.
- **Pourquoi** : une ligne, le marqueur de la grille (ou « hors grille »).
- **Niveau et type** en tête : **FORT** (tournure typique, gratuite, ou plusieurs marqueurs dans le même paragraphe), **MOYEN** (marqueur réel, mais qui peut être un choix de voix), **FAIBLE** (habitude humaine courante).
- **Choix** : une ou deux reformulations (A, B…) qui gardent chaque fait, nom et nuance, et toujours « Garder tel quel ». Ne toucher qu'aux mots en gras. Jamais d'exemple, de chiffre ou d'anecdote absents de la source : si le passage ne dit rien de concret, retirer la formule (comme A ci-dessus) et demander ce qu'elle voulait dire, sans le deviner.
- **Réponse attendue**, en dernière ligne : « A, B, garder, ou ta réponse. » (« votre réponse » si la personne vouvoie). On n'applique que ce qui a été choisi, et rien sans réponse (voir « Ce que vaut une réponse »).

**Pendant les fiches** :
- Quand un fait est corrigé, chercher tout de suite les autres endroits du document qui le répètent (ex. un tarif corrigé dans la section « Offre », encore présent dans la FAQ) et les proposer dans la même fiche.
- Une décision vaut pour la suite : si un passage reformulé contient un marqueur qu'il a déjà été décidé de réduire, l'intégrer dans la proposition A de la fiche et le dire. Rien n'est écrit sans réponse.
- Quand la personne dicte en vrac (souvenirs, avis, ce qu'elle veut dire), mettre en forme **avec ses mots** : ordre, ponctuation, accords, rien d'autre. Ne pas inventer d'humour, d'émotion ou de détail ; si le cadre en demande, le lui dire et la laisser compléter. Signaler une ambiguïté par une question courte.
- Source sans outil pour l'écrire (PDF, Keynote, outil en ligne non connecté) : ne rien modifier, garder la liste des décisions. Sinon, voir « Reporter dans la source ».

**4. Après la dernière fiche**, trois blocs, chacun sous un intitulé en gras et en liste (une ligne par élément) :
- **Décisions** : dans l'ordre suivi pour les fiches, une ligne par passage au format « avant → après », ou « gardé tel quel ». Prête à reporter dans le fichier source.
- **Non traité** : une ligne par niveau ou type laissé de côté, avec le nombre de passages.
- **Relu sans rien relever** : une ligne par section, avec ce qui y a été vérifié.

Texte collé dans la conversation : après ces trois blocs, rendre le texte complet avec les choix appliqués, prêt à copier.

## Trois modes plus rapides

Seulement si la personne les demande. Par défaut : une fiche à la fois.

### « Corrige typo, orthographe et registre »

Corrige directement la **langue** (typographie, accords, graphies en double) et le **registre**. Jamais les tournures IA, le ton, la régularité ni les brouillons : ceux-là restent en fiches.

Étapes, dans cet ordre :

1. **Références** : guide de voix et glossaire. Registre inconnu ou graphie en double sans référence : une seule question qui regroupe les deux. Pas de question « rédigé avec une IA ? » pour un fichier d'interface.
2. **Où écrire** :
   - texte collé dans la conversation : rendre le texte corrigé ;
   - Markdown pur, `.txt`, fichier de traduction JSON ou YAML : écrire directement (étapes 3 à 5) ;
   - `.strings`, `.po`, `.arb` ou autre format sans vérification simple : ne pas écrire ; rendre la liste des corrections, une par ligne ;
   - code (JSX, Vue, HTML, MDX, templates), CMS, design, présentation, document en ligne : ne pas écrire ; rendre le texte corrigé et la liste, puis proposer « Reporter dans la source », qui demande un accord à part.
3. **Copie** : garder le contenu d'origine (ou vérifier que le fichier est suivi par git, sans modification en cours).
4. **Corriger** :
   - valeurs seulement, jamais les clés, délimiteurs, guillemets de syntaxe, apostrophes d'échappement (ICU), variables ni balises (voir Textes d'interface) ;
   - registre : changements mécaniques seulement (pronom, conjugaison, possessif dans la même phrase) ; une phrase à restructurer, une chaîne qui s'allonge, une citation d'autrui ou un cas « à trancher » passent en fiche ;
   - espaces fines insécables dans une chaîne d'interface : seulement si le guide de voix les demande, certaines polices les affichent mal.
5. **Vérifier** que le fichier se lit encore (JSON, YAML : un analyseur, par exemple `python3 -m json.tool`). En cas d'échec : restaurer la copie, jamais reconstruire de mémoire, et passer en fiches.
6. **Lister** chaque changement, un par ligne, au format « avant → après ».
7. **Continuer** avec le score et les fiches pour le reste.

Texte collé dans la conversation : pas de fichier, rendre le texte corrigé.

### « Tout d'un coup »

Toutes les fiches retenues en tableaux numérotés, avec les colonnes Section, Passage, Pourquoi, A, B :
- une ligne par fiche ; dans « Passage », la phrase entière avec le passage en cause en gras (le contexte reste nécessaire) ;
- `|` échappé en `\|`, variables entre accents graves ;
- 20 lignes au plus par tableau, section par section, chaque tableau avec sa propre réponse en une ligne (« 1A, 2 garder, 3B… ») ;
- au-delà d'environ 40 fiches, proposer d'abord de limiter les niveaux traités.

Rien n'est appliqué sans réponse pour chaque numéro ; un numéro sans réponse reste inchangé et est rappelé à la fin.

### « Corrige tout »

Pour les très gros volumes (des centaines de passages). **Déconseillé** : le dire au lancement en une ligne (« Le texte va perdre une partie de votre voix ; je recommande de relire au moins les passages FORT »), puis continuer si la personne confirme. Si elle a confirmé d'avance, continuer sans attendre, mais redire cette ligne en tête du livrable.

1. Mêmes étapes 1 à 3 que « Corrige typo, orthographe et registre » (références, où écrire, copie). Partout où ce mode-là n'écrit pas (format non vérifiable, code, CMS, design, présentation), « Corrige tout » non plus : il produit le texte corrigé et la liste des décisions, sans repasser en fiches ; le report passe ensuite par « Reporter dans la source », avec accord.
2. Appliquer la typo, l'orthographe et le registre, puis la proposition A de chaque passage FORT et MOYEN. Les FAIBLE restent tels quels.
3. Ne jamais appliquer seul, mais lister sous **À voir vous-même** : brouillons, faits personnels à valider, citations d'autrui, passages où la fiche aurait posé une question, cas « à trancher ».
4. Vérifier avant de livrer (voir « Vérification avant de livrer », obligatoire dans ce mode).
5. Livrer, une information par ligne :
   - le score avant et après ;
   - la liste « avant → après », section par section ;
   - **À voir vous-même** ;
   - pour un texte collé, le texte complet corrigé.

## Vérification avant de livrer

Obligatoire en mode « Corrige tout » ; à proposer dans les autres modes quand plus de 20 passages ont été modifiés.

1. **Contrôle mécanique**, si Python est disponible : écrire le texte original et le texte corrigé (texte extrait seul, pas le fichier de code ou la présentation entière ; pour du code, ajouter les attributs de texte, un par ligne, au format « alt: valeur », en gardant les `{…}`) dans deux fichiers temporaires, puis lancer `python3 -I "${CLAUDE_SKILL_DIR}/scripts/compare.py" AVANT APRES`. Le script signale tout chiffre, variable, balise, lien, adresse e-mail ou citation modifiés (BLOQUANT), et les noms propres ajoutés ou retirés (À VÉRIFIER). Il ignore les espaces et la forme des guillemets : passer de “ ” à « » n'est pas bloquant.
2. **Relecture indépendante**, si l'outil Agent est disponible : lancer un agent qui reçoit seulement l'original, le résultat et cette liste, sans le raisonnement de la relecture :
   - aucun fait ajouté ni retiré (noms, chiffres, dates, lieux, promesses) ;
   - variables, balises et citations identiques ;
   - sens conservé (public visé, conviction, nuance) ;
   - aucune nouvelle tournure de la grille introduite, et le score du résultat ;
   - registre cohérent sur tout le texte.
   Il répond par passage : OK, ou le problème en une ligne.
3. Sans Agent : faire cette relecture soi-même, et le dire dans le rapport (« vérifié sans relecteur indépendant »).
4. Tout passage signalé par le script ou par le relecteur est **remis dans son état d'origine** et passe en fiche. Ne jamais livrer un passage qui a échoué.

## Reporter dans la source

Le texte relu vient souvent d'ailleurs que la conversation : le code d'un site, un CMS, un design, une présentation. Quand un outil permet d'y écrire, proposer d'y reporter les décisions ; sinon, rendre la liste des décisions à reporter à la main.

| Source | Comment écrire | Précautions |
|---|---|---|
| Markdown pur, fichiers de traduction | Edit sur le fichier, après avoir trouvé chaque occurrence par recherche | voir Textes d'interface pour les variables et les clés |
| Code d'un site ou d'une app (HTML, MDX, JSX, Vue, templates) | Edit sur le fichier | texte visible seulement : contenu des balises, `alt`, `title`, `aria-label`, `placeholder`, props de texte (`label`, `title`…), valeurs passées à une fonction de traduction. Jamais le balisage, les classes, les clés ni la logique. Échapper selon le contexte (`'` dans une chaîne entre apostrophes, `{` et `<` dans du JSX, `&` en HTML) |
| CMS connecté (Webflow, WordPress, Notion…) | l'outil de modification du connecteur, en mode brouillon (staged) | jamais un appel qui publie ou écrit directement en ligne ; si l'outil n'a pas de brouillon, liste à la main. Prévenir que les changements partiront à la prochaine publication du site, quelle que soit la personne qui la lance |
| Design Canva | les outils d'édition de Canva, puis l'enregistrement | l'enregistrement modifie le design tout de suite : proposer d'abord de travailler sur une copie. Après écriture, exporter une vignette des pages touchées et la montrer, pour vérifier qu'aucun texte ne déborde |
| Présentation PowerPoint (.pptx) | script Python avec `python-pptx`, sur une copie du fichier | vérifier d'abord `python3 -c "import pptx"` ; absent : demander avant d'installer quoi que ce soit, sinon liste à la main. Remplacer un passage seulement s'il tient dans un seul run (ou dans des runs de même mise en forme) ; sinon, liste à la main. Notes du présentateur : dans `notes_slide` seulement, jamais dans une zone de la slide |
| Google Docs, Google Slides | l'outil du connecteur, s'il a une fonction d'écriture | sinon, liste à la main |
| Keynote, PDF, outil non connecté | aucun | liste à la main |

Notes du présentateur (Canva, Google Slides) : seulement si l'outil y donne accès ; sinon, liste à la main.

Étapes :

1. **Trouver** chaque passage dans la source, exactement. S'il apparaît plusieurs fois (un titre repris en menu, une phrase dupliquée dans deux pages), le dire et demander si toutes les occurrences changent. S'il est introuvable (texte généré, traduit ou assemblé par le code), ne pas deviner : le mettre dans la liste à reporter à la main.
2. **Montrer** ce qui va changer, une ligne par endroit (fichier ou page, puis « avant → après »), et attendre un accord explicite (« applique »). Les décisions prises en fiche ne valent pas accord pour écrire dans une source distante.
3. **Sauvegarder** : fichier suivi par git sans modification en cours, ou copie de l'original ; pour un CMS ou un design, écrire l'état d'origine de chaque texte modifié dans un fichier de la session (pas seulement dans la conversation, qui peut être résumée).
4. **Écrire**, passage par passage.
5. **Relire la source** après écriture et comparer avec l'attendu (le script de « Vérification avant de livrer » sert aussi ici, sur le texte extrait). Code : lire d'abord les scripts du projet (`package.json` ou équivalent) et ne lancer qu'une vérification en lecture seule (lint ou typecheck sans `--fix` ni `--write`), jamais un build qui déploie, jamais une installation de dépendances ; sinon, dire « non vérifié ». Restaurer tout passage qui ne correspond pas.
6. **Ne jamais** publier un site, déployer, fusionner une branche, envoyer un e-mail ni partager un document : la personne le fait elle-même.

## Règles communes

Ne jamais relever ni reformuler une citation d'autrui (recommandation, témoignage, avis client) : c'est leur texte. Le vocabulaire métier d'un public (Head of Product, churn, MRR) n'est pas un calque à corriger.

## Selon le type de texte

- **Page web, libellé, FAQ, e-mail, newsletter** : grille complète.
- **Bio, page « À propos », lettre signée** : préférer la question à la reformulation (« qu'entends-tu par… ? »). Une proposition qui retire un élément du sens (public visé, conviction) est une faute.
- **Post LinkedIn ou autre réseau** : la question au lecteur et le « je » sont permis. Relever (niveau MOYEN) l'escalier de paragraphes d'une ligne, la chute-slogan et le « Et vous ? » mécanique.
- **Guide, livre blanc, support de formation** : grille complète sur le texte rédigé. Les intitulés courts (« Objectif », « Prérequis ») sont des libellés : les garder brefs et neutres, sans ton promotionnel. Les citations reproduites restent intactes.

- **Interface (app, logiciel, site applicatif)** : voir Textes d'interface.
- **Présentation (slides)** : voir Présentations.

### Textes d'interface

Boutons, libellés, messages d'erreur, états vides, onboarding, notifications, aide en ligne, souvent dans des fichiers de traduction (JSON, YAML, `.strings`, `.po`, `.arb`) ou dans le code.

- **Régularité voulue** : des boutons, erreurs ou confirmations construits pareil, c'est la cohérence d'une interface. Ne pas appliquer la grille §6 aux chaînes courtes ; la garder pour l'onboarding, l'aide et les textes de plus de deux phrases.
- **Variables et balises intouchables** : `{prenom}`, `%d`, `%@`, `{{count}}`, `{count, plural, …}`, `<b>`, `\n`. Chaque reformulation les garde toutes, à l'identique et sans en ajouter. Ne jamais modifier une clé de traduction, seulement la valeur. Vérifier aussi que chaque forme du pluriel est correcte en français (« 1 fichier », « 0 fichier »).
- **Longueur** : une reformulation n'est pas plus longue que l'original, sauf demande ou bouton trop vague (voir « Boutons explicites ») : dans ce cas, le dire dans la fiche. Si une limite est connue (bouton, titre de notification, écran mobile), l'indiquer dans la fiche avec le nombre de caractères.
- **Même nom pour la même chose** : relever le vocabulaire de l'interface (objets, actions) et signaler les doublons (« Supprimer » / « Effacer », « compte » / « profil », « Annuler » pour deux actions différentes). Type **langue**, niveau MOYEN, ou FORT si l'utilisateur peut se tromper d'action.
- **Forme des verbes** : une seule par type d'élément (boutons à l'infinitif « Enregistrer », ou à l'impératif « Enregistrez »). Signaler les écarts.
- **Boutons explicites** : le verbe dit ce qui se passe (« Supprimer le projet » plutôt que « OK » dans une confirmation de suppression).
- **Messages d'erreur** : dire ce qui s'est passé et quoi faire, sans reprocher ni s'excuser à l'excès (« Oups ! »). Un message vague (« Une erreur inattendue est survenue ») est à signaler : il ne dit ni la cause ni la suite.
- **Accessibilité** : relire aussi les textes alternatifs, `aria-label` et libellés pour lecteur d'écran. Un `alt` qui commence par « Image de » ou un bouton-icône sans libellé sont à signaler.
- **Ordre des fiches** : par écran ou par type d'élément (boutons, erreurs, états vides, aide) plutôt que dans l'ordre du fichier. Annoncer le regroupement choisi.

**Hors champ : l'accessibilité cognitive** (règles d'IHM adaptées aux personnes DYS, TDAH, TSA, FALC). Ce skill ne relit que la voix et la clarté des textes. Si un skill d'accessibilité cognitive est installé, le proposer à la fin du rapport ; sinon, le signaler en une ligne quand la demande porte sur ce sujet.

S'il existe un glossaire produit (même recherche que pour le guide de voix : `glossaire.md`, `glossary.md`, lien dans le `CLAUDE.md`, sinon une question), ses termes font référence.

Les règles propres à un projet passent avant cette grille (ex. une charte éditoriale qui impose la forme positive ou interdit le tiret cadratin).

### Présentations (slides)

PowerPoint, Keynote, Google Slides, Canva, ou texte collé.

- **Repérage** : fiches par numéro de slide et zone (« Slide 7, titre », « Slide 7, puce 2 », « Slide 7, notes »).
- **Notes du présentateur** : relues à part, avec la grille du post (registre oral, « je » et questions permis).
- **Régularité** : un gabarit répété (titre, sous-titre, pied de page) est normal. Relever en revanche les slides qui ont toutes trois puces de même longueur quand le contenu ne l'impose pas, et la slide « En résumé » qui répète les précédentes.
- **Titres** : un titre-slogan (« L'humain au cœur ») est FORT ; proposer un titre qui dit ce que montre la slide.
- **Longueur** : comme pour les interfaces, une reformulation n'est pas plus longue que l'original ; le texte doit tenir dans sa zone.
- **Mode « Corrige tout »** : jamais écrit directement dans le fichier ; rendre la liste des décisions, puis proposer « Reporter dans la source ».
- **Report dans le fichier** : voir le tableau de « Reporter dans la source » (PowerPoint, Canva, Google Slides, Keynote).

## Grille

### 1. Structures (les plus parlantes)

| Marqueur | Exemple typique | Piste de reformulation |
|---|---|---|
| Parallélisme négatif | « Ce n'est pas X, c'est Y », « Il ne s'agit pas seulement de X, mais de Y » | dire Y directement |
| Formule-choc en deux temps | « C'est simple et ça aide vraiment. », « Quelques minutes, et vous êtes des nôtres. » | le fait : « L'inscription prend 5 minutes. » |
| Deux-points de révélation | « … : autant d'économies pour l'association », « Le résultat ? » | une phrase liée normalement |
| Triade systématique | « innovant, inspirant et engagé » | un seul adjectif, le vrai, ou aucun |
| Phrase-slogan / titre-slogan | « On vous attend », « On commence quand vous voulez » | un titre qui dit ce que contient la section |
| Pseudo-clivée | « Ce qui fait bouger les choses, ce sont… », « C'est ce que nous faisons : » | sujet + verbe |
| Accroche en question | « Et si… ? », « Vous êtes-vous déjà demandé… ? » | commencer par l'information |
| Participe présent d'analyse en fin de phrase | « …, soulignant ainsi l'importance de… », « …, reflétant… » | couper, ou une seconde phrase avec un fait |
| Évitement de « être » | « se veut », « constitue », « sert de », « s'impose comme » | « est » |
| Conclusion ou résumé systématique | « En somme », « En résumé », « En conclusion » | s'arrêter quand c'est dit |
| Même idée reformulée deux fois | phrase d'intro puis phrase qui la répète | garder la meilleure |

### 2. Vocabulaire surreprésenté

Mots de style, pas de contenu. Les remplacer par le mot exact, ou les supprimer :

- importance gonflée : crucial, essentiel, incontournable, majeur, véritable, un tournant, ouvre la voie à, changer la donne ;
- décor : au cœur de, niché, riche (patrimoine, expérience), dynamique, vibrant, unique, d'exception ;
- verbes creux : plonger dans, explorer, naviguer, mettre en lumière, souligner, mettre en avant, favoriser, permettre de, booster, levier ;
- récits flatteurs : « qui a su », « a à cœur de », « animé·e par la passion de » ;
- abstractions vagues : « un soutien concret », « des actions concrètes », « chacun à sa façon », « une expérience enrichissante » ;
- précautions : « Il est important de noter que », « il convient de souligner », « Il est essentiel de » ;
- attributions vagues : « les experts estiment », « selon certains observateurs » ;
- ouvertures : « Dans un monde où », « À l'ère de », « Plongeons dans », « Parlons de », « Voici comment… » ;
- clôtures : « Et vous ? », « Et ça change tout. », « et bien plus encore », « en toute sérénité » ;
- connecteurs en série : « De plus », « Par ailleurs », « En effet », « Ainsi », « tout en + participe » ;
- lexique corporate : accompagner, valoriser, s'inscrire dans, dans le cadre de, écosystème, parcours, aventure, synergie, fort de, en termes de, pleinement, profondément.

Ces mots sont aussi du français courant : les remplacer quand ils sont creux, les garder quand ils disent quelque chose de précis. Test simple : si le mot peut sauter sans que le sens change, proposer de le retirer.

### 3. Mise en forme et typographie

- Tiret d'incise **en série** (plus d'un par paragraphe) : virgules, parenthèses ou deux phrases. Un tiret d'incise isolé est correct en français. Les projets qui interdisent le cadratin gardent leur règle.
- Gras semé partout ; puces qui commencent par « **Intitulé :** » ; listes à puces pour ce qui tient en une phrase.
- Emojis en tête de puce ou de titre (sauf charte qui les prévoit).
- Titres à l'anglaise (Une Majuscule À Chaque Mot) : une seule majuscule en français.
- Guillemets anglais ou droits : « » avec espaces insécables (les guillemets anglais restent justes pour une citation dans une citation).
- Espace insécable avant `:` et dans « », fine insécable (ou insécable) avant `; ! ?` ; absente : souvent un texte venu d'un outil anglophone (mais beaucoup de gens tapent sans).
- Tableau ou titres de sections pour un texte court.

### 4. Ton

- Promotionnel, façon communiqué ou guide de voyage, alors que le contexte demande de l'information.
- Enthousiasme générique, flatterie (« Excellente question ! »), superlatifs.
- Registre incohérent : tu et vous mêlés, « on » et « nous » mélangés, écriture inclusive appliquée par endroits. Vérifier chaque paire séparément (tu/vous, on/nous, inclusif/masculin), paragraphe par paragraphe puis sur tout le document. Un vouvoiement isolé dans une lettre signée peut être voulu : « à trancher ».
- Ton uniforme du début à la fin, aucune prise de position, aucune expérience vécue : si la source en contient, la garder ; sinon ne pas en inventer.
- Restes de conversation : « J'espère que cela vous aide », « N'hésitez pas à… », « Voici une version… ».

### 5. Calques de l'anglais

Niveau fort : « faire sens » (→ avoir du sens), « adresser un problème » (→ traiter), « en charge de » (→ chargé de).

Niveau faible (usage installé, préférence de style) : « impacter », « opportunité » au sens d'occasion, « digital » (mot du métier en marketing), « au final ».

### 6. Régularité

La structure imposée par le format est normale : 4 réponses par question de quiz, une case par ligne de tableau, des fiches produit au même gabarit. Ce qui trahit l'IA, c'est la **prose libre** coulée dans le même moule :
- paragraphes ou profils de **même longueur à quelques mots près** ;
- même **forme de phrase** répétée d'un item à l'autre (titre court + une phrase + une chute) ;
- même **formule de clôture** à chaque bloc (« Ton astuce : … », « Le résultat : … ») ;
- listes toujours du même nombre d'items quand le contenu ne l'impose pas ;
- finition uniforme : aucune hésitation, aucun mot familier qui dépasse, sur tout le document.

Piste de reformulation : varier la longueur selon ce qu'il y a à dire, retirer la formule répétée là où elle n'apporte rien, laisser la personne remettre ses propres mots.

## Hors grille

Signaler aussi, au même format : rupture de personne ou de nombre, accord douteux, titre qui annonce autre chose que son contenu, même mot écrit de deux façons (« e-mail » / « email »). Ce ne sont pas des marqueurs d'IA, mais une relecture qui les laisse passer n'est pas finie.

## Niveau de preuve (pour expliquer un choix)

- Solides : guide Wikipédia « Signs of AI writing » (en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) ; étude Kobak et al. sur le vocabulaire en excès des résumés PubMed (arXiv 2406.07016, liste : github.com/berenslab/llm-excess-vocab).
- Relayés par la presse française : tiret cadratin (Siècle Digital, Blog du Modérateur), « ce n'est pas X, c'est Y », triades, « il est important de noter ».
- Observés en relecture (tournures refusées sur des textes réels) : formules-chocs en deux temps, slogans en titre, deux-points de révélation, pseudo-clivées, abstractions vagues.
- Pas de liste française mesurée statistiquement : les équivalents français du vocabulaire sont des transpositions.
