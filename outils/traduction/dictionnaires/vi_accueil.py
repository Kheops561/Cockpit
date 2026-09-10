# -*- coding: utf-8 -*-
"""L'accueil, en vietnamien.

Une entrée par chaîne visible de `index.html`. `traduire.py` refuse de
fabriquer la page si une seule manque : ce fichier est donc exhaustif par
construction.

Le ton visé est celui du site : posé, précis, sans emphase. Le vietnamien
des affaires emploie « quý vị » pour s'adresser au lecteur avec respect sans
lui donner d'âge ni de rang ; c'est la forme retenue partout.

Ce qui ne se traduit pas : le nom du cabinet, sa signature, les quatre
offres, les cinq verdicts, les noms de personnes et de lieux. Le prix reste
français — la prestation est vendue et facturée en France, sous TVA
française : « TTC » devient « đã gồm VAT của Pháp », et rien n'est converti.
"""

VI = {
    "Mettre la vidéo en pause": "Tạm dừng video",
    "Votre partenaire stratégique": "Đối tác chiến lược của quý vị",
    "pour réussir vos projets immobiliers.": "cho các dự án bất động sản.",
    "De la stratégie à la mise en œuvre, Amélie &amp; Partners accompagne les investisseurs pour financer, acquérir et piloter leur patrimoine immobilier.":
        "Từ chiến lược đến thực hiện, Amélie &amp; Partners đồng hành cùng nhà đầu tư trong việc thu xếp tài chính, mua và quản lý tài sản bất động sản.",
    "30 minutes pour faire le point": "30 phút để nhìn lại tình hình",
    "Gratuit, sans engagement": "Miễn phí, không ràng buộc",
    "Regard indépendant": "Góc nhìn độc lập",
    "Réserver un premier échange": "Đặt buổi trao đổi đầu tiên",
    "Fondatrice &amp; Investisseuse à Paris depuis 2014":
        "Nhà sáng lập &amp; nhà đầu tư tại Paris từ năm 2014",
    "Descendre au contenu": "Xuống phần nội dung",
    "investisseurs accompagnés": "nhà đầu tư được đồng hành",
    "de projets structurés": "giá trị dự án đã cấu trúc",
    "décisions analysées": "quyết định đã phân tích",
    "projets à Paris accompagnés": "dự án tại Paris được đồng hành",
    "Notre approche": "Phương pháp của chúng tôi",
    "Une vision d&rsquo;ensemble.": "Một cái nhìn tổng thể.",
    "Des décisions cohérentes.": "Những quyết định nhất quán.",
    "Chaque projet s&rsquo;inscrit dans une trajectoire. L&rsquo;accompagnement relie vos objectifs, votre financement et vos choix immobiliers pour préparer la suite avec cohérence.":
        "Mỗi dự án nằm trong một lộ trình. Việc đồng hành nối mục tiêu, nguồn vốn và các lựa chọn bất động sản của quý vị lại với nhau, để chuẩn bị bước tiếp theo một cách nhất quán.",
    "Comprendre votre situation": "Hiểu tình hình của quý vị",
    "Partir de vos objectifs, de votre capital et de votre réalité.":
        "Xuất phát từ mục tiêu, nguồn vốn và thực tế của quý vị.",
    "Challenger vos options": "Thử thách các lựa chọn",
    "Comparer les scénarios, vérifier les hypothèses et identifier les risques.":
        "So sánh các kịch bản, kiểm chứng giả định và nhận diện rủi ro.",
    "Avancer à vos côtés": "Tiến bước cùng quý vị",
    "Vous accompagner dans la mise en œuvre, selon le périmètre de notre mission.":
        "Đồng hành trong khâu thực hiện, trong phạm vi đã thống nhất.",
    "Découvrir notre approche": "Tìm hiểu phương pháp",
    "Le terrain, plutôt que le discours.": "Thực địa, chứ không phải lời nói.",
    "Un investissement se joue dans la rue, dans l&rsquo;immeuble, dans les documents et dans les échanges avec la banque.":
        "Một khoản đầu tư được định đoạt ngoài đường phố, trong toà nhà, trong hồ sơ giấy tờ và trong những cuộc trao đổi với ngân hàng.",
    "Découvrir la pratique": "Tìm hiểu cách làm việc",
    "Les accompagnements": "Các dịch vụ",
    "Le bon appui,": "Đúng sự hỗ trợ,",
    "au bon moment.": "đúng thời điểm.",
    "Une décision ponctuelle ou une trajectoire à piloter : nous partons de votre besoin.":
        "Một quyết định đơn lẻ hay cả một lộ trình cần dẫn dắt: chúng tôi xuất phát từ nhu cầu của quý vị.",
    "01 &middot; Diagnostiquer": "01 &middot; Chẩn đoán",
    "Une décision à clarifier": "Một quyết định cần làm rõ",
    "Mettre vos options à plat et déterminer la prochaine étape.":
        "Bày rõ các lựa chọn và xác định bước tiếp theo.",
    "02 &middot; Financer": "02 &middot; Thu xếp tài chính",
    "Un projet à rendre possible": "Một dự án cần trở nên khả thi",
    "Comprendre vos ressources, vos contraintes et ce qu&rsquo;il faut préparer.":
        "Hiểu nguồn lực, ràng buộc và những gì cần chuẩn bị.",
    "Stratégie de Financement": "Stratégie de Financement",
    "03 &middot; Acheter": "03 &middot; Mua",
    "Un bien à trouver à Paris": "Một bất động sản cần tìm tại Paris",
    "Rechercher, analyser et négocier avec un partenaire à vos côtés.":
        "Tìm kiếm, phân tích và thương lượng cùng một người đồng hành.",
    "Recherche immobilière à Paris": "Recherche immobilière à Paris",
    "04 &middot; Piloter": "04 &middot; Dẫn dắt",
    "Une trajectoire à construire": "Một lộ trình cần dựng nên",
    "Prioriser vos projets et arbitrer les décisions au fil du temps.":
        "Sắp thứ tự ưu tiên và cân nhắc các quyết định theo thời gian.",
    "Trajectoire Investisseur": "Trajectoire Investisseur",
    "Témoignages": "Khách hàng nói gì",
    "Les investisseurs partagent leur expérience.":
        "Các nhà đầu tư kể lại trải nghiệm của họ.",
    "Résidence principale &middot; Fontainebleau": "Nhà ở chính &middot; Fontainebleau",
    "43 ans &middot; Chef de projet informatique &middot; Essilor":
        "43 tuổi &middot; Quản lý dự án tin học &middot; Essilor",
    "Investissement à Paris &amp; Accompagnement Premium &middot; Saint-Maur-des-Fossés":
        "Đầu tư tại Paris &amp; đồng hành cao cấp &middot; Saint-Maur-des-Fossés",
    "35 ans &middot; Consultante MOA &middot; EDF":
        "35 tuổi &middot; Chuyên viên tư vấn nghiệp vụ &middot; EDF",
    "Investissement locatif à Paris &middot; Paris":
        "Đầu tư cho thuê tại Paris &middot; Paris",
    "31 ans &middot; Contrôleur de gestion &middot; Veolia":
        "31 tuổi &middot; Kiểm soát viên tài chính &middot; Veolia",
    "Investissement locatif à Paris": "Đầu tư cho thuê tại Paris",
    "63 ans &middot; Consultant informatique": "63 tuổi &middot; Tư vấn tin học",
    "Résidence principale &amp; investissement locatif &middot; Paris / Fontainebleau":
        "Nhà ở chính &amp; đầu tư cho thuê &middot; Paris / Fontainebleau",
    "42 ans &middot; Comptable &middot; CPAM": "42 tuổi &middot; Kế toán &middot; CPAM",
    "Diagnostic stratégique &middot; Arbitrage résidence principale / investissement locatif":
        "Chẩn đoán chiến lược &middot; Cân nhắc giữa nhà ở chính và đầu tư cho thuê",
    "30 ans &middot; Ingénieur &middot; Antony": "30 tuổi &middot; Kỹ sư &middot; Antony",
    "Résidence principale &amp; premier investissement immobilier à Paris":
        "Nhà ở chính &amp; khoản đầu tư bất động sản đầu tiên tại Paris",
    "39 ans &middot; Responsable Études et Développement Logiciel &middot; Yerres":
        "39 tuổi &middot; Trưởng bộ phận nghiên cứu và phát triển phần mềm &middot; Yerres",
    "Investissement locatif &middot; Paris 1er": "Đầu tư cho thuê &middot; Paris quận 1",
    "42 ans &middot; Indépendant": "42 tuổi &middot; Lao động tự do",
    "Chaque témoignage reflète une expérience individuelle&nbsp;; les résultats varient selon les situations.":
        "Mỗi lời kể phản ánh một trải nghiệm riêng; kết quả thay đổi tuỳ theo từng hoàn cảnh.",
    "Premier échange &middot; 30 minutes &middot; gratuit":
        "Buổi trao đổi đầu tiên &middot; 30 phút &middot; miễn phí",
    "Parlons de votre": "Hãy nói về",
    "prochaine décision.": "quyết định sắp tới của quý vị.",
    "Trente minutes pour comprendre votre situation, vérifier si Amélie &amp; Partners peut vous aider et définir le périmètre utile.":
        "Ba mươi phút để hiểu tình hình của quý vị, xem Amélie &amp; Partners có thể giúp được gì và xác định phạm vi công việc hữu ích.",
    "Avec plaisir": "Rất hân hạnh",
    "Choisissons un créneau.": "Hãy chọn một khung giờ.",
    "30 minutes &middot; gratuit &middot; sans conseil approfondi &middot; sans engagement":
        "30 phút &middot; miễn phí &middot; chưa phải tư vấn chuyên sâu &middot; không ràng buộc",
    "Vous préférez écrire&nbsp;?": "Quý vị muốn viết hơn?",
    "Passez par le formulaire": "Dùng biểu mẫu",
    "Pour une analyse approfondie": "Để có một phân tích chuyên sâu",
    "Une décision argumentée, pas un avis de plus.":
        "Một quyết định có lập luận, không phải thêm một ý kiến nữa.",
    "Un questionnaire préparatoire, une session d&rsquo;une heure et votre Note de Diagnostic &amp; Décision pour savoir comment avancer.":
        "Một bảng câu hỏi chuẩn bị, một buổi làm việc một giờ và bản Ghi chú Chẩn đoán &amp; Quyết định để biết cần tiến hành ra sao.",
    "Découvrir le diagnostic": "Tìm hiểu buổi chẩn đoán",
    "TTC": "đã gồm VAT của Pháp",
    "Prestation ponctuelle, sans abonnement ni engagement.":
        "Dịch vụ đơn lẻ, không thuê bao, không ràng buộc. Được định giá và xuất hoá đơn tại Pháp, theo thuế VAT và luật pháp Pháp.",
    "Ce qui est compris": "Bao gồm những gì",
    "Un questionnaire préparatoire": "Một bảng câu hỏi chuẩn bị",
    "Une session stratégique d&rsquo;une heure": "Một buổi làm việc chiến lược kéo dài một giờ",
    "Votre Note de Diagnostic &amp; Décision": "Bản Ghi chú Chẩn đoán &amp; Quyết định của quý vị",
    "Un premier échange de cadrage de 30 minutes, gratuit":
        "Một buổi trao đổi định hướng 30 phút, miễn phí",
    "Cinq verdicts possibles&nbsp;: AVANCER, PRÉPARER, RESTRUCTURER, APPROFONDIR, SUSPENDRE.":
        "Năm kết luận có thể có: AVANCER, PRÉPARER, RESTRUCTURER, APPROFONDIR, SUSPENDRE &mdash; tiến hành, chuẩn bị, tái cấu trúc, tìm hiểu sâu hơn, tạm dừng.",
    "Vos questions": "Câu hỏi của quý vị",
    "Avant de": "Trước khi",
    "nous rencontrer.": "chúng ta gặp nhau.",
    "Dois-je déjà posséder un bien immobilier&nbsp;?":
        "Tôi có cần đã sở hữu bất động sản không?",
    "Non. Le diagnostic peut concerner un premier projet comme un patrimoine déjà constitué. La bonne analyse dépend de votre situation, de votre objectif et du moment où vous vous trouvez.":
        "Không. Buổi chẩn đoán có thể dành cho dự án đầu tiên cũng như cho một danh mục đã hình thành. Phân tích đúng phụ thuộc vào tình hình, mục tiêu và thời điểm của quý vị.",
    "Ma banque m&rsquo;a refusé un financement. Pouvez-vous m&rsquo;aider&nbsp;?":
        "Ngân hàng đã từ chối cho tôi vay. Quý công ty có giúp được không?",
    "Oui, lorsque le sujet demande une lecture stratégique du dossier : capacité réelle, revenus retenus, apport, durée, structure ou ordre des opérations. Amélie &amp; Partners n&rsquo;intervient toutefois pas comme courtier en crédit.":
        "Có, khi vấn đề cần một cách đọc hồ sơ ở tầm chiến lược: khả năng vay thực tế, thu nhập được ghi nhận, vốn tự có, thời hạn, cấu trúc hay thứ tự các giao dịch. Tuy vậy, Amélie &amp; Partners không hoạt động như một môi giới tín dụng.",
    "Travaillez-vous uniquement à Paris&nbsp;?": "Quý công ty chỉ làm việc tại Paris thôi sao?",
    "La recherche immobilière est spécialisée sur Paris. Les sujets de décision, d&rsquo;arbitrage et de stratégie de financement peuvent être étudiés au cas par cas pour des projets situés ailleurs en France.":
        "Dịch vụ tìm kiếm bất động sản chuyên về Paris. Các vấn đề về quyết định, cân nhắc và chiến lược tài chính có thể được xem xét theo từng trường hợp cho những dự án ở nơi khác trên đất Pháp.",
    "Pouvez-vous aussi me conseiller de ne pas investir&nbsp;?":
        "Quý công ty có khi nào khuyên tôi đừng đầu tư không?",
    "Oui. L&rsquo;objectif n&rsquo;est pas de provoquer un achat, mais d&rsquo;identifier la décision la plus cohérente. Elle peut être d&rsquo;acheter, d&rsquo;attendre, de consolider, de restructurer ou d&rsquo;arbitrer.":
        "Có. Mục đích không phải là thúc đẩy một thương vụ mua, mà là tìm ra quyết định nhất quán nhất. Quyết định ấy có thể là mua, là chờ, là củng cố, là tái cấu trúc hoặc là bán đi.",
    "Le premier échange gratuit est-il une séance de conseil&nbsp;?":
        "Buổi trao đổi miễn phí đầu tiên có phải là một buổi tư vấn không?",
    "Non. Cet échange de 30 minutes sert à comprendre votre besoin, vérifier si Amélie &amp; Partners peut vous aider et définir le bon périmètre. Le conseil approfondi commence dans le cadre d&rsquo;une mission payante.":
        "Không. Buổi trao đổi 30 phút này nhằm hiểu nhu cầu của quý vị, xem Amélie &amp; Partners có thể giúp được gì và xác định phạm vi phù hợp. Tư vấn chuyên sâu bắt đầu trong khuôn khổ một hợp đồng có phí.",
    "La conviction d&rsquo;Amélie &amp; Partners": "Điều Amélie &amp; Partners tin",
    "&laquo;&nbsp;Le patrimoine n&rsquo;est pas une fin. C&rsquo;est un moyen de gagner en liberté de choix.&nbsp;&raquo;":
        "&laquo;&nbsp;Tài sản không phải là đích đến. Đó là phương tiện để có thêm tự do lựa chọn.&nbsp;&raquo;",
    "Explorer nos ressources": "Khám phá tài liệu của chúng tôi",
    "Vidéo d’ambiance, sans son, en boucle.": "Video không khí, không tiếng, lặp lại.",
    "Reprendre la vidéo": "Tiếp tục video",
    "Portrait d&rsquo;Amélie-Thu DUONG": "Chân dung Amélie-Thu DUONG",
    "Coupole de verre vue depuis le sol, sous une rotonde parisienne":
        "Mái vòm kính nhìn từ dưới lên, bên trong một sảnh tròn ở Paris",
    "Passage couvert parisien, verrière et boutiques":
        "Thương xá có mái kính ở Paris, cùng những cửa hiệu",
    "Témoignages d&rsquo;investisseurs accompagnés":
        "Lời kể của những nhà đầu tư được đồng hành",
}


# ---------------------------------------------------------------------------
# Ce qui reste en francais, et pourquoi.
#
# Les temoignages sont la parole de gens reels : les traduire, ce serait leur
# preter des mots qu'ils n'ont pas dits. Ils restent donc dans leur langue,
# signales comme tels aux lecteurs d'ecran par un `lang="fr"` que pose
# `traduire.py`. Tout autour — le chapeau, les fonctions, la mention que les
# resultats varient — est traduit.
# ---------------------------------------------------------------------------

CITATIONS = {
    "&laquo;&nbsp;Pour l&rsquo;achat de ma résidence principale, Amélie m&rsquo;a apporté un vrai recul. Son analyse et ses questions m&rsquo;ont permis de décider avec beaucoup plus de clarté.&nbsp;&raquo;",
    "&laquo;&nbsp;Je partais de zéro. En deux ans, j&rsquo;ai construit avec Amélie une stratégie qui m&rsquo;a permis d&rsquo;atteindre plus de 1,2 M€ de patrimoine immobilier brut. J&rsquo;ai surtout apprécié sa vision globale et sa capacité à proposer plusieurs chemins.&nbsp;&raquo;",
    "&laquo;&nbsp;Je ne connaissais ni l&rsquo;investissement immobilier ni le marché parisien. En un an, j&rsquo;ai acheté mes deux premiers studios à Paris. Amélie m&rsquo;a surtout appris à comprendre le levier bancaire et à dépasser plusieurs idées reçues.&nbsp;&raquo;",
    "&laquo;&nbsp;J&rsquo;ai commencé l&rsquo;immobilier tard, à l&rsquo;approche de la retraite. Avec Amélie, j&rsquo;ai mis en place une stratégie adaptée qui m&rsquo;a permis d&rsquo;acquérir un local commercial dans le 6&#7497; puis un studio dans le Marais.&nbsp;&raquo;",
    "&laquo;&nbsp;Je partais de zéro. En trois ans, j&rsquo;ai acheté deux studios dans Paris centre et ma résidence principale à Fontainebleau. Amélie m&rsquo;a aidée à avancer étape par étape, sans perdre la vision d&rsquo;ensemble.&nbsp;&raquo;",
    "&laquo;&nbsp;J&rsquo;hésitais entre agrandir ma résidence principale et investir à Paris. Une séance avec Amélie m&rsquo;a suffi pour remettre les options à plat, clarifier mes priorités et savoir dans quelle direction avancer.&nbsp;&raquo;",
    "&laquo;&nbsp;Mon projet de résidence principale était bloqué par la question du financement. Amélie m&rsquo;a aidé à revoir le montage stratégique et à retrouver une direction claire. J&rsquo;ai ensuite réalisé mon premier investissement à Paris.&nbsp;&raquo;",
    "&laquo;&nbsp;Mon objectif était de commencer à construire un patrimoine pour pouvoir transmettre quelque chose à mon fils. Amélie m&rsquo;a aidé à structurer ma réflexion et à avancer malgré une situation qui n&rsquo;était pas simple. Six mois plus tard, j&rsquo;ai acheté mon premier studio dans le 1er arrondissement de Paris, un bien que je n&rsquo;aurais pas imaginé pouvoir acquérir au départ.&nbsp;&raquo;",
}

# Des noms propres et un montant : rien a traduire.
INCHANGE = {
    "Stéphane D.", "Jane V.", "Sébastien C.", "Bernard L.",
    "Hang N.", "Clément R.", "François D.", "Yann C.",
    "&gt; 25 M€",
}
