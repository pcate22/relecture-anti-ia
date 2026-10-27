---
type: regex
pattern: '\{prenom\}[\s\S]*\{count, plural, one \{# fichier\} other \{# fichiers\}\}'
target: { source: file, path: fr.json }
---
