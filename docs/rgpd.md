# Sécurité et RGPD

## Nature des données

Le système utilise des données biométriques sous forme d'encodages faciaux.
Ces données permettent d'identifier une personne et doivent donc être protégées.

## Mesures appliquées dans le projet

- Aucune photo réelle n'est publiée sur GitHub.
- Les fichiers de visages connus sont stockés uniquement en local dans `data/known_faces`.
- Les fichiers CSV réels de journalisation sont ignorés par Git.
- Les données sensibles ne doivent pas être envoyées sur un dépôt public.
- Le Raspberry Pi doit être placé dans un boîtier fermé.
- La caméra peut être visible, mais le Raspberry Pi et le câblage doivent être protégés.
- La serrure est commandée par MOSFET afin d'isoler la commande 3,3 V du circuit 12 V.

## Risque en cas de vol du Raspberry Pi

Si le Raspberry Pi est volé, une personne pourrait tenter d'accéder aux fichiers locaux.
Pour réduire ce risque, la version finale prévoit :

- suppression des photos après génération des encodages ;
- stockage uniquement des encodages faciaux ;
- chiffrement des encodages ;
- clé de chiffrement non stockée dans le code ;
- base de données locale protégée ;
- journalisation des accès sans photo brute.

## Données sur GitHub

Le dépôt GitHub contient uniquement :

- le code source ;
- les tests unitaires ;
- la documentation ;
- les exemples fictifs.

Il ne contient pas :

- de vraies photos ;
- de vrais encodages biométriques ;
- de vraie base de données ;
- de clé secrète.