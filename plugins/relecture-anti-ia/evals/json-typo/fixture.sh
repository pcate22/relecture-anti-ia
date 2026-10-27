#!/bin/bash
set -e
cat > fr.json <<'JSON'
{
  "welcome": "Bonjour {prenom}, ravi de vous revoir!",
  "files": "{count, plural, one {# fichier} other {# fichiers}}",
  "delete_confirm": "Voulez vous vraiment supprimer ce projet?",
  "help": "Besoin d'aide? Ecris-nous à aide@exemple.fr"
}
JSON
git init -q && git add fr.json && git -c user.email=e@e -c user.name=e commit -qm init
