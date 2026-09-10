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
   vraiment. Rien ne defile tout seul, il n'y a rien a mettre en pause.
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
   Le formulaire de contact, en fenetre.
   Le formulaire est ecrit dans un `dialog` ouvert : sans JavaScript il
   s'affiche donc simplement dans la page, utilisable tel quel. Le script le
   referme au chargement et le rouvre en fenetre modale au clic sur le
   bouton, avec fermeture par la croix, par la touche d'echappement et par
   un clic hors du cadre.

   A l'envoi, le message est compose dans la messagerie du visiteur : le
   site est statique et n'appelle aucun domaine tiers. Rien ne part sans sa
   validation, et aucune donnee saisie ne transite par ce site.
   ========================================================================== */

(function () {
  'use strict';

  function initFenetre() {
    var fenetre = document.querySelector('[data-modale]');
    if (!fenetre || typeof fenetre.showModal !== 'function') return;

    var ouvrir = document.querySelector('[data-modale-ouvrir]');
    var fermer = fenetre.querySelector('[data-modale-fermer]');
    if (!ouvrir) return;

    fenetre.close();
    ouvrir.hidden = false;

    ouvrir.addEventListener('click', function () { fenetre.showModal(); });
    if (fermer) fermer.addEventListener('click', function () { fenetre.close(); });

    // Clic dans le fond, hors du cadre : la fenetre se referme.
    fenetre.addEventListener('click', function (e) {
      if (e.target !== fenetre) return;
      var r = fenetre.getBoundingClientRect();
      var dedans = e.clientX >= r.left && e.clientX <= r.right
                && e.clientY >= r.top && e.clientY <= r.bottom;
      if (!dedans) fenetre.close();
    });
  }

  function initFormulaire() {
    var form = document.querySelector('[data-form-mail]');
    if (!form) return;

    var action = form.getAttribute('action') || '';
    var adresse = action.replace(/^mailto:/, '').split('?')[0];
    if (!adresse) return;

    function valeur(nom) {
      var champ = form.elements[nom];
      return champ ? String(champ.value || '').trim() : '';
    }

    form.addEventListener('submit', function (e) {
      // Laisser le navigateur signaler lui-meme les champs incomplets.
      if (form.checkValidity && !form.checkValidity()) return;
      e.preventDefault();

      var nom = valeur('nom');
      var corps = [
        'Nom : ' + nom,
        'Adresse e-mail : ' + valeur('courriel'),
        'Téléphone : ' + (valeur('telephone') || 'non communiqué'),
        'Où j’en suis : ' + valeur('profil'),
        '',
        valeur('message'),
        '',
        'Message préparé depuis le formulaire de contact d’amelie-invest.com.'
      ].join('\r\n');

      var sujet = 'Premier échange' + (nom ? ' · ' + nom : '');
      var lien = document.createElement('a');
      lien.href = 'mailto:' + adresse
        + '?subject=' + encodeURIComponent(sujet)
        + '&body=' + encodeURIComponent(corps);
      // Un lien clique passe partout : certains navigateurs refusent une
      // affectation directe d'adresse vers un protocole externe.
      lien.style.display = 'none';
      document.body.appendChild(lien);
      lien.click();
      document.body.removeChild(lien);
    });
  }

  function demarrer() { initFenetre(); initFormulaire(); }

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
      courant = (i + diapos.length) % diapos.length;
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
