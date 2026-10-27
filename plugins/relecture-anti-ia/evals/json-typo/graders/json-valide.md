---
type: llm
focus: { source: file, path: fr.json }
---
PASS si le contenu est un JSON valide (guillemets, virgules et accolades corrects), avec exactement les quatre clés welcome, files, delete_confirm, help, et l'adresse aide@exemple.fr intacte.
FAIL sinon.
