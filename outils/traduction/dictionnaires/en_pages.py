# -*- coding: utf-8 -*-
"""Les dictionnaires anglais, page par page.

Une entree par chaine visible de la page francaise. `traduire.py` refuse de
fabriquer une page dont une seule chaine manquerait : ce fichier est donc
exhaustif par construction.

Trois regles tenues partout :

- **Les noms propres ne se traduisent pas** : le cabinet, sa signature, les
  quatre offres, les cinq verdicts, les lieux.
- **Le prix reste francais.** 432 € TTC : la prestation est vendue en France,
  facturee en France, soumise a la TVA francaise. « TTC » devient donc
  « incl. French VAT », et non un prix converti.
- **Le droit reste francais.** Les pages legales ne sont pas traduites ; les
  renvois vers elles le disent.
"""

PAGES = {}

PAGES["404.html"] = {
    "Erreur 404": "Error 404",
    "Cette page n&rsquo;existe pas": "This page does not exist",
    "ou a été déplacée.": "or has moved.",
    "Le lien est peut-être ancien. Voici les pages les plus utiles pour reprendre votre parcours.":
        "The link may be an old one. Here are the pages most likely to help you pick up where you left off.",
    "Retour à l&rsquo;accueil": "Back to the home page",
    "Accompagnements": "Engagements",
}

PAGES["contact.html"] = {
    "Contact": "Contact",
    "Deux façons": "Two ways",
    "de nous joindre.": "of reaching us.",
    "Le plus simple reste de réserver un créneau&nbsp;: trente minutes suffisent à comprendre votre situation et à définir le périmètre utile.":
        "The simplest route is to book a slot: thirty minutes are enough to understand your situation and define a useful scope.",
    "Descendre au contenu": "Scroll to content",
    "01 &middot; Le plus direct": "01 &middot; The most direct",
    "Réserver un premier échange": "Book a first conversation",
    "Deux formats sont ouverts à la réservation. Le premier sert à cadrer&nbsp;; le second est la séance de travail elle-même.":
        "Two formats can be booked. The first is there to frame the question; the second is the working session itself.",
    "Appel de cadrage": "Framing call",
    "30 minutes": "30 minutes",
    "Offert": "Free",
    "Comprendre votre situation, identifier le besoin principal et déterminer si le cabinet peut vous accompagner, et sous quelle forme. Sans engagement, et sans analyse approfondie.":
        "To understand your situation, identify the main need and establish whether the firm can help you, and in what form. No commitment, and no in-depth analysis.",
    "1 heure": "1 hour",
    "432&nbsp;€ TTC": "432&nbsp;€ incl. French VAT",
    "Êtes-vous prêt à investir maintenant&nbsp;? Si non, pourquoi précisément, et quelles conditions réunir avant d&rsquo;agir. Questionnaire préparatoire, séance, puis Note de Diagnostic &amp; Décision.":
        "Are you ready to invest now? If not, precisely why, and what conditions to meet before acting. A preparatory questionnaire, the session, then a written Diagnosis &amp; Decision Note.",
    "L&rsquo;échange se tient en&nbsp;:": "The conversation can be held in:",
    "français": "French",
    "anglais": "English",
    "vietnamien": "Vietnamese",
    "Réservation ferme après validation du paiement. Report ou annulation sans frais jusqu&rsquo;à 48&nbsp;heures avant la séance&nbsp;: voir les":
        "The booking is confirmed once payment is validated. Free rescheduling or cancellation up to 48&nbsp;hours before the session: see the",
    "conditions générales de vente": "terms and conditions of sale, in French",
    "Choisir un créneau": "Choose a slot",
    "02 &middot; Par écrit": "02 &middot; In writing",
    "Nous écrire": "Write to us",
    "Décrivez votre situation en quelques lignes. Une réponse vous indiquera si un échange est utile et sous quel format.":
        "Describe your situation in a few lines. We will reply to say whether a conversation would be useful, and in what format.",
    "Votre projet ou la décision qui vous bloque": "Your project, or the decision you are stuck on",
    "Le profil d&rsquo;investisseur dont vous vous sentez le plus proche": "The investor profile you feel closest to",
    "L&rsquo;échéance que vous avez en tête, même approximative": "The timeframe you have in mind, even a rough one",
    "Le formulaire s&rsquo;ouvre sur sa propre page. Votre message nous est envoyé directement, sans passer par votre logiciel de messagerie, et nous répondons sous un jour ouvré. Les informations saisies servent uniquement à traiter votre demande&nbsp;: voir les":
        "The form opens on its own page. Your message reaches us directly, without going through your email software, and we reply within one working day. What you enter is used only to handle your enquiry: see the",
    "données personnelles": "personal data notice, in French",
    "Ouvrir le formulaire": "Open the form",
    "Nous suivre": "Follow us",
    "Nos analyses et nos publications paraissent sur LinkedIn.": "Our analyses and publications appear on LinkedIn.",
    "Suivre Amélie &amp; Partners": "Follow Amélie &amp; Partners",
    "Bon à savoir": "Worth knowing",
    "Zone d&rsquo;intervention et périmètre.": "Where we work, and on what.",
    "La recherche immobilière est spécialisée sur Paris.": "The property search is specialised in Paris.",
    "Les sujets de décision, d&rsquo;arbitrage et de stratégie de financement peuvent être étudiés au cas par cas pour des projets situés ailleurs en France.":
        "Questions of decision, of arbitrage and of financing strategy can be examined case by case for projects elsewhere in France.",
    "Amélie &amp; Partners ne vend ni bien immobilier, ni crédit, ni produit fiscal, et ne se substitue pas aux professionnels réglementés.":
        "Amélie &amp; Partners sells neither property, nor credit, nor tax products, and does not take the place of regulated professionals.",
    "Premier échange &middot; 30 minutes &middot; gratuit": "First conversation &middot; 30 minutes &middot; free",
    "Parlons de votre": "Let us talk about your",
    "prochaine décision.": "next decision.",
    "Trente minutes pour comprendre votre situation, vérifier si Amélie &amp; Partners peut vous aider et définir le périmètre utile.":
        "Thirty minutes to understand your situation, check whether Amélie &amp; Partners can help and define a useful scope.",
    "Avec plaisir": "With pleasure",
    "Choisissons un créneau.": "Let us find a slot.",
    "30 minutes &middot; gratuit &middot; sans conseil approfondi &middot; sans engagement":
        "30 minutes &middot; free &middot; no in-depth advice &middot; no commitment",
    "Vous préférez écrire&nbsp;?": "Would you rather write?",
    "Passez par le formulaire": "Use the form",
}

PAGES["ressources.html"] = {
    "La bibliothèque": "The library",
    "Des ressources gratuites": "Free resources",
    "pour mieux décider.": "for better decisions.",
    "Transmettre des raisonnements utiles pour comprendre les options, évaluer les risques et prendre des décisions éclairées.":
        "Passing on ways of reasoning that help you understand the options, weigh the risks and decide with your eyes open.",
    "Descendre au contenu": "Scroll to content",
    "La bibliothèque rassemble progressivement des analyses, des réflexes terrain et des outils simples autour d&rsquo;un même sujet&nbsp;: la maîtrise du capital immobilier.":
        "The library is gradually gathering analyses, field reflexes and simple tools around a single subject: keeping control of property capital.",
    "01 &middot; Cadre pédagogique &middot; 8 min de lecture": "01 &middot; Teaching note &middot; 8 min read",
    "Les 3 effets dans l&rsquo;immobilier": "The three effects in property",
    "On parle beaucoup de rendement. Pourtant, le vrai sujet est souvent ailleurs&nbsp;: comment la dette permet de contrôler un actif, comment cet actif construit du capital, puis comment ce capital peut être remis en mouvement.":
        "Yield gets most of the attention. Yet the real subject usually lies elsewhere: how debt lets you control an asset, how that asset builds capital, and how that capital can then be set moving again.",
    "01 &middot; Effet de levier": "01 &middot; The leverage effect",
    "02 &middot; Effet ascenseur": "02 &middot; The lift effect",
    "03 &middot; Effet boule de neige": "03 &middot; The snowball effect",
    "Lire la ressource": "Read the resource",
    "Les prochains sujets": "What comes next",
    "Un même sujet,": "One subject,",
    "vu sous plusieurs angles.": "seen from several angles.",
    "Financer, acheter et arbitrer sont trois portes d&rsquo;entrée pour apprendre à décider avec plus de méthode.":
        "Financing, buying and arbitrating are three ways in to deciding with more method.",
    "02 &middot; Financer": "02 &middot; Financing",
    "Un refus bancaire ne dit pas toujours ce que vous croyez.": "A bank refusal does not always mean what you think it means.",
    "Lire ce qui bloque réellement avant de conclure que votre capacité est épuisée.":
        "Read what is actually blocking you before concluding that your borrowing capacity is spent.",
    "En préparation": "In preparation",
    "Demander des renseignements": "Ask for details",
    "03 &middot; Acheter": "03 &middot; Buying",
    "Le prix maximal se décide avant l&rsquo;offre.": "Your maximum price is decided before the offer.",
    "Préparer la négociation avec un calcul, des hypothèses et une limite claire.":
        "Prepare the negotiation with a calculation, stated assumptions and a clear limit.",
    "04 &middot; Arbitrer": "04 &middot; Arbitrating",
    "Garder n&rsquo;est pas toujours la décision la plus prudente.": "Holding on is not always the most prudent decision.",
    "Comparer le rendement du capital immobilisé avec ses autres usages possibles.":
        "Compare the return on tied-up capital with the other uses it could be put to.",
    "Notre engagement éditorial": "Our editorial commitment",
    "Une ressource doit pouvoir vous être utile même si vous ne devenez jamais client.":
        "A resource should be useful to you even if you never become a client.",
    "Pas de recettes magiques. Pas de promesse de richesse rapide. Des idées claires, des hypothèses visibles et des limites expliquées.":
        "No magic recipes. No promise of quick riches. Clear ideas, visible assumptions and limits that are spelled out.",
    "Quel sujet aimeriez-vous approfondir&nbsp;?": "Which subject would you like to go into?",
    "Les meilleures ressources partent souvent d&rsquo;une vraie question posée sur le terrain.":
        "The best resources usually start from a real question asked in the field.",
    "Proposer une question": "Suggest a question",
    "Appliquer le raisonnement": "Applying the reasoning",
    "Votre capital est-il encore placé au bon endroit&nbsp;?": "Is your capital still in the right place?",
    "Le Diagnostic Stratégique applique cette lecture à votre situation, avec vos chiffres et vos contraintes.":
        "The Diagnostic Stratégique applies this reading to your situation, with your figures and your constraints.",
    "Découvrir le Diagnostic Stratégique": "Discover the Diagnostic Stratégique",
    "Vous préférez écrire&nbsp;?": "Would you rather write?",
    "Passez par le formulaire": "Use the form",
    "Amélie-Thu DUONG, dans un jardin": "Amélie-Thu DUONG, in a garden",
    "Fenêtre à rideaux, lumière d&rsquo;hiver": "A curtained window, winter light",
}

PAGES["approche.html"] = {
    "Notre approche": "Our approach",
    "Une manière de décider": "A way of deciding",
    "avant une manière d&rsquo;acheter.": "before a way of buying.",
    "Le bon investissement n&rsquo;existe pas dans l&rsquo;absolu. Il devient cohérent, ou non, selon votre situation, votre financement, votre horizon et l&rsquo;usage futur du capital.":
        "There is no such thing as the right investment in the abstract. It becomes coherent, or not, depending on your situation, your financing, your horizon and what the capital is later for.",
    "Descendre au contenu": "Scroll to content",
    "La méthode en cinq étapes": "The method in five steps",
    "Cinq étapes, dans cet ordre.": "Five steps, in this order.",
    "Comprendre": "Understand",
    "Chiffrer": "Cost",
    "Financer": "Finance",
    "Acheter": "Buy",
    "Arbitrer": "Arbitrate",
    "01 &middot; La thèse": "01 &middot; The thesis",
    "La question n&rsquo;est pas seulement&nbsp;: «&nbsp;Est-ce un bon bien&nbsp;?&nbsp;»":
        "The question is not only: &ldquo;Is this a good property?&rdquo;",
    "La vraie question est&nbsp;: «&nbsp;Que permet cette décision dans votre trajectoire&nbsp;?&nbsp;»":
        "The real question is: &ldquo;What does this decision make possible in your trajectory?&rdquo;",
    "Votre partenaire stratégique reste du même côté de la table que vous&nbsp;: comprendre le projet, challenger les hypothèses et remettre les décisions dans le bon ordre. La réussite est votre destination&nbsp;; la qualité de décision est notre contribution.":
        "Your strategic partner stays on your side of the table: understanding the project, challenging the assumptions and putting the decisions back in the right order. Success is your destination; the quality of the decision is our contribution.",
    "02 &middot; Le processus": "02 &middot; The process",
    "Du flou à la décision.": "From haze to decision.",
    "Cinq étapes, simples à comprendre et exigeantes à appliquer, volontairement centrées sur les décisions qui changent la suite.":
        "Five steps, simple to grasp and demanding to apply, deliberately centred on the decisions that change what follows.",
    "Clarifier l&rsquo;objectif réel, le point de départ, les contraintes et l&rsquo;horizon.":
        "Clarify the real objective, the starting point, the constraints and the horizon.",
    "Produit&nbsp;: une question bien posée.": "Output: a well-framed question.",
    "Tester les hypothèses, les équilibres, les risques et les scénarios possibles.":
        "Test the assumptions, the balances, the risks and the possible scenarios.",
    "Produit&nbsp;: des options comparables.": "Output: options you can compare.",
    "Clarifier les ressources, les contraintes et les scénarios à approfondir avant la prochaine opération.":
        "Clarify the resources, the constraints and the scenarios to examine before the next transaction.",
    "Produit&nbsp;: une préparation stratégique.": "Output: strategic preparation.",
    "Définir les critères, le prix maximal et les conditions qui rendent l&rsquo;achat acceptable.":
        "Define the criteria, the maximum price and the conditions that make the purchase acceptable.",
    "Produit&nbsp;: une décision préparée.": "Output: a prepared decision.",
    "Mesurer le capital immobilisé, la valeur créée et les usages possibles de ce capital.":
        "Measure the capital tied up, the value created and what that capital could be used for.",
    "Produit&nbsp;: la prochaine direction.": "Output: the next direction.",
    "03 &middot; Le capital": "03 &middot; Capital",
    "Le rendement est un indicateur. Le capital raconte la trajectoire.":
        "Yield is an indicator. Capital tells the story of the trajectory.",
    "Un actif peut sembler peu rentable et pourtant construire beaucoup de capital. Un autre peut afficher un rendement séduisant tout en immobilisant trop de trésorerie ou en limitant la capacité d&rsquo;emprunt suivante.":
        "An asset can look barely profitable and still build a great deal of capital. Another can show an attractive yield while tying up too much cash, or narrowing the next borrowing capacity.",
    "Nous lisons ensemble le bien, la dette, les revenus, la valeur créée, le risque et le temps. C&rsquo;est cette lecture globale qui permet de savoir s&rsquo;il faut conserver, céder, refinancer ou réinvestir.":
        "Together we read the property, the debt, the income, the value created, the risk and the time. It is this overall reading that shows whether to hold, sell, refinance or reinvest.",
    "Lire «&nbsp;Les 3 effets dans l&rsquo;immobilier&nbsp;»": "Read &ldquo;The three effects in property&rdquo;",
    "04 &middot; Nos principes": "04 &middot; Our principles",
    "Ce qui ne change pas d&rsquo;un dossier à l&rsquo;autre.": "What does not change from one case to the next.",
    "Indépendance": "Independence",
    "La recommandation ne dépend ni d&rsquo;un bien à vendre, ni d&rsquo;un crédit à placer, ni d&rsquo;un produit fiscal à proposer.":
        "The recommendation depends on no property to sell, no loan to place and no tax product to offer.",
    "Chiffrage": "Costing",
    "Une intuition peut ouvrir une piste. Elle ne remplace jamais les hypothèses, les calculs et la marge de sécurité.":
        "An intuition can open a line of enquiry. It never replaces the assumptions, the calculations and the safety margin.",
    "Terrain": "Field experience",
    "La méthode vient de décisions pratiquées&nbsp;: recherche, négociation, financement, travaux, exploitation et arbitrage.":
        "The method comes from decisions actually made: search, negotiation, financing, works, operation and arbitrage.",
    "Transmission": "Passing it on",
    "Une bonne recommandation ne vous rend pas dépendant. Elle vous aide à comprendre et à mieux décider ensuite.":
        "A good recommendation does not make you dependent. It helps you understand, and decide better next time.",
    "Nous ne promettons pas": "We do not promise",
    "devenir riche rapidement, vivre de l&rsquo;immobilier ou acheter à tout prix.":
        "getting rich quickly, living off property, or buying at any price.",
    "Nous cherchons": "We look for",
    "un chemin plus court, plus lisible et mieux maîtrisé vers davantage de choix.":
        "a shorter, clearer and better-controlled path towards more choice.",
    "Passer de l&rsquo;analyse à l&rsquo;action": "From analysis to action",
    "La bonne méthode commence par la bonne question.": "The right method starts with the right question.",
    "Apportez votre situation. Nous vous aiderons à identifier le vrai sujet.":
        "Bring us your situation. We will help you identify the real subject.",
    "Analyser ma situation": "Analyse my situation",
    "Vous préférez écrire&nbsp;?": "Would you rather write?",
    "Passez par le formulaire": "Use the form",
    "Les étapes de la méthode": "The steps of the method",
    "Coupole de verre vue depuis le sol, sous une rotonde parisienne": "A glass dome seen from below, inside a Paris rotunda",
    "Les cinq étapes de la méthode": "The five steps of the method",
    "Passage couvert parisien, verrière et boutiques": "A Paris covered arcade, glass roof and shopfronts",
}

PAGES["accompagnements.html"] = {
    "Accompagnements": "Engagements",
    "Un partenaire stratégique.": "A strategic partner.",
    "Quatre façons d&rsquo;intervenir.": "Four ways of working together.",
    "Diagnostiquer, financer, acheter, piloter&nbsp;: chaque moment de votre parcours appelle un regard et un format d&rsquo;intervention adaptés.":
        "Diagnose, finance, buy, steer: each moment of your journey calls for its own kind of attention and its own format.",
    "Descendre au contenu": "Scroll to content",
    "Une séance ponctuelle peut suffire. Certaines situations demandent ensuite une mission de financement, de recherche ou de pilotage plus complète.":
        "A single session may be enough. Some situations then call for a fuller financing, search or steering engagement.",
    "01 &middot; Diagnostiquer &middot; la porte d&rsquo;entrée": "01 &middot; Diagnose &middot; the way in",
    "Une décision importante à prendre&nbsp;? Un regard stratégique pour clarifier la situation, challenger vos options et déterminer la prochaine étape.":
        "An important decision to make? A strategic reading to clarify the situation, challenge your options and settle the next step.",
    "Nous mettons à plat le contexte, les contraintes, les scénarios et les conséquences de chaque option. L&rsquo;objectif est de savoir quoi faire maintenant, ou pourquoi il vaut mieux attendre.":
        "We lay out the context, the constraints, the scenarios and the consequences of each option. The aim is to know what to do now &mdash; or why waiting is the better course.",
    "Questionnaire préparatoire adapté à votre question": "A preparatory questionnaire tailored to your question",
    "Session stratégique d&rsquo;une heure": "A one-hour strategy session",
    "Note de Diagnostic &amp; Décision&nbsp;: verdict, priorités, prochaines actions":
        "A written Diagnosis &amp; Decision Note: verdict, priorities, next actions",
    "Tarification": "Price",
    "€ TTC": "€ incl. French VAT",
    "Questionnaire &middot; Session d&rsquo;une heure &middot; Note de Diagnostic &amp; Décision":
        "Questionnaire &middot; One-hour session &middot; Diagnosis &amp; Decision Note",
    "Premier échange de cadrage de 30 minutes gratuit.": "A free 30-minute framing conversation to begin.",
    "Découvrir le diagnostic": "Discover the diagnostic",
    "02 &middot; Financer": "02 &middot; Finance",
    "Stratégie de Financement": "Stratégie de Financement",
    "Comprendre ce que votre situation permet réellement, ce qui bloque et ce qu&rsquo;il faut préparer avant d&rsquo;engager la prochaine étape.":
        "Understand what your situation actually allows, what is blocking it, and what to prepare before committing to the next step.",
    "Capacité réelle, endettement, apport, durée, revenus locatifs, structure et ordre des opérations&nbsp;: nous analysons ce qui bloque, ce qui peut être amélioré et ce qui doit rester sécurisé.":
        "Real capacity, debt ratio, deposit, term, rental income, structure and the order of transactions: we analyse what is blocking, what can be improved and what must stay safe.",
    "Analyse de la situation et des refus ou avis contradictoires":
        "Analysis of the situation, and of any refusals or conflicting opinions",
    "Lecture des ressources, contraintes et incohérences": "A reading of the resources, constraints and inconsistencies",
    "Identification des informations manquantes": "Identification of the missing information",
    "Scénarios à approfondir avant la prochaine opération": "Scenarios to examine before the next transaction",
    "Amélie &amp; Partners intervient en analyse et préparation stratégique, en amont de la décision. Le cabinet ne place ni ne négocie le crédit et n&rsquo;en garantit pas l&rsquo;obtention. Il ne se substitue pas aux professionnels réglementés.":
        "Amélie &amp; Partners works on analysis and strategic preparation, upstream of the decision. The firm neither places nor negotiates credit, and does not guarantee that it will be granted. It does not take the place of regulated professionals.",
    "Échanger sur mon financement": "Talk about my financing",
    "03 &middot; Acheter à Paris": "03 &middot; Buy in Paris",
    "Recherche immobilière à Paris": "Recherche immobilière à Paris",
    "Votre partenaire de recherche, d&rsquo;analyse et de décision jusqu&rsquo;à l&rsquo;acquisition.":
        "Your partner for the search, the analysis and the decision, right through to the purchase.",
    "Pour un investissement locatif, une résidence principale ou un pied-à-terre, la mission associe connaissance du marché parisien, recherche ciblée, analyse et aide à la décision.":
        "For a rental investment, a main home or a pied-à-terre, the engagement combines knowledge of the Paris market, a targeted search, analysis and help in deciding.",
    "Définition du cahier des charges et du prix maximal": "Setting the brief and the maximum price",
    "Recherche, présélection et lecture des opportunités": "Search, shortlisting and reading of the opportunities",
    "Analyse du prix, des travaux, de la copropriété, du potentiel et des risques":
        "Analysis of the price, the works, the building&rsquo;s management, the potential and the risks",
    "Négociation et coordination avec le réseau de professionnels":
        "Negotiation, and coordination with the network of professionals",
    "Parler de ma recherche": "Talk about my search",
    "04 &middot; Piloter": "04 &middot; Steer",
    "Trajectoire Investisseur": "Trajectoire Investisseur",
    "Construire une trajectoire claire, arbitrer les options et prendre les décisions dans le bon ordre pour faire progresser votre patrimoine.":
        "Build a clear trajectory, weigh the options and take the decisions in the right order so that your assets move forward.",
    "Acquisition, financement, trésorerie, revente, refinancement ou réinvestissement&nbsp;: nous construisons une direction et un ordre d&rsquo;exécution adaptés à votre situation, du premier investissement à la prochaine phase d&rsquo;un patrimoine déjà constitué.":
        "Purchase, financing, cash, resale, refinancing or reinvestment: we build a direction and an order of execution that fit your situation &mdash; from a first investment to the next phase of an established portfolio.",
    "Lecture globale des actifs, dettes et liquidités": "An overall reading of assets, debts and liquidity",
    "Priorisation des acquisitions et des arbitrages": "Prioritising the purchases and the arbitrages",
    "Scénarios de mobilisation et de réemploi du capital": "Scenarios for releasing and redeploying capital",
    "Pilotage stratégique dans un périmètre défini à l&rsquo;avance": "Strategic steering within a scope agreed in advance",
    "Périmètre": "Scope",
    "Direction &middot; Arbitrage &middot; Priorisation": "Direction &middot; Arbitrage &middot; Prioritisation",
    "Présenter ma situation": "Present my situation",
    "05 &middot; Comment choisir&nbsp;?": "05 &middot; How to choose?",
    "Vous n&rsquo;avez pas à choisir seul la prestation.": "You do not have to pick the right engagement on your own.",
    "Le premier échange sert précisément à comprendre votre besoin et à vérifier si nous pouvons vous aider. Si une séance suffit, nous vous le dirons. Si la situation demande une mission plus complète, son périmètre est défini avant tout engagement.":
        "The first conversation exists precisely to understand what you need and to check whether we can help. If a single session is enough, we will say so. If the situation calls for a fuller engagement, its scope is agreed before any commitment.",
    "Réserver un premier échange": "Book a first conversation",
    "30 minutes gratuites &middot; Sans conseil approfondi &middot; Sans engagement":
        "30 minutes free &middot; No in-depth advice &middot; No commitment",
    "Un besoin précis": "One clear need",
    "Vous n&rsquo;avez peut-être pas besoin de tout. Vous avez besoin du bon point de départ.":
        "You may not need everything. You need the right starting point.",
    "Présentez-nous la situation. Nous déterminerons ensemble le périmètre utile.":
        "Tell us about the situation. Together we will work out the useful scope.",
    "Analyser ma situation": "Analyse my situation",
    "Vous préférez écrire&nbsp;?": "Would you rather write?",
    "Passez par le formulaire": "Use the form",
    "Enfilade intérieure vers une arche ouverte sur la rue": "A line of rooms leading to an arch open onto the street",
    "Quais de Seine bordés d&rsquo;arbres, à Paris": "Tree-lined banks of the Seine, in Paris",
    "Le Louvre et la rue de Rivoli au soleil couchant": "The Louvre and the rue de Rivoli at sunset",
    "La Seine au couchant, le Pont des Arts et la tour Eiffel": "The Seine at dusk, the Pont des Arts and the Eiffel Tower",
}

# ---------------------------------------------------------------------------
# Ce qui reste en francais sur une page donnee, sans etre un oubli.
# ---------------------------------------------------------------------------

INCHANGE = {}

# Les cinq verdicts sont les noms que porte la Note de Diagnostic & Decision :
# ce sont des termes du livrable, pas des mots de la page. La phrase qui les
# introduit en donne la traduction ; les cartes gardent le nom d'origine.
INCHANGE["diagnostic.html"] = {
    "Avancer", "Préparer", "Restructurer", "Approfondir", "Suspendre",
}

PAGES["diagnostic.html"] = {
    "Sortir du flou": "Out of the haze",
    "avant d&rsquo;engager le capital.": "before you commit the capital.",
    "Une décision importante à prendre&nbsp;? Un regard stratégique pour clarifier la situation, challenger vos options et déterminer la prochaine étape.":
        "An important decision to make? A strategic reading to clarify the situation, challenge your options and settle the next step.",
    "30 minutes gratuites pour cadrer": "30 minutes free, to frame the question",
    "Sans engagement": "No commitment",
    "Réserver un premier échange": "Book a first conversation",
    "Descendre au contenu": "Scroll to content",
    "Un besoin précis": "One clear need",
    "Une décision argumentée.": "A reasoned decision.",
    "Un regard stratégique pour clarifier la situation, challenger vos options et déterminer la prochaine étape.":
        "A strategic reading to clarify the situation, challenge your options and settle the next step.",
    "30&nbsp;minutes gratuites pour cadrer": "30&nbsp;minutes free, to frame the question",
    "Un regard indépendant": "An independent view",
    "Fondatrice &amp; Investisseuse à Paris depuis 2014": "Founder &amp; investor in Paris since 2014",
    "TTC": "incl. French VAT",
    "Prestation ponctuelle, sans abonnement ni engagement.":
        "A one-off engagement, with no subscription and no commitment. Priced and invoiced in France, under French VAT and French law.",
    "Ce qui est compris": "What is included",
    "Un questionnaire préparatoire": "A preparatory questionnaire",
    "Une session stratégique d&rsquo;une heure": "A one-hour strategy session",
    "Votre Note de Diagnostic &amp; Décision": "Your written Diagnosis &amp; Decision Note",
    "Un premier échange de cadrage de 30 minutes, gratuit": "A free 30-minute framing conversation to begin",
    "Cinq verdicts possibles&nbsp;: AVANCER, PRÉPARER, RESTRUCTURER, APPROFONDIR, SUSPENDRE.":
        "Five possible verdicts: AVANCER, PRÉPARER, RESTRUCTURER, APPROFONDIR, SUSPENDRE &mdash; proceed, prepare, restructure, look deeper, pause.",
    "01 &middot; Pour qui&nbsp;?": "01 &middot; Who is it for?",
    "Vous n&rsquo;avez pas besoin d&rsquo;un avis de plus. Vous avez besoin d&rsquo;une lecture structurée.":
        "You do not need one more opinion. You need a structured reading.",
    "Vous hésitez entre plusieurs projets ou plusieurs montages.":
        "You are hesitating between several projects, or several structures.",
    "Votre banque refuse, ou les avis reçus se contredisent.":
        "Your bank has said no, or the opinions you have been given contradict each other.",
    "Vous voulez savoir s&rsquo;il faut acheter maintenant ou consolider d&rsquo;abord.":
        "You want to know whether to buy now or consolidate first.",
    "Vous possédez déjà des biens et ne savez plus quoi conserver, vendre ou financer ensuite.":
        "You already own property and no longer know what to hold, sell or finance next.",
    "Vous voulez un regard indépendant avant d&rsquo;engager du capital ou de la dette.":
        "You want an independent view before committing capital or debt.",
    "02 &middot; Le déroulé": "02 &middot; How it runs",
    "Comprendre. Analyser. Trancher.": "Understand. Analyse. Decide.",
    "Un cadre court et précis, conçu pour produire une direction, pas une accumulation d&rsquo;informations.":
        "A short, precise framework, designed to produce a direction rather than a pile of information.",
    "Avant": "Before",
    "30 minutes, gratuit": "30 minutes, free",
    "Échange de cadrage": "Framing conversation",
    "Vous présentez la situation. Nous vérifions le besoin, les enjeux et le périmètre utile.":
        "You set out the situation. We check the need, what is at stake and the useful scope.",
    "Ce rendez-vous n&rsquo;est pas une séance de conseil approfondi.":
        "This conversation is not an in-depth advisory session.",
    "Questionnaire préparatoire": "Preparatory questionnaire",
    "Vous préparez la matière": "You gather the material",
    "Vous renseignez votre situation et transmettez les éléments utiles pour identifier le véritable nœud de décision.":
        "You describe your situation and send over what is needed to identify the real knot in the decision.",
    "Le cadre d&rsquo;analyse est adapté à votre question.": "The analytical framework is adapted to your question.",
    "Le jour J": "On the day",
    "Session d&rsquo;une heure": "One-hour session",
    "Analyse et décision": "Analysis and decision",
    "Nous comparons les options, leurs conditions, leurs risques et leurs effets sur la suite.":
        "We compare the options, their conditions, their risks and their effects on what follows.",
    "Vous repartez avec une direction argumentée.": "You leave with a reasoned direction.",
    "Après": "After",
    "Sous quelques jours": "Within a few days",
    "Note de Diagnostic &amp; Décision": "Diagnosis &amp; Decision Note",
    "Vous recevez une note qui formalise la lecture de votre situation, le verdict, les priorités et les prochaines actions.":
        "You receive a note setting down the reading of your situation, the verdict, the priorities and the next actions.",
    "Vous savez quoi faire, et dans quel ordre.": "You know what to do, and in what order.",
    "03 &middot; Le verdict": "03 &middot; The verdict",
    "Cinq directions possibles.": "Five possible directions.",
    "Une prochaine étape claire.": "One clear next step.",
    "«&nbsp;Pas maintenant&nbsp;» n&rsquo;est pas un refus. C&rsquo;est une décision qui protège votre marge de manœuvre et indique ce qui doit être consolidé avant la prochaine étape.":
        "&ldquo;Not now&rdquo; is not a refusal. It is a decision that protects your room for manoeuvre and shows what needs consolidating before the next step.",
    "Engager la prochaine étape avec des hypothèses et des risques identifiés.":
        "Commit to the next step, with the assumptions and the risks identified.",
    "Compléter les ressources et les informations nécessaires avant d&rsquo;agir.":
        "Assemble the resources and the information needed before acting.",
    "Revoir l&rsquo;organisation du projet ou du patrimoine pour retrouver de la cohérence.":
        "Rework the shape of the project or the portfolio to bring back coherence.",
    "Éclaircir une question déterminante avant de trancher.": "Clear up one decisive question before choosing.",
    "Préserver votre marge de manœuvre en différant ou en arrêtant le projet.":
        "Protect your room for manoeuvre by postponing or stopping the project.",
    "04 &middot; Pourquoi indépendant&nbsp;?": "04 &middot; Why independent?",
    "Le seul produit du diagnostic, c&rsquo;est la clarté.": "The only thing the diagnostic sells is clarity.",
    "Amélie &amp; Partners ne vend ni bien immobilier, ni crédit, ni produit fiscal dans le cadre du diagnostic. Nous n&rsquo;avons aucune raison de provoquer un achat si ce n&rsquo;est pas le bon moment.":
        "Within the diagnostic, Amélie &amp; Partners sells neither property, nor credit, nor tax products. We have no reason to push you into buying if this is not the right moment.",
    "Une autre mission peut être proposée lorsque son utilité est claire. Elle reste distincte et son périmètre est présenté séparément.":
        "Another engagement may be proposed when its usefulness is clear. It stays separate, and its scope is presented separately.",
    "Première étape &middot; 30 minutes &middot; gratuit": "First step &middot; 30 minutes &middot; free",
    "Parlons de la décision": "Let us talk about the decision",
    "qui vous bloque.": "you are stuck on.",
    "En 30 minutes, nous vérifions ensemble si un Diagnostic Stratégique est le bon format pour votre situation.":
        "In 30 minutes we check together whether a Diagnostic Stratégique is the right format for your situation.",
    "Avec plaisir": "With pleasure",
    "Choisissons un créneau.": "Let us find a slot.",
    "30 minutes &middot; gratuit &middot; sans conseil approfondi &middot; sans engagement":
        "30 minutes &middot; free &middot; no in-depth advice &middot; no commitment",
    "Vous préférez écrire&nbsp;?": "Would you rather write?",
    "Passez par le formulaire": "Use the form",
    "Amélie-Thu DUONG, en extérieur, appuyée à une bordure de lavandes":
        "Amélie-Thu DUONG, outdoors, leaning on a border of lavender",
    "Coupole vitrée vue de l&rsquo;intérieur, la structure entière visible d&rsquo;un seul regard":
        "A glazed dome seen from inside, the whole structure taken in at a glance",
}

# Les huit temoignages sont la parole d'investisseurs reels : ils restent
# dans leur langue, signales par un `lang="fr"`. Les noms, les titres
# d'oeuvre et les lieux ne se traduisent pas davantage.
CITATIONS = {"temoignages.html": {
    "&laquo;&nbsp;Pour l&rsquo;achat de ma résidence principale, Amélie m&rsquo;a apporté un vrai recul. Son analyse et ses questions m&rsquo;ont permis de décider avec beaucoup plus de clarté.&nbsp;&raquo;",
    "&laquo;&nbsp;Je partais de zéro. En deux ans, j&rsquo;ai construit avec Amélie une stratégie qui m&rsquo;a permis d&rsquo;atteindre plus de 1,2 M€ de patrimoine immobilier brut. J&rsquo;ai surtout apprécié sa vision globale et sa capacité à proposer plusieurs chemins.&nbsp;&raquo;",
    "&laquo;&nbsp;Je ne connaissais ni l&rsquo;investissement immobilier ni le marché parisien. En un an, j&rsquo;ai acheté mes deux premiers studios à Paris. Amélie m&rsquo;a surtout appris à comprendre le levier bancaire et à dépasser plusieurs idées reçues.&nbsp;&raquo;",
    "&laquo;&nbsp;J&rsquo;ai commencé l&rsquo;immobilier tard, à l&rsquo;approche de la retraite. Avec Amélie, j&rsquo;ai mis en place une stratégie adaptée qui m&rsquo;a permis d&rsquo;acquérir un local commercial dans le 6&#7497; puis un studio dans le Marais.&nbsp;&raquo;",
    "&laquo;&nbsp;Je partais de zéro. En trois ans, j&rsquo;ai acheté deux studios dans Paris centre et ma résidence principale à Fontainebleau. Amélie m&rsquo;a aidée à avancer étape par étape, sans perdre la vision d&rsquo;ensemble.&nbsp;&raquo;",
    "&laquo;&nbsp;J&rsquo;hésitais entre agrandir ma résidence principale et investir à Paris. Une séance avec Amélie m&rsquo;a suffi pour remettre les options à plat, clarifier mes priorités et savoir dans quelle direction avancer.&nbsp;&raquo;",
    "&laquo;&nbsp;Mon projet de résidence principale était bloqué par la question du financement. Amélie m&rsquo;a aidé à revoir le montage stratégique et à retrouver une direction claire. J&rsquo;ai ensuite réalisé mon premier investissement à Paris.&nbsp;&raquo;",
    "&laquo;&nbsp;Mon objectif était de commencer à construire un patrimoine pour pouvoir transmettre quelque chose à mon fils. Amélie m&rsquo;a aidé à structurer ma réflexion et à avancer malgré une situation qui n&rsquo;était pas simple. Six mois plus tard, j&rsquo;ai acheté mon premier studio dans le 1er arrondissement de Paris, un bien que je n&rsquo;aurais pas imaginé pouvoir acquérir au départ.&nbsp;&raquo;",
}}

INCHANGE["temoignages.html"] = {
    "Stéphane D.",
    "Jane V.",
    "Sébastien C.",
    "Bernard L.",
    "Hang N.",
    "Clément R.",
    "François D.",
    "Yann C.",
    "Mr Brainwash,",
    "I Love You",
}

PAGES["temoignages.html"] = {
    "Témoignages": "Client stories",
    "Les investisseurs": "Investors",
    "partagent leur expérience.": "share their experience.",
    "Huit personnes accompagnées racontent leur projet, la décision qu&rsquo;elles avaient à prendre et ce que l&rsquo;accompagnement a changé.":
        "Eight people we have advised describe their project, the decision they faced and what the engagement changed.",
    "Descendre au contenu": "Scroll to content",
    "Ce qu&rsquo;ils en disent.": "In their own words.",
    "Résidence principale &middot; Fontainebleau": "Main home &middot; Fontainebleau",
    "43 ans &middot; Chef de projet informatique &middot; Essilor": "43 &middot; IT project manager &middot; Essilor",
    "Investissement à Paris &amp; Accompagnement Premium &middot; Saint-Maur-des-Fossés":
        "Paris investment &amp; premium engagement &middot; Saint-Maur-des-Fossés",
    "35 ans &middot; Consultante MOA &middot; EDF": "35 &middot; Business analysis consultant &middot; EDF",
    "Investissement locatif à Paris &middot; Paris": "Rental investment in Paris &middot; Paris",
    "31 ans &middot; Contrôleur de gestion &middot; Veolia": "31 &middot; Management accountant &middot; Veolia",
    "Investissement locatif à Paris": "Rental investment in Paris",
    "63 ans &middot; Consultant informatique": "63 &middot; IT consultant",
    "Résidence principale &amp; investissement locatif &middot; Paris / Fontainebleau":
        "Main home &amp; rental investment &middot; Paris / Fontainebleau",
    "42 ans &middot; Comptable &middot; CPAM": "42 &middot; Accountant &middot; CPAM",
    "Diagnostic stratégique &middot; Arbitrage résidence principale / investissement locatif":
        "Strategic diagnostic &middot; Choosing between a main home and a rental investment",
    "30 ans &middot; Ingénieur &middot; Antony": "30 &middot; Engineer &middot; Antony",
    "Résidence principale &amp; premier investissement immobilier à Paris":
        "Main home &amp; a first property investment in Paris",
    "39 ans &middot; Responsable Études et Développement Logiciel &middot; Yerres":
        "39 &middot; Head of software design and development &middot; Yerres",
    "Investissement locatif &middot; Paris 1er": "Rental investment &middot; Paris 1st",
    "42 ans &middot; Indépendant": "42 &middot; Self-employed",
    "Chaque témoignage reflète une expérience individuelle&nbsp;; les résultats varient selon les situations.":
        "Each story reflects one individual experience; results vary from one situation to another.",
    ", 2020. Sérigraphie vue en vitrine, à Paris.": ", 2020. A screenprint seen in a shop window, in Paris.",
    "Pour finir": "To close",
    "Ce qu&rsquo;on retient d&rsquo;un projet mené&nbsp;:": "What stays with you from a project seen through:",
    "la clarté au moment de décider.": "the clarity you had when it was time to decide.",
    "Les témoignages ci-dessus ont été confiés par des investisseurs accompagnés. Chaque situation est différente&nbsp;; les résultats varient.":
        "The stories above were given by investors we have advised. Every situation is different; results vary.",
    "Premier échange": "First conversation",
    "Votre situation mérite": "Your situation deserves",
    "le même soin.": "the same care.",
    "Trente minutes, gratuites et sans engagement, pour comprendre votre point de départ et le périmètre utile.":
        "Thirty minutes, free and without commitment, to understand your starting point and the useful scope.",
    "Réserver un premier échange": "Book a first conversation",
    "Vous préférez écrire&nbsp;?": "Would you rather write?",
    "Passez par le formulaire": "Use the form",
    "Témoignages d&rsquo;investisseurs accompagnés": "Stories from investors we have guided",
    "Une sérigraphie « I love you » exposée en vitrine, la rue et les arbres se reflétant sur le verre":
        "An &ldquo;I love you&rdquo; screenprint in a shop window, the street and the trees reflected in the glass",
}

# La phrase d'Amelie est la sienne : elle reste dans sa langue.
CITATIONS["a-propos.html"] = {
    "&laquo;&nbsp;Ma vraie compétence n&rsquo;est pas de tout savoir sur l&rsquo;immobilier. C&rsquo;est de savoir chercher, vérifier, chiffrer et décider.&nbsp;&raquo;",
}

INCHANGE["a-propos.html"] = {
    "Hanoï",        # un nom de ville, sur la carte postale
    "&gt; 25 M€",   # un montant
}

PAGES["a-propos.html"] = {
    "Mettre la vidéo en pause": "Pause the video",
    "Une approche": "An approach",
    "née du terrain.": "born in the field.",
    "Fondé par Amélie-Thu DUONG, le cabinet s&rsquo;appuie sur une expérience de l&rsquo;investissement immobilier à Paris depuis 2014.":
        "Founded by Amélie-Thu DUONG, the firm draws on experience of property investment in Paris since 2014.",
    "Descendre au contenu": "Scroll to content",
    "Acquisition, financement, exploitation et arbitrage&nbsp;: cette pratique nourrit une approche structurée, des ressources et des accompagnements au service des investisseurs.":
        "Buying, financing, operating and arbitrating: that practice feeds a structured approach, a set of resources and engagements at the service of investors.",
    "01 &middot; Le parcours de la fondatrice": "01 &middot; The founder&rsquo;s path",
    "Construire sans mode d&rsquo;emploi.": "Building without an instruction manual.",
    "Née au Vietnam, Amélie arrive en France à 20 ans sans parler français, avec l&rsquo;envie d&rsquo;y construire sa vie.":
        "Born in Vietnam, Amélie arrived in France at 20 without speaking French, wanting to build a life there.",
    "Après ses études, elle travaille dans la banque à Paris. En parallèle de son CDI, elle achète son premier bien en 2014. Elle apprend à analyser les financements, le marché, les travaux et les structures, puis à relier ces dimensions pour décider.":
        "After her studies she worked in banking in Paris. Alongside that permanent post, she bought her first property in 2014. She learned to analyse financing, the market, building works and legal structures &mdash; and then to connect all of it in order to decide.",
    "Chaque projet enrichit cette expérience et les principes qui guident aujourd&rsquo;hui Amélie &amp; Partners.":
        "Each project adds to that experience, and to the principles that guide Amélie &amp; Partners today.",
    "Amélie-Thu DUONG &middot; Fondatrice &amp; Investisseuse à Paris depuis 2014":
        "Amélie-Thu DUONG &middot; Founder &amp; investor in Paris since 2014",
    "Amélie-Thu DUONG &middot; Fondatrice": "Amélie-Thu DUONG &middot; Founder",
    "Du Viêt Nam&hellip;": "From Viêt Nam&hellip;",
    "à Paris.": "to Paris.",
    "Le départ": "The start",
    "Née au Viêt Nam.": "Born in Viêt Nam.",
    "À 20 ans": "At 20",
    "Arrivée en France, sans parler français.": "Arrives in France, without speaking French.",
    "Après les études": "After her studies",
    "La banque, à Paris.": "Banking, in Paris.",
    "Première acquisition, en parallèle du CDI.": "A first purchase, alongside the day job.",
    "02 &middot; La pratique": "02 &middot; The practice",
    "Le terrain avant le discours.": "The field before the talk.",
    "Un investissement se joue rarement dans un tableau seul. Il se joue dans la rue, dans l&rsquo;immeuble, dans les documents, dans les échanges avec la banque, dans les travaux et dans la façon dont l&rsquo;actif vivra après l&rsquo;achat.":
        "An investment is rarely settled in a spreadsheet alone. It is settled in the street, in the building, in the paperwork, in the conversations with the bank, in the works &mdash; and in how the asset will live once it is bought.",
    "L&rsquo;approche d&rsquo;Amélie &amp; Partners recherche cette cohérence d&rsquo;ensemble&nbsp;: le bien, le prix, la dette, la trésorerie, l&rsquo;exploitation, le risque et la suite du parcours.":
        "The Amélie &amp; Partners approach looks for that overall coherence: the property, the price, the debt, the cash, the operation, the risk and what comes next.",
    "Comprendre notre approche": "Understand our approach",
    "03 &middot; Pourquoi transmettre&nbsp;?": "03 &middot; Why pass it on?",
    "Rendre les décisions": "Making decisions",
    "plus accessibles.": "more reachable.",
    "Amélie &amp; Partners structure et transmet les enseignements du terrain pour aider les investisseurs à comprendre leurs choix et à agir avec méthode.":
        "Amélie &amp; Partners sets down what the field teaches, and passes it on, so that investors understand their choices and act with method.",
    "Des ressources gratuites pour démystifier les fausses croyances. Des méthodes structurées pour apprendre à raisonner. Et, lorsque la situation le justifie, une expertise personnalisée pour décider ou exécuter avec plus de précision.":
        "Free resources to clear away false beliefs. Structured methods for learning to reason. And, where the situation warrants it, tailored expertise for deciding or executing with more precision.",
    "L&rsquo;objectif n&rsquo;est pas que vous suiviez une recette. C&rsquo;est que vous deveniez capable de comprendre la logique et de garder votre autonomie.":
        "The aim is not for you to follow a recipe. It is for you to grasp the logic, and keep your independence.",
    "Première acquisition à Paris": "First purchase in Paris",
    "Investisseurs accompagnés": "Investors advised",
    "Projets immobiliers structurés": "Property projects structured",
    "Projets parisiens étudiés": "Paris projects examined",
    "Le terrain": "The field",
    "Paris, au quotidien.": "Paris, day to day.",
    "Les projets accompagnés se jouent dans la rue, dans l&rsquo;immeuble et dans les documents autant que dans les tableaux.":
        "The projects we advise on are settled in the street, in the building and in the paperwork as much as in the spreadsheets.",
    "Mettre le défilement en pause": "Pause the scrolling",
    "Reprendre le défilement": "Resume the scrolling",
    "Travailler ensemble": "Working together",
    "Vous n&rsquo;avez pas besoin de tout savoir avant d&rsquo;avancer.": "You do not need to know everything before moving.",
    "Vous avez besoin de poser la bonne question, puis de vérifier chaque hypothèse dans le bon ordre.":
        "You need to ask the right question, then check each assumption in the right order.",
    "Analyser ma situation": "Analyse my situation",
    "Vous préférez écrire&nbsp;?": "Would you rather write?",
    "Passez par le formulaire": "Use the form",
    "Vidéo d’ambiance, sans son, en boucle.": "Ambient video, silent, looping.",
    "Reprendre la vidéo": "Resume the video",
    "Portrait d&rsquo;Amélie-Thu DUONG, dans un jardin": "Portrait of Amélie-Thu DUONG, in a garden",
    "La tour Eiffel vue depuis la Seine, un bateau-mouche au premier plan":
        "The Eiffel Tower seen from the Seine, a river boat in the foreground",
    "La tour de la Tortue et son reflet sur le lac Hoan Kiem, à la tombée du jour":
        "The Turtle Tower and its reflection on Hoan Kiem Lake, at nightfall",
    "Étals de bouquinistes le long des quais de Seine": "Booksellers&rsquo; stalls along the banks of the Seine",
}

PAGES["formulaire.html"] = {
    "Nous écrire": "Write to us",
    "Présentez": "Tell us about",
    "votre situation.": "your situation.",
    "Quelques lignes suffisent. Une réponse vous indiquera si un échange est utile et sous quel format.":
        "A few lines are enough. We will reply to say whether a conversation would be useful, and in what format.",
    "Descendre au contenu": "Scroll to content",
    "Formulaire de contact": "Contact form",
    "Ce qu&rsquo;il nous faut pour vous répondre": "What we need in order to reply",
    "Votre projet ou la décision qui vous bloque": "Your project, or the decision you are stuck on",
    "Le profil d&rsquo;investisseur dont vous vous sentez le plus proche": "The investor profile you feel closest to",
    "L&rsquo;échéance que vous avez en tête, même approximative": "The timeframe you have in mind, even a rough one",
    "Ne pas remplir": "Do not fill in",
    "Prénom": "First name",
    "Nom": "Surname",
    "Adresse e-mail": "Email address",
    "Téléphone": "Telephone",
    "facultatif": "optional",
    "France (+33)": "France (+33)",
    "Belgique (+32)": "Belgium (+32)",
    "Suisse (+41)": "Switzerland (+41)",
    "Luxembourg (+352)": "Luxembourg (+352)",
    "Monaco (+377)": "Monaco (+377)",
    "Espagne (+34)": "Spain (+34)",
    "Portugal (+351)": "Portugal (+351)",
    "Italie (+39)": "Italy (+39)",
    "Allemagne (+49)": "Germany (+49)",
    "Royaume-Uni (+44)": "United Kingdom (+44)",
    "Irlande (+353)": "Ireland (+353)",
    "Pays-Bas (+31)": "Netherlands (+31)",
    "États-Unis / Canada (+1)": "United States / Canada (+1)",
    "Maroc (+212)": "Morocco (+212)",
    "Tunisie (+216)": "Tunisia (+216)",
    "Algérie (+213)": "Algeria (+213)",
    "Sénégal (+221)": "Senegal (+221)",
    "Côte d’Ivoire (+225)": "Côte d’Ivoire (+225)",
    "La Réunion (+262)": "Réunion (+262)",
    "Guadeloupe (+590)": "Guadeloupe (+590)",
    "Martinique (+596)": "Martinique (+596)",
    "Nouvelle-Calédonie (+687)": "New Caledonia (+687)",
    "Viêt Nam (+84)": "Viêt Nam (+84)",
    "Singapour (+65)": "Singapore (+65)",
    "Émirats arabes unis (+971)": "United Arab Emirates (+971)",
    "Vous êtes": "You are",
    "Sélectionner": "Select",
    "Particulier": "A private individual",
    "Professionnel": "A professional",
    "Société (SCI, holding)": "A company (SCI, holding)",
    "Autre": "Other",
    "Votre échéance": "Your timeframe",
    "Dans les trois mois": "Within three months",
    "Dans trois à six mois": "In three to six months",
    "Dans six à douze mois": "In six to twelve months",
    "Au-delà d’un an": "More than a year away",
    "Pas de date fixée": "No date set",
    "Votre profil d&rsquo;investisseur": "Your investor profile",
    "Primo-investisseur · se constituer un patrimoine": "First-time investor · building up assets",
    "Investisseur locatif · générer des revenus réguliers": "Rental investor · generating regular income",
    "Rentier · vivre des revenus immobiliers": "Living off property · income as a livelihood",
    "Investisseur patrimonial · préserver et développer son capital":
        "Wealth-minded investor · preserving and growing capital",
    "Chasseur de rendement · maximiser la rentabilité": "Yield hunter · maximising returns",
    "Marchand de biens · acheter, rénover, revendre": "Property trader · buy, renovate, resell",
    "Investisseur fiscal · réduire sa fiscalité": "Tax-driven investor · reducing the tax bill",
    "Professionnel ou entrepreneur · développer un portefeuille":
        "Professional or entrepreneur · growing a portfolio",
    "Investisseur familial · transmettre un patrimoine": "Family investor · passing assets on",
    "Investisseur opportuniste · saisir une occasion": "Opportunistic investor · seizing a chance",
    "Investisseur en SCPI · investir sans gérer un bien":
        "SCPI investor · investing without managing a property",
    "Investisseur institutionnel · placer des capitaux importants":
        "Institutional investor · placing substantial capital",
    "Je ne sais pas encore": "I do not know yet",
    "Votre situation en quelques lignes": "Your situation, in a few lines",
    "de 20 à 5 000 caractères": "from 20 to 5,000 characters",
    "J&rsquo;accepte que ces informations soient utilisées pour répondre à ma demande, conformément à la page":
        "I agree that this information may be used to answer my enquiry, as set out on the page",
    "Données personnelles": "Personal data (in French)",
    "Envoyer mon message": "Send my message",
    "Champs nécessaires. Votre message nous est envoyé directement, sans passer par votre logiciel de messagerie. Nous répondons sous un jour ouvré.":
        "Required fields. Your message reaches us directly, without going through your email software. We reply within one working day.",
    "Les informations saisies servent uniquement à traiter votre demande et le suivi commercial qui en découle. Elles sont conservées trois ans à compter du dernier contact et ne sont ni vendues, ni cédées, ni louées. Vous disposez d&rsquo;un droit d&rsquo;accès, de rectification, d&rsquo;effacement et d&rsquo;opposition, que vous pouvez exercer par ce même formulaire. Le détail figure dans les":
        "What you enter is used only to handle your enquiry and the commercial follow-up arising from it. It is kept for three years from the last contact, and is never sold, transferred or rented out. You have rights of access, correction, erasure and objection, which you can exercise through this same form. The details are set out in the",
    "données personnelles": "personal data notice, in French",
    "Votre message est parti.": "Your message is on its way.",
    "Nous le lisons et vous répondons sous un jour ouvré, à l&rsquo;adresse que vous avez indiquée.":
        "We will read it and reply within one working day, to the address you gave us.",
    "Si votre situation demande d&rsquo;en parler plus tôt, le premier échange de trente minutes est ouvert à la réservation, gratuitement et sans engagement.":
        "If your situation calls for talking sooner, the thirty-minute first conversation can be booked, free and without commitment.",
    "Réserver un premier échange": "Book a first conversation",
    "Fermer": "Close",
    "Vous préférez parler de vive voix&nbsp;? L&rsquo;appel de cadrage dure trente minutes, il est gratuit et sans engagement.":
        "Would you rather speak? The framing call lasts thirty minutes, and is free and without commitment.",
    "Votre prénom": "Your first name",
    "Votre prénom nous permet de vous répondre correctement.": "Your first name lets us address you properly.",
    "Votre nom": "Your surname",
    "Nous avons besoin de votre nom.": "We need your surname.",
    "prenom.nom@exemple.fr": "first.last@example.com",
    "Sans adresse, nous ne pourrons pas vous répondre.": "Without an address, we cannot reply to you.",
    "Il manque quelque chose : une adresse s’écrit prenom.nom@exemple.fr.":
        "Something is missing: an address looks like first.last@example.com.",
    "Indicatif du pays": "Country dialling code",
    "Un numéro s’écrit en chiffres, espaces, points ou tirets.":
        "A number is written with digits, spaces, dots or dashes.",
    "Dites-nous à quel titre vous écrivez.": "Tell us in what capacity you are writing.",
    "Même approximative, elle nous aide à prioriser.": "Even a rough one helps us set priorities.",
    "Choisissez le profil le plus proche, ou « je ne sais pas encore ».":
        "Choose the closest profile, or &ldquo;I do not know yet&rdquo;.",
    "Votre projet ou la décision qui vous bloque, votre point de départ, et ce que vous attendez de cet échange.":
        "Your project or the decision you are stuck on, your starting point, and what you hope to get from the conversation.",
    "Quelques lignes suffisent : elles nous évitent un aller-retour.":
        "A few lines are enough: they save us a round trip.",
    "Quelques mots de plus, pour que nous puissions préparer une réponse utile.":
        "A few more words, so that we can prepare a useful reply.",
    "Cette case doit être cochée pour que nous puissions vous répondre.":
        "This box must be ticked before we can reply to you.",
}

# La phrase qui resume les trois effets est celle d'Amelie : elle reste
# dans sa langue.
CITATIONS["ressource-3-effets.html"] = {
    "&laquo;&nbsp;Le levier permet d&rsquo;acheter. L&rsquo;ascenseur construit le capital. La boule de neige le remet en mouvement.&nbsp;&raquo;",
}

PAGES["ressource-3-effets.html"] = {
    "Cadre pédagogique &middot; 8 min de lecture": "Teaching note &middot; 8 min read",
    "Les 3 effets": "The three effects",
    "dans l&rsquo;immobilier.": "in property.",
    "Le vrai sujet n&rsquo;est pas seulement le rendement. C&rsquo;est la manière dont un actif permet de contrôler, construire puis réemployer du capital.":
        "The real subject is not yield alone. It is the way an asset lets you control capital, build it, and then put it back to work.",
    "Par Amélie-Thu DUONG": "By Amélie-Thu DUONG",
    "Septembre 2026": "September 2026",
    "Descendre au contenu": "Scroll to content",
    "Format": "Format",
    "Fiche de lecture, en ligne, en accès libre": "A reading note, online, freely available",
    "Durée": "Length",
    "8&nbsp;minutes de lecture": "8&nbsp;minutes&rsquo; reading",
    "Niveau": "Level",
    "Premier niveau, sans prérequis financier": "Introductory, no financial background needed",
    "Pour qui": "For whom",
    "Toute personne qui prépare ou relit un investissement": "Anyone preparing or re-reading an investment",
    "Mise à jour": "Updated",
    "Emporter la fiche": "Take the note with you",
    "À lire hors ligne, ou à faire circuler.": "To read offline, or to pass on.",
    "PDF, 306&nbsp;Ko, 3 pages. Le partage ouvre votre messagerie avec un message déjà rédigé&nbsp;: rien n&rsquo;est envoyé sans votre validation.":
        "PDF, 306&nbsp;kB, 3 pages, in French. Sharing opens your email software with the message already written: nothing is sent without your say-so.",
    "Télécharger le PDF": "Download the PDF (in French)",
    "Partager par e-mail": "Share by email",
    "Objectifs de la fiche": "What the note is for",
    "Ce que cette lecture vous permet de faire.": "What this reading lets you do.",
    "Distinguer les trois mécanismes qui se succèdent dans une opération&nbsp;: le levier, l&rsquo;ascenseur, la boule de neige.":
        "Tell apart the three mechanisms that follow one another in a transaction: the lever, the lift, the snowball.",
    "Lire une opération autrement que par son seul rendement.": "Read a transaction by something other than its yield alone.",
    "Mesurer le capital réellement créé dans un actif, et non sa seule valeur.":
        "Measure the capital actually created inside an asset, not just its value.",
    "Situer le moment où un capital doit rester mobilisé, être refinancé ou être libéré.":
        "Judge when capital should stay tied up, be refinanced, or be released.",
    "Au programme": "What is covered",
    "Trois mécanismes,": "Three mechanisms,",
    "dans l&rsquo;ordre où ils se produisent.": "in the order they occur.",
    "Ils ne sont pas trois stratégies séparées. Ils forment une chaîne&nbsp;: chacun rend le suivant possible.":
        "They are not three separate strategies. They form a chain: each one makes the next possible.",
    "Amplifier&nbsp;: l&rsquo;effet de levier": "Amplify: the leverage effect",
    "Ce que la dette permet de contrôler, et ce qu&rsquo;elle amplifie en retour.":
        "What debt lets you control, and what it amplifies in return.",
    "Créer&nbsp;: l&rsquo;effet ascenseur": "Create: the lift effect",
    "Comment un actif financé se transforme progressivement en capital net.":
        "How a financed asset gradually turns into net capital.",
    "Réinvestir&nbsp;: l&rsquo;effet boule de neige": "Reinvest: the snowball effect",
    "Ce que devient le capital créé, et à quelle condition il repart au travail.":
        "What becomes of the capital created, and on what condition it goes back to work.",
    "La logique": "The logic",
    "Amplifier": "Amplify",
    "Créer": "Create",
    "Réinvestir": "Reinvest",
    "Appliquer à ma situation": "Apply this to my situation",
    "Quand on débute, on regarde souvent un investissement à travers un seul chiffre&nbsp;: le rendement. Il est utile, mais il ne suffit pas à expliquer comment un patrimoine se construit réellement.":
        "When you are starting out, you tend to look at an investment through a single figure: the yield. It is useful, but it does not explain how a portfolio is actually built.",
    "Pour lire une opération dans le temps, nous distinguons trois mécanismes. Ils ne sont pas trois stratégies séparées. Ils forment une chaîne&nbsp;: le levier permet de contrôler un actif, l&rsquo;ascenseur transforme progressivement la dette en capital net, puis la boule de neige remet ce capital au travail.":
        "To read a transaction over time, we separate out three mechanisms. They are not three separate strategies. They form a chain: the lever lets you control an asset, the lift gradually turns debt into net capital, and the snowball puts that capital back to work.",
    "01 &middot; Amplifier&nbsp;: l&rsquo;effet de levier": "01 &middot; Amplify: the leverage effect",
    "Notion clé": "Key idea",
    "Utiliser la dette bancaire pour contrôler un actif d&rsquo;une valeur supérieure à ses fonds propres.":
        "Using bank debt to control an asset worth more than your own funds.",
    "L&rsquo;effet de levier consiste à utiliser la dette bancaire pour contrôler un actif d&rsquo;une valeur supérieure à vos fonds propres. Avec 50&nbsp;000&nbsp;€ d&rsquo;apport, vous ne contrôlez pas seulement 50&nbsp;000&nbsp;€ d&rsquo;actif&nbsp;: vous pouvez contrôler une opération beaucoup plus importante, à condition que le financement reste soutenable.":
        "Leverage means using bank debt to control an asset worth more than your own funds. With a 50,000&nbsp;€ deposit you do not control only 50,000&nbsp;€ of asset: you can control a far larger transaction &mdash; provided the financing stays sustainable.",
    "Le levier amplifie le pouvoir d&rsquo;achat, mais il amplifie aussi les conséquences d&rsquo;une mauvaise hypothèse. Le taux, la durée, le niveau de mensualité, la vacance, les travaux et la marge de sécurité doivent être lus ensemble.":
        "Leverage amplifies buying power, but it also amplifies the consequences of a wrong assumption. The rate, the term, the monthly payment, void periods, the works and the safety margin have to be read together.",
    "La bonne question": "The right question",
    "Quelle quantité de dette puis-je utiliser sans fragiliser la suite de ma trajectoire&nbsp;?":
        "How much debt can I take on without weakening the rest of my trajectory?",
    "02 &middot; Créer&nbsp;: l&rsquo;effet ascenseur": "02 &middot; Create: the lift effect",
    "Le mouvement qui transforme progressivement un actif financé en capital net.":
        "The movement that gradually turns a financed asset into net capital.",
    "Nous appelons «&nbsp;effet ascenseur&nbsp;» le mouvement qui transforme progressivement un actif financé en capital net. À mesure que la dette s&rsquo;amortit, que les loyers sont encaissés, que des travaux créent de la valeur ou que le marché évolue, l&rsquo;écart entre la valeur du bien et le capital restant dû peut augmenter.":
        "We call the &ldquo;lift effect&rdquo; the movement that gradually turns a financed asset into net capital. As the debt is paid down, as rents come in, as works create value or as the market moves, the gap between the value of the property and the outstanding balance can widen.",
    "Ce capital existe, mais il peut rester enfermé dans l&rsquo;actif. L&rsquo;enjeu est donc de le mesurer, puis de décider s&rsquo;il doit rester mobilisé, être refinancé ou être libéré par un arbitrage. C&rsquo;est souvent là que se joue le changement d&rsquo;échelle.":
        "That capital exists, but it can stay locked inside the asset. The task is to measure it, then decide whether it should stay tied up, be refinanced, or be released by selling. This is often where a change of scale is decided.",
    "Lecture simplifiée": "A simplified reading",
    "Valeur du bien &minus; dette restante = capital net dans l&rsquo;actif. À compléter par les coûts de sortie, la fiscalité et la trésorerie réellement disponible.":
        "Value of the property &minus; outstanding debt = net capital in the asset. To be completed by exit costs, tax, and the cash actually available.",
    "Combien de capital ai-je créé, et que pourrait-il produire s&rsquo;il était libéré&nbsp;?":
        "How much capital have I created, and what could it produce if it were released?",
    "03 &middot; Réinvestir&nbsp;: l&rsquo;effet boule de neige": "03 &middot; Reinvest: the snowball effect",
    "Le capital déjà créé qui finance, à son tour, de nouveaux actifs.":
        "Capital already created going on to finance new assets in its turn.",
    "L&rsquo;effet boule de neige commence lorsque le capital déjà créé finance de nouveaux actifs. Un apport provenant d&rsquo;un arbitrage, une trésorerie accumulée ou un capital refinancé peut servir de point de départ à une opération plus importante.":
        "The snowball effect starts when capital already created finances new assets. A deposit released by a sale, accumulated cash or refinanced capital can be the starting point for a larger transaction.",
    "La vitesse n&rsquo;est pas l&rsquo;objectif en soi. Réinvestir trop vite, sans conserver de marge de sécurité, peut affaiblir tout le système. Le capital doit être réemployé selon l&rsquo;objectif, le risque accepté et les besoins de liquidité.":
        "Speed is not the point. Reinvesting too quickly, without keeping a safety margin, can weaken the whole structure. Capital should be redeployed according to the objective, the risk accepted and the need for liquidity.",
    "Où ce capital peut-il être le plus utile maintenant&nbsp;: nouvel actif, sécurité, diversification ou attente&nbsp;?":
        "Where is this capital most useful now: a new asset, safety, diversification, or waiting?",
    "Ce que cela change dans vos décisions": "What this changes in your decisions",
    "Vous ne regardez plus seulement «&nbsp;combien rapporte ce bien&nbsp;?&nbsp;». Vous cherchez à comprendre quelle quantité de capital il mobilise, ce qu&rsquo;il crée réellement et si ce capital est encore placé au bon endroit.":
        "You no longer look only at &ldquo;how much does this property earn?&rdquo;. You try to understand how much capital it ties up, what it actually creates, and whether that capital is still in the right place.",
    "C&rsquo;est cette lecture qui permet de choisir entre acheter, conserver, refinancer, vendre ou attendre, sans transformer l&rsquo;accumulation de biens en objectif final.":
        "It is this reading that lets you choose between buying, holding, refinancing, selling or waiting &mdash; without turning the accumulation of properties into the goal itself.",
    "Points de vigilance": "Points to watch",
    "Ce que la fiche ne passe pas sous silence.": "What the note does not gloss over.",
    "Le levier amplifie le pouvoir d&rsquo;achat, mais il amplifie aussi les conséquences d&rsquo;une mauvaise hypothèse.":
        "Leverage amplifies buying power, but it also amplifies the consequences of a wrong assumption.",
    "Le capital net ne se lit qu&rsquo;après les coûts de sortie, la fiscalité et la trésorerie réellement disponible.":
        "Net capital can only be read after exit costs, tax, and the cash actually available.",
    "Réinvestir trop vite, sans conserver de marge de sécurité, peut affaiblir tout le système.":
        "Reinvesting too quickly, without keeping a safety margin, can weaken the whole structure.",
    "La vitesse n&rsquo;est pas un objectif&nbsp;: le capital se réemploie selon l&rsquo;objectif, le risque accepté et les besoins de liquidité.":
        "Speed is not a goal: capital is redeployed according to the objective, the risk accepted and the need for liquidity.",
    "Cette fiche est pédagogique et générale. Elle ne remplace pas une analyse juridique, fiscale ou financière adaptée à votre situation. Les résultats varient selon les situations.":
        "This note is educational and general. It does not replace legal, tax or financial analysis fitted to your situation. Results vary from one situation to another.",
    "Appliquer le raisonnement à votre situation": "Applying the reasoning to your situation",
    "Votre capital est-il encore placé au bon endroit&nbsp;?": "Is your capital still in the right place?",
    "Le Diagnostic Stratégique reprend cette lecture avec vos chiffres, vos contraintes et votre horizon.":
        "The Diagnostic Stratégique takes up this reading with your figures, your constraints and your horizon.",
    "Découvrir le Diagnostic Stratégique": "Discover the Diagnostic Stratégique",
    "Vous préférez écrire&nbsp;?": "Would you rather write?",
    "Passez par le formulaire": "Use the form",
    "Les trois effets": "The three effects",
}
