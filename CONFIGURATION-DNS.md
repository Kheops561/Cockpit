# Configuration DNS chez OVH

Trois chantiers **indépendants**, à ne pas mélanger :

- **0 · Envoyer dès maintenant.** Aucun réglage DNS. Les essais partent
  depuis l'adresse de travail, avec un expéditeur provisoire.
- **A · Le formulaire au nom du domaine** (Resend). Trois enregistrements sur
  des sous-domaines. Aucun effet sur le site en ligne ni sur les boîtes aux
  lettres.
- **B · La bascule du site vers Vercel.** C'est elle, et elle seule, qui
  retire le site de Showit. À faire quand le nouveau site est validé.

## Règle d'or

**Ne jamais supprimer ni modifier les entrées `MX` de la racine, le `TXT` de
SPF de la racine, ni les clés DKIM d'OVH.** Ce sont vos boîtes aux lettres
`@amelie-invest.com`. Les toucher coupe la réception du courrier.

Tous les enregistrements ajoutés ci-dessous portent sur des **sous-domaines**
(`send.`, `resend._domainkey.`) ou remplacent des entrées précises. Rien
d'autre ne bouge.

## État actuel, relevé le 10 septembre 2026

| Nom | Type | Valeur | Qui c'est |
|---|---|---|---|
| `amelie-invest.com` | A | `75.101.134.27` | Showit (via Amazon) |
| `www.amelie-invest.com` | A | `75.101.134.27` | Showit |

Les `MX`, `SPF` et `DKIM` n'ont pas pu être relevés depuis l'environnement de
travail. Avant de commencer, ouvrez la zone DNS chez OVH et **notez tout ce
qui existe** : c'est votre filet de sécurité.

Où trouver la zone : `ovh.com` → **Web Cloud** → **Noms de domaine** →
`amelie-invest.com` → onglet **Zone DNS**.

---

# 0 · Envoyer dès maintenant, sans toucher au DNS

Le site de travail est `https://amelie-invest-phi.vercel.app`. Le formulaire
y poste sur `/api/contact`, c'est-à-dire sur lui-même : **cette adresse n'a
besoin d'aucun réglage DNS.**

Le seul obstacle est l'expéditeur. Resend refuse d'écrire au nom d'un domaine
qu'il n'a pas vérifié. Or `joytalents.com` **est déjà vérifié** sur le compte,
en `eu-west-1`, avec l'envoi autorisé. Il suffit donc de s'en servir le temps
des essais.

Dans le projet Vercel → **Settings** → **Environment Variables** :

| Nom | Valeur pour les essais |
|---|---|
| `RESEND_API_KEY` | la clé Resend, avec le **droit d'envoi seulement** |
| `CONTACT_FROM` | `Amélie & Partners <site@joytalents.com>` |
| `CONTACT_TO` | l'adresse où vous voulez recevoir les essais |

Puis **redéployer** : les variables ne sont lues qu'au démarrage.

Les messages partiront alors vers n'importe quel destinataire, avec le
visiteur en adresse de réponse. Seul le domaine de l'expéditeur est
provisoire : c'est ce que le chantier A corrige.

## Contrôler que tout est en place

Ouvrez `https://amelie-invest-phi.vercel.app/api/contact` dans un navigateur.
La fonction répond en JSON :

```json
{ "ok": true, "fonction": "contact", "cle": true, "expediteur": true, "destinataire": true }
```

- **Page introuvable** : la fonction n'est pas déployée. Vérifiez que le
  projet Vercel est bien relié au dépôt `Kheops561/Cockpit` et que le dernier
  commit est déployé.
- **`"cle": false`** : `RESEND_API_KEY` manque, ou le projet n'a pas été
  redéployé depuis qu'elle a été ajoutée.

Aucune valeur n'est révélée par ce contrôle, seulement leur présence.

---

# A · Le formulaire de contact

Le formulaire de `formulaire.html` envoie le message par **Resend**. Pour que
Resend ait le droit d'écrire au nom du domaine, il faut lui prouver que le
domaine vous appartient. C'est tout ce que font ces trois enregistrements.

## A.1 · Le domaine est déjà déclaré

`amelie-invest.com` a été créé dans Resend le 10 septembre 2026, en région
**Europe (Ireland) · `eu-west-1`**, suivi d'ouverture et suivi des clics
désactivés — ils réécrivent les liens et déposent des mouchards, ce que le
site s'interdit.

La région compte : c'est elle qui décide où les messages sont traités.
`eu-west-1` garde le traitement dans l'Union européenne, ce qui évite d'avoir
à citer un mécanisme de transfert sur la page « Données personnelles ». C'est
déjà la région de `joytalents.com`.

Il reste à poser les trois enregistrements ci-dessous. Tant qu'ils ne sont
pas en place, le domaine reste au statut `not_started` et l'envoi à son nom
est refusé.

## A.2 · Reporter les trois enregistrements chez OVH

Dans OVH, **Zone DNS** → **Ajouter une entrée**, une par une. Ce sont les
valeurs réelles de votre domaine, telles que Resend les a générées :

**1 · La clé DKIM** — c'est elle qui signe les messages.

| Champ | Valeur |
|---|---|
| Type | `TXT` |
| Sous-domaine | `resend._domainkey` |
| TTL | par défaut |

```
p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDAuL397Tg17cjRDFajVZtEe+enxrX4MMxjjP11F6DTfXpmgvpJ9n4LqY5hXXprh7V0UAgA8YRTY2O1N5fsUGep3utyORx5srdlM5Tp9SMaEcRSfgrYf7sRRHPC0xfj65mYXQK2Jq6KVEm+VMwo3Y2okepv7Jj3IbCSPVE6r6+tVQIDAQAB
```

**2 · Le MX des retours d'envoi**

| Champ | Valeur |
|---|---|
| Type | `MX` |
| Sous-domaine | `send` |
| Cible | `feedback-smtp.eu-west-1.amazonses.com.` |
| Priorité | `10` |

**3 · Le SPF de ce sous-domaine**

| Champ | Valeur |
|---|---|
| Type | `TXT` |
| Sous-domaine | `send` |
| Valeur | `v=spf1 include:amazonses.com ~all` |

Trois points d'attention :

1. **Le `MX` est sur `send`, pas sur la racine.** Il crée
   `send.amelie-invest.com`, une adresse technique qui ne sert qu'aux retours
   d'envoi. Vos `MX` de racine, ceux d'OVH, ne sont pas concernés — c'est
   toute la différence entre ce réglage et un réglage qui casserait votre
   courrier.
2. **La clé DKIM doit être copiée d'un seul tenant**, sans espace ni retour à
   la ligne ajouté par le copier-coller. C'est la première cause d'échec de
   vérification.
3. OVH ajoute parfois le nom du domaine tout seul en fin de champ. Si
   l'interface propose déjà `.amelie-invest.com`, saisissez seulement `send`
   ou `resend._domainkey`.

## A.3 · Vérifier

Une fois les trois entrées enregistrées chez OVH, dites-le moi : je lance la
vérification depuis Resend et je vous dis laquelle des trois n'est pas encore
vue, le cas échéant. Vous pouvez aussi le faire vous-même dans Resend →
**Verify DNS Records**.

La propagation prend de quelques minutes à quelques heures. Tant que le
domaine n'est pas vérifié, l'envoi à son nom est refusé — c'est normal, ce
n'est pas une panne du formulaire, et le chantier 0 vous permet d'envoyer
entre-temps.

Une fois le domaine vérifié, basculez `CONTACT_FROM` de `joytalents.com` vers
`Amélie & Partners <site@amelie-invest.com>`, et redéployez.

## A.4 · DMARC, si vous n'en avez pas déjà un

Si la zone ne contient aucun `_dmarc`, ajoutez-le : il dit aux serveurs
destinataires quoi faire d'un message qui se réclamerait de votre domaine
sans en avoir le droit.

| Type | Sous-domaine | Valeur |
|---|---|---|
| `TXT` | `_dmarc` | `v=DMARC1; p=none; rua=mailto:contact@amelie-invest.com` |

`p=none` observe sans rien rejeter : c'est le réglage prudent pour commencer.
**Si un `_dmarc` existe déjà, n'y touchez pas** — un domaine ne peut en avoir
qu'un, et le vôtre est peut-être déjà réglé plus strictement.

## A.5 · Côté Vercel

Les variables sont celles du chantier 0. Une fois le domaine vérifié, seul
`CONTACT_FROM` change :

| Nom | Valeur définitive |
|---|---|
| `CONTACT_FROM` | `Amélie & Partners <site@amelie-invest.com>` |
| `CONTACT_TO` | `contact@amelie-invest.com` |

`site@amelie-invest.com` n'a pas besoin d'être une vraie boîte aux lettres :
c'est une adresse d'expédition. Les réponses partent vers l'adresse du
visiteur, que la fonction place en `reply-to`.

---

# B · La bascule du site vers Vercel

> **À lire avant de commencer.** Cette étape retire le site Showit de
> l'adresse `amelie-invest.com`. Le site actuellement en ligne disparaît au
> profit du nouveau. Ne la faites qu'une fois le nouveau site validé et les
> mentions « à compléter » traitées — voir `A-VALIDER-AVANT-LIVE.md`.

## B.1 · La veille : baisser le TTL

Dans la zone OVH, passez le **TTL** des entrées `A` de la racine et du `www`
à **300 secondes**, et attendez 24 heures. Sans cela, un retour en arrière
mettrait des heures à se propager. C'est la seule précaution qui rende la
bascule réversible en quelques minutes.

## B.2 · Ajouter le domaine dans Vercel

Projet Vercel → **Settings** → **Domains** → ajouter `amelie-invest.com`,
puis `www.amelie-invest.com`.

Vercel affiche alors **les valeurs propres à votre projet** : une adresse IP
pour la racine, un nom pour le `www`.

**Recopiez ce que Vercel affiche, rien d'autre.** Ces valeurs ont changé en
2025 et diffèrent d'un compte à l'autre : les anciennes valeurs `76.76.21.21`
et `cname.vercel-dns.com` circulent encore partout sur le web, mais votre
projet en utilise peut-être d'autres (souvent `216.198.79.1` et un nom en
`…vercel-dns-0xx.com`). Une valeur recopiée de mémoire donne un site
injoignable.

## B.3 · Reporter chez OVH

| Nom | Type | Action |
|---|---|---|
| racine (vide) | `A` | **modifier** : remplacer `75.101.134.27` par l'IP affichée par Vercel |
| `www` | `A` puis `CNAME` | **supprimer** l'entrée `A` existante, **créer** un `CNAME` vers le nom affiché par Vercel |

Un même nom ne peut pas porter à la fois un `A` et un `CNAME` : d'où la
suppression avant création pour le `www`.

Ne touchez à rien d'autre. En particulier, les enregistrements du chantier A
et les `MX` d'OVH restent en place.

## B.4 · Vérifier

- `https://amelie-invest.com` et `https://www.amelie-invest.com` affichent le
  nouveau site, en HTTPS (Vercel délivre le certificat tout seul, comptez
  quelques minutes).
- Le formulaire envoie un message qui arrive bien.
- Un e-mail envoyé à `contact@amelie-invest.com` arrive toujours : c'est le
  contrôle qui prouve que les `MX` n'ont pas été abîmés.
- `https://amelie-invest.com/sitemap.xml` répond, puis envoyez-le à Google
  Search Console.

## B.5 · Retour en arrière

Remettre l'entrée `A` de la racine et du `www` sur `75.101.134.27`. Avec un
TTL à 300 s, le site Showit revient en quelques minutes.

---

# Ce qui reste à faire dire

- **La région Resend est tranchée** : `eu-west-1`, en Irlande. La page
  « Données personnelles » peut l'écrire noir sur blanc, et la mention
  « à compléter » qui l'accompagne disparaître.
- **Le bureau d'enregistrement du domaine**, cité dans les mentions légales :
  OVH, à confirmer.
- **La région de diffusion Vercel**, également citée dans les mentions
  légales et sur la page « Données personnelles ».
