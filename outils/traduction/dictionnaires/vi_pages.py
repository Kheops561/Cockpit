# -*- coding: utf-8 -*-
"""Les dictionnaires vietnamiens, page par page.

Une entrée par chaîne visible de la page française. `traduire.py` refuse de
fabriquer une page dont une seule chaîne manquerait : ce fichier est donc
exhaustif par construction.

Trois règles tenues partout :

- **Les noms propres ne se traduisent pas** : le cabinet, sa signature, les
  quatre offres, les cinq verdicts, les lieux.
- **Le prix reste français.** 432 € TTC : la prestation est vendue en France,
  facturée en France, soumise à la TVA française. « TTC » devient donc
  « đã gồm VAT của Pháp », et non un prix converti.
- **Le droit reste français.** Les pages légales ne sont pas traduites ; les
  renvois vers elles le disent.
"""

PAGES = {}
CITATIONS = {}
INCHANGE = {}

PAGES["404.html"] = {
    "Erreur 404": "Lỗi 404",
    "Cette page n&rsquo;existe pas": "Trang này không tồn tại",
    "ou a été déplacée.": "hoặc đã được chuyển đi.",
    "Le lien est peut-être ancien. Voici les pages les plus utiles pour reprendre votre parcours.":
        "Có thể đường dẫn đã cũ. Dưới đây là những trang hữu ích nhất để quý vị tiếp tục.",
    "Retour à l&rsquo;accueil": "Về trang chủ",
    "Accompagnements": "Dịch vụ",
}

PAGES["contact.html"] = {
    "Contact": "Liên hệ",
    "Deux façons": "Hai cách",
    "de nous joindre.": "để liên hệ với chúng tôi.",
    "Le plus simple reste de réserver un créneau&nbsp;: trente minutes suffisent à comprendre votre situation et à définir le périmètre utile.":
        "Cách đơn giản nhất là đặt một khung giờ: ba mươi phút là đủ để hiểu tình hình của quý vị và xác định phạm vi công việc hữu ích.",
    "Descendre au contenu": "Xuống phần nội dung",
    "01 &middot; Le plus direct": "01 &middot; Cách trực tiếp nhất",
    "Réserver un premier échange": "Đặt buổi trao đổi đầu tiên",
    "Deux formats sont ouverts à la réservation. Le premier sert à cadrer&nbsp;; le second est la séance de travail elle-même.":
        "Có hai hình thức để đặt lịch. Hình thức thứ nhất để định hướng; hình thức thứ hai là buổi làm việc thực sự.",
    "Appel de cadrage": "Cuộc gọi định hướng",
    "30 minutes": "30 phút",
    "Offert": "Miễn phí",
    "Comprendre votre situation, identifier le besoin principal et déterminer si le cabinet peut vous accompagner, et sous quelle forme. Sans engagement, et sans analyse approfondie.":
        "Hiểu tình hình của quý vị, xác định nhu cầu chính và xem công ty có thể đồng hành hay không, và dưới hình thức nào. Không ràng buộc, và chưa phải phân tích chuyên sâu.",
    "1 heure": "1 giờ",
    "432&nbsp;€ TTC": "432&nbsp;€ đã gồm VAT của Pháp",
    "Êtes-vous prêt à investir maintenant&nbsp;? Si non, pourquoi précisément, et quelles conditions réunir avant d&rsquo;agir. Questionnaire préparatoire, séance, puis Note de Diagnostic &amp; Décision.":
        "Quý vị đã sẵn sàng đầu tư chưa? Nếu chưa thì vì sao, và cần hội đủ những điều kiện nào trước khi hành động. Bảng câu hỏi chuẩn bị, buổi làm việc, rồi bản Ghi chú Chẩn đoán &amp; Quyết định.",
    "L&rsquo;échange se tient en&nbsp;:": "Buổi trao đổi có thể diễn ra bằng:",
    "français": "tiếng Pháp",
    "anglais": "tiếng Anh",
    "vietnamien": "tiếng Việt",
    "Réservation ferme après validation du paiement. Report ou annulation sans frais jusqu&rsquo;à 48&nbsp;heures avant la séance&nbsp;: voir les":
        "Lịch hẹn được xác nhận sau khi thanh toán. Dời lịch hoặc huỷ miễn phí cho đến 48&nbsp;giờ trước buổi làm việc: xem",
    "conditions générales de vente": "điều khoản bán hàng, bằng tiếng Pháp",
    "Choisir un créneau": "Chọn một khung giờ",
    "02 &middot; Par écrit": "02 &middot; Bằng văn bản",
    "Nous écrire": "Viết cho chúng tôi",
    "Décrivez votre situation en quelques lignes. Une réponse vous indiquera si un échange est utile et sous quel format.":
        "Hãy mô tả tình hình của quý vị trong vài dòng. Chúng tôi sẽ trả lời để cho biết một buổi trao đổi có hữu ích hay không, và dưới hình thức nào.",
    "Votre projet ou la décision qui vous bloque": "Dự án của quý vị, hoặc quyết định đang khiến quý vị bế tắc",
    "Le profil d&rsquo;investisseur dont vous vous sentez le plus proche": "Hồ sơ nhà đầu tư mà quý vị thấy gần mình nhất",
    "L&rsquo;échéance que vous avez en tête, même approximative": "Thời hạn quý vị hình dung, dù chỉ áng chừng",
    "Le formulaire s&rsquo;ouvre sur sa propre page. Votre message nous est envoyé directement, sans passer par votre logiciel de messagerie, et nous répondons sous un jour ouvré. Les informations saisies servent uniquement à traiter votre demande&nbsp;: voir les":
        "Biểu mẫu mở ra trên trang riêng của nó. Tin nhắn của quý vị đến thẳng chỗ chúng tôi, không đi qua phần mềm thư điện tử của quý vị, và chúng tôi trả lời trong vòng một ngày làm việc. Thông tin nhập vào chỉ dùng để xử lý yêu cầu của quý vị: xem",
    "données personnelles": "thông báo về dữ liệu cá nhân, bằng tiếng Pháp",
    "Ouvrir le formulaire": "Mở biểu mẫu",
    "Nous suivre": "Theo dõi chúng tôi",
    "Nos analyses et nos publications paraissent sur LinkedIn.":
        "Các phân tích và bài viết của chúng tôi được đăng trên LinkedIn.",
    "Suivre Amélie &amp; Partners": "Theo dõi Amélie &amp; Partners",
    "Bon à savoir": "Điều nên biết",
    "Zone d&rsquo;intervention et périmètre.": "Địa bàn và phạm vi làm việc.",
    "La recherche immobilière est spécialisée sur Paris.": "Dịch vụ tìm kiếm bất động sản chuyên về Paris.",
    "Les sujets de décision, d&rsquo;arbitrage et de stratégie de financement peuvent être étudiés au cas par cas pour des projets situés ailleurs en France.":
        "Các vấn đề về quyết định, cân nhắc và chiến lược tài chính có thể được xem xét theo từng trường hợp cho những dự án ở nơi khác trên đất Pháp.",
    "Amélie &amp; Partners ne vend ni bien immobilier, ni crédit, ni produit fiscal, et ne se substitue pas aux professionnels réglementés.":
        "Amélie &amp; Partners không bán bất động sản, không bán tín dụng, không bán sản phẩm thuế, và không thay thế các nghề nghiệp có quy chế riêng.",
    "Premier échange &middot; 30 minutes &middot; gratuit": "Buổi trao đổi đầu tiên &middot; 30 phút &middot; miễn phí",
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
}

PAGES["ressources.html"] = {
    "La bibliothèque": "Thư viện",
    "Des ressources gratuites": "Tài liệu miễn phí",
    "pour mieux décider.": "để quyết định tốt hơn.",
    "Transmettre des raisonnements utiles pour comprendre les options, évaluer les risques et prendre des décisions éclairées.":
        "Truyền lại những cách lập luận hữu ích để hiểu các lựa chọn, đánh giá rủi ro và quyết định một cách sáng suốt.",
    "Descendre au contenu": "Xuống phần nội dung",
    "La bibliothèque rassemble progressivement des analyses, des réflexes terrain et des outils simples autour d&rsquo;un même sujet&nbsp;: la maîtrise du capital immobilier.":
        "Thư viện dần tập hợp các bài phân tích, những phản xạ từ thực địa và vài công cụ đơn giản quanh cùng một chủ đề: làm chủ vốn bất động sản.",
    "01 &middot; Cadre pédagogique &middot; 8 min de lecture": "01 &middot; Bài giảng &middot; đọc trong 8 phút",
    "Les 3 effets dans l&rsquo;immobilier": "Ba hiệu ứng trong bất động sản",
    "On parle beaucoup de rendement. Pourtant, le vrai sujet est souvent ailleurs&nbsp;: comment la dette permet de contrôler un actif, comment cet actif construit du capital, puis comment ce capital peut être remis en mouvement.":
        "Người ta nói nhiều về tỷ suất sinh lời. Nhưng vấn đề thật sự thường nằm ở chỗ khác: nợ vay giúp kiểm soát một tài sản ra sao, tài sản ấy tạo ra vốn thế nào, rồi vốn ấy có thể được đưa trở lại vận động ra sao.",
    "01 &middot; Effet de levier": "01 &middot; Hiệu ứng đòn bẩy",
    "02 &middot; Effet ascenseur": "02 &middot; Hiệu ứng thang máy",
    "03 &middot; Effet boule de neige": "03 &middot; Hiệu ứng quả cầu tuyết",
    "Lire la ressource": "Đọc tài liệu",
    "Les prochains sujets": "Các chủ đề sắp tới",
    "Un même sujet,": "Cùng một chủ đề,",
    "vu sous plusieurs angles.": "nhìn từ nhiều góc.",
    "Financer, acheter et arbitrer sont trois portes d&rsquo;entrée pour apprendre à décider avec plus de méthode.":
        "Thu xếp tài chính, mua và cân nhắc là ba lối vào để học cách quyết định có phương pháp hơn.",
    "02 &middot; Financer": "02 &middot; Thu xếp tài chính",
    "Un refus bancaire ne dit pas toujours ce que vous croyez.":
        "Một lời từ chối của ngân hàng không phải lúc nào cũng có nghĩa như quý vị nghĩ.",
    "Lire ce qui bloque réellement avant de conclure que votre capacité est épuisée.":
        "Đọc cho ra điều thật sự đang cản trở, trước khi kết luận rằng khả năng vay đã cạn.",
    "En préparation": "Đang chuẩn bị",
    "Demander des renseignements": "Hỏi thêm thông tin",
    "03 &middot; Acheter": "03 &middot; Mua",
    "Le prix maximal se décide avant l&rsquo;offre.": "Mức giá tối đa được định trước khi trả giá.",
    "Préparer la négociation avec un calcul, des hypothèses et une limite claire.":
        "Chuẩn bị thương lượng bằng một phép tính, những giả định rõ ràng và một giới hạn dứt khoát.",
    "04 &middot; Arbitrer": "04 &middot; Cân nhắc",
    "Garder n&rsquo;est pas toujours la décision la plus prudente.":
        "Giữ lại không phải lúc nào cũng là quyết định thận trọng nhất.",
    "Comparer le rendement du capital immobilisé avec ses autres usages possibles.":
        "So sánh hiệu quả của phần vốn đang bị giam với những cách dùng khác của nó.",
    "Notre engagement éditorial": "Cam kết về nội dung",
    "Une ressource doit pouvoir vous être utile même si vous ne devenez jamais client.":
        "Một tài liệu phải hữu ích cho quý vị ngay cả khi quý vị không bao giờ trở thành khách hàng.",
    "Pas de recettes magiques. Pas de promesse de richesse rapide. Des idées claires, des hypothèses visibles et des limites expliquées.":
        "Không có công thức thần kỳ. Không hứa hẹn giàu nhanh. Chỉ có ý tưởng rõ ràng, giả định được nói ra và giới hạn được giải thích.",
    "Quel sujet aimeriez-vous approfondir&nbsp;?": "Quý vị muốn tìm hiểu sâu chủ đề nào?",
    "Les meilleures ressources partent souvent d&rsquo;une vraie question posée sur le terrain.":
        "Những tài liệu hay nhất thường bắt đầu từ một câu hỏi thật, đặt ra từ thực tế.",
    "Proposer une question": "Đề xuất một câu hỏi",
    "Appliquer le raisonnement": "Áp dụng cách lập luận",
    "Votre capital est-il encore placé au bon endroit&nbsp;?": "Vốn của quý vị còn đang đặt đúng chỗ không?",
    "Le Diagnostic Stratégique applique cette lecture à votre situation, avec vos chiffres et vos contraintes.":
        "Diagnostic Stratégique áp dụng cách đọc này vào tình hình của quý vị, với những con số và ràng buộc của quý vị.",
    "Découvrir le Diagnostic Stratégique": "Tìm hiểu Diagnostic Stratégique",
    "Vous préférez écrire&nbsp;?": "Quý vị muốn viết hơn?",
    "Passez par le formulaire": "Dùng biểu mẫu",
    "Amélie-Thu DUONG, dans un jardin": "Amélie-Thu DUONG, trong một khu vườn",
    "Fenêtre à rideaux, lumière d&rsquo;hiver": "Cửa sổ có rèm, ánh sáng mùa đông",
}

PAGES["approche.html"] = {
    "Notre approche": "Phương pháp của chúng tôi",
    "Une manière de décider": "Một cách quyết định",
    "avant une manière d&rsquo;acheter.": "trước khi là một cách mua.",
    "Le bon investissement n&rsquo;existe pas dans l&rsquo;absolu. Il devient cohérent, ou non, selon votre situation, votre financement, votre horizon et l&rsquo;usage futur du capital.":
        "Không có khoản đầu tư tốt một cách chung chung. Nó trở nên hợp lý, hay không, tuỳ theo tình hình, nguồn vốn vay, tầm nhìn thời gian và mục đích sử dụng vốn về sau của quý vị.",
    "Descendre au contenu": "Xuống phần nội dung",
    "La méthode en cinq étapes": "Phương pháp gồm năm bước",
    "Cinq étapes, dans cet ordre.": "Năm bước, theo đúng thứ tự này.",
    "Comprendre": "Hiểu",
    "Chiffrer": "Tính toán",
    "Financer": "Thu xếp tài chính",
    "Acheter": "Mua",
    "Arbitrer": "Cân nhắc",
    "01 &middot; La thèse": "01 &middot; Luận điểm",
    "La question n&rsquo;est pas seulement&nbsp;: «&nbsp;Est-ce un bon bien&nbsp;?&nbsp;»":
        "Câu hỏi không chỉ là: &laquo;&nbsp;Đây có phải một bất động sản tốt không?&nbsp;&raquo;",
    "La vraie question est&nbsp;: «&nbsp;Que permet cette décision dans votre trajectoire&nbsp;?&nbsp;»":
        "Câu hỏi thật sự là: &laquo;&nbsp;Quyết định này mở ra điều gì trong lộ trình của quý vị?&nbsp;&raquo;",
    "Votre partenaire stratégique reste du même côté de la table que vous&nbsp;: comprendre le projet, challenger les hypothèses et remettre les décisions dans le bon ordre. La réussite est votre destination&nbsp;; la qualité de décision est notre contribution.":
        "Đối tác chiến lược của quý vị luôn ngồi cùng phía bàn với quý vị: hiểu dự án, thử thách các giả định và sắp lại các quyết định theo đúng thứ tự. Thành công là đích đến của quý vị; chất lượng của quyết định là phần đóng góp của chúng tôi.",
    "02 &middot; Le processus": "02 &middot; Quy trình",
    "Du flou à la décision.": "Từ mơ hồ đến quyết định.",
    "Cinq étapes, simples à comprendre et exigeantes à appliquer, volontairement centrées sur les décisions qui changent la suite.":
        "Năm bước, dễ hiểu nhưng đòi hỏi khi thực hiện, được đặt trọng tâm vào những quyết định làm thay đổi phần còn lại.",
    "Clarifier l&rsquo;objectif réel, le point de départ, les contraintes et l&rsquo;horizon.":
        "Làm rõ mục tiêu thật sự, điểm xuất phát, các ràng buộc và tầm nhìn thời gian.",
    "Produit&nbsp;: une question bien posée.": "Kết quả: một câu hỏi được đặt đúng.",
    "Tester les hypothèses, les équilibres, les risques et les scénarios possibles.":
        "Thử các giả định, các thế cân bằng, các rủi ro và những kịch bản có thể xảy ra.",
    "Produit&nbsp;: des options comparables.": "Kết quả: những lựa chọn có thể so sánh được.",
    "Clarifier les ressources, les contraintes et les scénarios à approfondir avant la prochaine opération.":
        "Làm rõ nguồn lực, ràng buộc và những kịch bản cần tìm hiểu sâu trước giao dịch kế tiếp.",
    "Produit&nbsp;: une préparation stratégique.": "Kết quả: một sự chuẩn bị chiến lược.",
    "Définir les critères, le prix maximal et les conditions qui rendent l&rsquo;achat acceptable.":
        "Xác định tiêu chí, mức giá tối đa và những điều kiện khiến thương vụ trở nên chấp nhận được.",
    "Produit&nbsp;: une décision préparée.": "Kết quả: một quyết định đã được chuẩn bị.",
    "Mesurer le capital immobilisé, la valeur créée et les usages possibles de ce capital.":
        "Đo phần vốn đang bị giam, giá trị đã tạo ra và những cách dùng khả dĩ của phần vốn ấy.",
    "Produit&nbsp;: la prochaine direction.": "Kết quả: hướng đi kế tiếp.",
    "03 &middot; Le capital": "03 &middot; Vốn",
    "Le rendement est un indicateur. Le capital raconte la trajectoire.":
        "Tỷ suất sinh lời là một chỉ số. Vốn mới kể lại cả lộ trình.",
    "Un actif peut sembler peu rentable et pourtant construire beaucoup de capital. Un autre peut afficher un rendement séduisant tout en immobilisant trop de trésorerie ou en limitant la capacité d&rsquo;emprunt suivante.":
        "Một tài sản có thể trông kém sinh lời mà vẫn tạo ra rất nhiều vốn. Một tài sản khác có thể phô ra tỷ suất hấp dẫn nhưng lại giam quá nhiều tiền mặt, hoặc thu hẹp khả năng vay tiếp theo.",
    "Nous lisons ensemble le bien, la dette, les revenus, la valeur créée, le risque et le temps. C&rsquo;est cette lecture globale qui permet de savoir s&rsquo;il faut conserver, céder, refinancer ou réinvestir.":
        "Chúng ta cùng đọc bất động sản, khoản nợ, dòng thu, giá trị đã tạo ra, rủi ro và thời gian. Chính cách đọc tổng thể ấy cho biết nên giữ, nên bán, nên tái tài trợ hay nên tái đầu tư.",
    "Lire «&nbsp;Les 3 effets dans l&rsquo;immobilier&nbsp;»": "Đọc &laquo;&nbsp;Ba hiệu ứng trong bất động sản&nbsp;&raquo;",
    "04 &middot; Nos principes": "04 &middot; Những nguyên tắc",
    "Ce qui ne change pas d&rsquo;un dossier à l&rsquo;autre.": "Điều không thay đổi từ hồ sơ này sang hồ sơ khác.",
    "Indépendance": "Độc lập",
    "La recommandation ne dépend ni d&rsquo;un bien à vendre, ni d&rsquo;un crédit à placer, ni d&rsquo;un produit fiscal à proposer.":
        "Lời khuyến nghị không phụ thuộc vào một bất động sản cần bán, một khoản vay cần đẩy đi, hay một sản phẩm thuế cần chào.",
    "Chiffrage": "Tính toán",
    "Une intuition peut ouvrir une piste. Elle ne remplace jamais les hypothèses, les calculs et la marge de sécurité.":
        "Trực giác có thể mở ra một hướng. Nó không bao giờ thay được giả định, phép tính và biên độ an toàn.",
    "Terrain": "Thực địa",
    "La méthode vient de décisions pratiquées&nbsp;: recherche, négociation, financement, travaux, exploitation et arbitrage.":
        "Phương pháp đến từ những quyết định đã thực sự làm: tìm kiếm, thương lượng, vay vốn, sửa chữa, vận hành và cân nhắc bán giữ.",
    "Transmission": "Truyền lại",
    "Une bonne recommandation ne vous rend pas dépendant. Elle vous aide à comprendre et à mieux décider ensuite.":
        "Một khuyến nghị tốt không khiến quý vị lệ thuộc. Nó giúp quý vị hiểu, và quyết định tốt hơn ở lần sau.",
    "Nous ne promettons pas": "Chúng tôi không hứa",
    "devenir riche rapidement, vivre de l&rsquo;immobilier ou acheter à tout prix.":
        "làm giàu nhanh, sống bằng bất động sản, hay mua bằng mọi giá.",
    "Nous cherchons": "Chúng tôi tìm",
    "un chemin plus court, plus lisible et mieux maîtrisé vers davantage de choix.":
        "một con đường ngắn hơn, sáng rõ hơn và được kiểm soát tốt hơn để đi tới nhiều lựa chọn hơn.",
    "Passer de l&rsquo;analyse à l&rsquo;action": "Từ phân tích sang hành động",
    "La bonne méthode commence par la bonne question.": "Phương pháp đúng bắt đầu bằng câu hỏi đúng.",
    "Apportez votre situation. Nous vous aiderons à identifier le vrai sujet.":
        "Hãy mang tình hình của quý vị đến. Chúng tôi sẽ giúp quý vị nhận ra vấn đề thật sự.",
    "Analyser ma situation": "Phân tích tình hình của tôi",
    "Vous préférez écrire&nbsp;?": "Quý vị muốn viết hơn?",
    "Passez par le formulaire": "Dùng biểu mẫu",
    "Les étapes de la méthode": "Các bước của phương pháp",
    "Coupole de verre vue depuis le sol, sous une rotonde parisienne":
        "Mái vòm kính nhìn từ dưới lên, bên trong một sảnh tròn ở Paris",
    "Les cinq étapes de la méthode": "Năm bước của phương pháp",
    "Passage couvert parisien, verrière et boutiques": "Thương xá có mái kính ở Paris, cùng những cửa hiệu",
}

PAGES["accompagnements.html"] = {
    "Accompagnements": "Dịch vụ",
    "Un partenaire stratégique.": "Một đối tác chiến lược.",
    "Quatre façons d&rsquo;intervenir.": "Bốn cách làm việc cùng nhau.",
    "Diagnostiquer, financer, acheter, piloter&nbsp;: chaque moment de votre parcours appelle un regard et un format d&rsquo;intervention adaptés.":
        "Chẩn đoán, thu xếp tài chính, mua, dẫn dắt: mỗi chặng trong hành trình của quý vị đòi hỏi một cách nhìn và một hình thức làm việc riêng.",
    "Descendre au contenu": "Xuống phần nội dung",
    "Une séance ponctuelle peut suffire. Certaines situations demandent ensuite une mission de financement, de recherche ou de pilotage plus complète.":
        "Một buổi làm việc đơn lẻ có thể là đủ. Một số hoàn cảnh sau đó cần đến một hợp đồng đầy đủ hơn về tài chính, tìm kiếm hoặc dẫn dắt.",
    "01 &middot; Diagnostiquer &middot; la porte d&rsquo;entrée": "01 &middot; Chẩn đoán &middot; lối vào",
    "Une décision importante à prendre&nbsp;? Un regard stratégique pour clarifier la situation, challenger vos options et déterminer la prochaine étape.":
        "Một quyết định quan trọng cần đưa ra? Một cách đọc ở tầm chiến lược để làm rõ tình hình, thử thách các lựa chọn và xác định bước tiếp theo.",
    "Nous mettons à plat le contexte, les contraintes, les scénarios et les conséquences de chaque option. L&rsquo;objectif est de savoir quoi faire maintenant, ou pourquoi il vaut mieux attendre.":
        "Chúng tôi bày rõ bối cảnh, các ràng buộc, các kịch bản và hệ quả của từng lựa chọn. Mục đích là biết cần làm gì ngay lúc này &mdash; hoặc vì sao chờ đợi lại tốt hơn.",
    "Questionnaire préparatoire adapté à votre question": "Bảng câu hỏi chuẩn bị, làm riêng cho câu hỏi của quý vị",
    "Session stratégique d&rsquo;une heure": "Buổi làm việc chiến lược kéo dài một giờ",
    "Note de Diagnostic &amp; Décision&nbsp;: verdict, priorités, prochaines actions":
        "Bản Ghi chú Chẩn đoán &amp; Quyết định: kết luận, thứ tự ưu tiên, các việc kế tiếp",
    "Tarification": "Giá",
    "€ TTC": "€ đã gồm VAT của Pháp",
    "Questionnaire &middot; Session d&rsquo;une heure &middot; Note de Diagnostic &amp; Décision":
        "Bảng câu hỏi &middot; Buổi làm việc một giờ &middot; Ghi chú Chẩn đoán &amp; Quyết định",
    "Premier échange de cadrage de 30 minutes gratuit.": "Buổi trao đổi định hướng 30 phút, miễn phí, để bắt đầu.",
    "Découvrir le diagnostic": "Tìm hiểu buổi chẩn đoán",
    "02 &middot; Financer": "02 &middot; Thu xếp tài chính",
    "Stratégie de Financement": "Stratégie de Financement",
    "Comprendre ce que votre situation permet réellement, ce qui bloque et ce qu&rsquo;il faut préparer avant d&rsquo;engager la prochaine étape.":
        "Hiểu tình hình của quý vị thật sự cho phép những gì, điều gì đang cản trở và cần chuẩn bị gì trước khi bước tiếp.",
    "Capacité réelle, endettement, apport, durée, revenus locatifs, structure et ordre des opérations&nbsp;: nous analysons ce qui bloque, ce qui peut être amélioré et ce qui doit rester sécurisé.":
        "Khả năng vay thực tế, tỷ lệ nợ, vốn tự có, thời hạn, thu nhập cho thuê, cấu trúc và thứ tự các giao dịch: chúng tôi phân tích điều gì đang cản trở, điều gì có thể cải thiện và điều gì phải giữ an toàn.",
    "Analyse de la situation et des refus ou avis contradictoires":
        "Phân tích tình hình, cùng những lời từ chối hoặc ý kiến trái ngược đã nhận",
    "Lecture des ressources, contraintes et incohérences": "Đọc lại nguồn lực, ràng buộc và những điểm thiếu nhất quán",
    "Identification des informations manquantes": "Nhận diện những thông tin còn thiếu",
    "Scénarios à approfondir avant la prochaine opération": "Các kịch bản cần tìm hiểu sâu trước giao dịch kế tiếp",
    "Amélie &amp; Partners intervient en analyse et préparation stratégique, en amont de la décision. Le cabinet ne place ni ne négocie le crédit et n&rsquo;en garantit pas l&rsquo;obtention. Il ne se substitue pas aux professionnels réglementés.":
        "Amélie &amp; Partners làm việc ở khâu phân tích và chuẩn bị chiến lược, trước khi quyết định. Công ty không thu xếp cũng không thương lượng khoản vay, và không bảo đảm khoản vay sẽ được cấp. Công ty không thay thế các nghề nghiệp có quy chế riêng.",
    "Échanger sur mon financement": "Trao đổi về phương án tài chính của tôi",
    "03 &middot; Acheter à Paris": "03 &middot; Mua tại Paris",
    "Recherche immobilière à Paris": "Recherche immobilière à Paris",
    "Votre partenaire de recherche, d&rsquo;analyse et de décision jusqu&rsquo;à l&rsquo;acquisition.":
        "Người đồng hành trong việc tìm kiếm, phân tích và quyết định, cho đến khi mua xong.",
    "Pour un investissement locatif, une résidence principale ou un pied-à-terre, la mission associe connaissance du marché parisien, recherche ciblée, analyse et aide à la décision.":
        "Dù là đầu tư cho thuê, nhà ở chính hay một chốn đi về, công việc kết hợp hiểu biết về thị trường Paris, việc tìm kiếm có định hướng, phân tích và hỗ trợ ra quyết định.",
    "Définition du cahier des charges et du prix maximal": "Xác định yêu cầu và mức giá tối đa",
    "Recherche, présélection et lecture des opportunités": "Tìm kiếm, sàng lọc và đọc kỹ các cơ hội",
    "Analyse du prix, des travaux, de la copropriété, du potentiel et des risques":
        "Phân tích giá, phần sửa chữa, ban quản trị toà nhà, tiềm năng và rủi ro",
    "Négociation et coordination avec le réseau de professionnels":
        "Thương lượng và phối hợp với mạng lưới các chuyên gia",
    "Parler de ma recherche": "Trao đổi về việc tìm kiếm của tôi",
    "04 &middot; Piloter": "04 &middot; Dẫn dắt",
    "Trajectoire Investisseur": "Trajectoire Investisseur",
    "Construire une trajectoire claire, arbitrer les options et prendre les décisions dans le bon ordre pour faire progresser votre patrimoine.":
        "Dựng một lộ trình rõ ràng, cân nhắc các lựa chọn và ra quyết định theo đúng thứ tự để tài sản của quý vị tiến lên.",
    "Acquisition, financement, trésorerie, revente, refinancement ou réinvestissement&nbsp;: nous construisons une direction et un ordre d&rsquo;exécution adaptés à votre situation, du premier investissement à la prochaine phase d&rsquo;un patrimoine déjà constitué.":
        "Mua vào, vay vốn, dòng tiền, bán lại, tái tài trợ hay tái đầu tư: chúng tôi dựng một hướng đi và một thứ tự thực hiện phù hợp với tình hình của quý vị &mdash; từ khoản đầu tư đầu tiên đến giai đoạn kế tiếp của một danh mục đã hình thành.",
    "Lecture globale des actifs, dettes et liquidités": "Đọc tổng thể tài sản, nợ và tiền mặt",
    "Priorisation des acquisitions et des arbitrages": "Sắp thứ tự ưu tiên cho việc mua và việc bán giữ",
    "Scénarios de mobilisation et de réemploi du capital": "Các kịch bản giải phóng và dùng lại vốn",
    "Pilotage stratégique dans un périmètre défini à l&rsquo;avance": "Dẫn dắt chiến lược trong phạm vi đã thống nhất trước",
    "Périmètre": "Phạm vi",
    "Direction &middot; Arbitrage &middot; Priorisation": "Hướng đi &middot; Cân nhắc &middot; Ưu tiên",
    "Présenter ma situation": "Trình bày tình hình của tôi",
    "05 &middot; Comment choisir&nbsp;?": "05 &middot; Chọn thế nào?",
    "Vous n&rsquo;avez pas à choisir seul la prestation.": "Quý vị không phải tự mình chọn dịch vụ nào.",
    "Le premier échange sert précisément à comprendre votre besoin et à vérifier si nous pouvons vous aider. Si une séance suffit, nous vous le dirons. Si la situation demande une mission plus complète, son périmètre est défini avant tout engagement.":
        "Buổi trao đổi đầu tiên có mặt chính là để hiểu nhu cầu của quý vị và xem chúng tôi có giúp được không. Nếu một buổi làm việc là đủ, chúng tôi sẽ nói vậy. Nếu hoàn cảnh cần một hợp đồng đầy đủ hơn, phạm vi của nó được xác định trước mọi cam kết.",
    "Réserver un premier échange": "Đặt buổi trao đổi đầu tiên",
    "30 minutes gratuites &middot; Sans conseil approfondi &middot; Sans engagement":
        "30 phút miễn phí &middot; Chưa phải tư vấn chuyên sâu &middot; Không ràng buộc",
    "Un besoin précis": "Một nhu cầu rõ ràng",
    "Vous n&rsquo;avez peut-être pas besoin de tout. Vous avez besoin du bon point de départ.":
        "Có lẽ quý vị không cần tất cả. Quý vị cần một điểm xuất phát đúng.",
    "Présentez-nous la situation. Nous déterminerons ensemble le périmètre utile.":
        "Hãy kể cho chúng tôi về tình hình. Chúng ta sẽ cùng xác định phạm vi công việc hữu ích.",
    "Analyser ma situation": "Phân tích tình hình của tôi",
    "Vous préférez écrire&nbsp;?": "Quý vị muốn viết hơn?",
    "Passez par le formulaire": "Dùng biểu mẫu",
    "Enfilade intérieure vers une arche ouverte sur la rue": "Dãy phòng nối nhau dẫn tới một vòm cửa mở ra phố",
    "Quais de Seine bordés d&rsquo;arbres, à Paris": "Bờ sông Seine rợp cây, tại Paris",
    "Le Louvre et la rue de Rivoli au soleil couchant": "Bảo tàng Louvre và phố Rivoli lúc mặt trời lặn",
    "La Seine au couchant, le Pont des Arts et la tour Eiffel":
        "Sông Seine lúc chạng vạng, cầu Pont des Arts và tháp Eiffel",
}

# Les cinq verdicts sont les noms que porte la Note de Diagnostic & Decision :
# ce sont des termes du livrable, pas des mots de la page. La phrase qui les
# introduit en donne la traduction ; les cartes gardent le nom d'origine.
INCHANGE["diagnostic.html"] = {
    "Avancer", "Préparer", "Restructurer", "Approfondir", "Suspendre",
}

PAGES["diagnostic.html"] = {
    "Sortir du flou": "Ra khỏi vùng mơ hồ",
    "avant d&rsquo;engager le capital.": "trước khi bỏ vốn.",
    "Une décision importante à prendre&nbsp;? Un regard stratégique pour clarifier la situation, challenger vos options et déterminer la prochaine étape.":
        "Một quyết định quan trọng cần đưa ra? Một cách đọc ở tầm chiến lược để làm rõ tình hình, thử thách các lựa chọn và xác định bước tiếp theo.",
    "30 minutes gratuites pour cadrer": "30 phút miễn phí để định hướng",
    "Sans engagement": "Không ràng buộc",
    "Réserver un premier échange": "Đặt buổi trao đổi đầu tiên",
    "Descendre au contenu": "Xuống phần nội dung",
    "Un besoin précis": "Một nhu cầu rõ ràng",
    "Une décision argumentée.": "Một quyết định có lập luận.",
    "Un regard stratégique pour clarifier la situation, challenger vos options et déterminer la prochaine étape.":
        "Một cách đọc ở tầm chiến lược để làm rõ tình hình, thử thách các lựa chọn và xác định bước tiếp theo.",
    "30&nbsp;minutes gratuites pour cadrer": "30&nbsp;phút miễn phí để định hướng",
    "Un regard indépendant": "Một góc nhìn độc lập",
    "Fondatrice &amp; Investisseuse à Paris depuis 2014": "Nhà sáng lập &amp; nhà đầu tư tại Paris từ năm 2014",
    "TTC": "đã gồm VAT của Pháp",
    "Prestation ponctuelle, sans abonnement ni engagement.":
        "Dịch vụ đơn lẻ, không thuê bao, không ràng buộc. Được định giá và xuất hoá đơn tại Pháp, theo thuế VAT và luật pháp Pháp.",
    "Ce qui est compris": "Bao gồm những gì",
    "Un questionnaire préparatoire": "Một bảng câu hỏi chuẩn bị",
    "Une session stratégique d&rsquo;une heure": "Một buổi làm việc chiến lược kéo dài một giờ",
    "Votre Note de Diagnostic &amp; Décision": "Bản Ghi chú Chẩn đoán &amp; Quyết định của quý vị",
    "Un premier échange de cadrage de 30 minutes, gratuit": "Một buổi trao đổi định hướng 30 phút, miễn phí",
    "Cinq verdicts possibles&nbsp;: AVANCER, PRÉPARER, RESTRUCTURER, APPROFONDIR, SUSPENDRE.":
        "Năm kết luận có thể có: AVANCER, PRÉPARER, RESTRUCTURER, APPROFONDIR, SUSPENDRE &mdash; tiến hành, chuẩn bị, tái cấu trúc, tìm hiểu sâu hơn, tạm dừng.",
    "01 &middot; Pour qui&nbsp;?": "01 &middot; Dành cho ai?",
    "Vous n&rsquo;avez pas besoin d&rsquo;un avis de plus. Vous avez besoin d&rsquo;une lecture structurée.":
        "Quý vị không cần thêm một ý kiến nữa. Quý vị cần một cách đọc có cấu trúc.",
    "Vous hésitez entre plusieurs projets ou plusieurs montages.":
        "Quý vị đang phân vân giữa nhiều dự án hoặc nhiều cách sắp xếp.",
    "Votre banque refuse, ou les avis reçus se contredisent.":
        "Ngân hàng từ chối, hoặc những ý kiến quý vị nhận được mâu thuẫn nhau.",
    "Vous voulez savoir s&rsquo;il faut acheter maintenant ou consolider d&rsquo;abord.":
        "Quý vị muốn biết nên mua ngay hay nên củng cố trước đã.",
    "Vous possédez déjà des biens et ne savez plus quoi conserver, vendre ou financer ensuite.":
        "Quý vị đã có bất động sản và không còn biết nên giữ gì, bán gì, hay vay tiếp cho gì.",
    "Vous voulez un regard indépendant avant d&rsquo;engager du capital ou de la dette.":
        "Quý vị muốn một góc nhìn độc lập trước khi bỏ vốn hay vay nợ.",
    "02 &middot; Le déroulé": "02 &middot; Diễn tiến",
    "Comprendre. Analyser. Trancher.": "Hiểu. Phân tích. Quyết.",
    "Un cadre court et précis, conçu pour produire une direction, pas une accumulation d&rsquo;informations.":
        "Một khuôn khổ ngắn và chính xác, được thiết kế để cho ra một hướng đi, chứ không phải một đống thông tin.",
    "Avant": "Trước",
    "30 minutes, gratuit": "30 phút, miễn phí",
    "Échange de cadrage": "Buổi trao đổi định hướng",
    "Vous présentez la situation. Nous vérifions le besoin, les enjeux et le périmètre utile.":
        "Quý vị trình bày tình hình. Chúng tôi xem lại nhu cầu, điều đang đặt ra và phạm vi công việc hữu ích.",
    "Ce rendez-vous n&rsquo;est pas une séance de conseil approfondi.": "Buổi hẹn này chưa phải một buổi tư vấn chuyên sâu.",
    "Questionnaire préparatoire": "Bảng câu hỏi chuẩn bị",
    "Vous préparez la matière": "Quý vị chuẩn bị dữ liệu",
    "Vous renseignez votre situation et transmettez les éléments utiles pour identifier le véritable nœud de décision.":
        "Quý vị mô tả tình hình và gửi những dữ liệu cần thiết để nhận ra nút thắt thật sự của quyết định.",
    "Le cadre d&rsquo;analyse est adapté à votre question.": "Khung phân tích được làm riêng cho câu hỏi của quý vị.",
    "Le jour J": "Ngày làm việc",
    "Session d&rsquo;une heure": "Buổi làm việc một giờ",
    "Analyse et décision": "Phân tích và quyết định",
    "Nous comparons les options, leurs conditions, leurs risques et leurs effets sur la suite.":
        "Chúng ta so sánh các lựa chọn, điều kiện, rủi ro và ảnh hưởng của chúng lên phần còn lại.",
    "Vous repartez avec une direction argumentée.": "Quý vị ra về với một hướng đi có lập luận.",
    "Après": "Sau",
    "Sous quelques jours": "Trong vài ngày",
    "Note de Diagnostic &amp; Décision": "Ghi chú Chẩn đoán &amp; Quyết định",
    "Vous recevez une note qui formalise la lecture de votre situation, le verdict, les priorités et les prochaines actions.":
        "Quý vị nhận một bản ghi chú đúc kết cách đọc tình hình của quý vị, kết luận, thứ tự ưu tiên và những việc kế tiếp.",
    "Vous savez quoi faire, et dans quel ordre.": "Quý vị biết cần làm gì, và theo thứ tự nào.",
    "03 &middot; Le verdict": "03 &middot; Kết luận",
    "Cinq directions possibles.": "Năm hướng đi có thể.",
    "Une prochaine étape claire.": "Một bước tiếp theo rõ ràng.",
    "«&nbsp;Pas maintenant&nbsp;» n&rsquo;est pas un refus. C&rsquo;est une décision qui protège votre marge de manœuvre et indique ce qui doit être consolidé avant la prochaine étape.":
        "&laquo;&nbsp;Chưa phải lúc này&nbsp;&raquo; không phải là một lời từ chối. Đó là một quyết định giữ lại dư địa xoay xở cho quý vị, và chỉ ra điều gì cần củng cố trước bước tiếp theo.",
    "Engager la prochaine étape avec des hypothèses et des risques identifiés.":
        "Bước tiếp, với những giả định và rủi ro đã được nhận diện.",
    "Compléter les ressources et les informations nécessaires avant d&rsquo;agir.":
        "Bổ sung nguồn lực và thông tin cần thiết trước khi hành động.",
    "Revoir l&rsquo;organisation du projet ou du patrimoine pour retrouver de la cohérence.":
        "Sắp xếp lại dự án hoặc danh mục tài sản để tìm lại sự nhất quán.",
    "Éclaircir une question déterminante avant de trancher.": "Làm sáng tỏ một câu hỏi có tính quyết định trước khi chọn.",
    "Préserver votre marge de manœuvre en différant ou en arrêtant le projet.":
        "Giữ dư địa xoay xở bằng cách hoãn lại hoặc dừng dự án.",
    "04 &middot; Pourquoi indépendant&nbsp;?": "04 &middot; Vì sao độc lập?",
    "Le seul produit du diagnostic, c&rsquo;est la clarté.": "Thứ duy nhất buổi chẩn đoán bán ra là sự sáng rõ.",
    "Amélie &amp; Partners ne vend ni bien immobilier, ni crédit, ni produit fiscal dans le cadre du diagnostic. Nous n&rsquo;avons aucune raison de provoquer un achat si ce n&rsquo;est pas le bon moment.":
        "Trong khuôn khổ buổi chẩn đoán, Amélie &amp; Partners không bán bất động sản, không bán tín dụng, không bán sản phẩm thuế. Chúng tôi không có lý do gì để thúc quý vị mua nếu chưa đúng thời điểm.",
    "Une autre mission peut être proposée lorsque son utilité est claire. Elle reste distincte et son périmètre est présenté séparément.":
        "Một hợp đồng khác có thể được đề xuất khi sự hữu ích của nó đã rõ. Nó tách bạch, và phạm vi của nó được trình bày riêng.",
    "Première étape &middot; 30 minutes &middot; gratuit": "Bước đầu tiên &middot; 30 phút &middot; miễn phí",
    "Parlons de la décision": "Hãy nói về quyết định",
    "qui vous bloque.": "đang khiến quý vị bế tắc.",
    "En 30 minutes, nous vérifions ensemble si un Diagnostic Stratégique est le bon format pour votre situation.":
        "Trong 30 phút, chúng ta cùng xem Diagnostic Stratégique có phải là hình thức phù hợp với tình hình của quý vị hay không.",
    "Avec plaisir": "Rất hân hạnh",
    "Choisissons un créneau.": "Hãy chọn một khung giờ.",
    "30 minutes &middot; gratuit &middot; sans conseil approfondi &middot; sans engagement":
        "30 phút &middot; miễn phí &middot; chưa phải tư vấn chuyên sâu &middot; không ràng buộc",
    "Vous préférez écrire&nbsp;?": "Quý vị muốn viết hơn?",
    "Passez par le formulaire": "Dùng biểu mẫu",
    "Amélie-Thu DUONG, en extérieur, appuyée à une bordure de lavandes":
        "Amélie-Thu DUONG, ngoài trời, tựa bên một luống oải hương",
    "Coupole vitrée vue de l&rsquo;intérieur, la structure entière visible d&rsquo;un seul regard":
        "Mái vòm kính nhìn từ bên trong, toàn bộ kết cấu thu vào một tầm mắt",
}

# Les huit temoignages sont la parole d'investisseurs reels : ils restent
# dans leur langue, signales par un `lang="fr"`. Les noms, les titres
# d'oeuvre et les lieux ne se traduisent pas davantage.
CITATIONS["temoignages.html"] = {
    "&laquo;&nbsp;Pour l&rsquo;achat de ma résidence principale, Amélie m&rsquo;a apporté un vrai recul. Son analyse et ses questions m&rsquo;ont permis de décider avec beaucoup plus de clarté.&nbsp;&raquo;",
    "&laquo;&nbsp;Je partais de zéro. En deux ans, j&rsquo;ai construit avec Amélie une stratégie qui m&rsquo;a permis d&rsquo;atteindre plus de 1,2 M€ de patrimoine immobilier brut. J&rsquo;ai surtout apprécié sa vision globale et sa capacité à proposer plusieurs chemins.&nbsp;&raquo;",
    "&laquo;&nbsp;Je ne connaissais ni l&rsquo;investissement immobilier ni le marché parisien. En un an, j&rsquo;ai acheté mes deux premiers studios à Paris. Amélie m&rsquo;a surtout appris à comprendre le levier bancaire et à dépasser plusieurs idées reçues.&nbsp;&raquo;",
    "&laquo;&nbsp;J&rsquo;ai commencé l&rsquo;immobilier tard, à l&rsquo;approche de la retraite. Avec Amélie, j&rsquo;ai mis en place une stratégie adaptée qui m&rsquo;a permis d&rsquo;acquérir un local commercial dans le 6&#7497; puis un studio dans le Marais.&nbsp;&raquo;",
    "&laquo;&nbsp;Je partais de zéro. En trois ans, j&rsquo;ai acheté deux studios dans Paris centre et ma résidence principale à Fontainebleau. Amélie m&rsquo;a aidée à avancer étape par étape, sans perdre la vision d&rsquo;ensemble.&nbsp;&raquo;",
    "&laquo;&nbsp;J&rsquo;hésitais entre agrandir ma résidence principale et investir à Paris. Une séance avec Amélie m&rsquo;a suffi pour remettre les options à plat, clarifier mes priorités et savoir dans quelle direction avancer.&nbsp;&raquo;",
    "&laquo;&nbsp;Mon projet de résidence principale était bloqué par la question du financement. Amélie m&rsquo;a aidé à revoir le montage stratégique et à retrouver une direction claire. J&rsquo;ai ensuite réalisé mon premier investissement à Paris.&nbsp;&raquo;",
    "&laquo;&nbsp;Mon objectif était de commencer à construire un patrimoine pour pouvoir transmettre quelque chose à mon fils. Amélie m&rsquo;a aidé à structurer ma réflexion et à avancer malgré une situation qui n&rsquo;était pas simple. Six mois plus tard, j&rsquo;ai acheté mon premier studio dans le 1er arrondissement de Paris, un bien que je n&rsquo;aurais pas imaginé pouvoir acquérir au départ.&nbsp;&raquo;",
}

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
    "Témoignages": "Khách hàng nói gì",
    "Les investisseurs": "Các nhà đầu tư",
    "partagent leur expérience.": "kể lại trải nghiệm của họ.",
    "Huit personnes accompagnées racontent leur projet, la décision qu&rsquo;elles avaient à prendre et ce que l&rsquo;accompagnement a changé.":
        "Tám người từng được đồng hành kể lại dự án của mình, quyết định họ phải đưa ra và điều mà sự đồng hành đã thay đổi.",
    "Descendre au contenu": "Xuống phần nội dung",
    "Ce qu&rsquo;ils en disent.": "Bằng lời của chính họ.",
    "Résidence principale &middot; Fontainebleau": "Nhà ở chính &middot; Fontainebleau",
    "43 ans &middot; Chef de projet informatique &middot; Essilor": "43 tuổi &middot; Quản lý dự án tin học &middot; Essilor",
    "Investissement à Paris &amp; Accompagnement Premium &middot; Saint-Maur-des-Fossés":
        "Đầu tư tại Paris &amp; đồng hành cao cấp &middot; Saint-Maur-des-Fossés",
    "35 ans &middot; Consultante MOA &middot; EDF": "35 tuổi &middot; Chuyên viên tư vấn nghiệp vụ &middot; EDF",
    "Investissement locatif à Paris &middot; Paris": "Đầu tư cho thuê tại Paris &middot; Paris",
    "31 ans &middot; Contrôleur de gestion &middot; Veolia": "31 tuổi &middot; Kiểm soát viên tài chính &middot; Veolia",
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
    ", 2020. Sérigraphie vue en vitrine, à Paris.": ", 2020. Tranh in lụa nhìn thấy trong tủ kính một cửa hiệu ở Paris.",
    "Pour finir": "Để khép lại",
    "Ce qu&rsquo;on retient d&rsquo;un projet mené&nbsp;:": "Điều còn đọng lại sau một dự án đã đi đến cùng:",
    "la clarté au moment de décider.": "sự sáng rõ vào lúc phải quyết định.",
    "Les témoignages ci-dessus ont été confiés par des investisseurs accompagnés. Chaque situation est différente&nbsp;; les résultats varient.":
        "Những lời kể trên đây do các nhà đầu tư từng được đồng hành chia sẻ. Mỗi hoàn cảnh một khác; kết quả thay đổi.",
    "Premier échange": "Buổi trao đổi đầu tiên",
    "Votre situation mérite": "Tình hình của quý vị xứng đáng",
    "le même soin.": "được chăm chút như vậy.",
    "Trente minutes, gratuites et sans engagement, pour comprendre votre point de départ et le périmètre utile.":
        "Ba mươi phút, miễn phí và không ràng buộc, để hiểu điểm xuất phát của quý vị và phạm vi công việc hữu ích.",
    "Réserver un premier échange": "Đặt buổi trao đổi đầu tiên",
    "Vous préférez écrire&nbsp;?": "Quý vị muốn viết hơn?",
    "Passez par le formulaire": "Dùng biểu mẫu",
    "Témoignages d&rsquo;investisseurs accompagnés": "Lời kể của những nhà đầu tư được đồng hành",
    "Une sérigraphie « I love you » exposée en vitrine, la rue et les arbres se reflétant sur le verre":
        "Bức tranh in lụa &laquo;&nbsp;I love you&nbsp;&raquo; bày trong tủ kính, phố và hàng cây soi bóng trên mặt kính",
}

# La phrase d'Amelie est la sienne : elle reste dans sa langue.
CITATIONS["a-propos.html"] = {
    "&laquo;&nbsp;Ma vraie compétence n&rsquo;est pas de tout savoir sur l&rsquo;immobilier. C&rsquo;est de savoir chercher, vérifier, chiffrer et décider.&nbsp;&raquo;",
}

INCHANGE["a-propos.html"] = {
    "&gt; 25 M€",   # un montant
}

PAGES["a-propos.html"] = {
    "Mettre la vidéo en pause": "Tạm dừng video",
    "Une approche": "Một phương pháp",
    "née du terrain.": "sinh ra từ thực địa.",
    "Fondé par Amélie-Thu DUONG, le cabinet s&rsquo;appuie sur une expérience de l&rsquo;investissement immobilier à Paris depuis 2014.":
        "Do Amélie-Thu DUONG sáng lập, công ty dựa trên kinh nghiệm đầu tư bất động sản tại Paris từ năm 2014.",
    "Descendre au contenu": "Xuống phần nội dung",
    "Acquisition, financement, exploitation et arbitrage&nbsp;: cette pratique nourrit une approche structurée, des ressources et des accompagnements au service des investisseurs.":
        "Mua vào, vay vốn, vận hành và cân nhắc bán giữ: chính việc làm ấy nuôi dưỡng một phương pháp có cấu trúc, những tài liệu và những dịch vụ dành cho nhà đầu tư.",
    "01 &middot; Le parcours de la fondatrice": "01 &middot; Hành trình của nhà sáng lập",
    "Construire sans mode d&rsquo;emploi.": "Dựng nên mà không có sách hướng dẫn.",
    "Née au Vietnam, Amélie arrive en France à 20 ans sans parler français, avec l&rsquo;envie d&rsquo;y construire sa vie.":
        "Sinh ra tại Việt Nam, Amélie sang Pháp năm 20 tuổi, chưa nói được tiếng Pháp, với mong muốn dựng lấy cuộc đời mình ở đó.",
    "Après ses études, elle travaille dans la banque à Paris. En parallèle de son CDI, elle achète son premier bien en 2014. Elle apprend à analyser les financements, le marché, les travaux et les structures, puis à relier ces dimensions pour décider.":
        "Học xong, chị làm trong ngành ngân hàng tại Paris. Song song với công việc chính thức, chị mua bất động sản đầu tiên năm 2014. Chị học cách phân tích các phương án vay, thị trường, phần sửa chữa và các cấu trúc pháp lý &mdash; rồi nối tất cả lại với nhau để quyết định.",
    "Chaque projet enrichit cette expérience et les principes qui guident aujourd&rsquo;hui Amélie &amp; Partners.":
        "Mỗi dự án lại bồi thêm cho kinh nghiệm ấy, và cho những nguyên tắc dẫn dắt Amélie &amp; Partners hôm nay.",
    "Amélie-Thu DUONG &middot; Fondatrice &amp; Investisseuse à Paris depuis 2014":
        "Amélie-Thu DUONG &middot; Nhà sáng lập &amp; nhà đầu tư tại Paris từ năm 2014",
    "Amélie-Thu DUONG &middot; Fondatrice": "Amélie-Thu DUONG &middot; Nhà sáng lập",
    "De Hanoï&hellip;": "Từ Hà Nội&hellip;",
    "à Paris.": "đến Paris.",
    "Hanoï": "Hà Nội",
    "Le départ": "Khởi đầu",
    "Née au Viêt Nam.": "Sinh ra tại Việt Nam.",
    "À 20 ans": "Năm 20 tuổi",
    "Arrivée en France, sans parler français.": "Sang Pháp, chưa nói được tiếng Pháp.",
    "Après les études": "Sau khi học xong",
    "La banque, à Paris.": "Ngành ngân hàng, tại Paris.",
    "Première acquisition, en parallèle du CDI.": "Bất động sản đầu tiên, song song với công việc chính thức.",
    "02 &middot; La pratique": "02 &middot; Cách làm việc",
    "Le terrain avant le discours.": "Thực địa trước lời nói.",
    "Un investissement se joue rarement dans un tableau seul. Il se joue dans la rue, dans l&rsquo;immeuble, dans les documents, dans les échanges avec la banque, dans les travaux et dans la façon dont l&rsquo;actif vivra après l&rsquo;achat.":
        "Một khoản đầu tư hiếm khi được định đoạt chỉ trong một bảng tính. Nó được định đoạt ngoài đường phố, trong toà nhà, trong hồ sơ giấy tờ, trong những cuộc trao đổi với ngân hàng, trong phần sửa chữa &mdash; và trong cách tài sản ấy sẽ sống sau khi mua.",
    "L&rsquo;approche d&rsquo;Amélie &amp; Partners recherche cette cohérence d&rsquo;ensemble&nbsp;: le bien, le prix, la dette, la trésorerie, l&rsquo;exploitation, le risque et la suite du parcours.":
        "Phương pháp của Amélie &amp; Partners tìm chính sự nhất quán tổng thể ấy: bất động sản, giá, khoản nợ, dòng tiền, việc vận hành, rủi ro và chặng đường phía sau.",
    "Comprendre notre approche": "Tìm hiểu phương pháp của chúng tôi",
    "03 &middot; Pourquoi transmettre&nbsp;?": "03 &middot; Vì sao phải truyền lại?",
    "Rendre les décisions": "Để các quyết định",
    "plus accessibles.": "trở nên dễ tiếp cận hơn.",
    "Amélie &amp; Partners structure et transmet les enseignements du terrain pour aider les investisseurs à comprendre leurs choix et à agir avec méthode.":
        "Amélie &amp; Partners đúc kết và truyền lại những gì thực địa dạy, để nhà đầu tư hiểu được lựa chọn của mình và hành động có phương pháp.",
    "Des ressources gratuites pour démystifier les fausses croyances. Des méthodes structurées pour apprendre à raisonner. Et, lorsque la situation le justifie, une expertise personnalisée pour décider ou exécuter avec plus de précision.":
        "Những tài liệu miễn phí để dẹp đi các niềm tin sai. Những phương pháp có cấu trúc để học cách lập luận. Và, khi hoàn cảnh đòi hỏi, một sự hỗ trợ chuyên môn riêng để quyết định hoặc thực hiện chính xác hơn.",
    "L&rsquo;objectif n&rsquo;est pas que vous suiviez une recette. C&rsquo;est que vous deveniez capable de comprendre la logique et de garder votre autonomie.":
        "Mục đích không phải là để quý vị làm theo một công thức. Mà là để quý vị nắm được cái lô-gích, và giữ được sự tự chủ của mình.",
    "Première acquisition à Paris": "Bất động sản đầu tiên tại Paris",
    "Investisseurs accompagnés": "Nhà đầu tư được đồng hành",
    "Projets immobiliers structurés": "Dự án bất động sản đã cấu trúc",
    "Projets parisiens étudiés": "Dự án tại Paris đã nghiên cứu",
    "Le terrain": "Thực địa",
    "Paris, au quotidien.": "Paris, mỗi ngày.",
    "Les projets accompagnés se jouent dans la rue, dans l&rsquo;immeuble et dans les documents autant que dans les tableaux.":
        "Những dự án được đồng hành định đoạt ngoài đường phố, trong toà nhà và trong hồ sơ giấy tờ, không kém gì trong các bảng tính.",
    "Mettre le défilement en pause": "Tạm dừng phần chạy",
    "Reprendre le défilement": "Tiếp tục phần chạy",
    "Travailler ensemble": "Làm việc cùng nhau",
    "Vous n&rsquo;avez pas besoin de tout savoir avant d&rsquo;avancer.": "Quý vị không cần biết hết mọi thứ mới bước tới được.",
    "Vous avez besoin de poser la bonne question, puis de vérifier chaque hypothèse dans le bon ordre.":
        "Quý vị cần đặt đúng câu hỏi, rồi kiểm chứng từng giả định theo đúng thứ tự.",
    "Analyser ma situation": "Phân tích tình hình của tôi",
    "Vous préférez écrire&nbsp;?": "Quý vị muốn viết hơn?",
    "Passez par le formulaire": "Dùng biểu mẫu",
    "Vidéo d’ambiance, sans son, en boucle.": "Video không khí, không tiếng, lặp lại.",
    "Reprendre la vidéo": "Tiếp tục video",
    "Portrait d&rsquo;Amélie-Thu DUONG, dans un jardin": "Chân dung Amélie-Thu DUONG, trong một khu vườn",
    "La tour de la Tortue et son reflet sur le lac Hoan Kiem, à la tombée du jour":
        "Tháp Rùa và bóng của nó trên hồ Hoàn Kiếm, lúc chiều buông",
    "La tour Eiffel vue depuis la Seine, un bateau-mouche au premier plan":
        "Tháp Eiffel nhìn từ sông Seine, một chiếc tàu du lịch ở tiền cảnh",
    "Étals de bouquinistes le long des quais de Seine": "Những quầy sách cũ dọc bờ sông Seine",
}

PAGES["formulaire.html"] = {
    "Nous écrire": "Viết cho chúng tôi",
    "Présentez": "Hãy kể về",
    "votre situation.": "tình hình của quý vị.",
    "Quelques lignes suffisent. Une réponse vous indiquera si un échange est utile et sous quel format.":
        "Vài dòng là đủ. Chúng tôi sẽ trả lời để cho biết một buổi trao đổi có hữu ích hay không, và dưới hình thức nào.",
    "Descendre au contenu": "Xuống phần nội dung",
    "Formulaire de contact": "Biểu mẫu liên hệ",
    "Ce qu&rsquo;il nous faut pour vous répondre": "Những gì chúng tôi cần để trả lời quý vị",
    "Votre projet ou la décision qui vous bloque": "Dự án của quý vị, hoặc quyết định đang khiến quý vị bế tắc",
    "Le profil d&rsquo;investisseur dont vous vous sentez le plus proche": "Hồ sơ nhà đầu tư mà quý vị thấy gần mình nhất",
    "L&rsquo;échéance que vous avez en tête, même approximative": "Thời hạn quý vị hình dung, dù chỉ áng chừng",
    "Ne pas remplir": "Không điền vào ô này",
    "Prénom": "Tên",
    "Nom": "Họ",
    "Adresse e-mail": "Địa chỉ e-mail",
    "Téléphone": "Điện thoại",
    "facultatif": "không bắt buộc",
    "France (+33)": "Pháp (+33)",
    "Belgique (+32)": "Bỉ (+32)",
    "Suisse (+41)": "Thuỵ Sĩ (+41)",
    "Luxembourg (+352)": "Luxembourg (+352)",
    "Monaco (+377)": "Monaco (+377)",
    "Espagne (+34)": "Tây Ban Nha (+34)",
    "Portugal (+351)": "Bồ Đào Nha (+351)",
    "Italie (+39)": "Ý (+39)",
    "Allemagne (+49)": "Đức (+49)",
    "Royaume-Uni (+44)": "Anh (+44)",
    "Irlande (+353)": "Ireland (+353)",
    "Pays-Bas (+31)": "Hà Lan (+31)",
    "États-Unis / Canada (+1)": "Hoa Kỳ / Canada (+1)",
    "Maroc (+212)": "Ma-rốc (+212)",
    "Tunisie (+216)": "Tunisia (+216)",
    "Algérie (+213)": "Algeria (+213)",
    "Sénégal (+221)": "Senegal (+221)",
    "Côte d’Ivoire (+225)": "Bờ Biển Ngà (+225)",
    "La Réunion (+262)": "La Réunion (+262)",
    "Guadeloupe (+590)": "Guadeloupe (+590)",
    "Martinique (+596)": "Martinique (+596)",
    "Nouvelle-Calédonie (+687)": "Nouvelle-Calédonie (+687)",
    "Viêt Nam (+84)": "Việt Nam (+84)",
    "Singapour (+65)": "Singapore (+65)",
    "Émirats arabes unis (+971)": "Các Tiểu vương quốc Ả Rập Thống nhất (+971)",
    "Vous êtes": "Quý vị là",
    "Sélectionner": "Chọn",
    "Particulier": "Cá nhân",
    "Professionnel": "Người hành nghề chuyên nghiệp",
    "Société (SCI, holding)": "Công ty (SCI, holding)",
    "Autre": "Khác",
    "Votre échéance": "Thời hạn của quý vị",
    "Dans les trois mois": "Trong vòng ba tháng",
    "Dans trois à six mois": "Trong ba đến sáu tháng nữa",
    "Dans six à douze mois": "Trong sáu đến mười hai tháng nữa",
    "Au-delà d’un an": "Hơn một năm nữa",
    "Pas de date fixée": "Chưa định thời điểm",
    "Votre profil d&rsquo;investisseur": "Hồ sơ nhà đầu tư của quý vị",
    "Primo-investisseur · se constituer un patrimoine": "Đầu tư lần đầu · gây dựng tài sản",
    "Investisseur locatif · générer des revenus réguliers": "Đầu tư cho thuê · tạo dòng thu đều đặn",
    "Rentier · vivre des revenus immobiliers": "Sống bằng bất động sản · lấy dòng thu làm sinh kế",
    "Investisseur patrimonial · préserver et développer son capital":
        "Đầu tư giữ của · bảo toàn và phát triển vốn",
    "Chasseur de rendement · maximiser la rentabilité": "Săn tỷ suất · tối đa hoá sinh lời",
    "Marchand de biens · acheter, rénover, revendre": "Kinh doanh bất động sản · mua, sửa, bán lại",
    "Investisseur fiscal · réduire sa fiscalité": "Đầu tư vì thuế · giảm gánh nặng thuế",
    "Professionnel ou entrepreneur · développer un portefeuille":
        "Người hành nghề hoặc chủ doanh nghiệp · mở rộng danh mục",
    "Investisseur familial · transmettre un patrimoine": "Đầu tư cho gia đình · để lại tài sản",
    "Investisseur opportuniste · saisir une occasion": "Đầu tư cơ hội · nắm lấy dịp tốt",
    "Investisseur en SCPI · investir sans gérer un bien":
        "Đầu tư qua quỹ SCPI · đầu tư mà không phải quản lý bất động sản",
    "Investisseur institutionnel · placer des capitaux importants":
        "Nhà đầu tư tổ chức · giải ngân vốn lớn",
    "Je ne sais pas encore": "Tôi chưa biết",
    "Votre situation en quelques lignes": "Tình hình của quý vị, trong vài dòng",
    "de 20 à 5 000 caractères": "từ 20 đến 5 000 ký tự",
    "J&rsquo;accepte que ces informations soient utilisées pour répondre à ma demande, conformément à la page":
        "Tôi đồng ý để những thông tin này được dùng nhằm trả lời yêu cầu của tôi, theo đúng trang",
    "Données personnelles": "Dữ liệu cá nhân (tiếng Pháp)",
    "Envoyer mon message": "Gửi tin nhắn của tôi",
    "Champs nécessaires. Votre message nous est envoyé directement, sans passer par votre logiciel de messagerie. Nous répondons sous un jour ouvré.":
        "Các mục bắt buộc. Tin nhắn của quý vị đến thẳng chỗ chúng tôi, không đi qua phần mềm thư điện tử của quý vị. Chúng tôi trả lời trong vòng một ngày làm việc.",
    "Les informations saisies servent uniquement à traiter votre demande et le suivi commercial qui en découle. Elles sont conservées trois ans à compter du dernier contact et ne sont ni vendues, ni cédées, ni louées. Vous disposez d&rsquo;un droit d&rsquo;accès, de rectification, d&rsquo;effacement et d&rsquo;opposition, que vous pouvez exercer par ce même formulaire. Le détail figure dans les":
        "Thông tin nhập vào chỉ dùng để xử lý yêu cầu của quý vị và việc theo dõi thương mại phát sinh từ đó. Thông tin được lưu ba năm kể từ lần liên hệ cuối, và không bao giờ được bán, nhượng hay cho thuê. Quý vị có quyền truy cập, sửa, xoá và phản đối, và có thể thực hiện các quyền ấy qua chính biểu mẫu này. Chi tiết được nêu trong",
    "données personnelles": "thông báo về dữ liệu cá nhân, bằng tiếng Pháp",
    "Votre message est parti.": "Tin nhắn của quý vị đã được gửi đi.",
    "Nous le lisons et vous répondons sous un jour ouvré, à l&rsquo;adresse que vous avez indiquée.":
        "Chúng tôi sẽ đọc và trả lời trong vòng một ngày làm việc, tới địa chỉ quý vị đã cho.",
    "Si votre situation demande d&rsquo;en parler plus tôt, le premier échange de trente minutes est ouvert à la réservation, gratuitement et sans engagement.":
        "Nếu tình hình của quý vị cần trao đổi sớm hơn, buổi trao đổi đầu tiên ba mươi phút luôn có thể đặt lịch, miễn phí và không ràng buộc.",
    "Réserver un premier échange": "Đặt buổi trao đổi đầu tiên",
    "Fermer": "Đóng",
    "Vous préférez parler de vive voix&nbsp;? L&rsquo;appel de cadrage dure trente minutes, il est gratuit et sans engagement.":
        "Quý vị muốn nói chuyện trực tiếp hơn? Cuộc gọi định hướng kéo dài ba mươi phút, miễn phí và không ràng buộc.",
    "Votre prénom": "Tên của quý vị",
    "Votre prénom nous permet de vous répondre correctement.": "Tên giúp chúng tôi xưng hô cho đúng.",
    "Votre nom": "Họ của quý vị",
    "Nous avons besoin de votre nom.": "Chúng tôi cần họ của quý vị.",
    "prenom.nom@exemple.fr": "ten.ho@vidu.com",
    "Sans adresse, nous ne pourrons pas vous répondre.": "Không có địa chỉ, chúng tôi không thể trả lời quý vị.",
    "Il manque quelque chose : une adresse s’écrit prenom.nom@exemple.fr.":
        "Còn thiếu gì đó: một địa chỉ trông như ten.ho@vidu.com.",
    "Indicatif du pays": "Mã vùng quốc gia",
    "Un numéro s’écrit en chiffres, espaces, points ou tirets.":
        "Số điện thoại viết bằng chữ số, khoảng trắng, dấu chấm hoặc gạch nối.",
    "Dites-nous à quel titre vous écrivez.": "Cho chúng tôi biết quý vị viết với tư cách nào.",
    "Même approximative, elle nous aide à prioriser.": "Dù chỉ áng chừng, nó cũng giúp chúng tôi sắp thứ tự ưu tiên.",
    "Choisissez le profil le plus proche, ou « je ne sais pas encore ».":
        "Hãy chọn hồ sơ gần nhất, hoặc &laquo;&nbsp;tôi chưa biết&nbsp;&raquo;.",
    "Votre projet ou la décision qui vous bloque, votre point de départ, et ce que vous attendez de cet échange.":
        "Dự án của quý vị hoặc quyết định đang khiến quý vị bế tắc, điểm xuất phát của quý vị, và điều quý vị mong có được từ buổi trao đổi này.",
    "Quelques lignes suffisent : elles nous évitent un aller-retour.":
        "Vài dòng là đủ: chúng giúp chúng ta khỏi phải hỏi đi hỏi lại.",
    "Quelques mots de plus, pour que nous puissions préparer une réponse utile.":
        "Thêm vài chữ nữa, để chúng tôi chuẩn bị được một câu trả lời hữu ích.",
    "Cette case doit être cochée pour que nous puissions vous répondre.":
        "Cần đánh dấu ô này thì chúng tôi mới có thể trả lời quý vị.",
}

# La phrase qui resume les trois effets est celle d'Amelie : elle reste
# dans sa langue.
CITATIONS["ressource-3-effets.html"] = {
    "&laquo;&nbsp;Le levier permet d&rsquo;acheter. L&rsquo;ascenseur construit le capital. La boule de neige le remet en mouvement.&nbsp;&raquo;",
}

PAGES["ressource-3-effets.html"] = {
    "Cadre pédagogique &middot; 8 min de lecture": "Bài giảng &middot; đọc trong 8 phút",
    "Les 3 effets": "Ba hiệu ứng",
    "dans l&rsquo;immobilier.": "trong bất động sản.",
    "Le vrai sujet n&rsquo;est pas seulement le rendement. C&rsquo;est la manière dont un actif permet de contrôler, construire puis réemployer du capital.":
        "Vấn đề thật sự không chỉ là tỷ suất sinh lời. Đó là cách một tài sản cho phép kiểm soát, tạo dựng rồi dùng lại vốn.",
    "Par Amélie-Thu DUONG": "Tác giả: Amélie-Thu DUONG",
    "Septembre 2026": "Tháng 9 năm 2026",
    "Descendre au contenu": "Xuống phần nội dung",
    "Format": "Hình thức",
    "Fiche de lecture, en ligne, en accès libre": "Một bài đọc, trực tuyến, tự do truy cập",
    "Durée": "Thời lượng",
    "8&nbsp;minutes de lecture": "đọc trong 8&nbsp;phút",
    "Niveau": "Trình độ",
    "Premier niveau, sans prérequis financier": "Nhập môn, không cần kiến thức tài chính",
    "Pour qui": "Dành cho ai",
    "Toute personne qui prépare ou relit un investissement": "Bất kỳ ai đang chuẩn bị hoặc xem lại một khoản đầu tư",
    "Mise à jour": "Cập nhật",
    "Emporter la fiche": "Mang bài đọc theo",
    "À lire hors ligne, ou à faire circuler.": "Để đọc ngoại tuyến, hoặc chuyển cho người khác.",
    "PDF, 306&nbsp;Ko, 3 pages. Le partage ouvre votre messagerie avec un message déjà rédigé&nbsp;: rien n&rsquo;est envoyé sans votre validation.":
        "Tệp PDF, 306&nbsp;Ko, 3 trang, bằng tiếng Pháp. Nút chia sẻ mở phần mềm thư của quý vị với một tin nhắn đã soạn sẵn: không có gì được gửi đi nếu quý vị chưa đồng ý.",
    "Télécharger le PDF": "Tải tệp PDF (tiếng Pháp)",
    "Partager par e-mail": "Chia sẻ qua e-mail",
    "Objectifs de la fiche": "Bài đọc này để làm gì",
    "Ce que cette lecture vous permet de faire.": "Điều mà bài đọc này giúp quý vị làm được.",
    "Distinguer les trois mécanismes qui se succèdent dans une opération&nbsp;: le levier, l&rsquo;ascenseur, la boule de neige.":
        "Phân biệt ba cơ chế nối tiếp nhau trong một giao dịch: đòn bẩy, thang máy, quả cầu tuyết.",
    "Lire une opération autrement que par son seul rendement.":
        "Đọc một giao dịch bằng thứ khác chứ không chỉ bằng tỷ suất sinh lời.",
    "Mesurer le capital réellement créé dans un actif, et non sa seule valeur.":
        "Đo phần vốn thật sự được tạo ra bên trong một tài sản, chứ không chỉ đo giá trị của nó.",
    "Situer le moment où un capital doit rester mobilisé, être refinancé ou être libéré.":
        "Nhận ra lúc nào vốn nên nằm yên, lúc nào nên tái tài trợ, lúc nào nên giải phóng.",
    "Au programme": "Nội dung",
    "Trois mécanismes,": "Ba cơ chế,",
    "dans l&rsquo;ordre où ils se produisent.": "theo thứ tự chúng xảy ra.",
    "Ils ne sont pas trois stratégies séparées. Ils forment une chaîne&nbsp;: chacun rend le suivant possible.":
        "Chúng không phải ba chiến lược tách rời. Chúng làm thành một chuỗi: cái này mở đường cho cái kia.",
    "Amplifier&nbsp;: l&rsquo;effet de levier": "Khuếch đại: hiệu ứng đòn bẩy",
    "Ce que la dette permet de contrôler, et ce qu&rsquo;elle amplifie en retour.":
        "Nợ vay cho phép kiểm soát những gì, và đổi lại nó khuếch đại những gì.",
    "Créer&nbsp;: l&rsquo;effet ascenseur": "Tạo dựng: hiệu ứng thang máy",
    "Comment un actif financé se transforme progressivement en capital net.":
        "Một tài sản mua bằng vốn vay dần biến thành vốn ròng ra sao.",
    "Réinvestir&nbsp;: l&rsquo;effet boule de neige": "Tái đầu tư: hiệu ứng quả cầu tuyết",
    "Ce que devient le capital créé, et à quelle condition il repart au travail.":
        "Phần vốn đã tạo ra rồi đi về đâu, và với điều kiện nào nó lại bắt đầu làm việc.",
    "La logique": "Mạch lô-gích",
    "Amplifier": "Khuếch đại",
    "Créer": "Tạo dựng",
    "Réinvestir": "Tái đầu tư",
    "Appliquer à ma situation": "Áp dụng vào tình hình của tôi",
    "Quand on débute, on regarde souvent un investissement à travers un seul chiffre&nbsp;: le rendement. Il est utile, mais il ne suffit pas à expliquer comment un patrimoine se construit réellement.":
        "Khi mới bắt đầu, người ta hay nhìn một khoản đầu tư qua đúng một con số: tỷ suất sinh lời. Con số ấy có ích, nhưng không đủ để giải thích một danh mục tài sản thật sự được dựng nên thế nào.",
    "Pour lire une opération dans le temps, nous distinguons trois mécanismes. Ils ne sont pas trois stratégies séparées. Ils forment une chaîne&nbsp;: le levier permet de contrôler un actif, l&rsquo;ascenseur transforme progressivement la dette en capital net, puis la boule de neige remet ce capital au travail.":
        "Để đọc một giao dịch theo dòng thời gian, chúng tôi tách ra ba cơ chế. Chúng không phải ba chiến lược tách rời. Chúng làm thành một chuỗi: đòn bẩy cho phép kiểm soát một tài sản, thang máy dần biến nợ thành vốn ròng, rồi quả cầu tuyết đưa vốn ấy trở lại làm việc.",
    "01 &middot; Amplifier&nbsp;: l&rsquo;effet de levier": "01 &middot; Khuếch đại: hiệu ứng đòn bẩy",
    "Notion clé": "Ý chính",
    "Utiliser la dette bancaire pour contrôler un actif d&rsquo;une valeur supérieure à ses fonds propres.":
        "Dùng nợ ngân hàng để kiểm soát một tài sản có giá trị lớn hơn vốn tự có.",
    "L&rsquo;effet de levier consiste à utiliser la dette bancaire pour contrôler un actif d&rsquo;une valeur supérieure à vos fonds propres. Avec 50&nbsp;000&nbsp;€ d&rsquo;apport, vous ne contrôlez pas seulement 50&nbsp;000&nbsp;€ d&rsquo;actif&nbsp;: vous pouvez contrôler une opération beaucoup plus importante, à condition que le financement reste soutenable.":
        "Đòn bẩy nghĩa là dùng nợ ngân hàng để kiểm soát một tài sản có giá trị lớn hơn vốn tự có của quý vị. Với 50&nbsp;000&nbsp;€ vốn tự có, quý vị không chỉ kiểm soát 50&nbsp;000&nbsp;€ tài sản: quý vị có thể kiểm soát một giao dịch lớn hơn nhiều &mdash; với điều kiện khoản vay vẫn gánh được.",
    "Le levier amplifie le pouvoir d&rsquo;achat, mais il amplifie aussi les conséquences d&rsquo;une mauvaise hypothèse. Le taux, la durée, le niveau de mensualité, la vacance, les travaux et la marge de sécurité doivent être lus ensemble.":
        "Đòn bẩy khuếch đại sức mua, nhưng cũng khuếch đại hậu quả của một giả định sai. Lãi suất, thời hạn, mức trả hằng tháng, thời gian bỏ trống, phần sửa chữa và biên độ an toàn phải được đọc cùng nhau.",
    "La bonne question": "Câu hỏi đúng",
    "Quelle quantité de dette puis-je utiliser sans fragiliser la suite de ma trajectoire&nbsp;?":
        "Tôi có thể vay đến mức nào mà không làm yếu phần còn lại của lộ trình?",
    "02 &middot; Créer&nbsp;: l&rsquo;effet ascenseur": "02 &middot; Tạo dựng: hiệu ứng thang máy",
    "Le mouvement qui transforme progressivement un actif financé en capital net.":
        "Chuyển động dần biến một tài sản mua bằng vốn vay thành vốn ròng.",
    "Nous appelons «&nbsp;effet ascenseur&nbsp;» le mouvement qui transforme progressivement un actif financé en capital net. À mesure que la dette s&rsquo;amortit, que les loyers sont encaissés, que des travaux créent de la valeur ou que le marché évolue, l&rsquo;écart entre la valeur du bien et le capital restant dû peut augmenter.":
        "Chúng tôi gọi &laquo;&nbsp;hiệu ứng thang máy&nbsp;&raquo; là chuyển động dần biến một tài sản mua bằng vốn vay thành vốn ròng. Khi nợ được trả dần, khi tiền thuê thu về, khi việc sửa chữa tạo thêm giá trị hay khi thị trường đổi thay, khoảng cách giữa giá trị bất động sản và dư nợ còn lại có thể rộng ra.",
    "Ce capital existe, mais il peut rester enfermé dans l&rsquo;actif. L&rsquo;enjeu est donc de le mesurer, puis de décider s&rsquo;il doit rester mobilisé, être refinancé ou être libéré par un arbitrage. C&rsquo;est souvent là que se joue le changement d&rsquo;échelle.":
        "Phần vốn ấy có thật, nhưng có thể vẫn bị khoá trong tài sản. Việc cần làm là đo nó, rồi quyết định nên để yên, nên tái tài trợ, hay nên giải phóng bằng cách bán. Bước nhảy về quy mô thường được định đoạt chính ở đây.",
    "Lecture simplifiée": "Cách đọc giản lược",
    "Valeur du bien &minus; dette restante = capital net dans l&rsquo;actif. À compléter par les coûts de sortie, la fiscalité et la trésorerie réellement disponible.":
        "Giá trị bất động sản &minus; dư nợ = vốn ròng trong tài sản. Còn phải trừ thêm chi phí bán, thuế và số tiền mặt thật sự sẵn có.",
    "Combien de capital ai-je créé, et que pourrait-il produire s&rsquo;il était libéré&nbsp;?":
        "Tôi đã tạo ra bao nhiêu vốn, và nó có thể sinh ra gì nếu được giải phóng?",
    "03 &middot; Réinvestir&nbsp;: l&rsquo;effet boule de neige": "03 &middot; Tái đầu tư: hiệu ứng quả cầu tuyết",
    "Le capital déjà créé qui finance, à son tour, de nouveaux actifs.":
        "Phần vốn đã tạo ra, đến lượt nó, đi tài trợ cho những tài sản mới.",
    "L&rsquo;effet boule de neige commence lorsque le capital déjà créé finance de nouveaux actifs. Un apport provenant d&rsquo;un arbitrage, une trésorerie accumulée ou un capital refinancé peut servir de point de départ à une opération plus importante.":
        "Hiệu ứng quả cầu tuyết bắt đầu khi phần vốn đã tạo ra đi tài trợ cho những tài sản mới. Tiền thu từ một thương vụ bán, tiền mặt tích luỹ hay vốn được tái tài trợ đều có thể làm điểm xuất phát cho một giao dịch lớn hơn.",
    "La vitesse n&rsquo;est pas l&rsquo;objectif en soi. Réinvestir trop vite, sans conserver de marge de sécurité, peut affaiblir tout le système. Le capital doit être réemployé selon l&rsquo;objectif, le risque accepté et les besoins de liquidité.":
        "Tốc độ tự nó không phải mục tiêu. Tái đầu tư quá nhanh mà không giữ biên độ an toàn có thể làm yếu cả cấu trúc. Vốn cần được dùng lại tuỳ theo mục tiêu, mức rủi ro chấp nhận được và nhu cầu tiền mặt.",
    "Où ce capital peut-il être le plus utile maintenant&nbsp;: nouvel actif, sécurité, diversification ou attente&nbsp;?":
        "Lúc này, phần vốn ấy hữu ích nhất ở đâu: một tài sản mới, sự an toàn, sự đa dạng hoá, hay là chờ?",
    "Ce que cela change dans vos décisions": "Điều này thay đổi gì trong các quyết định của quý vị",
    "Vous ne regardez plus seulement «&nbsp;combien rapporte ce bien&nbsp;?&nbsp;». Vous cherchez à comprendre quelle quantité de capital il mobilise, ce qu&rsquo;il crée réellement et si ce capital est encore placé au bon endroit.":
        "Quý vị không còn chỉ nhìn &laquo;&nbsp;bất động sản này sinh ra bao nhiêu?&nbsp;&raquo;. Quý vị tìm hiểu xem nó giam bao nhiêu vốn, nó thật sự tạo ra gì, và phần vốn ấy còn đang đặt đúng chỗ hay không.",
    "C&rsquo;est cette lecture qui permet de choisir entre acheter, conserver, refinancer, vendre ou attendre, sans transformer l&rsquo;accumulation de biens en objectif final.":
        "Chính cách đọc ấy cho phép chọn giữa mua, giữ, tái tài trợ, bán hay chờ &mdash; mà không biến việc gom góp bất động sản thành mục đích cuối cùng.",
    "Points de vigilance": "Những điểm cần lưu ý",
    "Ce que la fiche ne passe pas sous silence.": "Điều bài đọc này không né tránh.",
    "Le levier amplifie le pouvoir d&rsquo;achat, mais il amplifie aussi les conséquences d&rsquo;une mauvaise hypothèse.":
        "Đòn bẩy khuếch đại sức mua, nhưng cũng khuếch đại hậu quả của một giả định sai.",
    "Le capital net ne se lit qu&rsquo;après les coûts de sortie, la fiscalité et la trésorerie réellement disponible.":
        "Vốn ròng chỉ đọc được sau khi đã trừ chi phí bán, thuế và số tiền mặt thật sự sẵn có.",
    "Réinvestir trop vite, sans conserver de marge de sécurité, peut affaiblir tout le système.":
        "Tái đầu tư quá nhanh mà không giữ biên độ an toàn có thể làm yếu cả cấu trúc.",
    "La vitesse n&rsquo;est pas un objectif&nbsp;: le capital se réemploie selon l&rsquo;objectif, le risque accepté et les besoins de liquidité.":
        "Tốc độ không phải mục tiêu: vốn được dùng lại tuỳ theo mục tiêu, mức rủi ro chấp nhận được và nhu cầu tiền mặt.",
    "Cette fiche est pédagogique et générale. Elle ne remplace pas une analyse juridique, fiscale ou financière adaptée à votre situation. Les résultats varient selon les situations.":
        "Bài đọc này mang tính giảng giải và khái quát. Nó không thay thế một phân tích pháp lý, thuế hay tài chính làm riêng cho tình hình của quý vị. Kết quả thay đổi tuỳ theo từng hoàn cảnh.",
    "Appliquer le raisonnement à votre situation": "Áp dụng cách lập luận vào tình hình của quý vị",
    "Votre capital est-il encore placé au bon endroit&nbsp;?": "Vốn của quý vị còn đang đặt đúng chỗ không?",
    "Le Diagnostic Stratégique reprend cette lecture avec vos chiffres, vos contraintes et votre horizon.":
        "Diagnostic Stratégique lấy lại cách đọc này với những con số, ràng buộc và tầm nhìn thời gian của quý vị.",
    "Découvrir le Diagnostic Stratégique": "Tìm hiểu Diagnostic Stratégique",
    "Vous préférez écrire&nbsp;?": "Quý vị muốn viết hơn?",
    "Passez par le formulaire": "Dùng biểu mẫu",
    "Les trois effets": "Ba hiệu ứng",
}
