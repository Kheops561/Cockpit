# Mettre le formulaire de contact en service

Le formulaire de `contact.html` envoie le message **directement**, sans
passer par la messagerie du visiteur. Il lui faut donc un serveur, et un
seul morceau de code y tourne : `api/contact.js`.

Le site reste un ensemble de fichiers statiques. `api/contact.js` reçoit le
formulaire, le contrôle, puis fait partir le message par l'API **Resend**.

**Le navigateur n'appelle jamais Resend.** Il ne parle qu'au site lui-même,
sur `/api/contact`. C'est la fonction, et elle seule, qui contacte l'API. La
clé ne quitte donc jamais le serveur et ne figure pas dans le dépôt.

## Où le site est publié

Le projet est déployé sur **Vercel**, qui sert les pages statiques et
exécute les fonctions du dossier `api/`. Aucune configuration
supplémentaire n'est nécessaire : Vercel reconnaît ce dossier tout seul.

L'aperçu de travail est `https://amelie-invest-phi.vercel.app`. Le domaine
`amelie-invest.com` pointe pour l'instant ailleurs : le jour où il sera
basculé sur Vercel, la marche à suivre est au point 4.

## 1. Créer la clé Resend

1. Sur [resend.com](https://resend.com), ajouter le domaine
   `amelie-invest.com` et suivre la procédure de vérification : Resend donne
   des enregistrements DNS (SPF, DKIM) à créer dans la zone DNS **OVH**, où
   le domaine est géré. Tant que le domaine n'est pas vérifié, l'envoi est
   refusé.
2. Créer une clé d'API avec le **droit d'envoi seulement**.
3. Choisir la région de traitement dans le compte Resend. Ce choix a des
   conséquences sur la page « Données personnelles » : voir le point 5.

Tant que le domaine n'est pas vérifié, il est possible de tester avec le
domaine d'essai fourni par Resend (`onboarding@resend.dev`) : les messages
ne partent alors que vers l'adresse du compte Resend.

## 2. Déclarer les variables sur Vercel

Dans le projet Vercel : **Settings → Environment Variables**. Trois
variables, à cocher pour *Production*, *Preview* et *Development* :

| Nom | Valeur | Obligatoire |
| --- | --- | --- |
| `RESEND_API_KEY` | `re_xxxxxxxxxxxxxxxxxxxx` | oui |
| `CONTACT_TO` | `contact@amelie-invest.com` | non, c'est la valeur par défaut |
| `CONTACT_FROM` | `Amélie & Partners <site@amelie-invest.com>` | non, c'est la valeur par défaut |

**La clé ne doit jamais être versionnée.** Si elle a été exposée, la
révoquer dans Resend et en créer une autre.

Le domaine de `CONTACT_FROM` doit être celui vérifié à l'étape 1.

Après avoir ajouté ou modifié une variable, **redéployer** : les variables
ne sont lues qu'au démarrage de la fonction.

## 3. Vérifier

- Envoyer un message depuis `contact.html` : il doit arriver sur l'adresse
  destinataire, avec le visiteur en adresse de réponse.
- Désactiver JavaScript et recommencer : le formulaire part en envoi
  classique et la page revient avec `?envoi=ok`.
- Ouvrir la page sur un serveur qui n'exécute pas `api/contact.js` (un
  simple `python3 -m http.server`, par exemple) : l'envoi échoue, et le
  message d'erreur propose un lien qui reprend la saisie dans la messagerie
  du visiteur. Rien de ce qui a été écrit n'est perdu.

En cas d'échec, le détail part dans les journaux Vercel (**Deployments →
Functions → Logs**) ; le visiteur, lui, ne voit qu'un message général. C'est
volontaire : il ne doit rien apprendre de la configuration.

## 4. Le jour où le domaine bascule sur Vercel

1. Dans le projet Vercel : **Settings → Domains**, ajouter
   `amelie-invest.com` et `www.amelie-invest.com`.
2. Dans la zone DNS OVH, remplacer l'enregistrement `A` de l'apex et le
   `CNAME` du `www` par les valeurs que Vercel indique.
3. **Ne pas toucher aux enregistrements `MX`, `SPF`, `DKIM` et `DMARC`** :
   les boîtes aux lettres restent chez OVH, et ces enregistrements portent
   aussi la vérification Resend. Les supprimer casserait à la fois la
   réception du courrier et l'envoi du formulaire.
4. Mettre à jour la mention de l'hébergeur dans `mentions-legales.html`.

## 5. Ce qui reste à trancher

- **La région de traitement Resend.** Si elle est hors Union européenne, la
  page « Données personnelles » doit citer le mécanisme de transfert
  applicable. La mention est en attente sur cette page.
- **L'adresse d'expédition.** `site@amelie-invest.com` est une proposition ;
  toute adresse du domaine vérifié convient.

## Protection contre les envois automatisés

Elle est entièrement dans la fonction, sans service extérieur :

- un champ piège, masqué et hors du parcours au clavier, qui doit rester
  vide ;
- un contrôle du délai : un formulaire rempli en moins de trois secondes
  n'a pas été rempli par une personne ;
- une revalidation complète côté serveur : les listes déroulantes ne
  prennent que les valeurs proposées, les longueurs sont bornées, les
  caractères de contrôle sont retirés.

Dans les deux premiers cas, la fonction répond « message reçu » sans rien
envoyer : un robot ne doit pas apprendre qu'il a été repéré.

Un service comme Cloudflare Turnstile a été écarté : il faudrait charger un
script depuis un domaine tiers dans les pages, ce que le cahier des charges
interdit. Si cette protection devenait insuffisante, ce serait un arbitrage
à reprendre avec Amélie.
