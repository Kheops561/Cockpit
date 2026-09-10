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

  /* ------------------------------------------- choix de la langue */

  /* Le menu des langues est un `details` : il s'ouvre et se ferme tout seul,
     au clic comme au clavier, sans une ligne de JavaScript. Ce qui suit ne
     fait qu'ajouter les deux gestes qu'un `details` ne connait pas de
     lui-meme — la touche d'echappement, et le clic a cote — parce qu'un menu
     qui reste ouvert derriere le doigt agace. Sans JavaScript, il faut
     recliquer sur le bouton : le menu reste utilisable. */

  function initLangues() {
    var menus = document.querySelectorAll('[data-langues]');
    if (!menus.length) return;

    function fermerLesAutres(sauf) {
      Array.prototype.forEach.call(menus, function (m) {
        if (m !== sauf) m.open = false;
      });
    }

    Array.prototype.forEach.call(menus, function (menu) {
      menu.addEventListener('toggle', function () {
        if (menu.open) fermerLesAutres(menu);
      });
    });

    document.addEventListener('click', function (e) {
      Array.prototype.forEach.call(menus, function (menu) {
        if (menu.open && !menu.contains(e.target)) menu.open = false;
      });
    });

    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      Array.prototype.forEach.call(menus, function (menu) {
        if (!menu.open) return;
        menu.open = false;
        // Le focus revient sur le bouton : on ne perd pas sa place.
        var bouton = menu.querySelector('summary');
        if (bouton) bouton.focus();
      });
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
    initLangues();
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
    // Les libelles ne paraissent qu'une fois le fil pose. Avant cela, un
    // premier calcul fait sur une mise en page encore mouvante pouvait les
    // laisser en haut de page, ou leur coussin s'imprimait en travers du
    // bandeau de tete.
    window.requestAnimationFrame(function () {
      place();
      rail.classList.add('est-pose');
    });
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
   Le voile de transition.
   La levee du voile est une animation CSS : elle se termine seule, meme si
   ce script ne s'execute jamais, et la page ne peut donc pas rester
   masquee. On n'ajoute ici que le depart : au clic sur un lien interne, le
   voile revient avant que la page suivante ne s'ouvre.

   Sous mouvement reduit, rien n'est intercepte : les liens fonctionnent
   comme des liens.
   ========================================================================== */

(function () {
  'use strict';

  var DUREE = 340;      // doit correspondre a la transition de .est-sortant
  var SECOURS = 2500;   // si la navigation n'aboutit pas, on releve le voile

  function initVoile() {
    var voile = document.querySelector('[data-voile]');
    if (!voile) return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    var parti = false;

    function interne(a) {
      if (!a || a.target || a.hasAttribute('download')) return null;
      var url;
      try { url = new URL(a.getAttribute('href'), window.location.href); }
      catch (err) { return null; }
      // Ni mailto:, ni tel:, ni un autre domaine.
      if (url.protocol !== 'http:' && url.protocol !== 'https:') return null;
      if (url.origin !== window.location.origin) return null;
      // Une ancre dans la page courante n'est pas un changement de page.
      if (url.pathname === window.location.pathname && url.hash) return null;
      if (url.href === window.location.href) return null;
      return url;
    }

    document.addEventListener('click', function (e) {
      if (parti || e.defaultPrevented) return;
      if (e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
      var url = interne(a);
      if (!url) return;

      e.preventDefault();
      parti = true;
      voile.classList.remove('est-pose');
      // Forcer un calcul : sans cela, le passage de l'animation a la
      // transition se ferait d'un coup, sans fondu.
      void voile.offsetWidth;
      voile.classList.add('est-sortant');
      window.setTimeout(function () { window.location.href = url.href; }, DUREE);
      window.setTimeout(function () {
        parti = false;
        voile.classList.remove('est-sortant');
        voile.classList.add('est-pose');
      }, SECOURS);
    });

    // Retour par le bouton precedent : la page revient du cache, le voile
    // doit se retirer.
    window.addEventListener('pageshow', function () {
      parti = false;
      voile.classList.remove('est-sortant');
      voile.classList.add('est-pose');
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initVoile);
  } else {
    initVoile();
  }
})();

/* ==========================================================================
   Le carrousel.
   La piste defile deja toute seule : c'est un conteneur a debordement
   horizontal avec accrochage, utilisable au doigt, a la molette et au
   clavier sans ce script. On n'ajoute ici que le confort : deux chevrons,
   un repere par carte, et on ne les montre que si la piste deborde
   vraiment. Les carrousels qui portent `data-defilement` avancent en plus
   tout seuls ; ceux-la recoivent une commande de pause visible et au
   clavier, et ne demarrent jamais en mouvement reduit.
   ========================================================================== */

(function () {
  'use strict';

  function initCarrousel(bloc) {
    var piste = bloc.querySelector('.carrousel__piste');
    var items = bloc.querySelectorAll('.carrousel__item');
    if (!piste || items.length < 2) return;

    var doux = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    var chevron = function (d) {
      return '<svg class="icon" width="16" height="16" viewBox="0 0 16 16" fill="none"'
           + ' aria-hidden="true" focusable="false"><path d="M' + (d < 0 ? '10 3L5 8l5 5' : '6 3l5 5-5 5')
           + '" stroke="currentColor" stroke-width="1.4" stroke-linecap="square"/></svg>';
    };

    var commandes = document.createElement('div');
    commandes.className = 'carrousel__commandes';

    var avant = document.createElement('button');
    avant.type = 'button';
    avant.className = 'pile__fleche carrousel__fleche';
    avant.innerHTML = chevron(-1) + '<span class="sr-only">Carte précédente</span>';

    var reperes = document.createElement('ul');
    reperes.className = 'pile__reperes';

    var apres = document.createElement('button');
    apres.type = 'button';
    apres.className = 'pile__fleche carrousel__fleche';
    apres.innerHTML = chevron(1) + '<span class="sr-only">Carte suivante</span>';

    var boutons = [];
    Array.prototype.forEach.call(items, function (item, i) {
      var li = document.createElement('li');
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'pile__repere';
      b.innerHTML = '<span class="sr-only">Carte ' + (i + 1) + ' sur ' + items.length + '</span>';
      b.addEventListener('click', function () { aller(i); });
      li.appendChild(b);
      reperes.appendChild(li);
      boutons.push(b);
    });

    commandes.appendChild(avant);
    commandes.appendChild(reperes);
    commandes.appendChild(apres);
    bloc.appendChild(commandes);

    function butee() { return piste.scrollWidth - piste.clientWidth; }

    // Position de repos d'une carte, ramenee dans la course reelle : les
    // dernieres cartes ne peuvent pas toutes venir se caler a gauche.
    function repos(i) {
      return Math.min(items[i].offsetLeft - piste.offsetLeft, butee());
    }

    function courant() {
      var g = piste.scrollLeft;
      var meilleur = 0;
      var ecart = Infinity;
      for (var k = 0; k < items.length; k++) {
        var d = Math.abs(repos(k) - g);
        // A egalite, la carte la plus avancee : en bout de course, plusieurs
        // cartes partagent la meme position de repos.
        if (d <= ecart) { ecart = d; meilleur = k; }
      }
      return meilleur;
    }

    function glisser(x) {
      try {
        piste.scrollTo({ left: x, behavior: doux ? 'smooth' : 'auto' });
      } catch (err) {
        piste.scrollLeft = x;
      }
    }

    function aller(i) {
      glisser(repos(Math.max(0, Math.min(items.length - 1, i))));
    }

    // Les chevrons avancent d'une carte, jamais d'un indice : en bout de
    // course, raisonner par indice bloquerait le retour en arriere.
    function pas() {
      var style = getComputedStyle(piste);
      var gouttiere = parseFloat(style.columnGap || style.gap) || 0;
      return items[0].getBoundingClientRect().width + gouttiere;
    }

    avant.addEventListener('click', function () {
      glisser(Math.max(0, piste.scrollLeft - pas()));
    });
    apres.addEventListener('click', function () {
      glisser(Math.min(butee(), piste.scrollLeft + pas()));
    });

    var attente = false;
    function etat() {
      attente = false;
      // Marge d'un pixel : les navigateurs arrondissent le defilement.
      var debut = piste.scrollLeft <= 1;
      var fin = piste.scrollLeft >= butee() - 1;
      avant.disabled = debut;
      apres.disabled = fin;
      bloc.classList.toggle('est-au-bout', fin);
      var c = courant();
      for (var k = 0; k < boutons.length; k++) {
        boutons[k].setAttribute('aria-current', String(k === c));
      }
      // Sans debordement, il n'y a rien a commander.
      commandes.hidden = piste.scrollWidth <= piste.clientWidth + 1;
    }
    function planifier() {
      if (attente) return;
      attente = true;
      window.requestAnimationFrame(etat);
    }

    // Des liens ailleurs dans la page peuvent viser une carte. Le saut natif
    // est peu fiable dans un conteneur defilant : quand la carte est deja
    // visible dans la piste, le navigateur ne fait rien du tout, pas meme
    // descendre la page. On mene donc le saut nous-memes.
    var entete = document.querySelector('.header');
    Array.prototype.forEach.call(items, function (item, i) {
      if (!item.id) return;
      var liens = document.querySelectorAll('a[href="#' + item.id + '"]');
      Array.prototype.forEach.call(liens, function (a) {
        a.addEventListener('click', function (e) {
          e.preventDefault();
          var marge = (entete ? entete.offsetHeight : 0) + 32;
          var y = window.pageYOffset + bloc.getBoundingClientRect().top - marge;
          try {
            window.scrollTo({ top: y, behavior: doux ? 'smooth' : 'auto' });
          } catch (err) {
            window.scrollTo(0, y);
          }
          aller(i);
          if (window.history && window.history.replaceState) {
            window.history.replaceState(null, '', '#' + item.id);
          }
        });
      });
    });

    // ---------------------------------------- defilement automatique
    // Seuls les carrousels qui portent `data-defilement` avancent seuls.
    // Rien ne demarre en mouvement reduit. Comme toute animation en boucle
    // du site, celle-ci recoit une commande d'arret visible et atteignable
    // au clavier ; elle s'interrompt aussi au survol, au focus, quand le
    // bloc sort de l'ecran et quand l'onglet passe a l'arriere-plan.
    if (doux && bloc.hasAttribute('data-defilement')) {
      var delai = parseInt(bloc.getAttribute('data-defilement'), 10) || 7000;
      var arrete = false;
      var survole = false;
      var focalise = false;
      var visible = true;
      var minuteur = null;

      var pause = document.createElement('button');
      pause.type = 'button';
      pause.className = 'pile__fleche carrousel__pause';
      pause.setAttribute('aria-pressed', 'false');

      var dessinPause = '<svg class="icon" width="14" height="14" viewBox="0 0 12 12"'
        + ' fill="none" aria-hidden="true" focusable="false"><path d="M4 2v8M8 2v8"'
        + ' stroke="currentColor" stroke-width="1.4" stroke-linecap="square"/></svg>';
      var dessinLecture = '<svg class="icon" width="14" height="14" viewBox="0 0 12 12"'
        + ' aria-hidden="true" focusable="false"><path d="M3.5 2 10 6l-6.5 4Z"'
        + ' fill="currentColor"/></svg>';

      function habiller() {
        pause.innerHTML = (arrete ? dessinLecture : dessinPause)
          + '<span class="sr-only">'
          + (arrete ? 'Reprendre le défilement' : 'Mettre le défilement en pause')
          + '</span>';
        pause.setAttribute('aria-pressed', String(arrete));
      }
      habiller();
      commandes.appendChild(pause);

      function peutTourner() {
        return !arrete && !survole && !focalise && visible && !document.hidden
          && piste.scrollWidth > piste.clientWidth + 1;
      }

      function tic() {
        if (!peutTourner()) return;
        // Arrive au bout, le carrousel revient a la premiere carte.
        if (piste.scrollLeft >= butee() - 1) glisser(0);
        else glisser(Math.min(butee(), piste.scrollLeft + pas()));
      }

      function relancer() {
        window.clearInterval(minuteur);
        minuteur = window.setInterval(tic, delai);
      }
      relancer();

      pause.addEventListener('click', function () {
        arrete = !arrete;
        habiller();
        if (!arrete) relancer();
      });

      // Survol et focus retiennent le defilement quand ils sont dans la
      // piste, la ou l'on lit. Pas sur les commandes : la touche
      // « Reprendre » garde le pointeur et le focus apres le clic, et le
      // defilement ne repartirait jamais.
      piste.addEventListener('mouseenter', function () { survole = true; });
      piste.addEventListener('mouseleave', function () { survole = false; });
      piste.addEventListener('focusin', function () { focalise = true; });
      piste.addEventListener('focusout', function () { focalise = false; });

      // Une action de la personne repart d'un delai complet. On n'ecoute que
      // les gestes reels : notre propre defilement declenche lui aussi des
      // evenements `scroll`, et remettrait le compteur a zero sans fin.
      ['pointerdown', 'wheel', 'touchstart', 'keydown'].forEach(function (nom) {
        bloc.addEventListener(nom, relancer, { passive: true });
      });

      document.addEventListener('visibilitychange', function () {
        if (!document.hidden && !arrete) relancer();
      });

      if (window.IntersectionObserver) {
        new IntersectionObserver(function (entrees) {
          visible = entrees[0].isIntersecting;
        }, { threshold: 0.35 }).observe(bloc);
      }
    }

    piste.addEventListener('scroll', planifier, { passive: true });
    window.addEventListener('resize', planifier);
    // La piste peut etre mesuree alors qu'elle est encore masquee : sa
    // largeur vaut alors zero, et les commandes se cacheraient pour de bon.
    // On la surveille : des qu'elle prend une taille, l'etat est refait.
    if (window.ResizeObserver) {
      new ResizeObserver(planifier).observe(piste);
    }
    etat();
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(etat);
  }

  function tout() {
    var blocs = document.querySelectorAll('[data-carrousel]');
    Array.prototype.forEach.call(blocs, function (b) { initCarrousel(b); });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', tout);
  } else {
    tout();
  }
})();

/* ==========================================================================
   Le formulaire de contact.
   Il occupe sa propre page, `formulaire.html` : dans une fenetre il etait a
   l'etroit, et une fenetre ne se partage pas par un lien.

   A l'envoi, il est poste sur `/api/contact`, la seule fonction serveur du
   site : les pages n'appellent donc aucun domaine tiers. Si cette fonction
   ne repond pas, la saisie n'est pas perdue — un lien reprend le message
   dans la messagerie du visiteur.

   Sans JavaScript, le formulaire part en envoi classique et la page revient
   avec le resultat en parametre : il reste utilisable tel quel.
   ========================================================================== */

(function () {
  'use strict';

  function initFormulaire() {
    var form = document.querySelector('[data-form]');
    if (!form) return;

    var etat = form.querySelector('[data-form-etat]');
    var bouton = form.querySelector('button[type="submit"]');
    var libelle = bouton ? bouton.querySelector('span') : null;
    var libelleInitial = libelle ? libelle.textContent : '';

    // L'heure a laquelle le formulaire a ete pose. La fonction serveur s'en
    // sert pour ecarter les envois instantanes, qui ne viennent pas d'une
    // personne. Sans script, le champ reste vide et le controle est ignore.
    var pose = form.querySelector('[data-pose]');
    if (pose) pose.value = String(Math.floor(Date.now() / 1000));

    // ------------------------------------------ signalement des champs
    // Sans ce script, le navigateur affiche ses propres bulles et le
    // formulaire part en POST classique : il reste utilisable tel quel.
    var ALERTE = '<svg class="icon" width="14" height="14" viewBox="0 0 16 16" fill="none"'
      + ' aria-hidden="true" focusable="false"><circle cx="8" cy="8" r="6.4" stroke="currentColor"'
      + ' stroke-width="1.2"/><path d="M8 4.6v4.2M8 11.1v.9" stroke="currentColor"'
      + ' stroke-width="1.4" stroke-linecap="square"/></svg>';

    function boite(champ) {
      var id = champ.getAttribute('aria-describedby');
      return id ? document.getElementById(id) : null;
    }

    function motif(champ) {
      var v = champ.validity;
      if (!v) return '';
      if (v.valueMissing) return champ.getAttribute('data-manque') || 'Ce champ est nécessaire.';
      // « Un peu court » ne disait pas combien il manque : on voyait un champ
      // rempli et un formulaire declare incomplet, sans comprendre pourquoi.
      // Le compte, lui, se comprend sans explication.
      if (v.tooShort) {
        var mini = parseInt(champ.getAttribute('minlength'), 10) || 0;
        var reste = mini - champ.value.length;
        if (reste > 0) {
          return 'Encore ' + reste + ' caractère' + (reste > 1 ? 's' : '')
            + ' : une phrase entière nous suffit.';
        }
        return champ.getAttribute('data-court') || 'Ce texte est un peu court.';
      }
      // `typeMismatch` vient du type du champ, `patternMismatch` du motif
      // qu'on lui a donne : les deux disent la meme chose au lecteur.
      if (v.typeMismatch || v.patternMismatch) {
        return champ.getAttribute('data-format') || 'Ce format ne semble pas valide.';
      }
      return champ.validationMessage || '';
    }

    function signaler(champ, montrer) {
      var zone = boite(champ);
      var enveloppe = champ.closest ? champ.closest('.field') : null;
      var faux = montrer && champ.checkValidity && !champ.checkValidity();
      if (enveloppe) enveloppe.classList.toggle('est-fautif', !!faux);
      champ.setAttribute('aria-invalid', faux ? 'true' : 'false');
      if (!zone) return faux;
      if (faux) {
        zone.innerHTML = ALERTE + '<span>' + motif(champ) + '</span>';
        zone.hidden = false;
      } else {
        zone.hidden = true;
        zone.textContent = '';
      }
      return faux;
    }

    var champs = form.querySelectorAll('input, select, textarea');
    form.setAttribute('novalidate', 'novalidate');
    Array.prototype.forEach.call(champs, function (champ) {
      champ.addEventListener('blur', function () { signaler(champ, true); });
      function siFautif() {
        var enveloppe = champ.closest ? champ.closest('.field') : null;
        if (enveloppe && enveloppe.classList.contains('est-fautif')) signaler(champ, true);
      }
      champ.addEventListener('input', siFautif);
      champ.addEventListener('change', siFautif);
    });

    // Adresse de repli : elle est lue sur le formulaire, pour qu'une seule
    // source la porte.
    var ADRESSE = form.getAttribute('data-courriel') || 'contact@amelie-invest.com';

    // Si l'envoi echoue — fonction serveur absente, panne, coupure — rien de
    // ce qui a ete ecrit n'est perdu : on propose un lien qui reprend la
    // saisie dans la messagerie du visiteur.
    function lienDeSecours() {
      function v(nom) {
        var c = form.querySelector('[name="' + nom + '"]');
        return c ? String(c.value || '').trim() : '';
      }
      var tel = v('telephone') ? (v('indicatif') + ' ' + v('telephone')).trim() : 'non communiqué';
      var corps = [
        'Prénom : ' + v('prenom'),
        'Nom : ' + v('nom'),
        'Adresse e-mail : ' + v('courriel'),
        'Téléphone : ' + tel,
        'Vous êtes : ' + v('qualite'),
        'Où j’en suis : ' + v('profil'),
        '',
        'Message :',
        v('message')
      ].join('\n');
      var lien = document.createElement('a');
      lien.className = 'form__secours';
      lien.href = 'mailto:' + ADRESSE
        + '?subject=' + encodeURIComponent('Formulaire de contact · ' + v('prenom') + ' ' + v('nom'))
        + '&body=' + encodeURIComponent(corps);
      lien.textContent = 'Envoyer ce message par votre messagerie';
      return lien;
    }

    // ------------------------------------------ la confirmation d'envoi
    // Une fenetre s'ouvre quand le message est parti. Elle ne remplace pas
    // le message en clair sous le bouton : elle s'ajoute. Sans JavaScript,
    // ou si le navigateur ne sait pas ouvrir de fenetre modale, seul le
    // message reste — et il dit la meme chose.
    var recu = document.querySelector('[data-recu]');
    var recuFermer = recu ? recu.querySelector('[data-recu-fermer]') : null;
    var rendu = null;   // a qui rendre le focus en refermant

    function annoncerRecu() {
      if (!recu || typeof recu.showModal !== 'function') return;
      rendu = document.activeElement;
      recu.showModal();
      // Le navigateur donne le focus au premier element atteignable, ici le
      // bouton de reservation : il s'affiche enfonce, et une touche Entree
      // ouvrirait Calendly sans qu'on l'ait demande. On le pose donc sur le
      // cadre, d'ou la lecture commence proprement.
      var cadre = recu.querySelector('[data-recu-cadre]');
      if (cadre && typeof cadre.focus === 'function') cadre.focus();
    }

    if (recu) {
      if (recuFermer) {
        recuFermer.addEventListener('click', function () { recu.close(); });
      }
      // Clic dans le fond, hors du cadre : la fenetre se referme.
      recu.addEventListener('click', function (e) {
        if (e.target === recu) recu.close();
      });
      // La touche d'echappement est geree par le navigateur ; on se contente
      // de rendre le focus a l'endroit d'ou l'on venait.
      recu.addEventListener('close', function () {
        if (rendu && typeof rendu.focus === 'function') rendu.focus();
        rendu = null;
      });
    }

    function dire(message, reussi, secours) {
      if (!etat) return;
      etat.textContent = message;
      if (secours) {
        etat.appendChild(document.createTextNode(' '));
        etat.appendChild(lienDeSecours());
      }
      etat.hidden = false;
      etat.classList.toggle('form__etat--ok', !!reussi);
      etat.classList.toggle('form__etat--ko', !reussi);
    }

    // ------------------------------------------------------- l'envoi
    form.addEventListener('submit', function (e) {
      var premier = null;
      Array.prototype.forEach.call(champs, function (champ) {
        if (signaler(champ, true) && !premier) premier = champ;
      });
      if (premier) {
        e.preventDefault();
        premier.focus();
        dire('Le formulaire n’est pas complet. Les champs signalés attendent une réponse.', false);
        return;
      }

      // `fetch` absent : on laisse le navigateur poster le formulaire, et
      // la page revient avec le resultat en parametre.
      if (typeof window.fetch !== 'function') return;

      e.preventDefault();
      if (bouton) bouton.disabled = true;
      if (libelle) libelle.textContent = 'Envoi en cours…';
      dire('Envoi en cours…', true);

      // Le corps part en `application/x-www-form-urlencoded`, comme le ferait
      // le navigateur sans JavaScript. Un `FormData` partirait en
      // `multipart/form-data`, que l'hebergeur ne decoupe pas : la fonction
      // recevait alors un corps qu'elle ne savait pas lire, et repondait que
      // tous les champs manquaient alors que le formulaire etait rempli.
      var donnees = new URLSearchParams();
      Array.prototype.forEach.call(form.elements, function (el) {
        if (!el.name || el.disabled) return;
        if ((el.type === 'checkbox' || el.type === 'radio') && !el.checked) return;
        if (el.type === 'submit' || el.type === 'button') return;
        donnees.append(el.name, el.value);
      });

      fetch(form.getAttribute('action'), {
        method: 'POST',
        body: donnees.toString(),
        headers: {
          'Accept': 'application/json',
          'X-Requested-With': 'fetch',
          'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
      }).then(function (r) {
        return r.json().catch(function () { return { ok: r.ok, message: '' }; });
      }).then(function (d) {
        if (d && d.ok) {
          form.reset();
          if (pose) pose.value = String(Math.floor(Date.now() / 1000));
          dire(d.message || 'Message envoyé. Nous répondons sous un jour ouvré.', true);
          annoncerRecu();
        } else {
          dire((d && d.message) || 'L’envoi a échoué. Réessayez dans un moment,'
            + ' ou écrivez-nous directement à ' + ADRESSE + '.', false, true);
        }
      }).catch(function () {
        dire('L’envoi a échoué. Vérifiez votre connexion, puis réessayez,'
          + ' ou écrivez-nous directement à ' + ADRESSE + '.', false, true);
      }).then(function () {
        if (bouton) bouton.disabled = false;
        if (libelle) libelle.textContent = libelleInitial;
      });
    });

    // ------------------------------------------- le compte de caracteres
    // Il suit la saisie du message, et dit ce qui manque tant que le
    // minimum n'est pas atteint. Sans JavaScript il n'apparait pas : la
    // mention « de 20 a 5 000 caracteres » sous l'etiquette suffit alors.
    var compte = form.querySelector('[data-compte]');
    var champCompte = compte ? document.getElementById('message') : null;

    if (compte && champCompte) {
      var mini = parseInt(champCompte.getAttribute('minlength'), 10) || 0;
      var maxi = parseInt(champCompte.getAttribute('maxlength'), 10) || 0;

      var direCompte = function () {
        var n = champCompte.value.length;
        if (!n) { compte.hidden = true; return; }
        compte.hidden = false;
        var court = n < mini;
        compte.textContent = court
          ? 'Encore ' + (mini - n) + ' caractère' + (mini - n > 1 ? 's' : '')
          : n + ' / ' + maxi + ' caractères';
        compte.classList.toggle('field__compte--court', court);
      };

      champCompte.addEventListener('input', direCompte);
      // La page peut revenir avec un message deja pose — un sujet venu d'une
      // ressource, ou un retour de navigation.
      window.setTimeout(direCompte, 0);
    }

    // ------------------------------- une demande venue d'une ressource
    // Les feuillets « en preparation » mènent ici avec `?sujet=`. Le texte
    // pose dans le message ne vient jamais de l'adresse : il est choisi dans
    // cette table. Recopier ce que porte l'URL, meme echappe, ouvrirait la
    // porte a un message ecrit par un tiers et attribue au visiteur.
    var SUJETS = {
      financer: 'Je souhaite être prévenu de la parution de la ressource sur le '
        + 'financement, et j’aimerais en savoir plus sur ce sujet.',
      acheter: 'Je souhaite être prévenu de la parution de la ressource sur la '
        + 'préparation d’une offre, et j’aimerais en savoir plus sur ce sujet.',
      arbitrer: 'Je souhaite être prévenu de la parution de la ressource sur '
        + 'l’arbitrage, et j’aimerais en savoir plus sur ce sujet.'
    };

    var champMessage = form.querySelector('#message');
    var sujet = new URLSearchParams(window.location.search).get('sujet');
    if (champMessage && sujet && Object.prototype.hasOwnProperty.call(SUJETS, sujet)
        && !champMessage.value) {
      champMessage.value = SUJETS[sujet];
    }

    // Retour d'un envoi sans JavaScript : la page revient avec `?envoi=`.
    var params = new URLSearchParams(window.location.search);
    if (params.get('envoi') === 'ok') {
      dire('Message envoyé. Nous répondons sous un jour ouvré.', true);
      annoncerRecu();
    } else if (params.get('envoi') === 'erreur') {
      dire('L’envoi a échoué. Réessayez dans un moment, ou écrivez-nous'
        + ' directement à ' + ADRESSE + '.', false, true);
    }
  }

  function demarrer() { initFormulaire(); }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', demarrer);
  } else {
    demarrer();
  }
})();

/* ==========================================================================
   Les accompagnements, en diapositives.
   Les quatre formats d'intervention passent l'un apres l'autre. Sans ce
   script, ils se suivent simplement dans la page, tous lisibles : le
   defilement est un confort, jamais une condition d'acces. Rien ne defile
   tout seul, il n'y a donc rien a mettre en pause.

   Les diapositives sont superposees en grille : le bloc prend la hauteur de
   la plus longue et ne saute plus d'un format a l'autre, sans qu'aucune
   mesure soit necessaire.
   ========================================================================== */

(function () {
  'use strict';

  function initDiapos() {
    var bloc = document.querySelector('[data-diapos]');
    if (!bloc) return;

    var diapos = bloc.querySelectorAll('[data-diapo]');
    if (diapos.length < 2) return;

    var doux = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var courant = 0;

    var chevron = function (d) {
      return '<svg class="icon" width="16" height="16" viewBox="0 0 16 16" fill="none"'
           + ' aria-hidden="true" focusable="false"><path d="M' + (d < 0 ? '10 3L5 8l5 5' : '6 3l5 5-5 5')
           + '" stroke="currentColor" stroke-width="1.4" stroke-linecap="square"/></svg>';
    };

    // --- La barre nommee : elle annonce les quatre formats.
    var barre = document.createElement('div');
    barre.className = 'diapos__barre';
    var reperes = [];
    Array.prototype.forEach.call(diapos, function (d, i) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'diapos__repere';
      b.innerHTML = '<span class="diapos__nom"></span>'
                  + '<span class="diapos__rang"></span>';
      b.querySelector('.diapos__nom').textContent = d.getAttribute('data-diapo-nom') || ('Format ' + (i + 1));
      b.querySelector('.diapos__rang').textContent = ('0' + (i + 1)).slice(-2) + ' / ' + ('0' + diapos.length).slice(-2);
      b.addEventListener('click', function () { montrer(i); });
      barre.appendChild(b);
      reperes.push(b);
    });

    // --- Les deux chevrons.
    var commandes = document.createElement('div');
    commandes.className = 'diapos__commandes';
    var avant = document.createElement('button');
    avant.type = 'button';
    avant.className = 'pile__fleche';
    avant.innerHTML = chevron(-1) + '<span class="sr-only">Accompagnement précédent</span>';
    var apres = document.createElement('button');
    apres.type = 'button';
    apres.className = 'pile__fleche';
    apres.innerHTML = chevron(1) + '<span class="sr-only">Accompagnement suivant</span>';
    var rangs = document.createElement('span');
    rangs.className = 'diapos__rangs';
    commandes.appendChild(avant);
    commandes.appendChild(apres);
    commandes.appendChild(rangs);

    bloc.appendChild(barre);
    bloc.appendChild(commandes);

    function montrer(i) {
      var vise = (i + diapos.length) % diapos.length;
      // Le sens de lecture : en avancant, le format entre par la droite ;
      // en revenant, par la gauche. Le passage d'un bout a l'autre garde le
      // sens du geste. La CSS s'en sert, le contenu n'en depend pas.
      var sens = vise === courant ? 1 : (vise > courant ? 1 : -1);
      if (courant === 0 && vise === diapos.length - 1) sens = -1;
      if (courant === diapos.length - 1 && vise === 0) sens = 1;
      courant = vise;
      // Le format entrant doit d'abord se poser du bon cote, sans animation :
      // le transform est une propriete en transition, et le changer
      // l'enverrait glisser d'un bord a l'autre alors qu'il est encore
      // invisible. On coupe donc la transition, on force le calcul de la
      // mise en page, puis on la rend.
      var entrant = diapos[courant];
      entrant.classList.add('sans-glissement');
      for (var k = 0; k < diapos.length; k++) {
        diapos[k].style.setProperty('--diapo-sens', String(k === courant ? sens : -sens));
      }
      void entrant.offsetWidth;
      entrant.classList.remove('sans-glissement');
      for (var k = 0; k < diapos.length; k++) {
        diapos[k].classList.toggle('est-visible', k === courant);
        reperes[k].setAttribute('aria-current', String(k === courant));
      }
      rangs.textContent = ('0' + (courant + 1)).slice(-2) + ' / ' + ('0' + diapos.length).slice(-2);
    }

    avant.addEventListener('click', function () { montrer(courant - 1); });
    apres.addEventListener('click', function () { montrer(courant + 1); });

    bloc.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (!d) return;
      e.preventDefault();
      montrer(courant + d);
    });

    // Un lien ailleurs dans la page peut viser un format : on l'amene.
    var entete = document.querySelector('.header');
    Array.prototype.forEach.call(diapos, function (d, i) {
      if (!d.id) return;
      var liens = document.querySelectorAll('a[href="#' + d.id + '"]');
      Array.prototype.forEach.call(liens, function (a) {
        a.addEventListener('click', function (e) {
          e.preventDefault();
          montrer(i);
          var marge = (entete ? entete.offsetHeight : 0) + 32;
          var y = window.pageYOffset + bloc.getBoundingClientRect().top - marge;
          try {
            window.scrollTo({ top: y, behavior: doux ? 'smooth' : 'auto' });
          } catch (err) {
            window.scrollTo(0, y);
          }
        });
      });
    });

    bloc.classList.add('est-defilante');
    montrer(0);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDiapos);
  } else {
    initDiapos();
  }
})();

/* ==========================================================================
   L'ecriture au survol.
   Une phrase se reecrit quand le curseur la traverse : chaque mot est
   devoile de gauche a droite, avec un decalage, si bien que le regard suit
   une plume plutot qu'un fondu.

   Le texte est ecrit en clair dans la page : ce script ne fait que
   l'entourer mot a mot. Sans JavaScript, il ne se passe rien et la phrase
   se lit telle quelle. Sous mouvement reduit, l'effet ne s'arme pas.
   ========================================================================== */

(function () {
  'use strict';

  var reduit = window.matchMedia('(prefers-reduced-motion: reduce)');

  /* Chaque mot recoit son enveloppe. Les espaces restent des noeuds de
     texte : le retour a la ligne se fait donc comme avant, et la mesure ne
     bouge pas d'un pixel. On ne coupe que sur l'espace ordinaire, pour que
     l'espace insecable garde le guillemet colle a son mot. */
  function decouper(bloc) {
    var marcheur = document.createTreeWalker(bloc, NodeFilter.SHOW_TEXT, null, false);
    var noeuds = [];
    while (marcheur.nextNode()) noeuds.push(marcheur.currentNode);

    var mots = [];
    noeuds.forEach(function (noeud) {
      if (!noeud.nodeValue || !noeud.nodeValue.trim()) return;
      var lot = document.createDocumentFragment();
      noeud.nodeValue.split(/( +)/).forEach(function (bout) {
        if (bout === '') return;
        if (/^ +$/.test(bout)) {
          lot.appendChild(document.createTextNode(bout));
          return;
        }
        var mot = document.createElement('span');
        mot.className = 'ecrit__mot';
        mot.textContent = bout;
        lot.appendChild(mot);
        mots.push(mot);
      });
      noeud.parentNode.replaceChild(lot, noeud);
    });
    return mots;
  }

  function armer(bloc) {
    var mots = decouper(bloc);
    if (!mots.length) return;

    var enCours = false;
    // La plume traverse la phrase en deux secondes et demie environ, quelle
    // que soit sa longueur : une citation courte ne doit pas paraitre plus
    // lente qu'une longue. Chaque mot, lui, se decouvre posement.
    var pas = Math.max(70, Math.min(190, 2500 / mots.length));
    var glisse = 620;

    function ecrire() {
      if (enCours || reduit.matches) return;
      enCours = true;

      mots.forEach(function (mot) {
        mot.style.transition = 'none';
        mot.style.clipPath = 'inset(0 100% -25% 0)';
      });
      // Une mesure force le navigateur a prendre acte de l'etat ferme avant
      // qu'on ne l'ouvre : sans elle, les deux ecritures sont fondues en une
      // seule et il n'y a rien a animer.
      void bloc.offsetWidth;

      mots.forEach(function (mot, i) {
        mot.style.transition = 'clip-path ' + glisse + 'ms cubic-bezier(.22,.61,.36,1) '
          + Math.round(i * pas) + 'ms';
        mot.style.clipPath = 'inset(0 0 -25% 0)';
      });

      window.setTimeout(function () {
        mots.forEach(function (mot) {
          mot.style.transition = '';
          mot.style.clipPath = '';
        });
        enCours = false;
      }, mots.length * pas + glisse + 120);
    }

    bloc.addEventListener('mouseenter', ecrire);
    // Au clavier : la phrase se reecrit quand le bloc, ou ce qu'il contient,
    // recoit le focus.
    bloc.addEventListener('focusin', ecrire);
  }

  function initEcriture() {
    var blocs = document.querySelectorAll('[data-ecriture]');
    if (!blocs.length) return;
    // `clip-path` avec `inset()` : sans lui, on ne touche a rien.
    if (!window.CSS || !CSS.supports || !CSS.supports('clip-path', 'inset(0 100% 0 0)')) return;
    Array.prototype.forEach.call(blocs, armer);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initEcriture);
  } else {
    initEcriture();
  }
})();
