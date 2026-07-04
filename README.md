# Système de contrôle d'accès par reconnaissance faciale

Projet de système embarqué permettant de contrôler l'accès à une porte à l'aide de la reconnaissance faciale.

Le système repose sur une caméra, un Raspberry Pi, une reconnaissance faciale en Python, une commande GPIO et une serrure électrique 12 V commandée par MOSFET.

## Objectif du projet

L'objectif est de concevoir un prototype capable de :

- détecter un visage à l'aide d'une caméra ;
- comparer ce visage avec une base locale d'utilisateurs autorisés ;
- autoriser ou refuser l'accès ;
- commander une serrure électrique 12 V ;
- enregistrer les événements d'accès ;
- respecter les contraintes de sécurité et de protection des données.

## Architecture générale

```text
Utilisateur
    |
Caméra
    |
OpenCV
    |
Reconnaissance faciale
    |
Décision autorisé / refusé
    |
GPIO17 Raspberry Pi
    |
MOSFET
    |
Serrure électrique 12 V
    |
Journalisation CSV
```

## Technologies utilisées

- Python 3.11
- OpenCV
- face_recognition
- NumPy
- Pytest
- Raspberry Pi
- GPIOZero
- Git / GitHub

## Structure du projet

```text
src/smart_door_lock/
├── access_control.py
├── access_service.py
├── camera.py
├── config.py
├── database.py
├── face_encoding.py
├── face_recognition_adapter.py
├── face_repository.py
├── lock_control.py
├── main.py
├── opencv_camera.py
├── raspberry_gpio_lock.py
├── recognition.py
└── workflow.py
```

## Matériel prévu

- Raspberry Pi 4
- Caméra USB ou caméra Raspberry Pi
- Carte microSD
- Alimentation Raspberry Pi 5 V
- Serrure électrique 12 V
- Alimentation externe 12 V
- MOSFET logique N-channel compatible 3,3 V
- Résistance 220 ohms
- Résistance 10 kOhms
- Diode de roue libre 1N4007
- Câbles et boîtier

## Installation

Cloner le projet :

```bash
git clone https://github.com/Hdmourad/controle-acces-reconnaissance-faciale.git
cd controle-acces-reconnaissance-faciale
```

Installer le projet en mode développement :

```bash
python -m pip install -e .
```

Installer les dépendances :

```bash
python -m pip install -r requirements.txt
```

## Lancer les tests

```bash
pytest
```

Résultat actuel :

```text
43 passed
```

## Lancement de la démonstration simulée

```bash
python -m smart_door_lock.main
```

Cette démonstration simule :

- une personne reconnue ;
- une autorisation d'accès ;
- l'ouverture de la serrure simulée ;
- la journalisation de l'accès.

## Sécurité et RGPD

Le dépôt GitHub ne contient aucune donnée biométrique réelle.

Les photos, encodages faciaux, bases locales et journaux réels doivent rester uniquement sur la machine locale ou sur le Raspberry Pi.

Mesures prévues :

- aucune photo réelle publiée sur GitHub ;
- encodages biométriques stockés localement ;
- possibilité de chiffrement des encodages ;
- clé secrète non stockée dans le code ;
- Raspberry Pi placé dans un boîtier fermé ;
- commande serrure isolée par MOSFET ;
- journalisation sans stockage de photos brutes.

## Câblage MOSFET

Le câblage est documenté dans :

```text
hardware/wiring_mosfet.md
```

Principe :

```text
GPIO17 Raspberry Pi
→ résistance 220 ohms
→ Gate MOSFET
→ serrure 12 V
```

Le Raspberry Pi ne doit jamais alimenter directement la serrure 12 V.

## Auteur

Projet développé par Mourad HADJI dans le cadre du Mastère Expert en Robotique et Systèmes Embarqués.