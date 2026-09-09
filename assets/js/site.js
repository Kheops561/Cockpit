/* ==========================================================================
   AMÉLIE & PARTNERS · comportements du site
   Amélioration progressive : sans JavaScript, toutes les pages restent
   lisibles, navigables et utilisables (menu déplié, contenus visibles,
   FAQ native, témoignages défilables à la main).
   Toute animation est neutralisée sous prefers-reduced-motion.
   ========================================================================== */

(function () {
  'use strict';

  document.documentElement.classList.add('js');

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  var isReduced = function () { return reduced.matches; };

  /* ------------------------------------------------------ menu mobile */

  function initMenu() {
    var burger = document.querySelector('[data-burger]');
    var drawer = document.getElementById('menu-mobile');
    if (!burger || !drawer) return;

    drawer.hidden = true;
    burger.hidden = false;
    burger.setAttribute('aria-expanded', 'false');

    function setOpen(open) {
      burger.setAttribute('aria-expanded', String(open));
      drawer.hidden = !open;
    }

    burger.addEventListener('click', function () {
      setOpen(burger.getAttribute('aria-expanded') !== 'true');
    });

    drawer.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && burger.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        burger.focus();
      }
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth >= 1200) setOpen(false);
    });
  }

  /* --------------------------------------------- ombre de l'en-tête */

  function initHeader() {
    var header = document.querySelector('[data-header]');
    if (!header) return;
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ------------------------------------- apparition au défilement */

  function initReveal() {
    var items = document.querySelectorAll('.reveal, .frame--sheen, .frame--underline');
    if (!items.length) return;

    if (isReduced() || !('IntersectionObserver' in window)) {
      Array.prototype.forEach.call(items, function (el) { el.classList.add('is-visible'); });
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        show(entry.target);
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0 });

    Array.prototype.forEach.call(items, function (el) { io.observe(el); });

    function show(el) {
      el.classList.add('is-visible');
      io.unobserve(el);
    }

    // Filet de sécurité. Les notifications de l'observateur sont
    // asynchrones : elles sont évaluées au moment où elles sont remises, si
    // bien qu'un défilement rapide peut faire manquer un bloc et le laisser
    // invisible. Ce balayage, appelé au défilement et au redimensionnement,
    // révèle tout ce qui a déjà atteint le bas de la fenêtre.
    var ticking = false;

    function sweep() {
      ticking = false;
      var limit = window.innerHeight * 0.92;
      Array.prototype.forEach.call(items, function (el) {
        if (el.classList.contains('is-visible')) return;
        if (el.getBoundingClientRect().top < limit) show(el);
      });
    }

    function onScroll() {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(sweep);
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    window.addEventListener('load', sweep);
    sweep();
  }

  /* --------------------------------------------- compteurs chiffrés
     Le libellé complet reste dans data-value ; seul le nombre s'anime.
     Aucun chiffre n'est calculé : la valeur affichée est celle du HTML. */

  function initCounters() {
    var counters = document.querySelectorAll('[data-count]');
    if (!counters.length) return;

    if (isReduced() || !('IntersectionObserver' in window)) return;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        run(entry.target);
        io.unobserve(entry.target);
      });
    }, { threshold: 0.6 });

    Array.prototype.forEach.call(counters, function (el) { io.observe(el); });

    function run(el) {
      var full = el.textContent;
      var match = full.match(/(\d+(?:[.,]\d+)?)/);
      if (!match) return;
      var target = parseFloat(match[1].replace(',', '.'));
      var decimals = (match[1].split(/[.,]/)[1] || '').length;
      var start = performance.now();
      var duration = 1200;

      function frame(now) {
        var p = Math.min((now - start) / duration, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        var value = (target * eased).toFixed(decimals).replace('.', ',');
        el.textContent = full.replace(match[1], value);
        if (p < 1) requestAnimationFrame(frame);
        else el.textContent = full;
      }
      el.textContent = full.replace(match[1], (0).toFixed(decimals).replace('.', ','));
      requestAnimationFrame(frame);
    }
  }

  /* ----------------------------------------- bandeau des témoignages
     Grand écran comme mobile : défilement continu, pause au survol et
     au focus, plus une commande explicite pause / reprise.
     Mouvement réduit : défilement manuel, sans animation. */

  function initMarquee() {
    var marquee = document.querySelector('[data-marquee]');
    var button = document.querySelector('[data-marquee-toggle]');
    if (!marquee) return;

    if (isReduced()) {
      if (button) button.hidden = true;
      return;
    }

    if (!button) return;
    button.hidden = false;

    var labelPause = button.getAttribute('data-label-pause') || 'Mettre en pause';
    var labelPlay = button.getAttribute('data-label-play') || 'Reprendre le défilement';
    var text = button.querySelector('[data-marquee-label]') || button;

    button.addEventListener('click', function () {
      var paused = marquee.classList.toggle('is-paused');
      button.setAttribute('aria-pressed', String(paused));
      text.textContent = paused ? labelPlay : labelPause;
    });
  }

  /* ------------------------------------------------ parallaxe légère
     Décalage vertical très faible (quelques dizaines de pixels au
     maximum) : le rythme est suggéré, la lecture n'est pas gênée. */

  function initParallax() {
    var layers = document.querySelectorAll('[data-parallax]');
    if (!layers.length || isReduced()) return;

    var ticking = false;

    function update() {
      var vh = window.innerHeight;
      Array.prototype.forEach.call(layers, function (layer) {
        var rect = layer.getBoundingClientRect();
        if (rect.bottom < -200 || rect.top > vh + 200) return;
        var amount = parseFloat(layer.getAttribute('data-parallax')) || 12;
        var progress = (rect.top + rect.height / 2 - vh / 2) / vh;
        var target = layer.querySelector('img') || layer;
        target.style.transform = 'translate3d(0,' + (-progress * amount).toFixed(2) + 'px,0) scale(1.06)';
      });
      ticking = false;
    }

    function onScroll() {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(update);
    }

    update();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
  }

  /* --------------------------------------- année courante du footer */

  function initYear() {
    var nodes = document.querySelectorAll('[data-year]');
    var year = String(new Date().getFullYear());
    Array.prototype.forEach.call(nodes, function (el) { el.textContent = year; });
  }

  /* ------------------------------------------------------ démarrage */

  function init() {
    initMenu();
    initHeader();
    initReveal();
    initCounters();
    initMarquee();
    initParallax();
    initYear();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

/* ==========================================================================
   Bloc « Travaillons ensemble » : révélation du créneau en deux temps.
   Sans ce script, le titre reste un lien direct vers la réservation.
   ========================================================================== */

(function () {
  'use strict';

  function initBooking() {
    var blocks = document.querySelectorAll('[data-booking]');
    if (!blocks.length) return;

    Array.prototype.forEach.call(blocks, function (block) {
      var invite = block.querySelector('[data-booking-invite]');
      var confirm = block.querySelector('[data-booking-confirm]');
      if (!invite || !confirm) return;

      var target = confirm.querySelector('a, button');

      invite.addEventListener('click', function (e) {
        e.preventDefault();
        block.classList.add('is-open');
        invite.setAttribute('tabindex', '-1');
        invite.setAttribute('aria-hidden', 'true');
        if (target) {
          window.setTimeout(function () { target.focus(); }, 420);
        }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBooking);
  } else {
    initBooking();
  }
})();

/* ==========================================================================
   Vidéos d'ambiance.
   La vidéo se superpose à une photographie et n'apparaît que si elle peut
   réellement être lue. Fichier absent, format refusé, lecture automatique
   bloquée ou préférence de mouvement réduit : la photographie reste seule.
   Toute vidéo en boucle reçoit une commande de pause explicite.
   ========================================================================== */

(function () {
  'use strict';

  function initVideos() {
    var videos = document.querySelectorAll('[data-video]');
    if (!videos.length) return;

    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');

    Array.prototype.forEach.call(videos, function (video) {
      var control = video.parentNode.querySelector('[data-video-toggle]');

      function abandon() {
        video.classList.remove('is-ready');
        if (video.parentNode) video.parentNode.removeChild(video);
        if (control) control.hidden = true;
      }

      if (reduced.matches) { abandon(); return; }

      video.addEventListener('error', abandon);
      video.addEventListener('stalled', function () {
        if (!video.classList.contains('is-ready')) abandon();
      });

      var sources = video.querySelectorAll('source');
      Array.prototype.forEach.call(sources, function (s) {
        s.addEventListener('error', function () {
          // Plus aucune source utilisable : on revient à la photographie.
          if (video.networkState === 3 || sources.length === 1) abandon();
        });
      });

      video.addEventListener('playing', function () {
        video.classList.add('is-ready');
        if (control) {
          control.hidden = false;
          control.setAttribute('aria-pressed', 'false');
        }
      });

      var promise = video.play();
      if (promise && typeof promise.catch === 'function') {
        promise.catch(abandon);
      }

      if (control) {
        var labelPause = control.getAttribute('data-label-pause') || 'Mettre la vidéo en pause';
        var labelPlay = control.getAttribute('data-label-play') || 'Reprendre la vidéo';
        var text = control.querySelector('[data-video-label]') || control;
        control.addEventListener('click', function () {
          if (video.paused) {
            video.play();
            control.setAttribute('aria-pressed', 'false');
            text.textContent = labelPause;
          } else {
            video.pause();
            control.setAttribute('aria-pressed', 'true');
            text.textContent = labelPlay;
          }
        });
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initVideos);
  } else {
    initVideos();
  }
})();

/* ==========================================================================
   Parcours de la fondatrice : tracé qui se dessine au défilement, étapes qui
   apparaissent en séquence, note manuscrite qui se découvre.
   Sans ce script, le tracé est déjà dessiné, les étapes visibles et la note
   entièrement lisible : l'animation n'ajoute que du rythme.
   ========================================================================== */

(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');

  function initJourney() {
    var carte = document.querySelector('[data-carte]');
    var path = document.querySelector('[data-journey-path]');
    var steps = document.querySelectorAll('[data-journey-step]');
    var note = document.querySelector('[data-handnote]');
    if (!carte && !path && !steps.length && !note) return;

    if (path) {
      // La longueur réelle du tracé sert de motif de pointillés : le trait
      // paraît alors se dessiner d'un bout à l'autre.
      var length = Math.ceil(path.getTotalLength());
      path.style.setProperty('--len', length);
    }

    if (reduced.matches || !('IntersectionObserver' in window)) {
      if (carte) carte.classList.add('is-visible');
      Array.prototype.forEach.call(steps, function (s) { s.classList.add('is-visible'); });
      if (note) note.classList.add('is-visible');
      return;
    }

    var cibles = [];
    // La carte porte l'état : le tracé, l'avion et les vignettes en découlent.
    if (carte) cibles.push([carte, 'is-visible']);
    Array.prototype.forEach.call(steps, function (s, i) {
      s.style.setProperty('--step-delay', (0.45 + i * 0.22).toFixed(2) + 's');
      cibles.push([s, 'is-visible']);
    });
    if (note) cibles.push([note, 'is-visible']);

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add(entry.target.getAttribute('data-reveal-class') || 'is-visible');
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0 });

    cibles.forEach(function (paire) {
      paire[0].setAttribute('data-reveal-class', paire[1]);
      io.observe(paire[0]);
    });

    // Même filet de sécurité que pour les autres apparitions.
    function sweep() {
      var limit = window.innerHeight * 0.92;
      cibles.forEach(function (paire) {
        var el = paire[0];
        if (el.classList.contains(paire[1])) return;
        if (el.getBoundingClientRect().top < limit) {
          el.classList.add(paire[1]);
          io.unobserve(el);
        }
      });
    }
    window.addEventListener('scroll', sweep, { passive: true });
    window.addEventListener('load', sweep);
    sweep();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initJourney);
  } else {
    initJourney();
  }
})();

/* ==========================================================================
   Fil du parcours : repère vertical qui se remplit au fil du défilement.
   Entièrement construit ici : sans JavaScript, la page se lit normalement,
   sans repère. Il double la structure des titres et ne porte aucune
   information qui n'y figure pas déjà.
   ========================================================================== */

(function () {
  'use strict';

  function initTimeline() {
    var zone = document.querySelector('[data-timeline]');
    if (!zone) return;

    var sections = zone.querySelectorAll('[data-timeline-step]');
    if (sections.length < 2) return;

    var rail = document.createElement('div');
    rail.className = 'timeline__rail';
    rail.setAttribute('aria-hidden', 'true');
    rail.innerHTML = '<span class="timeline__track"></span><span class="timeline__progress"></span>';

    var progress = rail.querySelector('.timeline__progress');
    var points = [];

    Array.prototype.forEach.call(sections, function (section) {
      var step = document.createElement('span');
      step.className = 'timeline__step';
      if (section.classList.contains('section--ink') || section.classList.contains('cta')) {
        step.className += ' on-ink';
      }
      step.innerHTML = '<span class="timeline__dot"></span><span class="timeline__label"></span>';
      step.querySelector('.timeline__label').textContent = section.getAttribute('data-timeline-step');
      rail.appendChild(step);
      points.push({ section: section, step: step });
    });

    zone.appendChild(rail);
    if (getComputedStyle(zone).position === 'static') zone.style.position = 'relative';

    var ticking = false;

    function place() {
      var haut = zone.getBoundingClientRect().top + window.scrollY;
      var hauteur = zone.offsetHeight || 1;
      points.forEach(function (p) {
        var centre = p.section.getBoundingClientRect().top + window.scrollY
                   + p.section.offsetHeight / 2 - haut;
        p.step.style.top = (centre / hauteur * 100).toFixed(3) + '%';
        p.repere = centre;
      });
      update();
    }

    function update() {
      ticking = false;
      var haut = zone.getBoundingClientRect().top + window.scrollY;
      var hauteur = zone.offsetHeight || 1;
      // Le point de lecture est le milieu de la fenêtre.
      var lecture = window.scrollY + window.innerHeight / 2 - haut;
      var ratio = Math.max(0, Math.min(1, lecture / hauteur));
      progress.style.height = (ratio * 100).toFixed(3) + '%';

      var courant = -1;
      points.forEach(function (p, i) {
        if (p.repere <= lecture) courant = i;
      });
      points.forEach(function (p, i) {
        p.step.classList.toggle('is-passed', i <= courant);
        p.step.classList.toggle('is-current', i === courant);
      });
    }

    function onScroll() {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(update);
    }

    place();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', place);
    window.addEventListener('load', place);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTimeline);
  } else {
    initTimeline();
  }
})();

/* Schéma des quatre étapes : une seule bascule, les décalages sont en CSS. */
(function () {
  'use strict';

  function initSchema() {
    var blocs = document.querySelectorAll('[data-schema]');
    if (!blocs.length) return;

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches
        || !('IntersectionObserver' in window)) {
      Array.prototype.forEach.call(blocs, function (b) { b.classList.add('is-visible'); });
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0 });

    Array.prototype.forEach.call(blocs, function (b) { io.observe(b); });

    function sweep() {
      var limit = window.innerHeight * 0.92;
      Array.prototype.forEach.call(blocs, function (b) {
        if (b.classList.contains('is-visible')) return;
        if (b.getBoundingClientRect().top < limit) { b.classList.add('is-visible'); io.unobserve(b); }
      });
    }
    window.addEventListener('scroll', sweep, { passive: true });
    window.addEventListener('load', sweep);
    sweep();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSchema);
  } else {
    initSchema();
  }
})();

/* ==========================================================================
   Le processus : une barre de reperes et le recapitulatif complet.
   Les cinq etapes restent toutes affichees, comme un schema recapitulatif.
   La barre au-dessus est faite de vrais liens d'ancre : elle mene deja a
   l'etape voulue sans ce script. Le script n'ajoute que deux conforts, le
   defilement adouci et la mise en surbrillance de l'etape lue. Sous
   mouvement reduit, le saut reste instantane.
   ========================================================================== */

(function () {
  'use strict';

  function initProcessus() {
    var bloc = document.querySelector('[data-processus]');
    if (!bloc) return;

    var stops = bloc.querySelectorAll('.processus__stop');
    var etapes = bloc.querySelectorAll('.step');
    if (!stops.length || stops.length !== etapes.length) return;

    var doux = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function marquer(i) {
      for (var k = 0; k < stops.length; k++) {
        stops[k].setAttribute('aria-current', k === i ? 'true' : 'false');
        etapes[k].classList.toggle('est-active', k === i);
      }
    }

    Array.prototype.forEach.call(stops, function (stop, i) {
      stop.addEventListener('click', function (e) {
        marquer(i);
        if (!doux || !etapes[i].scrollIntoView) return;
        e.preventDefault();
        etapes[i].scrollIntoView({ behavior: 'smooth', block: 'center' });
        if (window.history && window.history.replaceState) {
          window.history.replaceState(null, '', stop.getAttribute('href'));
        }
      });
    });

    // Repere de lecture : l'etape dont le centre est le plus proche de celui
    // de l'ecran. Le lecteur voit ou il en est sans avoir rien a cliquer.
    var attente = false;
    function suivre() {
      attente = false;
      var milieu = window.innerHeight / 2;
      var meilleur = 0;
      var ecart = Infinity;
      for (var k = 0; k < etapes.length; k++) {
        var r = etapes[k].getBoundingClientRect();
        var d = Math.abs(r.top + r.height / 2 - milieu);
        if (d < ecart) { ecart = d; meilleur = k; }
      }
      marquer(meilleur);
    }
    function planifier() {
      if (attente) return;
      attente = true;
      window.requestAnimationFrame(suivre);
    }

    window.addEventListener('scroll', planifier, { passive: true });
    window.addEventListener('resize', planifier);

    marquer(0);
    suivre();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initProcessus);
  } else {
    initProcessus();
  }
})();

/* ==========================================================================
   Les temoignages en pile.
   Une carte devant, les suivantes derriere. On avance au doigt, a la
   souris, au clavier ou par les reperes. Sans ce script, les huit
   temoignages restent affiches en grille : la pile est un confort de
   lecture, jamais une condition d'acces. Rien ne defile tout seul, il n'y
   a donc rien a mettre en pause.
   ========================================================================== */

(function () {
  'use strict';

  var SEUIL = 90;   // deplacement, en pixels, au-dela duquel la carte part

  function initPile() {
    var bloc = document.querySelector('[data-pile]');
    if (!bloc) return;

    var liste = bloc.querySelector('.pile__cartes');
    var cartes = bloc.querySelectorAll('[data-pile-carte]');
    if (cartes.length < 2) return;

    var courant = 0;

    // --- Hauteur figee : la pile ne doit pas sauter d'une carte a l'autre.
    function figerHauteur() {
      liste.style.removeProperty('--pile-h');
      bloc.classList.remove('est-empilee');
      // Mesurer les cartes a la largeur qu'elles auront une fois empilees :
      // la grille a trois colonnes les rendrait bien plus hautes.
      bloc.classList.add('est-mesure');
      var h = 0;
      for (var k = 0; k < cartes.length; k++) {
        h = Math.max(h, cartes[k].getBoundingClientRect().height);
      }
      bloc.classList.remove('est-mesure');
      bloc.classList.add('est-empilee');
      liste.style.setProperty('--pile-h', Math.ceil(h) + 'px');
    }

    // --- Commandes : deux chevrons et un repere par temoignage.
    var chevron = function (d) {
      return '<svg class="icon" width="16" height="16" viewBox="0 0 16 16" fill="none"'
           + ' aria-hidden="true" focusable="false"><path d="M' + (d < 0 ? '10 3L5 8l5 5' : '6 3l5 5-5 5')
           + '" stroke="currentColor" stroke-width="1.4" stroke-linecap="square"/></svg>';
    };

    var commandes = document.createElement('div');
    commandes.className = 'pile__commandes';

    var avant = document.createElement('button');
    avant.type = 'button';
    avant.className = 'pile__fleche';
    avant.innerHTML = chevron(-1) + '<span class="sr-only">Témoignage précédent</span>';

    var reperes = document.createElement('ul');
    reperes.className = 'pile__reperes';

    var apres = document.createElement('button');
    apres.type = 'button';
    apres.className = 'pile__fleche';
    apres.innerHTML = chevron(1) + '<span class="sr-only">Témoignage suivant</span>';

    var boutons = [];
    Array.prototype.forEach.call(cartes, function (carte, i) {
      var li = document.createElement('li');
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'pile__repere';
      b.innerHTML = '<span class="sr-only">Témoignage ' + (i + 1) + ' sur ' + cartes.length + '</span>';
      b.addEventListener('click', function () { montrer(i); });
      li.appendChild(b);
      reperes.appendChild(li);
      boutons.push(b);
    });

    commandes.appendChild(avant);
    commandes.appendChild(reperes);
    commandes.appendChild(apres);
    liste.parentNode.insertBefore(commandes, liste.nextSibling);

    avant.addEventListener('click', function () { montrer(courant - 1); });
    apres.addEventListener('click', function () { montrer(courant + 1); });

    // --- Placement : trois cartes visibles, les autres retirees du plan.
    function montrer(i) {
      courant = (i + cartes.length) % cartes.length;
      for (var k = 0; k < cartes.length; k++) {
        var rang = (k - courant + cartes.length) % cartes.length;
        cartes[k].setAttribute('data-rang', rang > 2 ? '-1' : String(rang));
        cartes[k].style.transform = '';
        // Les huit temoignages restent lus par les technologies
        // d'assistance : la pile est un effet visuel, pas un filtre.
        boutons[k].setAttribute('aria-current', String(k === courant));
      }
    }

    // --- Saisie : la carte de devant suit le doigt ou la souris.
    var depart = null;
    liste.addEventListener('pointerdown', function (e) {
      var carte = cartes[courant];
      if (!carte.contains(e.target)) return;
      depart = e.clientX;
      carte.classList.add('est-saisie');
      carte.setPointerCapture(e.pointerId);
    });
    liste.addEventListener('pointermove', function (e) {
      if (depart === null) return;
      var d = e.clientX - depart;
      cartes[courant].style.transform = 'translateX(' + d + 'px) rotate(' + (d / 22) + 'deg)';
    });
    function relacher(e) {
      if (depart === null) return;
      var d = e.clientX - depart;
      var carte = cartes[courant];
      depart = null;
      carte.classList.remove('est-saisie');
      carte.style.transform = '';
      if (Math.abs(d) > SEUIL) montrer(courant + (d < 0 ? 1 : -1));
    }
    liste.addEventListener('pointerup', relacher);
    liste.addEventListener('pointercancel', relacher);

    // --- Clavier : les fleches parcourent la pile.
    bloc.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (!d) return;
      e.preventDefault();
      montrer(courant + d);
    });

    figerHauteur();
    montrer(0);

    var attente = null;
    window.addEventListener('resize', function () {
      window.clearTimeout(attente);
      attente = window.setTimeout(function () { figerHauteur(); montrer(courant); }, 150);
    });
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(function () { figerHauteur(); montrer(courant); });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPile);
  } else {
    initPile();
  }
})();
