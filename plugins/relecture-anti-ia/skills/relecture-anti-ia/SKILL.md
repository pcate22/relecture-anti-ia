---
name: relecture-anti-ia
description: Relire un texte en français et rendre un rapport détaillé des tournures typiques d'une IA (ChatGPT, Claude, Gemini) : chaque passage cité dans son contexte, niveau estimé, reformulations proposées. La personne qui écrit tranche : rien n'est modifié sans son accord, sauf le mode « Corrige le simple » (langue et registre) quand elle le demande. À utiliser avant de livrer un texte web ou pro destiné à être lu par d'autres (page web, FAQ, post LinkedIn, e-mail, newsletter, slide, textes d'interface d'une app ou d'un logiciel : boutons, messages d'erreur, onboarding, fichiers de traduction), et dès que l'utilisateur dit « ça fait IA », « phrase IA », « trop ChatGPT », « pas naturel », « réécris plus simple », même sans dire « anti-IA ». Ne s'applique pas à la fiction.
---

# Relecture anti-IA (français)

But : aider la personne qui écrit à rendre un texte tel qu'elle l'aurait écrit elle-même. Le skill **montre et propose, il ne corrige pas** : aucune modification du texte ou du fichier sans son accord, passage par passage. Seule exception, à sa demande : le mode « Corrige le simple » (voir plus bas), limité à la langue et au registre.

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

**Ce que vaut une réponse** : choisir A ou B sur une fiche vaut accord pour ce passage seulement. Fichier à portée : le modifier pour ce passage, rien d'autre. Texte collé dans la conversation ou fichier hors de portée : noter la décision pour la liste finale.

**Demande de réécriture explicite** (« réécris plus simple ce paragraphe ») : ne pas dérouler le rapport. Proposer directement une version réécrite, sans fait ajouté, en gardant intactes les variables et les citations, puis lister en une ligne les marqueurs retirés. La personne garde, ajuste ou refuse.

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

**3. Le détail, une fiche à la fois, dans l'ordre du texte** (section par section ; pour une interface, voir « Ordre des fiches » dans Textes d'interface) : sans cet ordre, on ne suit plus. Montrer une seule fiche, attendre la réponse, l'appliquer seulement si elle a été choisie, puis passer à la suivante. Annoncer la position (« 3 sur 8 »). La fiche suit toujours cet ordre :

> **3 sur 8. [FORT, tournure IA] Page d'accueil, section « Qui suis-je »**
> « Consultante en stratégie digitale, j'accompagne les PME. **Mon approche ? Simple et efficace** : **placer l'humain au cœur de** chaque projet. »
> Pourquoi : accroche en question, formule-choc en deux temps, « au cœur de ».
> A. « Consultante en stratégie digitale, j'aide les PME à choisir leurs outils et à former leurs équipes. »
> B. Garder tel quel.
> Question : « l'humain », concrètement, ce sont les équipes, les clients, ou les deux ?

- **Contexte** : la phrase entière, plus celle d'avant ou d'après si elle éclaire le choix ; le passage en cause en **gras**. Jamais un fragment isolé : sans contexte, on ne peut pas trancher.
- **Pourquoi** : une ligne, le marqueur de la grille (ou « hors grille »).
- **Niveau et type** en tête : **FORT** (tournure typique, gratuite, ou plusieurs marqueurs dans le même paragraphe), **MOYEN** (marqueur réel, mais qui peut être un choix de voix), **FAIBLE** (habitude humaine courante).
- **Choix** : une ou deux reformulations (A, B…) qui gardent chaque fait, nom et nuance, et toujours « Garder tel quel ». Une question si le sens est incertain. Jamais d'exemple, de chiffre ou d'anecdote absents de la source : dans l'exemple ci-dessus, la proposition A ne vaut que si la source parle d'outils et de formation ; sinon, poser seulement la question.

**Pendant les fiches** :
- Quand un fait est corrigé, chercher tout de suite les autres endroits du document qui le répètent (ex. un tarif corrigé dans la section « Offre », encore présent dans la FAQ) et les proposer dans la même fiche.
- Une décision vaut pour la suite : si un passage reformulé contient un marqueur qu'il a déjà été décidé de réduire, l'appliquer et le dire.
- Quand la personne dicte en vrac (souvenirs, avis, ce qu'elle veut dire), mettre en forme **avec ses mots** : ordre, ponctuation, accords, rien d'autre. Ne pas inventer d'humour, d'émotion ou de détail ; si le cadre en demande, le lui dire et la laisser compléter. Signaler une ambiguïté par une question courte.
- Fichier source hors de portée (PDF, outil en ligne) : ne rien modifier, garder la liste des décisions.

**Deux modes plus rapides, seulement si la personne les demande** (par défaut : une fiche à la fois) :
- **« Corrige le simple »** : appliquer directement au fichier les corrections de type **langue** (typographie, accords, graphies en double) et **registre** (une fois le registre connu, par le guide de voix ou par une seule question ; hors citations d'autrui et hors cas « à trancher », qui restent en fiche). Dans un fichier de traduction ou de code : modifier les valeurs seulement, jamais les clés, délimiteurs, guillemets de syntaxe, apostrophes d'échappement (ICU), variables ni balises ; vérifier ensuite que le fichier se lit encore (JSON, YAML…), sinon annuler et passer en fiches. Puis lister chaque changement au format « avant → après », et enchaîner sur les fiches pour le reste. Jamais pour les tournures IA, le ton, la régularité ni les brouillons : ces choix restent passage par passage. Hors fichier (texte collé dans la conversation), rendre le texte corrigé au lieu de modifier un fichier.
- **« Tout d'un coup »** : montrer toutes les fiches retenues dans un seul tableau numéroté (passage, pourquoi, A, B), et accepter une réponse en une ligne (« 1A, 2 garder, 3B… »). Rien n'est appliqué sans réponse pour chaque numéro ; un numéro sans réponse reste inchangé et est rappelé à la fin.

**4. Après la dernière fiche** : la liste complète des décisions, dans l'ordre suivi pour les fiches, au format « avant → après » (et les passages gardés tels quels), prête à reporter dans le fichier source ; les niveaux et types non traités en une ligne chacun (dans l'ordre du texte), puis les sections relues sans rien relever et ce qui y a été vérifié.

**5. La réponse attendue**, sous chaque fiche : « A, B, garder, ou ta réponse. » (ou « votre réponse » si la personne vouvoie : suivre son registre) On n'applique que ce qui a été choisi, et rien sans réponse.

Ne jamais relever ni reformuler une citation d'autrui (recommandation, témoignage, avis client) : c'est leur texte. Le vocabulaire métier d'un public (Head of Product, churn, MRR) n'est pas un calque à corriger.

## Selon le type de texte

- **Page web, libellé, FAQ, e-mail, newsletter** : grille complète.
- **Bio, page « À propos », lettre signée** : préférer la question à la reformulation (« qu'entends-tu par… ? »). Une proposition qui retire un élément du sens (public visé, conviction) est une faute.
- **Post LinkedIn ou autre réseau** : la question au lecteur et le « je » sont permis. Refuser l'escalier de paragraphes d'une ligne, la chute-slogan et le « Et vous ? » mécanique.
- **Guide, livre blanc, support de formation, slides** : grille complète sur le texte rédigé. Les intitulés courts (« Objectif », « Prérequis ») sont des libellés : les garder brefs et neutres, sans ton promotionnel. Les citations reproduites restent intactes.

- **Interface (app, logiciel, site applicatif)** : voir la section suivante.

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

S'il existe un glossaire produit (même recherche que pour le guide de voix : `glossaire.md`, `glossary.md`, lien dans le `CLAUDE.md`, sinon une question), ses termes font référence.

Les règles propres à un projet passent avant cette grille (ex. une charte éditoriale qui impose la forme positive ou interdit le tiret cadratin).

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
| Accroche en question | « Et si… ? », « Vous êtes-vous déjà demandé… ? », « Voici comment… » | commencer par l'information |
| Participe présent d'analyse en fin de phrase | « …, soulignant ainsi l'importance de… », « …, reflétant… » | couper, ou une seconde phrase avec un fait |
| Évitement de « être » | « se veut », « constitue », « sert de », « s'impose comme » | « est » |
| Conclusion ou résumé systématique | « En somme », « En résumé », « En conclusion », « Malgré ces défis… » | s'arrêter quand c'est dit |
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
- ouvertures : « Dans un monde où », « À l'ère de », « Plongeons dans », « Parlons de » ;
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
- Espace insécable avant `:` et dans « », fine insécable (ou insécable) avant `; ! ?` ; absente = texte collé d'un outil anglophone.
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
