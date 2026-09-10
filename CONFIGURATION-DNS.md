# Configuration DNS chez OVH

Deux chantiers **indépendants**, à ne pas mélanger :

- **A · Le formulaire de contact** (Resend). Aucun effet sur le site
  actuellement en ligne, ni sur les boîtes aux lettres. Peut se faire tout de
  suite.
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

# A · Le formulaire de contact

Le formulaire de `formulaire.html` envoie le message par **Resend**. Pour que
Resend ait le droit d'écrire au nom du domaine, il faut lui prouver que le
domaine vous appartient. C'est tout ce que font ces trois enregistrements.

## A.1 · Déclarer le domaine dans Resend

Sur `resend.com` → **Domains** → **Add Domain** :

- Domaine : `amelie-invest.com`
- Région : **Europe (Ireland) · `eu-west-1`**

La région compte : c'est elle qui décide où les messages sont traités.
`eu-west-1` garde le traitement dans l'Union européenne, ce qui évite d'avoir
à citer un mécanisme de transfert sur la page « Données personnelles ». C'est
déjà la région de votre domaine `joytalents.com`.

Ne pas activer *Open tracking* ni *Click tracking* : ils réécrivent les liens
et déposent des mouchards, ce que le site s'interdit.

## A.2 · Reporter les trois enregistrements chez OVH

Resend affiche alors trois lignes. Dans OVH, **Zone DNS** → **Ajouter une
entrée**, une par une :

| Type | Sous-domaine | Valeur | Priorité |
|---|---|---|---|
| `MX` | `send` | `feedback-smtp.eu-west-1.amazonses.com.` | `10` |
| `TXT` | `send` | `v=spf1 include:amazonses.com ~all` | — |
| `TXT` | `resend._domainkey` | la longue clé `p=MIGfMA0…` affichée par Resend | — |

Trois points d'attention :

1. **Le `MX` est sur `send`, pas sur la racine.** Il crée
   `send.amelie-invest.com`, une adresse technique qui ne sert qu'aux retours
   d'envoi. Vos `MX` de racine, ceux d'OVH, ne sont pas concernés.
2. **La clé DKIM est unique à votre domaine.** Copiez-la depuis Resend, ne la
   recopiez de nulle part ailleurs. Elle est longue : vérifiez qu'elle est
   complète, sans espace ni retour à la ligne ajouté.
3. OVH ajoute parfois le nom du domaine tout seul en fin de champ. Si
   l'interface propose déjà `.amelie-invest.com`, saisissez seulement `send`
   ou `resend._domainkey`.

## A.3 · Vérifier

Retour dans Resend → **Verify DNS Records**. La propagation prend de quelques
minutes à quelques heures. Tant que le domaine n'est pas vérifié, l'envoi est
refusé — c'est normal, ce n'est pas une panne du formulaire.

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

Dans le projet Vercel → **Settings** → **Environment Variables**, pour
*Production*, *Preview* et *Development* :

| Nom | Valeur |
|---|---|
| `RESEND_API_KEY` | la clé créée dans Resend, avec le **droit d'envoi seulement** |
| `CONTACT_FROM` | `Amélie & Partners <site@amelie-invest.com>` |
| `CONTACT_TO` | `contact@amelie-invest.com` |

Puis **redéployer** : les variables ne sont lues qu'au démarrage de la
fonction.

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

- **La région Resend.** Une fois le domaine créé en `eu-west-1`, la page
  « Données personnelles » peut l'écrire noir sur blanc, et la mention
  « à compléter » qui l'accompagne disparaît.
- **Le bureau d'enregistrement du domaine**, cité dans les mentions légales :
  OVH, à confirmer.
- **La région de diffusion Vercel**, également citée dans les mentions
  légales et sur la page « Données personnelles ».
