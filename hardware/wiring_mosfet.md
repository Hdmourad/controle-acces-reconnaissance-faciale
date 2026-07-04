# Câblage MOSFET pour serrure 12 V

## Objectif

Commander une serrure électrique 12 V à partir d'un Raspberry Pi.

Le Raspberry Pi ne peut pas alimenter directement une serrure 12 V.
Il envoie seulement un signal logique 3,3 V sur un GPIO.

Le MOSFET joue le rôle d'interrupteur électronique.

## Matériel

- Raspberry Pi 4
- Serrure électrique 12 V
- Alimentation 12 V externe
- MOSFET logique N-channel compatible 3,3 V
- Résistance 220 ohms pour la Gate
- Résistance 10 kOhms pull-down
- Diode de roue libre 1N4007 ou équivalent
- Câbles

## Connexions

```text
Raspberry Pi GPIO17
    |
    | résistance 220 ohms
    |
Gate MOSFET

Source MOSFET
    |
GND alimentation 12 V
    |
GND Raspberry Pi

+12 V alimentation
    |
+ serrure électrique

- serrure électrique
    |
Drain MOSFET
```

## Diode de protection

La diode est placée en parallèle sur la serrure.

```text
Cathode diode côté +12 V
Anode diode côté Drain MOSFET
```

Elle protège le circuit contre les surtensions générées par la serrure.

## Sécurité

- Ne jamais connecter le 12 V directement au Raspberry Pi.
- Relier le GND Raspberry Pi et le GND alimentation 12 V.
- Utiliser un MOSFET compatible avec une commande logique 3,3 V.
- Tester d'abord avec une LED avant de brancher la serrure.
- Mettre le Raspberry Pi et le câblage dans un boîtier fermé.

## Justification technique

Le GPIO du Raspberry Pi fournit seulement un signal logique 3,3 V.
Il ne peut pas fournir le courant nécessaire à une serrure 12 V.

Le MOSFET permet donc de séparer :

- la partie commande : Raspberry Pi 3,3 V ;
- la partie puissance : alimentation 12 V de la serrure.

Ce choix protège le Raspberry Pi et rend le système plus fiable.