# Mettre le formulaire de contact en service

Le site reste un ensemble de fichiers statiques. `contact.php` est le seul
composant serveur : il reçoit le formulaire et fait envoyer le message par
Resend.

**Le navigateur n'appelle jamais Resend.** Il ne parle qu'à
`amelie-invest.com`. C'est le serveur, et lui seul, qui contacte l'API. La
clé d'API ne quitte donc jamais le serveur et ne figure pas dans le dépôt.

## 1. Vérifier que l'hébergement OVH sait exécuter PHP

Il faut une offre OVH avec PHP 8.0 ou plus récent et l'extension cURL, ce
qui est le cas des hébergements mutualisés courants. Sur une offre
strictement statique, le formulaire ne fonctionnera pas.

Pour vérifier : déposer un fichier `test.php` contenant
`<?php phpinfo();`, l'ouvrir dans un navigateur, **puis le supprimer**.

## 2. Créer la clé Resend

1. Sur [resend.com](https://resend.com), ajouter le domaine
   `amelie-invest.com` et suivre la procédure de vérification : Resend
   donne des enregistrements DNS (SPF, DKIM) à créer dans la zone DNS OVH.
   Tant que le domaine n'est pas vérifié, l'envoi est refusé.
2. Créer une clé d'API avec le **droit d'envoi seulement**.
3. Choisir la région de traitement dans le compte Resend. Ce choix a des
   conséquences sur la page « Données personnelles » : voir le point 5.

## 3. Déposer la configuration sur le serveur

Copier `contact-config.example.php` sous le nom `contact-config.php`, à la
racine du site, et le remplir :

```php
return [
    'cle_resend'   => 're_xxxxxxxxxxxxxxxxxxxx',
    'expediteur'   => 'Amélie & Partners <site@amelie-invest.com>',
    'destinataire' => 'contact@amelie-invest.com',
];
```

`contact-config.php` est exclu du dépôt par `.gitignore`. **La clé ne doit
jamais être versionnée.** Si elle a été exposée, la révoquer dans Resend et
en créer une autre.

Le domaine de l'expéditeur doit être celui vérifié à l'étape 2.

## 4. Vérifier

- Envoyer un message depuis `contact.html` : il doit arriver sur l'adresse
  destinataire, avec le visiteur en adresse de réponse.
- Désactiver JavaScript et recommencer : le formulaire part en envoi
  classique et la page revient avec `?envoi=ok`.
- Envoyer six messages d'affilée : le sixième doit être refusé. La limite
  est de cinq par heure et par adresse IP.

En cas d'échec, le détail part dans le journal d'erreurs PHP de
l'hébergement ; le visiteur, lui, ne voit qu'un message général. C'est
volontaire : il ne doit rien apprendre de la configuration.

## 5. Ce qui reste à trancher

- **La région de traitement Resend.** Si elle est hors Union européenne, la
  page « Données personnelles » doit citer le mécanisme de transfert
  applicable. La mention est en attente sur cette page.
- **L'adresse d'expédition.** `site@amelie-invest.com` est une proposition ;
  toute adresse du domaine vérifié convient.

## Protection contre les envois automatisés

Elle est entièrement côté serveur, sans service extérieur :

- un champ piège, masqué et hors du parcours au clavier, qui doit rester
  vide ;
- un contrôle du délai : un formulaire rempli en moins de trois secondes
  n'a pas été rempli par une personne ;
- une limite de cinq envois par heure et par adresse IP.

Un service comme Cloudflare Turnstile a été écarté : il faudrait charger un
script depuis un domaine tiers dans les pages, ce que le cahier des charges
interdit. Si cette protection devenait insuffisante, ce serait un arbitrage
à reprendre avec Amélie.
