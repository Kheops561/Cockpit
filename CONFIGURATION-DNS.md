# Configuration DNS chez OVH

Le domaine des e-mails est **`amelie-invest.com`**. Sa zone DNS est gérée chez
OVH, et c'est là que se font les trois ajouts.

La configuration se fait donc **à deux endroits**, une fois pour toutes :

- **dans Resend**, on déclare le domaine — c'est fait, le 10 septembre 2026 ;
- **dans OVH**, on ajoute les trois entrées que Resend a générées, pour lui
  prouver que le domaine vous appartient.

Il n'y a rien d'autre à régler dans Resend. Tout ce qui suit se passe dans
l'espace client OVH.

Deux chantiers **indépendants**, à ne pas mélanger :

- **A · Le formulaire de contact.** Trois entrées à ajouter, toutes sur des
  sous-domaines. Aucun effet sur le site actuellement en ligne, ni sur vos
  boîtes aux lettres. À faire maintenant.
- **B · La bascule du site vers Vercel.** C'est elle, et elle seule, qui
  retire le site de Showit. À faire quand le nouveau site est validé.

Le site de travail, `https://amelie-invest-phi.vercel.app`, **n'a besoin
d'aucun réglage DNS** : le formulaire y poste sur lui-même. Le chantier A
suffit donc à faire partir de vrais e-mails, au nom du domaine, sans toucher
au site en ligne.

## Règle d'or

**Ne jamais supprimer ni modifier les entrées `MX` de la racine, le `TXT` de
SPF de la racine, ni les clés DKIM déjà présentes.** Ce sont vos boîtes aux
lettres `@amelie-invest.com`. Les toucher coupe la réception du courrier.

Les trois entrées du chantier A portent toutes sur des **sous-domaines**
(`send.`, `resend._domainkey.`). Elles s'ajoutent, elles ne remplacent rien.

## État actuel, relevé le 10 septembre 2026

| Nom | Type | Valeur | Qui c'est |
|---|---|---|---|
| `amelie-invest.com` | A | `75.101.134.27` | Showit (via Amazon) |
| `www.amelie-invest.com` | A | `75.101.134.27` | Showit |

Les `MX`, `SPF` et `DKIM` existants n'ont pas pu être relevés depuis
l'environnement de travail. Avant de commencer, ouvrez la zone et **notez ce
qui existe déjà** : c'est votre filet de sécurité.

---

# A · Le formulaire de contact

Le formulaire envoie le message par **Resend**. Pour que Resend ait le droit
d'écrire au nom de `amelie-invest.com`, il faut lui prouver que le domaine
vous appartient. C'est tout ce que font ces trois entrées.

## A.1 · Le domaine est déjà déclaré dans Resend

`amelie-invest.com` a été créé le 10 septembre 2026, région **Europe
(Ireland) · `eu-west-1`**, suivi d'ouverture et suivi des clics désactivés —
ils réécrivent les liens et déposent des mouchards, ce que le site s'interdit.

La région compte : c'est elle qui décide où les messages sont traités.
`eu-west-1` garde le traitement dans l'Union européenne, ce qui évite d'avoir
à citer un mécanisme de transfert sur la page « Données personnelles ».

Statut actuel : **`not_started`** sur les trois entrées. Aucune n'est encore
vue. C'est ce que la suite corrige.

## A.2 · Où aller dans OVH

1. `ovh.com` → **Espace client** → **Web Cloud** (menu de gauche)
2. **Noms de domaine** → `amelie-invest.com`
3. Onglet **Zone DNS**
4. Bouton **Ajouter une entrée**, en haut à droite

Trois fois de suite, une entrée par tableau ci-dessous.

> **Choisissez le type `TXT`, pas le type `DKIM`.** OVH propose un formulaire
> `DKIM` avec des champs séparés qui reconstruit la clé à sa façon. Resend
> attend la valeur telle quelle : passez par `TXT` et collez la valeur brute.

## A.3 · Les trois entrées

### 1 · La clé DKIM — elle signe les messages

| Champ OVH | À saisir |
|---|---|
| Type | `TXT` |
| Sous-domaine | `resend._domainkey` |
| TTL | laisser par défaut |
| Valeur | la clé ci-dessous, d'un seul tenant |

```
p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDAuL397Tg17cjRDFajVZtEe+enxrX4MMxjjP11F6DTfXpmgvpJ9n4LqY5hXXprh7V0UAgA8YRTY2O1N5fsUGep3utyORx5srdlM5Tp9SMaEcRSfgrYf7sRRHPC0xfj65mYXQK2Jq6KVEm+VMwo3Y2okepv7Jj3IbCSPVE6r6+tVQIDAQAB
```

### 2 · Le MX des retours d'envoi

| Champ OVH | À saisir |
|---|---|
| Type | `MX` |
| Sous-domaine | `send` |
| TTL | laisser par défaut |
| Priorité | `10` |
| Cible | `feedback-smtp.eu-west-1.amazonses.com.` |

### 3 · Le SPF de ce sous-domaine

| Champ OVH | À saisir |
|---|---|
| Type | `TXT` |
| Sous-domaine | `send` |
| TTL | laisser par défaut |
| Valeur | `v=spf1 include:amazonses.com ~all` |

## A.4 · Les pièges, dans l'ordre où on tombe dedans

1. **Le `MX` est sur `send`, pas sur la racine.** Il crée
   `send.amelie-invest.com`, une adresse technique qui ne sert qu'aux retours
   d'envoi. Vos `MX` de racine, ceux d'OVH, ne bougent pas. C'est toute la
   différence entre ce réglage et un réglage qui casserait votre courrier.
   Si le champ « Sous-domaine » est vide au moment de valider, **annulez**.
2. **OVH complète le nom tout seul.** Sous le champ, l'interface affiche le
   nom final : elle doit lire `send.amelie-invest.com` et
   `resend._domainkey.amelie-invest.com`. Si elle affiche
   `send.amelie-invest.com.amelie-invest.com`, retirez le domaine de votre
   saisie.
3. **La clé DKIM doit être collée d'un seul tenant**, sans espace, sans
   retour à la ligne, sans guillemets ajoutés à la main. C'est la première
   cause d'échec de vérification. OVH pose les guillemets lui-même.
4. **Le point final de la cible MX** — `…amazonses.com.` — n'est pas une
   faute de frappe. S'il manque, OVH peut interpréter la cible comme un
   sous-domaine de `amelie-invest.com`.

> **Le mode textuel de la zone** (« Modifier en mode textuel ») va plus vite,
> mais il **remplace la zone entière** par ce que vous collez. Utilisé
> distraitement, il efface vos `MX` et coupe votre courrier. Si vous y allez,
> **ajoutez** les trois lignes au contenu existant, n'en remplacez aucune. Le
> formulaire « Ajouter une entrée » ne présente pas ce risque.

## A.5 · Vérifier

Une fois les trois entrées enregistrées, **dites-le moi** : je lance la
vérification depuis Resend et je vous dis précisément laquelle des trois
n'est pas encore vue, s'il en manque une. Vous pouvez aussi le faire
vous-même dans Resend → **Verify DNS Records**.

La propagation prend de quelques minutes à quelques heures. Tant que le
domaine n'est pas vérifié, l'envoi à son nom est refusé — c'est normal, ce
n'est pas une panne du formulaire.

> Si vous voulez essayer le formulaire avant la fin de la propagation :
> `joytalents.com` est déjà vérifié sur le compte Resend. Poser
> `CONTACT_FROM` sur une adresse de ce domaine fait partir de vrais messages
> tout de suite. C'est un dépannage, pas la configuration finale : l'adresse
> d'expédition doit porter le nom de la marque.

## A.6 · Côté Vercel

Dans le projet Vercel → **Settings** → **Environment Variables**, pour
*Production*, *Preview* et *Development* :

| Nom | Valeur |
|---|---|
| `RESEND_API_KEY` | la clé Resend, avec le **droit d'envoi seulement** |
| `CONTACT_FROM` | `Amélie & Partners <site@amelie-invest.com>` |
| `CONTACT_TO` | `contact@amelie-invest.com` |

Puis **redéployer** : les variables ne sont lues qu'au démarrage de la
fonction.

`site@amelie-invest.com` n'a pas besoin d'être une vraie boîte aux lettres :
c'est une adresse d'expédition. Les réponses partent vers l'adresse du
visiteur, que la fonction place en `reply-to`.

## A.7 · Contrôler que la fonction est en place

Ouvrez `https://amelie-invest-phi.vercel.app/api/contact` dans un navigateur.
Elle répond en JSON :

```json
{ "ok": true, "fonction": "contact", "cle": true, "expediteur": true, "destinataire": true }
```

- **Page introuvable** : la fonction n'est pas déployée. Vérifiez que le
  projet Vercel est relié au dépôt `Kheops561/Cockpit` et que le dernier
  commit est déployé.
- **`"cle": false`** : `RESEND_API_KEY` manque, ou le projet n'a pas été
  redéployé depuis qu'elle a été ajoutée.

Aucune valeur n'est révélée par ce contrôle, seulement leur présence.

## A.8 · DMARC, si vous n'en avez pas déjà un

Si la zone ne contient aucun `_dmarc`, ajoutez-le : il dit aux serveurs
destinataires quoi faire d'un message qui se réclamerait de votre domaine
sans en avoir le droit.

| Type | Sous-domaine | Valeur |
|---|---|---|
| `TXT` | `_dmarc` | `v=DMARC1; p=none; rua=mailto:contact@amelie-invest.com` |

`p=none` observe sans rien rejeter : c'est le réglage prudent pour commencer.
**Si un `_dmarc` existe déjà, n'y touchez pas** — un domaine ne peut en avoir
qu'un, et le vôtre est peut-être déjà réglé plus strictement.

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

Ne touchez à rien d'autre. En particulier, les trois entrées du chantier A et
les `MX` de la racine restent en place.

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

# Et si on se passait de Resend ?

La question mérite d'être posée, puisque les boîtes aux lettres sont déjà
chez OVH. Envoyer par le serveur SMTP d'OVH (`ssl0.ovh.net`, avec les
identifiants d'une boîte du domaine) éviterait un sous-traitant de plus sur
la page « Données personnelles », et ne demanderait **aucune** des trois
entrées ci-dessus.

Ce n'est pas la voie retenue, pour deux raisons :

1. **Une dépendance.** Parler SMTP demande une bibliothèque côté serveur. Le
   projet s'interdit les dépendances ; Resend s'appelle en une requête HTTPS,
   sans rien installer.
2. **Un mot de passe de boîte aux lettres dans les variables d'un
   hébergeur.** Une clé d’API Resend se révoque en un clic et ne donne que le
   droit d'envoyer. Les identifiants d'une boîte OVH ouvrent la boîte.

Si vous préférez tout de même cette voie, dites-le : elle est faisable, et
c'est un arbitrage, pas un obstacle technique.

---

# Ce qui reste à faire dire

- **La région Resend est tranchée** : `eu-west-1`, en Irlande. La page
  « Données personnelles » peut l'écrire noir sur blanc, et la mention
  « à compléter » qui l'accompagne disparaître.
- **Le bureau d'enregistrement du domaine**, cité dans les mentions légales :
  OVH, à confirmer.
- **La région de diffusion Vercel**, également citée dans les mentions
  légales et sur la page « Données personnelles ».
