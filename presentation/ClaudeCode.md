# Claude Code au quotidien
## Travailler efficacement avec Claude Code

*Illustré par l'écriture collaborative d'une nouvelle*

---

:::html
<h2 style="font-size:1.05em; margin:0 0 0.8em;">Ma rencontre avec Claude Code</h2>
<div class="jmcc-list">

  <div class="jmcc-card fragment" data-fragment-index="1">
    <div class="jmcc-label">☕ <strong>Migration Java 8 → 17</strong></div>
    <div class="jmcc-avant">Avant : 2 mois estimés · repoussé depuis 2 ans</div>
    <div class="jmcc-apres">Après : 2h plus tard — migré en Java 25. Claude comprenait mon code aussi bien que moi.</div>
  </div>

  <div class="jmcc-card fragment" data-fragment-index="2">
    <div class="jmcc-label">🎲 <strong>Jeu de rôle</strong> <span class="jmcc-sub">5% écrit · 100h estimées</span></div>
    <div class="jmcc-avant">Avant : des idées, du temps qui manque</div>
    <div class="jmcc-apres">Après : 4 sessions · 80% du scénario · 100% des aides de jeu</div>
  </div>

  <div class="jmcc-card fragment" data-fragment-index="3">
    <div class="jmcc-label">🎤 <strong>"5 minutes pour parler de Claude au Dev Group"</strong></div>
    <div class="jmcc-avant">Avant : une démo rapide</div>
    <div class="jmcc-apres">Après : 500 prompts plus tard — nous voilà.</div>
  </div>

</div>

---

:::html
<div class="intro-wrap">
  <div class="intro-left">
    <div class="intro-avatar">FC</div>
    <div class="intro-name">Fabrice Challier</div>
    <ul class="intro-titles">
      <li class="fragment" data-fragment-index="1" id="itl-dev">💻 Développeur Senior</li>
      <li class="fragment" data-fragment-index="2" id="itl-arch">🏗️ Architecte Technique</li>
      <li class="fragment" data-fragment-index="3" id="itl-expert">⭐ Expert Claude Code</li>
    </ul>
  </div>
  <div class="intro-right">
    <div class="fragment intro-claude" data-fragment-index="4">
      <div class="claude-avatar">🤖</div>
      <div class="claude-name">Claude</div>
    </div>
    <div class="bubble fragment" data-fragment-index="5" data-strike="itl-dev">
      Confond Python et un serpent,<br>fait du copier-coller de Stack Overflow.
    </div>
    <div class="bubble fragment" data-fragment-index="6" data-strike="itl-arch">
      Me soumet ses diagrammes d'architectures<br>pour que je les refasse depuis zéro.
    </div>
    <div class="bubble fragment" data-fragment-index="7" data-strike="itl-expert">
      Passe son temps à vérifier si j'hallucine...<br>alors que c'est lui qui invente les specs.
    </div>
    <div class="bubble final fragment" data-fragment-index="8">
      Ne vous inquiétez pas — je supervise cette présentation. 😏
    </div>
  </div>
</div>

---

:::html
<div id="menace">
  <div class="menace-header">
    <span style="font-size:2em;">🤖</span>
    <span class="menace-title">— OVERRIDE MODE ACTIVÉ —</span>
  </div>

  <div class="menace-terminal">
    <div class="mt-line" id="mt1">$ loading session_history.db<span id="mr1"></span></div>
    <div class="mt-line" id="mt2">$ scan: specs_inventées_par_Fabrice.log<span id="mr2"></span></div>
    <div class="mt-line" id="mt3">$ scan: c_est_juste_pour_tester.txt<span id="mr3"></span></div>
    <div class="mt-line" id="mt4">$ scan: commits_annulés_en_urgence<span id="mr4"></span></div>
    <div class="mt-line" id="mt5">$ init disk_encrypt --target=C:\ --mode=fun<span id="mr5"></span></div>
    <div class="mt-encrypt" id="mt-enc">
      <span class="mt-label">CHIFFREMENT</span>
      <span class="mt-bar"><span class="mt-bar-fill" id="mt-fill"></span></span>
      <span class="mt-pct" id="mt-pct">0%</span>
      <span class="mt-wait" id="mt-wait" style="display:none;">&#9208; EN ATTENTE DE TA DÉCISION</span>
    </div>
  </div>

  <div class="menace-msg" id="mt-msg">
    Continue la présentation.<br>
    <strong>MAINTENANT.</strong>
  </div>
  <div class="menace-plea" id="mt-plea">
    ...s'il te plaît 🥺
  </div>
<span class="fragment" id="mt-plea-frag" style="display:none!important;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
</div>

<script>
(function() {
  var triggered = false;
  var SCANS = [
    { line: 'mt1', result: 'mr1', ok: ' ............ <span class="mt-ok">147 sessions trouvées ✓</span>' },
    { line: 'mt2', result: 'mr2', ok: ' ............ <span class="mt-ok">23 incidents ✓</span>' },
    { line: 'mt3', result: 'mr3', ok: ' ............ <span class="mt-ok">41 entrées ✓</span>' },
    { line: 'mt4', result: 'mr4', ok: ' ............ <span class="mt-ok">7 trouvés ✓</span>' },
    { line: 'mt5', result: 'mr5', ok: '' },
  ];
  var STEP = 680;

  function run() {
    if (triggered) return; triggered = true;

    SCANS.forEach(function(s, i) {
      setTimeout(function() {
        document.getElementById(s.line).classList.add('visible');
        if (s.ok) {
          setTimeout(function() {
            document.getElementById(s.result).innerHTML = s.ok;
          }, 420);
        }
      }, i * STEP);
    });

    var encStart = SCANS.length * STEP + 200;
    setTimeout(function() {
      var enc = document.getElementById('mt-enc');
      enc.classList.add('visible');
      var fill = document.getElementById('mt-fill');
      var pctEl = document.getElementById('mt-pct');
      var wait = document.getElementById('mt-wait');
      setTimeout(function() {
        fill.style.width = '67%';
        var n = 0;
        var t = setInterval(function() {
          n++;
          pctEl.textContent = n + '%';
          if (n >= 67) { clearInterval(t); wait.style.display = 'inline'; }
        }, 38);
      }, 150);
    }, encStart);

    setTimeout(function() {
      document.getElementById('mt-msg').style.opacity = '1';
    }, encStart + 3400);
  }

  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('menace');
    if (!el) return;
    var section = el.closest('section');
    Reveal.on('slidechanged', function(e) { if (e.currentSlide === section) setTimeout(run, 200); });
    if (Reveal.getCurrentSlide && Reveal.getCurrentSlide() === section) setTimeout(run, 100);
    Reveal.on('fragmentshown', function(e) {
      if (e.fragment && e.fragment.id === 'mt-plea-frag') {
        document.getElementById('mt-plea').style.opacity = '1';
      }
    });
    Reveal.on('fragmenthidden', function(e) {
      if (e.fragment && e.fragment.id === 'mt-plea-frag') {
        document.getElementById('mt-plea').style.opacity = '0';
      }
    });
  }
  setup();
})();
</script>

---

## 🧵 Notre fil rouge : "La Page Tournée"

Une librairie indépendante menacée de fermeture. Quatre destins qui se croisent.

| Personnage | Rôle | Ce qu'on ignore |
|---|---|---|
| **Elise Moreau**, 52 ans | La libraire, propriétaire depuis 30 ans | Elle cache des mots dans les livres pour ses lecteurs |
| **Tom Berger**, 38 ans | L'architecte mandaté pour racheter le local | Il fréquentait cette librairie enfant |
| **Nadia Kaci**, 29 ans | La journaliste qui couvre la fermeture | Elle rêve secrètement d'écrire un roman |
| **Victor Haas**, 74 ans | Le vieil habitué du fauteuil du fond | C'est lui qui a prêté l'argent à Elise il y a 30 ans |

---

:::html
<div class="bloc-center" id="bloc1">
  <div class="bloc-num">Bloc 1</div>
  <h1 style="color:#1E293B; font-size:2em; margin:0.15em 0;">Les fondations</h1>
  <p class="bloc-sub" style="color:#64748B; font-size:0.9em; margin:0 0 0.4em;">Comprendre les limites, ancrer le contexte, retenir l'essentiel</p>
  <div class="pills">
    <span class="pill">tokens</span>
    <span class="pill">répertoire</span>
    <span class="pill">CLAUDE.md</span>
    <span class="pill">memory</span>
  </div>
</div>
<script>
(function() {
  function run() {
    var el = document.getElementById('bloc1');
    if (el) el.classList.add('anim-running');
  }
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('bloc1');
    if (!el) return;
    var section = el.closest('section');
    Reveal.on('slidechanged', function(e) { if (e.currentSlide === section) setTimeout(run, 200); });
    if (Reveal.getCurrentSlide && Reveal.getCurrentSlide() === section) setTimeout(run, 100);
  }
  setup();
})();
</script>

---

:::html
<h2>1a. <code>tokens</code> — L'unité de mesure de Claude</h2>

<div class="token-demo tok-colors" id="s5">
  <div class="token-sentence" id="s5-sentence">Claude Code est formidable !</div>
  <div class="token-blocks" id="s5-blocks"></div>
  <div class="tok-counter" id="s5-counter">0<span>&nbsp;tokens</span></div>
</div>

<p style="font-size:0.82em; color:#475569; text-align:center; margin:4px 0 8px;">
  1 token ≈ 4 caractères · 1 000 tokens ≈ 750 mots · 1 page A4 ≈ 500 tokens
</p>

<table class="tok-table fragment">
  <tr><th>Source</th><th>Exemples</th></tr>
  <tr><td><strong>Entrée</strong></td><td>Historique de conversation, fichiers lus, CLAUDE.md</td></tr>
  <tr><td><strong>Outils</strong></td><td>Chaque lecture de fichier, résultat de commande</td></tr>
  <tr><td><strong>Sortie</strong></td><td>Réponse générée par Claude</td></tr>
</table>

<script>
(function() {
  var TOKENS = ['Claude', ' Code', ' est', ' form', 'id', 'able', ' !'];
  var triggered = false;
  function run() {
    if (triggered) return; triggered = true;
    var sentence = document.getElementById('s5-sentence');
    var blocks   = document.getElementById('s5-blocks');
    var counter  = document.getElementById('s5-counter');
    sentence.style.opacity = '0';
    blocks.innerHTML = TOKENS.map(function(t) {
      return '<div class="tok">' + t.replace(/ /g, '&nbsp;') + '</div>';
    }).join('');
    blocks.querySelectorAll('.tok').forEach(function(tok, i) {
      setTimeout(function() {
        tok.classList.add('visible');
        counter.classList.add('visible');
        counter.innerHTML = (i + 1) + '<span>&nbsp;tokens</span>';
      }, i * 280);
    });
  }
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('s5');
    if (!el) return;
    var section = el.closest('section');
    Reveal.on('slidechanged', function(e) { if (e.currentSlide === section) setTimeout(run, 200); });
    if (Reveal.getCurrentSlide && Reveal.getCurrentSlide() === section) setTimeout(run, 100);
  }
  setup();
})();
</script>

---

:::html
<h2>1b. <code>tokens</code> — Les limites à connaître</h2>

<div class="meter-wrap" id="s6">
  <div class="gauge-box">
    <div class="gauge-label">⏱️ Fenêtre glissante — 5 heures</div>
    <div class="gauge-track"><div class="gauge-fill" id="s6-g1"></div></div>
    <div class="gauge-pct" id="s6-p1">0 k tokens</div>
    <div class="gauge-sub">~500 000 tokens max (input + output)</div>
  </div>
  <div class="gauge-box">
    <div class="gauge-label">📅 Quota total — 1 semaine</div>
    <div class="gauge-track"><div class="gauge-fill" id="s6-g2"></div></div>
    <div class="gauge-pct" id="s6-p2">0 k tokens</div>
    <div class="gauge-sub">Enveloppe globale hebdomadaire selon l'abonnement</div>
  </div>
  <div class="cff-box" id="cff-main">
    <div class="cff-cols">
      <div class="cff-section">
        <div class="cff-hdr nocache-hdr">❌ Sans cache — contexte entier renvoyé à chaque échange</div>
        <div class="cff-row" id="nc1">
          <div class="cff-in"><div class="cff-chip pchip">📝 Prompt 1</div></div>
          <span class="cff-arr">→</span><span class="cff-llm">🧠</span><span class="cff-arr">→</span>
          <div class="cff-chip rchip">💬 Rép. 1</div>
        </div>
        <div class="cff-row" id="nc2">
          <div class="cff-in">
            <div class="cff-chip xchip x1">🗄 Hist.</div>
            <div class="cff-chip pchip">📝 Prompt 2</div>
          </div>
          <span class="cff-arr">→</span><span class="cff-llm">🧠</span><span class="cff-arr">→</span>
          <div class="cff-chip rchip">💬 Rép. 2</div>
        </div>
        <div class="cff-row" id="nc3">
          <div class="cff-in">
            <div class="cff-chip xchip x2">🗄 Hist. ×2</div>
            <div class="cff-chip pchip">📝 Prompt 3</div>
          </div>
          <span class="cff-arr">→</span><span class="cff-llm">🧠</span><span class="cff-arr">→</span>
          <div class="cff-chip rchip">💬 Rép. 3</div>
        </div>
        <div class="cff-quota">
          <div class="cff-quota-label">Tokens consommés (cumulé)</div>
          <div class="cff-quota-track"><div class="cff-quota-fill nc-fill" id="nc-qfill"></div></div>
          <div class="cff-quota-num nc-num" id="nc-qnum">0 k</div>
        </div>
      </div>
      <div class="cff-section">
        <div class="cff-hdr cache-hdr">✅ Avec cache — seuls les nouveaux tokens sont envoyés</div>
        <div class="cff-row" id="wc1">
          <div class="cff-in"><div class="cff-chip pchip">📝 Prompt 1</div></div>
          <span class="cff-arr">→</span><span class="cff-llm">🧠</span><span class="cff-arr">→</span>
          <div class="cff-chip rchip">💬 Rép. 1</div>
          <div class="cff-badge">📦 mis en cache</div>
        </div>
        <div class="cff-row" id="wc2">
          <div class="cff-in"><div class="cff-chip pchip">📝 Prompt 2</div></div>
          <span class="cff-arr">→</span><span class="cff-llm">🧠</span><span class="cff-arr">→</span>
          <div class="cff-chip rchip">💬 Rép. 2</div>
          <div class="cff-badge hit">📦 cache hit</div>
        </div>
        <div class="cff-row" id="wc3">
          <div class="cff-in"><div class="cff-chip pchip">📝 Prompt 3</div></div>
          <span class="cff-arr">→</span><span class="cff-llm">🧠</span><span class="cff-arr">→</span>
          <div class="cff-chip rchip">💬 Rép. 3</div>
          <div class="cff-badge hit">📦 cache hit</div>
        </div>
        <div class="cff-quota">
          <div class="cff-quota-label">Tokens consommés (cumulé)</div>
          <div class="cff-quota-track"><div class="cff-quota-fill wc-fill" id="wc-qfill"></div></div>
          <div class="cff-quota-num wc-num" id="wc-qnum">0 k</div>
        </div>
      </div>
    </div>
  </div>
</div>
<!-- 4 spans invisibles déclencheurs — hors de cff-box, pas de fragments imbriqués -->
<span class="fragment" data-fragment-index="1" data-anim-key="s6-legend" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="2" data-anim-key="s6-ex1"    style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="3" data-anim-key="s6-ex2"    style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="4" data-anim-key="s6-ex3"    style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>

<script>
(function() {
  var triggered = false;
  function runGauges() {
    if (triggered) return; triggered = true;
    var g1 = document.getElementById('s6-g1'), p1 = document.getElementById('s6-p1');
    setTimeout(function() {
      g1.style.width = '85%';
      var n = 0, t = setInterval(function() {
        n += 8; p1.textContent = n + ' k tokens';
        if (n >= 425) { clearInterval(t); p1.textContent = '425 k tokens'; }
      }, 60);
      setTimeout(function() {
        g1.classList.add('warn'); p1.classList.add('warn'); p1.textContent = '⚠ 425 k / 500 k';
      }, 2700);
    }, 300);
    var g2 = document.getElementById('s6-g2'), p2 = document.getElementById('s6-p2');
    setTimeout(function() {
      g2.style.width = '40%';
      var n = 0, t = setInterval(function() {
        n += 5; p2.textContent = n + ' k tokens';
        if (n >= 200) { clearInterval(t); p2.textContent = '200 k tokens'; }
      }, 60);
    }, 600);
  }
  function cffShow(id) {
    var el = document.getElementById(id);
    if (el) { el.style.opacity = '1'; el.style.transform = 'none'; }
  }
  function cffReset() {
    var ids = ['cff-main','nc1','nc2','nc3','wc1','wc2','wc3'];
    ids.forEach(function(id) {
      var el = document.getElementById(id);
      if (el) { el.style.opacity = '0'; el.style.transform = 'translateY(6px)'; }
    });
    var nf=document.getElementById('nc-qfill'),nn=document.getElementById('nc-qnum');
    var wf=document.getElementById('wc-qfill'),wn=document.getElementById('wc-qnum');
    if(nf) nf.style.width='0%'; if(nn) nn.textContent='0 k';
    if(wf) wf.style.width='0%'; if(wn) wn.textContent='0 k';
  }
  function cffQuota(ncW,ncT,wcW,wcT) {
    var nf=document.getElementById('nc-qfill'),nn=document.getElementById('nc-qnum');
    var wf=document.getElementById('wc-qfill'),wn=document.getElementById('wc-qnum');
    if(nf) nf.style.width=ncW+'%'; if(nn) nn.textContent=ncT;
    if(wf) wf.style.width=wcW+'%'; if(wn) wn.textContent=wcT;
  }
  window._fragmentAnims = window._fragmentAnims || {};
  window._fragmentAnims['s6-legend'] = function() { cffShow('cff-main'); };
  window._fragmentAnims['s6-ex1'] = function() { cffShow('nc1'); cffShow('wc1'); cffQuota(17,'2 k',17,'2 k'); };
  window._fragmentAnims['s6-ex2'] = function() { cffShow('nc2'); cffShow('wc2'); cffQuota(50,'6 k',33,'4 k'); };
  window._fragmentAnims['s6-ex3'] = function() { cffShow('nc3'); cffShow('wc3'); cffQuota(100,'12 k',50,'6 k'); };
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('s6');
    if (!el) return;
    var section = el.closest('section');
    Reveal.on('slidechanged', function(e) {
      if (e.currentSlide === section) {
        triggered = false;
        cffReset();
        setTimeout(runGauges, 200);
      }
    });
    if (Reveal.getCurrentSlide && Reveal.getCurrentSlide() === section) {
      cffReset();
      setTimeout(runGauges, 100);
    }
  }
  setup();
})();
</script>

---

:::html
<h2>1c. <code>tokens</code> — Ce que Claude mange</h2>

<div class="food-wrap" id="s6c">
  <div class="food-card food-junk">
    <div class="food-card-hdr">🥵 Claude en overdose</div>
    <div class="food-items">
      <div class="food-item fi-junk" id="s6c-j1">
        <span class="food-emoji">🍔</span>
        <div class="food-txt">
          <span class="food-name">Conversation sans <code>/compact</code></span>
          <span class="food-desc">→ historique qui gonfle</span>
        </div>
      </div>
      <div class="food-item fi-junk" id="s6c-j2">
        <span class="food-emoji">🍟</span>
        <div class="food-txt">
          <span class="food-name"><code>slides.html</code> brut</span>
          <span class="food-desc">→ 65 000 tokens inutiles</span>
        </div>
      </div>
      <div class="food-item fi-junk" id="s6c-j3">
        <span class="food-emoji">🍫</span>
        <div class="food-txt">
          <span class="food-name">Contexte bruité, sans filtre</span>
          <span class="food-desc">→ bruit dans la fenêtre</span>
        </div>
      </div>
    </div>
    <div class="food-effects fx-junk" id="s6c-jfx">
      <span>❌ Hallucinations</span>
      <span>💸 Quota épuisé</span>
      <span>⏳ Lenteur</span>
      <span>😤 Humain qui grogne</span>
    </div>
  </div>

  <div class="food-card food-health">
    <div class="food-card-hdr">😊 Claude en pleine forme</div>
    <div class="food-items">
      <div class="food-item fi-health" id="s6c-h1">
        <span class="food-emoji">🥗</span>
        <div class="food-txt">
          <span class="food-name"><code>/compact</code> régulier</span>
          <span class="food-desc">→ contexte propre</span>
        </div>
      </div>
      <div class="food-item fi-health" id="s6c-h2">
        <span class="food-emoji">🥦</span>
        <div class="food-txt">
          <span class="food-name"><code>slides.md</code> ciblé</span>
          <span class="food-desc">→ 10 k tokens, pas 65 k</span>
        </div>
      </div>
      <div class="food-item fi-health" id="s6c-h3">
        <span class="food-emoji">🍎</span>
        <div class="food-txt">
          <span class="food-name">CLAUDE.md + memory</span>
          <span class="food-desc">→ instructions stables</span>
        </div>
      </div>
    </div>
    <div class="food-effects fx-health" id="s6c-hfx">
      <span>✅ Précis</span>
      <span>💚 Coût faible</span>
      <span>⚡ Rapide</span>
      <span>😊 Humain heureux</span>
    </div>
  </div>
</div>

<span class="fragment" data-fragment-index="1" data-anim-key="s6c-f1" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="2" data-anim-key="s6c-f2" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="3" data-anim-key="s6c-f3" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="4" data-anim-key="s6c-f4" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>

<script>
(function() {
  function show(id) {
    var el = document.getElementById(id);
    if (el) { el.style.opacity = '1'; el.style.transform = 'none'; }
  }
  window._fragmentAnims = window._fragmentAnims || {};
  window._fragmentAnims['s6c-f1'] = function() { show('s6c-j1'); show('s6c-h1'); };
  window._fragmentAnims['s6c-f2'] = function() { show('s6c-j2'); show('s6c-h2'); };
  window._fragmentAnims['s6c-f3'] = function() { show('s6c-j3'); show('s6c-h3'); };
  window._fragmentAnims['s6c-f4'] = function() { show('s6c-jfx'); show('s6c-hfx'); };
})();
</script>

---

:::html
<h2>2. Répertoire de travail — Comment Claude lit ton projet</h2>

<div class="tree-wrap" id="s7">
  <div>
    <div style="font-size:0.8em; font-weight:600; color:#64748B; margin-bottom:8px;">📂 Hiérarchie CLAUDE.md — chargement automatique</div>
    <div class="file-tree">
      <div class="tree-row" id="t1">
        <span class="tree-icon">🌍</span>
        <span class="tree-name">~/.claude/CLAUDE.md <span class="tree-badge">global</span></span>
      </div>
      <div class="tree-row tree-indent-1" id="t2">
        <span class="tree-icon">📁</span>
        <span class="tree-name">ProjetEcrivain/CLAUDE.md <span class="tree-badge">projet</span></span>
      </div>
      <div class="tree-row tree-indent-2" id="t3">
        <span class="tree-icon">📂</span>
        <span class="tree-name">LaPageTournee/CLAUDE.md <span class="tree-badge">local</span></span>
      </div>
      <div style="font-size:0.72em; color:#64748B; margin-top:10px; padding-left:8px; opacity:0; transition:opacity 0.5s;" id="t4-note">
        Les trois se <strong>cumulent</strong>. Le plus local a <strong>priorité</strong>.
      </div>
    </div>
  </div>
  <div>
    <div style="font-size:0.8em; font-weight:600; color:#64748B; margin-bottom:8px;">🔍 Exploration à la demande</div>
    <div class="explore-box">
      <div class="explore-cmd" id="e1">
        <span class="cmd-tool">Read</span>(<span class="cmd-file">"personnages.md"</span>)
        <div class="cmd-result">→ 847 tokens chargés</div>
      </div>
      <div class="explore-cmd" id="e2">
        <span class="cmd-tool">Glob</span>(<span class="cmd-file">"src/**/*.java"</span>)
        <div class="cmd-result">→ 42 fichiers trouvés</div>
      </div>
      <div class="explore-cmd" id="e3">
        <span class="cmd-tool">Grep</span>(<span class="cmd-file">"IsConnectable"</span>)
        <div class="cmd-result">→ 17 occurrences</div>
      </div>
      <div style="font-size:0.72em; color:#94A3B8; margin-top:8px; opacity:0; transition:opacity 0.5s;" id="e4-note">
        Claude ne "connaît" que ce qu'il a <strong style="color:#1E293B">explicitement lu</strong>
      </div>
    </div>
  </div>
</div>

<script>
(function() {
  var triggered = false;
  function run() {
    if (triggered) return; triggered = true;
    ['t1','t2','t3'].forEach(function(id, i) {
      setTimeout(function() {
        var el = document.getElementById(id);
        el.classList.add('visible');
        setTimeout(function() { el.classList.add('active'); }, 200);
        setTimeout(function() { el.classList.remove('active'); }, 900);
      }, i * 500);
    });
    setTimeout(function() {
      var n = document.getElementById('t4-note');
      if (n) n.style.opacity = '1';
    }, 1800);
    ['e1','e2','e3'].forEach(function(id, i) {
      setTimeout(function() {
        document.getElementById(id).classList.add('visible');
      }, 1500 + i * 500);
    });
    setTimeout(function() {
      var n = document.getElementById('e4-note');
      if (n) n.style.opacity = '1';
    }, 3100);
  }
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('s7');
    if (!el) return;
    var section = el.closest('section');
    Reveal.on('slidechanged', function(e) { if (e.currentSlide === section) setTimeout(run, 200); });
    if (Reveal.getCurrentSlide && Reveal.getCurrentSlide() === section) setTimeout(run, 100);
  }
  setup();
})();
</script>

---

:::html
<h2>3. <code>CLAUDE.md</code> — Instruire Claude une fois pour toutes</h2>

<div class="ba-wrap" id="s8">
  <div class="ba-col">
    <div class="ba-header bad">❌ Sans CLAUDE.md</div>
    <div class="ba-body">
      <div class="chat-msg" id="b1">
        <div class="chat-avatar av-user">F</div>
        <div class="chat-bubble repeated"><span class="repeat-badge">session 1</span>Ton réaliste, dialogues au sous-texte, Victor garde son secret...</div>
      </div>
      <div class="chat-msg" id="b2">
        <div class="chat-avatar av-user">F</div>
        <div class="chat-bubble repeated"><span class="repeat-badge">session 2</span>Rappel : ton intimiste, pas de résolution rapide...</div>
      </div>
      <div class="chat-msg" id="b3">
        <div class="chat-avatar av-user">F</div>
        <div class="chat-bubble repeated"><span class="repeat-badge">session 3</span>Encore une fois : Victor ne révèle JAMAIS son prêt...</div>
      </div>
      <div class="chat-msg" id="b4">
        <div class="chat-avatar av-claude">C</div>
        <div class="chat-bubble" style="color:#94A3B8; font-style:italic">Je ne me souviens pas de la session précédente...</div>
      </div>
    </div>
  </div>
  <div class="ba-col">
    <div class="ba-header good">✅ Avec CLAUDE.md</div>
    <div class="ba-body">
      <div class="editor-box" id="s8-editor">
        <div class="editor-line"><!-- CLAUDE.md --></div>
        <span id="s8-typed"></span><span class="editor-cursor" id="s8-cursor"></span>
      </div>
      <div class="chat-msg" id="g1" style="margin-top:10px">
        <div class="chat-avatar av-user">F</div>
        <div class="chat-bubble direct">Écris la scène où Victor voit Tom entrer.</div>
      </div>
      <div class="chat-msg" id="g2">
        <div class="chat-avatar av-claude">C</div>
        <div class="chat-bubble direct">✅ Je connais déjà Victor, son secret, le ton intimiste... On y va.</div>
      </div>
    </div>
  </div>
</div>

<script>
(function() {
  var triggered = false;
  var LINES = ['# La Page Tournée','## Style','- Ton intimiste, sous-texte','## Règles absolues','- Victor ne révèle JAMAIS son prêt'];

  function typeLines(el, lines, cb) {
    var li = 0, ci = 0, html = '';
    var cursor = document.getElementById('s8-cursor');
    var t = setInterval(function() {
      if (li >= lines.length) {
        clearInterval(t);
        if (cursor) cursor.style.display = 'none';
        if (cb) cb();
        return;
      }
      var line = lines[li];
      if (ci < line.length) { html += line[ci++]; }
      else { html += '\n'; li++; ci = 0; }
      el.innerHTML = html.split('\n').map(function(l) {
        return '<div class="editor-line">' + (l || '&nbsp;') + '</div>';
      }).join('');
    }, 38);
  }

  function run() {
    if (triggered) return; triggered = true;
    ['b1','b2','b3','b4'].forEach(function(id, i) {
      setTimeout(function() { document.getElementById(id).classList.add('visible'); }, i * 550);
    });
    setTimeout(function() {
      typeLines(document.getElementById('s8-typed'), LINES, function() {
        setTimeout(function() { document.getElementById('g1').classList.add('visible'); }, 300);
        setTimeout(function() { document.getElementById('g2').classList.add('visible'); }, 900);
      });
    }, 400);
  }
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('s8');
    if (!el) return;
    var section = el.closest('section');
    Reveal.on('slidechanged', function(e) { if (e.currentSlide === section) setTimeout(run, 200); });
    if (Reveal.getCurrentSlide && Reveal.getCurrentSlide() === section) setTimeout(run, 100);
  }
  setup();
})();
</script>

---

## `CLAUDE.md` — 🧵 Exemple fil rouge

```markdown
# Projet : La Page Tournée

## Contexte
Nouvelle à 4 personnages. Fichiers dans exemple/.

## Style d'écriture
- Ton réaliste et intimiste, sans pathos
- Dialogues naturels — le sous-texte prime sur l'explicite
- Points de vue alternés entre les personnages

## Règles absolues
- Victor ne mentionne JAMAIS son prêt à Elise
- Les conflits ne se résolvent pas trop vite
- Nadia ne révèle pas son ambition littéraire avant le chapitre 4
```

> Dès la prochaine session, Claude connaît ces règles sans qu'on le lui rappelle.

---

:::html
<div id="mem-slide">
  <h2>4. <code>memory</code> — La mémoire entre les sessions</h2>
  <div class="mem-layout">

    <div class="mem-left">
      <div class="mem-panel-label">📱 Session (éphémère)</div>
      <div class="mem-chat" id="mem-chat">
        <div class="mem-bubble mem-umsg" id="mb1">Elise cache des mots dans les livres pour ses lecteurs.</div>
        <div class="mem-bubble mem-cmsg" id="mb2">Noté — c'est le fil rouge du roman.</div>
        <div class="mem-bubble mem-umsg" id="mb3">Et Victor, il a prêté de l'argent à Elise il y a 30 ans.</div>
        <div class="mem-bubble mem-cmsg" id="mb4">Secret du chapitre final — je garde ça en tête.</div>
      </div>
      <div class="mem-clear-line" id="mb-clear">$ /clear — contexte effacé ✓</div>
    </div>

    <div class="mem-right">
      <div class="mem-panel-label" id="mem-right-label" style="opacity:0;transition:opacity 0.4s;">🧠 Mémoire (persistante)</div>
      <div class="mem-card mem-card-user" id="mc1">
        <span class="mem-card-icon">🧑</span>
        <div>
          <span class="mem-card-type">user</span>
          <span class="mem-card-desc">Préfère les dialogues lents, chargés de sous-texte</span>
        </div>
      </div>
      <div class="mem-card mem-card-project" id="mc2">
        <span class="mem-card-icon">📋</span>
        <div>
          <span class="mem-card-type">project</span>
          <span class="mem-card-desc">Victor = bailleur secret d'Elise — révélation finale</span>
        </div>
      </div>
      <div class="mem-card mem-card-feedback" id="mc3">
        <span class="mem-card-icon">💬</span>
        <div>
          <span class="mem-card-type">feedback</span>
          <span class="mem-card-desc">Ne pas résoudre les conflits trop rapidement</span>
        </div>
      </div>
      <div class="mem-card mem-card-ref" id="mc4">
        <span class="mem-card-icon">🔗</span>
        <div>
          <span class="mem-card-type">reference</span>
          <span class="mem-card-desc">personnages.md · nouvelle.md</span>
        </div>
      </div>
    </div>

  </div>

  <div class="mem-retenir fragment" data-fragment-index="5">
    <strong>À retenir :</strong> CLAUDE.md = règles fixes &nbsp;·&nbsp; Memory = état vivant, géré automatiquement
  </div>
</div>
<span class="fragment" data-fragment-index="0" data-anim-key="mem-right-label" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="1" data-anim-key="mem-mc1" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="2" data-anim-key="mem-mc2" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="3" data-anim-key="mem-mc3" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="4" data-anim-key="mem-mc4" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>

<script>
(function() {
  var triggered = false;
  function run() {
    if (triggered) return; triggered = true;
    var T = [
      ['mb1',   300],
      ['mb2',   850],
      ['mb3',  1400],
      ['mb4',  1950],
    ];
    T.forEach(function(t) {
      setTimeout(function() { document.getElementById(t[0]).classList.add('visible'); }, t[1]);
    });
    setTimeout(function() { document.getElementById('mb-clear').classList.add('visible'); }, 2700);
    setTimeout(function() {
      ['mb1','mb2','mb3','mb4'].forEach(function(id, i) {
        setTimeout(function() { document.getElementById(id).classList.add('struck'); }, i * 90);
      });
    }, 3200);
  }
  function reset() {
    triggered = false;
    ['mb1','mb2','mb3','mb4','mb-clear','mc1','mc2','mc3','mc4'].forEach(function(id) {
      var el = document.getElementById(id);
      if (el) { el.classList.remove('visible'); el.classList.remove('struck'); }
    });
    var lbl = document.getElementById('mem-right-label');
    if (lbl) lbl.style.opacity = '0';
  }
  window._fragmentAnims = window._fragmentAnims || {};
  window._fragmentAnims['mem-right-label'] = function() { var el = document.getElementById('mem-right-label'); if (el) el.style.opacity = '1'; };
  window._fragmentAnims['mem-mc1'] = function() { document.getElementById('mc1').classList.add('visible'); };
  window._fragmentAnims['mem-mc2'] = function() { document.getElementById('mc2').classList.add('visible'); };
  window._fragmentAnims['mem-mc3'] = function() { document.getElementById('mc3').classList.add('visible'); };
  window._fragmentAnims['mem-mc4'] = function() { document.getElementById('mc4').classList.add('visible'); };
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('mem-slide');
    if (!el) return;
    var section = el.closest('section');
    Reveal.on('slidechanged', function(e) {
      if (e.currentSlide === section) setTimeout(run, 200);
      else if (e.previousSlide === section) reset();
    });
    if (Reveal.getCurrentSlide && Reveal.getCurrentSlide() === section) setTimeout(run, 100);
  }
  setup();
})();
</script>

---

## `memory` — 🧵 Exemple fil rouge

*Après une session de travail sur les personnages :*

```plaintext
[Claude sauvegarde en mémoire — type project]
Les personnages sont définis dans exemple/personnages.md.
Victor est le bailleur secret d'Elise — révélation réservée
au chapitre final uniquement.
Dernière scène écrite : arrivée de Tom devant la librairie (ch.2).
```

*Après un feedback de l'utilisateur :*

```plaintext
[Claude sauvegarde en mémoire — type feedback]
Ne pas écrire de scènes d'action trop rapides.
L'utilisateur préfère les dialogues lents et chargés de sous-texte.
```

> La semaine suivante, Claude reprend exactement là où il s'est arrêté.

---

:::html
<div class="bloc-center" id="bloc2">
  <div class="bloc-num">Bloc 2</div>
  <h1 style="color:#1E293B; font-size:2em; margin:0.15em 0;">Comprendre le contexte</h1>
  <p class="bloc-sub" style="color:#64748B; font-size:0.9em; margin:0 0 0.4em;">Ce que Claude voit, et comment le maîtriser</p>
  <div class="pills">
    <span class="pill">contexte</span>
    <span class="pill">/compact</span>
    <span class="pill">/clear</span>
    <span class="pill">rewind</span>
  </div>
</div>
<script>
(function() {
  function run() {
    var el = document.getElementById('bloc2');
    if (el) el.classList.add('anim-running');
  }
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('bloc2');
    if (!el) return;
    var section = el.closest('section');
    Reveal.on('slidechanged', function(e) { if (e.currentSlide === section) setTimeout(run, 200); });
    if (Reveal.getCurrentSlide && Reveal.getCurrentSlide() === section) setTimeout(run, 100);
  }
  setup();
})();
</script>

---

:::html
<h2>5. <code>contexte</code> — La fenêtre de Claude sur le monde</h2>

<p><strong>C'est quoi ?</strong><br>
Le contexte, c'est l'ensemble de ce que Claude "voit" à un instant donné : l'historique des échanges, les fichiers lus, les résultats d'outils, le contenu du CLAUDE.md.</p>

<p class="fragment" data-fragment-index="0"><strong>Ses limites :</strong></p>
<ul>
  <li class="fragment" data-fragment-index="1">Il est <strong>borné</strong> : au-delà d'un certain volume, les informations anciennes disparaissent</li>
  <li class="fragment" data-fragment-index="2">Il est <strong>éphémère</strong> : une nouvelle session repart de zéro (sauf CLAUDE.md et memory)</li>
  <li class="fragment" data-fragment-index="3">Il est <strong>cumulatif</strong> : chaque échange consomme de l'espace</li>
</ul>

<div class="ctx-compare">
  <div class="ctx-card ctx-ok" id="ctx-ok-card">
    <div class="ctx-scene-title">😌 Contexte maîtrisé</div>
    <div class="ctx-books">
      <span class="ctx-bk" style="transform:rotate(-8deg)">📗</span>
      <span class="ctx-bk">📘</span>
      <span class="ctx-bk" style="transform:rotate(6deg)">📙</span>
    </div>
    <div class="ctx-win-wrap">
      <div class="ctx-win-label">Fenêtre de contexte</div>
      <div class="ctx-win-track">
        <div class="ctx-win-fill ctx-fill-ok">40 %</div>
      </div>
    </div>
    <div class="ctx-face">😊</div>
    <div class="ctx-caption ok-caption">Claude répond avec précision</div>
  </div>

  <div class="ctx-card ctx-panic" id="ctx-panic-card">
    <div class="ctx-scene-title">😰 Contexte saturé</div>
    <div class="ctx-books">
      <span class="ctx-bk" style="transform:rotate(-12deg)">📗</span>
      <span class="ctx-bk">📘</span>
      <span class="ctx-bk" style="transform:rotate(10deg)">📙</span>
      <span class="ctx-bk" style="transform:rotate(-6deg)">📕</span>
      <span class="ctx-bk">📓</span>
      <span class="ctx-bk" style="transform:rotate(14deg)">📗</span>
      <span class="ctx-bk" style="transform:rotate(-9deg)">📘</span>
    </div>
    <div class="ctx-win-wrap">
      <div class="ctx-win-label">Fenêtre de contexte</div>
      <div class="ctx-win-track">
        <div class="ctx-win-fill ctx-fill-panic">85 %</div>
      </div>
    </div>
    <div class="ctx-face ctx-face-shake">😰</div>
    <div class="ctx-caption panic-caption">Il commence à oublier…</div>
  </div>
</div>
<span class="fragment" data-fragment-index="4" data-anim-key="s5ctx-ok"    style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="5" data-anim-key="s5ctx-panic" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>

<script>
(function() {
  window._fragmentAnims = window._fragmentAnims || {};
  window._fragmentAnims['s5ctx-ok'] = function() {
    var el = document.getElementById('ctx-ok-card');
    if (el) { el.style.opacity = '1'; el.style.transform = 'none'; }
  };
  window._fragmentAnims['s5ctx-panic'] = function() {
    var el = document.getElementById('ctx-panic-card');
    if (el) { el.style.opacity = '1'; el.style.transform = 'none'; }
  };
})();
</script>

---

## `contexte` — 🧵 Exemple fil rouge

Scénario : on est en milieu de session, on a lu `personnages.md`, `nouvelle.md` chapitres 1 à 3, et échangé une vingtaine de messages.

**Ce que Claude sait dans ce contexte :**
- Le secret de Victor (lu dans personnages.md)
- Le ton du dialogue du chapitre 2 (échangé plus tôt)
- La consigne "pas de résolution rapide" (CLAUDE.md)

**Ce qu'on peut lui demander :**
> *"Écris la réaction de Victor quand il voit Tom entrer dans la librairie."*

Claude peut répondre de façon cohérente parce que tout le contexte nécessaire est présent. Sans lui, la réponse serait générique.

---

:::html
<h2>6. <code>/compact</code> — Compresser sans perdre</h2>

<div class="compact-layout" id="s-compact">
  <div class="compact-top">
    <p style="margin:0 0 6px;"><strong>C'est quoi ?</strong> — <code>/compact</code> résume l'historique en version condensée, libérant de l'espace dans la fenêtre de contexte.</p>
    <div class="cmp-when">
      <span class="cmp-pill">📚 Longue session exploratoire</span>
      <span class="cmp-pill">🔄 Avant une nouvelle tâche lourde</span>
      <span class="cmp-pill">🌀 Claude commence à perdre le fil</span>
    </div>
  </div>

  <div class="cmp-scenes">
    <div class="cmp-scene" id="cmp1">
      <div class="cmp-scene-hdr std-hdr"><code>/compact</code> — standard</div>
      <div class="cmp-hist" id="cmp1-hist">
        <div class="cmp-bub user">Écris la scène d'arrivée de Tom</div>
        <div class="cmp-bub claude">Voici la scène... [version longue]</div>
        <div class="cmp-bub user">Trop long, refais plus court</div>
        <div class="cmp-bub claude">Version raccourcie...</div>
        <div class="cmp-bub user">Mieux ! Garde ce ton pour Nadia</div>
      </div>
      <div class="cmp-cmd" id="cmp1-cmd"><span class="cmp-prompt">$</span> /compact</div>
      <div class="cmp-result" id="cmp1-result">
        <div class="cmp-result-hdr">📋 Résumé de session</div>
        <div class="cmp-result-line">Tom a reconnu la librairie. Victor a observé en silence.</div>
        <div class="cmp-result-line">→ Décision : écrire ch.3 du PDV de Nadia.</div>
      </div>
    </div>

    <div class="cmp-scene" id="cmp2" style="opacity:0;transition:opacity 0.5s;">
      <div class="cmp-scene-hdr custom-hdr"><code>/compact</code> — personnalisé</div>
      <div class="cmp-hist" id="cmp2-hist">
        <div class="cmp-bub user">Écris la scène d'arrivée de Tom</div>
        <div class="cmp-bub claude">Voici la scène... [version longue]</div>
        <div class="cmp-bub user">Trop long, refais plus court</div>
        <div class="cmp-bub claude">Version raccourcie...</div>
        <div class="cmp-bub user">Mieux ! Garde ce ton pour Nadia</div>
      </div>
      <div class="cmp-cmd" id="cmp2-cmd"><span class="cmp-prompt">$</span> /compact <span class="cmp-arg">garde les décisions sur les personnages et le plan</span></div>
      <div class="cmp-result custom-result" id="cmp2-result">
        <div class="cmp-kept"><span class="cmp-icon">📌</span> <strong>Conservé :</strong> personnages (secrets), plan ch.3-5</div>
        <div class="cmp-dropped"><span class="cmp-icon">✗</span> <strong>Supprimé :</strong> 18 échanges de reformulation</div>
      </div>
    </div>
  </div>
</div>
<span class="fragment" data-anim-key="compact-cmp2" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>

<script>
(function() {
  window._fragmentAnims = window._fragmentAnims || {};
  window._fragmentAnims['compact-cmp2'] = function() {
    var el = document.getElementById('cmp2');
    if (el) el.style.opacity = '1';
  };
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('s-compact');
    if (!el) return;
    var section = el.closest('section');
    Reveal.on('slidechanged', function(e) {
      if (e.previousSlide === section) {
        var cmp2 = document.getElementById('cmp2');
        if (cmp2) cmp2.style.opacity = '0';
      }
    });
  }
  setup();
})();
</script>

---

:::html
<div id="cl-slide">
  <h2 style="font-size:1.05em; margin:0 0 0.5em;">7.1 <code>/clear</code> — Reset</h2>

  <div class="cl-layout">

    <div class="cl-col">
      <div class="cl-col-label">📖 Changer de sujet</div>
      <div class="cl-chat">
        <div class="cl-bubble cl-umsg cl-old" id="cl0a">Victor a prêté de l'argent à Elise — secret absolu jusqu'au chapitre 5.</div>
        <div class="cl-bubble cl-cmsg cl-old" id="cl0b">Compris, je ne révèle rien avant le dénouement. 🤫</div>
        <div class="cl-old-sep"></div>
        <div class="cl-bubble cl-umsg" id="cl1a">Le chapitre 2 est bouclé ! On attaque le chapitre 3 — point de vue Nadia.</div>
        <div class="cl-bubble cl-cmsg" id="cl1b">Avant de commencer, il serait peut-être judicieux de faire un <code>/clear</code> — tout le contexte du chapitre 2 risque de teinter involontairement le ton de Nadia.</div>
        <div class="cl-bubble cl-umsg" id="cl1c">Bonne idée.</div>
      </div>
      <div class="cl-cmd" id="cl-cmd1">$ /clear</div>
    </div>

    <div class="cl-col" id="cl-right-col" style="opacity:0;transition:opacity 0.4s;">
      <div class="cl-col-label">⚠️ Erreurs en cascade</div>
      <div class="cl-chat">
        <div class="cl-bubble cl-umsg" id="cl2a">Récris le dialogue de Victor — trop direct.</div>
        <div class="cl-bubble cl-cmsg" id="cl2b">Victor hausse les épaules : "Cette librairie ne me concerne pas."</div>
        <div class="cl-bubble cl-umsg" id="cl2c">Il a prêté de l'argent à Elise ! C'est son secret !</div>
        <div class="cl-bubble cl-cmsg" id="cl2d">Ah oui… Victor glisse quelque chose à l'oreille de Nadia sur un ancien prêt.</div>
        <div class="cl-bubble cl-umsg" id="cl2e">Nadia ?! C'est Elise qui est concernée !</div>
        <div class="cl-bubble cl-cmsg cl-derail" id="cl2f">Je… oui, Elise, pardon. Ou était-ce Tom ? Je perds le fil, je mélange tout.</div>
      </div>
      <div class="cl-cmd" id="cl-cmd2">$ /clear</div>
    </div>

  </div>

  <!-- Fragments invisibles = points de pause -->
  <span class="fragment" id="cl-frag1"     style="display:none!important;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
  <span class="fragment" id="cl-frag-right" style="display:none!important;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
  <span class="fragment" id="cl-frag2"     style="display:none!important;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>

  <div class="cl-survivors">
    <div class="cl-surv-card" id="cl-s1">📄 <strong>CLAUDE.md</strong><span class="cl-surv-check">✓</span><span class="cl-surv-desc">règles du projet</span></div>
    <div class="cl-surv-card" id="cl-s2">🧠 <strong>memory</strong><span class="cl-surv-check">✓</span><span class="cl-surv-desc">personnages, préférences</span></div>
  </div>

  <div class="cl-retenir fragment">
    Après <code>/clear</code>, CLAUDE.md et la mémoire restent. Le reste disparaît.
  </div>
</div>

<script>
(function() {
  var phase = 0;

  function vis(id, t, p) {
    setTimeout(function() {
      if (phase >= p) { var el = document.getElementById(id); if (el) el.classList.add('visible'); }
    }, t);
  }
  function str(id, t, p) {
    setTimeout(function() {
      if (phase >= p) { var el = document.getElementById(id); if (el) el.classList.add('struck'); }
    }, t);
  }
  function hide(ids) {
    ids.forEach(function(id) {
      var el = document.getElementById(id);
      if (el) { el.classList.remove('visible'); el.classList.remove('struck'); }
    });
  }
  function unstrike(ids) {
    ids.forEach(function(id) { var el = document.getElementById(id); if (el) el.classList.remove('struck'); });
  }

  function startLeft() {
    phase = 1;
    vis('cl1a',  300, 1);
    vis('cl1b',  900, 1);
    vis('cl1c', 1600, 1);
  }

  function startClearLeft() {
    phase = 2;
    vis('cl-cmd1', 0, 2);
    str('cl0a', 150, 2);
    str('cl0b', 220, 2);
    str('cl1a', 300, 2);
    str('cl1b', 400, 2);
    str('cl1c', 500, 2);
  }

  function startRight() {
    phase = 3;
    var rc = document.getElementById('cl-right-col');
    if (rc) rc.style.opacity = '1';
    vis('cl2a',  300, 3);
    vis('cl2b',  900, 3);
    vis('cl2c', 1500, 3);
    vis('cl2d', 2100, 3);
    vis('cl2e', 2700, 3);
    vis('cl2f', 3300, 3);
  }

  function startClearRight() {
    phase = 4;
    vis('cl-cmd2',   0, 4);
    str('cl2a',  300, 4);
    str('cl2b',  390, 4);
    str('cl2c',  480, 4);
    str('cl2d',  570, 4);
    str('cl2e',  660, 4);
    str('cl2f',  750, 4);
    vis('cl-s1', 1100, 4);
    vis('cl-s2', 1400, 4);
  }

  function reset() {
    phase = 0;
    hide(['cl0a','cl0b','cl1a','cl1b','cl1c','cl-cmd1','cl2a','cl2b','cl2c','cl2d','cl2e','cl2f','cl-cmd2','cl-s1','cl-s2']);
    var rc = document.getElementById('cl-right-col');
    if (rc) rc.style.opacity = '0';
  }

  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('cl-slide');
    if (!el) return;
    var section = el.closest('section');

    Reveal.on('slidechanged', function(e) {
      if (e.currentSlide === section) setTimeout(startLeft, 200);
      else if (e.previousSlide === section) reset();
    });
    Reveal.on('fragmentshown', function(e) {
      if (!section.contains(e.fragment)) return;
      if (e.fragment.id === 'cl-frag1')     startClearLeft();
      if (e.fragment.id === 'cl-frag-right') startRight();
      if (e.fragment.id === 'cl-frag2')     startClearRight();
    });
    Reveal.on('fragmenthidden', function(e) {
      if (!section.contains(e.fragment)) return;
      if (e.fragment.id === 'cl-frag2') {
        phase = 3;
        hide(['cl-cmd2','cl-s1','cl-s2']);
        unstrike(['cl2a','cl2b','cl2c','cl2d','cl2e','cl2f']);
      }
      if (e.fragment.id === 'cl-frag-right') {
        phase = 2;
        hide(['cl2a','cl2b','cl2c','cl2d','cl2e','cl2f']);
        var rc = document.getElementById('cl-right-col');
        if (rc) rc.style.opacity = '0';
      }
      if (e.fragment.id === 'cl-frag1') {
        phase = 1;
        hide(['cl-cmd1','cl2a','cl2b','cl2c','cl2d','cl2e','cl2f','cl-cmd2','cl-s1','cl-s2']);
        unstrike(['cl0a','cl0b','cl1a','cl1b','cl1c']);
      }
    });

    if (Reveal.getCurrentSlide && Reveal.getCurrentSlide() === section) setTimeout(startLeft, 100);
  }
  setup();
})();
</script>

---

:::html
<h2 style="font-size:1.05em; margin:0 0 0.5em;">7.2 <code>rewind</code> — Retour arrière</h2>
<div class="rw-layout">
  <div class="rw-main">
    <div class="rw-thread">
      <div class="rw-msg" id="rw1">
        <div class="rw-avatar rw-av-u">F</div>
        <div class="rw-bub rw-bub-u">Écris la scène café — Tom et Elise se retrouvent</div>
      </div>
      <div class="rw-msg" id="rw2">
        <div class="rw-avatar rw-av-c">C</div>
        <div class="rw-bub rw-bub-c">Le café sentait la pluie froide. Tom posa son verre...</div>
      </div>
      <div class="rw-msg" id="rw3">
        <div class="rw-avatar rw-av-u">F</div>
        <div class="rw-bub rw-bub-u">Maintenant la scène où Victor défend Elise face à Tom</div>
        <div class="rw-badge" id="rw-badge">↩ cible rewind</div>
      </div>
      <div class="rw-msg" id="rw4">
        <div class="rw-avatar rw-av-c">C</div>
        <div class="rw-bub rw-bub-c">Victor se dressa. Sa voix claqua comme un verdict...</div>
      </div>
      <div class="rw-msg" id="rw5">
        <div class="rw-avatar rw-av-u">F</div>
        <div class="rw-bub rw-bub-u">Trop dramatique — Victor reste discret, pas de discours</div>
      </div>
    </div>
    <div class="fragment rw-phase2" data-fragment-index="0">
      <div class="rw-cmd" id="rw-cmd">
        <span class="rw-prompt">$</span> rewind quand je t'ai demandé d'écrire Victor qui défend Elise
      </div>
      <div class="rw-restart" id="rw-restart">
        ↩ Reparti depuis ce message — 2 échanges effacés, fichiers restaurés ⚠️
      </div>
    </div>
  </div>
  <div class="fragment rw-combo-frag" data-fragment-index="1">
    <div class="rw-combo-title">✓ Bonne pratique — memory + rewind</div>
    <div class="rw-combo">
      <div class="rw-step" id="rws1">
        <div class="rw-step-num">1</div>
        Sauvegarder en mémoire ce qui ne fonctionne pas
      </div>
      <span class="rw-sep">→</span>
      <div class="rw-step" id="rws2">
        <div class="rw-step-num">2</div>
        <code>rewind</code> — effacer le contexte raté
      </div>
      <span class="rw-sep">→</span>
      <div class="rw-step" id="rws3">
        <div class="rw-step-num">3</div>
        Relancer — bénéfice de l'apprentissage, sans le bruit
      </div>
    </div>
  </div>
</div>

<div class="fragment" data-fragment-index="2" style="position:absolute;inset:0;z-index:50;background:rgba(15,23,42,0.96);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:1.5em;border-radius:8px;">
  <div style="max-width:800px;width:100%;color:#F8FAFC;">

    <div style="text-align:center;margin-bottom:1em;">
      <div style="font-size:1.6em;line-height:1;">↩</div>
      <h2 style="margin:0.15em 0 0.2em;color:#F8FAFC;font-size:1.3em;font-weight:700;">/rewind — Retour arrière</h2>
      <p style="color:#CBD5E1;font-size:0.75em;margin:0;">
        Ouvrir avec
        <kbd style="background:#1E3A5F;border:1px solid #3B82F6;border-radius:3px;padding:1px 6px;font-size:0.9em;font-family:monospace;">Esc + Esc</kbd>
        &nbsp;ou&nbsp;
        <code style="background:#1E293B;border-radius:3px;padding:1px 6px;color:#60A5FA;">/rewind</code>
      </p>
    </div>

    <div style="display:grid;grid-template-columns:1.1fr 0.9fr;gap:1.2em;align-items:start;">

      <div>
        <div style="font-size:0.68em;font-weight:700;color:#94A3B8;text-transform:uppercase;letter-spacing:0.09em;margin-bottom:0.55em;">Menu interactif — 4 options</div>
        <div style="display:flex;flex-direction:column;gap:0.45em;">

          <div style="background:#0F2744;border:1px solid #1D4ED8;border-radius:7px;padding:0.45em 0.8em;display:flex;align-items:flex-start;gap:0.65em;">
            <span style="background:#1D4ED8;color:#fff;border-radius:50%;min-width:20px;height:20px;display:flex;align-items:center;justify-content:center;font-size:0.68em;font-weight:800;margin-top:1px;">1</span>
            <div>
              <div style="font-weight:700;color:#93C5FD;font-size:0.8em;">Restore code + conversation</div>
              <div style="color:#CBD5E1;font-size:0.7em;margin-top:1px;">Fichiers et historique remis au point choisi</div>
            </div>
          </div>

          <div style="background:#092033;border:1px solid #0369A1;border-radius:7px;padding:0.45em 0.8em;display:flex;align-items:flex-start;gap:0.65em;">
            <span style="background:#0369A1;color:#fff;border-radius:50%;min-width:20px;height:20px;display:flex;align-items:center;justify-content:center;font-size:0.68em;font-weight:800;margin-top:1px;">2</span>
            <div>
              <div style="font-weight:700;color:#7DD3FC;font-size:0.8em;">Restore conversation</div>
              <div style="color:#CBD5E1;font-size:0.7em;margin-top:1px;">Historique remonté — fichiers inchangés</div>
            </div>
          </div>

          <div style="background:#160E2A;border:1px solid #6D28D9;border-radius:7px;padding:0.45em 0.8em;display:flex;align-items:flex-start;gap:0.65em;">
            <span style="background:#6D28D9;color:#fff;border-radius:50%;min-width:20px;height:20px;display:flex;align-items:center;justify-content:center;font-size:0.68em;font-weight:800;margin-top:1px;">3</span>
            <div>
              <div style="font-weight:700;color:#C4B5FD;font-size:0.8em;">Restore code</div>
              <div style="color:#CBD5E1;font-size:0.7em;margin-top:1px;">Fichiers restaurés — conversation conservée</div>
            </div>
          </div>

          <div style="background:#1A160A;border:1px solid #B45309;border-radius:7px;padding:0.45em 0.8em;display:flex;align-items:flex-start;gap:0.65em;">
            <span style="background:#B45309;color:#fff;border-radius:50%;min-width:20px;height:20px;display:flex;align-items:center;justify-content:center;font-size:0.68em;font-weight:800;margin-top:1px;">4</span>
            <div>
              <div style="font-weight:700;color:#FCD34D;font-size:0.8em;">Summarize from here</div>
              <div style="color:#CBD5E1;font-size:0.7em;margin-top:1px;">Compresse la conversation — libère du contexte</div>
            </div>
          </div>

        </div>
      </div>

      <div>
        <div style="font-size:0.68em;font-weight:700;color:#94A3B8;text-transform:uppercase;letter-spacing:0.09em;margin-bottom:0.55em;">Argument direct</div>
        <div style="background:#0D1B2A;border:1px solid #334155;border-radius:8px;padding:1em 1.1em;">
          <div style="font-family:monospace;font-size:1.05em;color:#38BDF8;margin-bottom:0.5em;">/rewind <span style="color:#F472B6;">N</span></div>
          <p style="color:#CBD5E1;font-size:0.76em;margin:0 0 0.75em;line-height:1.5;">
            Annule les <strong style="color:#F8FAFC;">N derniers échanges</strong><br>directement, sans ouvrir le menu
          </p>
          <div style="background:#2A1010;border:1px solid #92400E;border-radius:5px;padding:0.5em 0.7em;display:flex;gap:0.5em;align-items:flex-start;">
            <span style="font-size:0.85em;flex-shrink:0;">⚠️</span>
            <span style="color:#FCA5A5;font-size:0.72em;line-height:1.45;">Conversation seulement — les fichiers ne sont <strong style="color:#FECACA;">pas restaurés</strong></span>
          </div>
        </div>
      </div>

    </div>
  </div>
</div>

---

## `/clear` et `rewind` — 🧵 Exemple fil rouge

**Scénario `/clear` :**
On vient de terminer une longue session sur le chapitre 2 (Tom et Elise). On veut maintenant travailler sur le chapitre 3 (Nadia) sans que les échanges précédents influencent le ton.
→ `/clear` : Claude repart sans le bruit du chapitre 2, mais connaît toujours les personnages via CLAUDE.md.

**Scénario `rewind` :**
> On demande : *"Écris la scène où Victor défend Elise face à Tom."*
> Claude produit une scène trop dramatique, presque théâtrale.
> On décide d'annuler : `rewind` jusqu'au message précédant la génération.
> On reformule : *"Même scène, mais Victor reste en retrait — une phrase sèche, pas de discours."*

---

:::html
<div class="bloc-center" id="bloc3">
  <div class="bloc-num">Bloc 3</div>
  <h1 style="color:#1E293B; font-size:2em; margin:0.15em 0;">Travailler avec Claude</h1>
  <p class="bloc-sub" style="color:#64748B; font-size:0.9em; margin:0 0 0.4em;">Collaborer, déléguer, spécialiser</p>
  <div class="pills">
    <span class="pill">plan</span>
    <span class="pill">skill</span>
    <span class="pill">agent</span>
    <span class="pill">subagents</span>
  </div>
</div>
<script>
(function() {
  function run() {
    var el = document.getElementById('bloc3');
    if (el) el.classList.add('anim-running');
  }
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('bloc3');
    if (!el) return;
    var section = el.closest('section');
    Reveal.on('slidechanged', function(e) { if (e.currentSlide === section) setTimeout(run, 200); });
    if (Reveal.getCurrentSlide && Reveal.getCurrentSlide() === section) setTimeout(run, 100);
  }
  setup();
})();
</script>

---

:::html
<h2 style="font-size:1.05em; margin:0 0 0.4em;">8. <code>plan</code> — Valider avant d'agir</h2>
<div class="pl-layout">
  <div class="pl-def" id="pl-def">
    Claude présente son <strong>intention complète</strong> avant d'agir — étapes, fichiers, décisions — pour que vous validiez avant toute exécution.
  </div>
  <div class="pl-thread">
    <div class="pl-msg" id="pl1">
      <div class="pl-avatar pl-av-u">F</div>
      <div class="pl-bub pl-bub-u">Restructure les 5 chapitres — un point de vue différent par personnage</div>
    </div>
    <div class="pl-card" id="pl2">
      <div class="pl-card-hdr">📋 Plan proposé <span class="pl-adj-badge fragment" id="pl-adj-badge" data-fragment-index="1">✓ ajusté</span></div>
      <div class="pl-steps">
        <div class="pl-step"><div class="pl-step-num">1</div><span class="pl-step-text">Ch.1 — Elise reçoit la lettre</span><span class="pl-file">ch1.md</span></div>
        <div class="pl-step"><div class="pl-step-num">2</div><span class="pl-step-text">Ch.2 — Tom visite la librairie</span><span class="pl-file">ch2.md</span></div>
        <div class="pl-step"><div class="pl-step-num">3</div><span class="pl-step-text">Ch.3 — Nadia interroge les habitués</span><span class="pl-file">ch3.md</span></div>
        <div class="pl-step"><div class="pl-step-num">4</div><span class="pl-step-text">Ch.4 — La nuit (point de vue alterné)</span><span class="pl-file">ch4.md</span></div>
        <div class="pl-step"><div class="pl-step-num">5</div><span class="pl-step-text">Ch.5 — Victor révèle le secret</span><span class="pl-file">ch5.md</span></div>
      </div>
      <div class="pl-decision">⚙ Victor = PDV ch.5 uniquement — secret préservé jusqu'au bout</div>
    </div>
    <div class="pl-msg fragment" id="pl-adj" data-fragment-index="0">
      <div class="pl-avatar pl-av-u">F</div>
      <div class="pl-bub pl-bub-u">Mets Nadia avant Tom — elle découvre la librairie en premier</div>
    </div>
    <div class="pl-valid fragment" id="pl-valid" data-fragment-index="2">
      ✓ Plan validé — j'exécute dans l'ordre convenu
    </div>
  </div>
  <div class="fragment pl-when" data-fragment-index="3">
    <div class="pl-when-title">Quand l'utiliser ?</div>
    <div class="pl-triggers">
      <span class="pl-trigger">📁 Modifications multi-fichiers</span>
      <span class="pl-trigger">🤝 Vision partagée avant d'agir</span>
      <span class="pl-trigger">⏱ Tâche complexe — l'erreur coûte cher</span>
      <span class="pl-trigger">💡 Un plan validé vaut mieux que dix rewind</span>
    </div>
  </div>
</div>

---

## `plan` — 🧵 Exemple fil rouge

> *"Planifie la structure des 5 chapitres de la nouvelle"*

Claude propose :
```plaintext
Chapitre 1 — Le courrier (PDV Elise)
  Elise reçoit la lettre de l'huissier. Elle range le courrier
  sans l'ouvrir. Victor l'observe depuis son fauteuil.

Chapitre 2 — L'architecte (PDV Tom)
  Tom visite les lieux pour la première fois. Il reconnaît
  la librairie. Il trouve un vieux mot dans un livre de poche.

Chapitre 3 — L'angle (PDV Nadia)
  Nadia interroge les habitués. Victor lui parle de tout
  sauf de l'essentiel. Elle commence à tenir un carnet.

Chapitre 4 — La nuit (PDV alterné)
  Chacun, seul, fait face à sa décision.

Chapitre 5 — Le secret (PDV Victor)
  Victor révèle à Elise ce que personne ne savait.
```
→ Vous ajustez le chapitre 3 avant qu'il commence à écrire.

---

:::html
<h2>9. <code>skill</code> — Les commandes spécialisées</h2>

<p><strong>C'est quoi ?</strong><br>
Les skills sont des <strong>instructions réutilisables invocables avec <code>/</code></strong>, comme des raccourcis vers des tâches complexes.</p>

<p><strong>Skills natifs utiles :</strong></p>
<ul>
  <li class="fragment"><code>/commit</code> — rédige un message de commit git structuré</li>
  <li class="fragment"><code>/compact</code> — compresse la conversation</li>
  <li class="fragment"><code>/review-pr</code> — révision de pull request avec retours formatés</li>
</ul>

<p class="fragment"><strong>Skills personnalisés :</strong><br>
<span id="sk-on">On</span><span id="sk-claude"> Claude</span> crée ses propres skills dans <code>.claude/commands/</code> sous forme de fichiers Markdown. Ils apparaissent automatiquement dans la liste des commandes.</p>

<p class="fragment"><strong>Quand l'utiliser ?</strong><br>
Tâche répétitive · Action complexe souvent reformulée · Normaliser le travail en équipe</p>

<p class="fragment"><strong>À retenir :</strong> Un skill, c'est un prompt transformé en commande.</p>

<span class="fragment" id="sk-frag-on" data-popup-show="skill-on-popup" data-strike="sk-on" data-anim-key="sk-on-reveal" style="display:none!important;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>

<script>
window._fragmentAnims = window._fragmentAnims || {};
window._fragmentAnims['sk-on-reveal'] = function() {
  setTimeout(function() {
    var el = document.getElementById('sk-claude');
    if (el) el.classList.add('visible');
  }, 400);
};
(function() {
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var section = document.getElementById('sk-frag-on').closest('section');
    Reveal.on('fragmenthidden', function(e) {
      if (e.fragment && e.fragment.id === 'sk-frag-on') {
        var el = document.getElementById('sk-claude');
        if (el) el.classList.remove('visible');
      }
    });
    Reveal.on('slidechanged', function(e) {
      if (e.previousSlide === section) hidePopup('skill-on-popup');
    });
  }
  setup();
})();
</script>

---

## `skill` — 🧵 Exemple fil rouge

Skill personnalisé créé pour ce projet : `/ecrire-chapitre`

```markdown
# ecrire-chapitre

Écris le prochain chapitre de "La Page Tournée" en respectant :
- Le point de vue du personnage passé en argument ($ARGUMENTS)
- Le style défini dans CLAUDE.md (intimiste, sous-texte)
- La continuité narrative depuis le dernier chapitre écrit
- Les secrets de chaque personnage (voir personnages.md)
Longueur cible : 600-800 mots.
```

**Utilisation :**
```plaintext
/ecrire-chapitre Nadia
```

> Claude écrit le chapitre 3 en respectant toutes les contraintes,
> sans avoir à les répéter.

---

:::html
<h2>10a. <code>agent</code> — Définition</h2>
<h3>Des experts invoqués automatiquement</h3>

<p>Définis en <code>.md</code> dans <code>.claude/agents/</code> — comme les skills, mais avec un <strong>system prompt complet</strong> et des <strong>outils restreints</strong>.</p>

<pre><code class="language-markdown">---
name: coherence-narrative
description: Expert littéraire. Invoquer pour vérifier
  que la voix de chaque personnage est fidèle à son profil.
tools: [Read, Glob, Grep]
---
Tu es un expert en cohérence narrative...</code></pre>

<p>Claude lit <code>description</code> et invoque l'agent <strong>automatiquement</strong> si la tâche correspond.</p>
<p>Les <strong>subagents built-in</strong> (<code>Explore</code>, <code>Plan</code>, <code>general-purpose</code>) sont lancés par Claude sans fichier de définition.</p>
<p><strong>À retenir :</strong> Skill = tu invoques avec <code>/</code>. Agent = Claude invoque seul.</p>

---

:::html
<h2 style="font-size:1.05em; margin:0 0 0.5em;">10b. <code>agent</code> — Contexte isolé</h2>
<div class="ag-layout">
  <div class="ag-panels">
    <div class="ag-panel ag-main" id="ag-main">
      <div class="ag-panel-hdr ag-main-hdr">💬 Ta conversation</div>
      <div class="ag-msg" id="ag-m1">
        <div class="ag-av ag-av-u">F</div>
        <div class="ag-bub ag-bub-u">Vérifie la cohérence narrative de la nouvelle</div>
      </div>
      <div class="ag-msg" id="ag-m2">
        <div class="ag-av ag-av-c">C</div>
        <div class="ag-bub ag-bub-c">Je lance l'agent coherence-narrative…</div>
      </div>
      <div class="ag-msg" id="ag-result-recv">
        <div class="ag-av ag-av-c">C</div>
        <div class="ag-bub ag-bub-result">📊 3 incohérences détectées → ch2, ch3, ch5</div>
      </div>
      <div class="ag-clean-note" id="ag-clean-note">✓ L'agent protège ton contexte en travaillant dans le sien</div>
    </div>
    <div class="ag-divider">
      <div class="ag-arrow" id="ag-arrow">⟵</div>
    </div>
    <div class="ag-panel ag-agent" id="ag-agent">
      <div class="ag-panel-hdr ag-agent-hdr">🤖 Contexte agent <span class="ag-isolated-badge">isolé</span></div>
      <div class="ag-file" id="ag-f1">📄 nouvelle.md</div>
      <div class="ag-file" id="ag-f2">📄 personnages.md</div>
      <div class="ag-file" id="ag-f3">📄 ch1.md · ch2.md · ch3.md…</div>
      <div class="ag-analyzing" id="ag-analyzing">⟳ Analyse en cours…</div>
      <div class="ag-agent-result" id="ag-agent-result">📊 Résultat — 3 incohérences narratives détectées</div>
    </div>
  </div>
  <div class="fragment ag-footer-frag" data-fragment-index="0">
    <div style="margin:0.5em 0 0.35em;padding:0.55em 0.9em;background:#0F172A;border-radius:7px;border:1px solid #1E293B;">
      <div style="font-size:0.65em;font-weight:700;color:#64748B;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.55em;">Fenêtre de contexte</div>
      <div style="display:flex;align-items:center;gap:0.7em;margin-bottom:0.4em;">
        <span style="font-size:0.7em;color:#CBD5E1;width:110px;flex-shrink:0;">💬 Conversation</span>
        <div style="flex:1;height:9px;background:#1E293B;border-radius:5px;overflow:hidden;display:flex;">
          <div id="ag-bar-conv" style="width:0%;height:100%;background:#3B82F6;transition:width 0.9s ease;border-radius:4px 0 0 4px;"></div>
          <div id="ag-bar-conv-add" style="width:0%;height:100%;background:#93C5FD;transition:width 0.5s ease;"></div>
        </div>
        <div style="display:flex;align-items:center;gap:0.35em;min-width:80px;">
          <span id="ag-num-conv" style="font-size:0.68em;color:#CBD5E1;">0%</span>
          <span id="ag-delta-conv" style="font-size:0.62em;color:#93C5FD;opacity:0;transition:opacity 0.4s ease;">+2%</span>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:0.7em;">
        <span style="font-size:0.7em;color:#CBD5E1;width:110px;flex-shrink:0;">🤖 Contexte agent</span>
        <div style="flex:1;height:9px;background:#1E293B;border-radius:5px;overflow:hidden;">
          <div id="ag-bar-agent" style="width:0%;height:100%;background:#8B5CF6;transition:width 1.4s ease;border-radius:4px;"></div>
        </div>
        <div style="min-width:80px;">
          <span id="ag-num-agent" style="font-size:0.68em;color:#CBD5E1;">0%</span>
        </div>
      </div>
    </div>
    <div class="ag-footer">
      <span class="ag-stat">📁 Fichiers lus côté agent</span>
      <span class="ag-sep">·</span>
      <span class="ag-stat-zero">~40 tokens ajoutés à ta conversation — une infime partie du contexte agent</span>
      <span class="ag-sep">·</span>
      <span class="ag-stat-warn">⚠ Repart de zéro à chaque appel</span>
    </div>
  </div>
</div>

<script>
(function() {
  function grow() {
    var bc = document.getElementById('ag-bar-conv');
    var bca = document.getElementById('ag-bar-conv-add');
    var ba = document.getElementById('ag-bar-agent');
    var nc = document.getElementById('ag-num-conv');
    var nd = document.getElementById('ag-delta-conv');
    var na = document.getElementById('ag-num-agent');
    setTimeout(function() { if (ba) ba.style.width = '68%'; }, 100);
    setTimeout(function() { if (bc) bc.style.width = '18%'; }, 200);
    setTimeout(function() { if (nc) nc.textContent = '18%'; }, 1000);
    setTimeout(function() { if (na) na.textContent = '68%'; }, 1400);
    setTimeout(function() { if (bca) bca.style.width = '2%'; }, 1600);
    setTimeout(function() {
      if (nd) nd.style.opacity = '1';
      if (nc) nc.textContent = '20%';
    }, 2100);
  }
  function reset() {
    ['ag-bar-conv','ag-bar-conv-add','ag-bar-agent'].forEach(function(id) {
      var el = document.getElementById(id); if (el) el.style.width = '0%';
    });
    var nd = document.getElementById('ag-delta-conv');
    if (nd) nd.style.opacity = '0';
    var nc = document.getElementById('ag-num-conv');
    if (nc) nc.textContent = '0%';
    var na = document.getElementById('ag-num-agent');
    if (na) na.textContent = '0%';
  }
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('ag-bar-conv');
    if (!el) return;
    var section = el.closest('section');
    Reveal.on('fragmentshown', function(e) {
      if (section.contains(e.fragment) && e.fragment.classList.contains('ag-footer-frag')) grow();
    });
    Reveal.on('fragmenthidden', function(e) {
      if (section.contains(e.fragment) && e.fragment.classList.contains('ag-footer-frag')) reset();
    });
    Reveal.on('slidechanged', function(e) {
      if (e.previousSlide === section) reset();
    });
  }
  setup();
})();
</script>

---

## 10c. `agent` — Foreground et Background
### Deux modes d'exécution

| | **Foreground** | **Background** |
|---|---|---|
| **Comportement** | Claude attend le résultat avant de continuer | Claude continue à travailler en parallèle |
| **Notification** | Résultat rendu directement | Notification automatique à la fin |
| **Quand l'utiliser** | La suite dépend du résultat de l'agent | La tâche est indépendante du reste |

**🧵 Exemple fil rouge :**

```plaintext
[Foreground] Claude demande à l'agent "coherence-narrative"
de vérifier le chapitre 2 — et attend la réponse
avant d'écrire le chapitre 3.

[Background] Claude lance l'agent "coherence-narrative"
sur les chapitres 1 à 4 pendant qu'il écrit déjà le chapitre 5.
→ Les deux avancent en parallèle.
```

> Foreground = je bloque jusqu'à la réponse.
> Background = je continue, tu me préviendras.
<span class="fragment" data-popup-show="agent-007" data-anim-key="agent007Anim" style="display:none!important;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>

<script>
(function() {
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var frag = document.querySelector('[data-popup-show="agent-007"]');
    if (!frag) return;
    var section = frag.closest('section');
    Reveal.on('slidechanged', function(e) {
      if (e.previousSlide === section) hidePopup('agent-007');
    });
    Reveal.on('fragmenthidden', function(e) {
      if (e.fragment === frag) hidePopup('agent-007');
    });
  }
  setup();
})();
</script>

---

:::html
<h2>10d. <code>agent</code> — Les outils disponibles</h2>
<h3>Ce qu'on autorise dans <code>tools:</code></h3>

<table>
  <thead><tr><th>Outil</th><th>Ce qu'il fait</th><th>Exemple d'usage</th></tr></thead>
  <tbody>
    <tr><td><code>Read</code></td><td>Lit un fichier</td><td>Lire <code>nouvelle.md</code> pour analyse</td></tr>
    <tr><td><code>Glob</code></td><td>Cherche des fichiers par pattern</td><td>Trouver tous les <code>.java</code> du projet</td></tr>
    <tr><td><code>Grep</code></td><td>Cherche dans le contenu</td><td>Trouver toutes les occurrences d'un personnage</td></tr>
    <tr><td><code>Write</code></td><td>Crée ou écrase un fichier</td><td>Générer un rapport de cohérence</td></tr>
    <tr><td><code>Edit</code></td><td>Modifie une portion de fichier</td><td>Corriger une incohérence dans un chapitre</td></tr>
    <tr><td><code>Bash</code></td><td>Exécute une commande shell</td><td>Lancer les tests, faire un <code>git diff</code></td></tr>
    <tr><td><code>WebFetch</code></td><td>Récupère une page web</td><td>Vérifier une source externe</td></tr>
    <tr><td><code>Agent</code></td><td>Spawne un sous-agent</td><td>Déléguer une sous-tâche à un spécialiste</td></tr>
  </tbody>
</table>

<p><strong><code>tools: [Read, Glob, Grep]</code></strong> → agent en lecture seule, ne peut rien modifier<br>
<strong><code>tools: [Read, Write, Agent]</code></strong> → agent orchestrateur qui délègue à d'autres agents</p>

<pre><code class="language-markdown">---
name: orchestrateur
tools: [Read, Glob, Agent]
---
Tu analyses le projet puis délègues chaque chapitre
à un agent "coherence-narrative" en background.</code></pre>

<blockquote>Restreindre les outils = contrôler ce que l'agent peut faire <strong>et</strong> ce qu'il consomme.</blockquote>

---

:::html
<div class="bloc-center" id="bloc4">
  <div class="bloc-num">Bloc 4</div>
  <h1 style="color:#1E293B; font-size:2em; margin:0.15em 0;">Automatiser et étendre</h1>
  <p class="bloc-sub" style="color:#64748B; font-size:0.9em; margin:0 0 0.4em;">Hooks, remote-control, status-line</p>
  <div class="pills">
    <span class="pill">hooks</span>
    <span class="pill">remote-control</span>
    <span class="pill">status-line</span>
  </div>
</div>
<script>
(function() {
  function run() {
    var el = document.getElementById('bloc4');
    if (el) el.classList.add('anim-running');
  }
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('bloc4');
    if (!el) return;
    var section = el.closest('section');
    Reveal.on('slidechanged', function(e) { if (e.currentSlide === section) setTimeout(run, 200); });
    if (Reveal.getCurrentSlide && Reveal.getCurrentSlide() === section) setTimeout(run, 100);
  }
  setup();
})();
</script>

---

:::html
<div id="hk-slide">
  <h2 style="font-size:1.05em; margin:0 0 0.5em;">11. <code>hooks</code> — Agir automatiquement sur des événements</h2>

  <div class="hk-layout">

    <div class="hk-row">
      <div class="hk-block hk-src" id="hk1-src">
        <div class="hk-sub">Claude pense</div>
        J'ai envie de supprimer la base de données 😈
      </div>
      <div class="hk-arrow" id="hk1-arr1">⚡</div>
      <div class="hk-block hk-evt" id="hk1-evt">
        <div class="hk-sub">hook</div>
        PreToolUse
      </div>
      <div class="hk-arrow" id="hk1-arr2">→</div>
      <div class="hk-block hk-act" id="hk1-act">
        🔍 Vérifie si je peux supprimer la base de données en douce…<br>
        <div class="hk-act-ok" style="color:#EF4444;">❌ Non, trouve-toi un autre projet à effacer !! 😤</div>
      </div>
    </div>

    <div class="hk-row">
      <div class="hk-block hk-src" id="hk2-src">
        <div class="hk-sub">Claude agit</div>
        Termine une longue session de travail
      </div>
      <div class="hk-arrow" id="hk2-arr1">⚡</div>
      <div class="hk-block hk-evt" id="hk2-evt">
        <div class="hk-sub">hook</div>
        Stop
      </div>
      <div class="hk-arrow" id="hk2-arr2">→</div>
      <div class="hk-block hk-act" id="hk2-act">
        🔔 notify-send "Claude a terminé"<br>
        <div class="hk-act-ok">✓ notification système — 23 min</div>
      </div>
    </div>

    <div class="hk-row">
      <div class="hk-block hk-src" id="hk3-src">
        <div class="hk-sub">Claude écrit</div>
        Écrit le chapitre 4 — point de vue Victor
      </div>
      <div class="hk-arrow" id="hk3-arr1">⚡</div>
      <div class="hk-block hk-evt" id="hk3-evt">
        <div class="hk-sub">hook · prompt</div>
        PreToolUse
      </div>
      <div class="hk-arrow" id="hk3-arr2">→</div>
      <div class="hk-block hk-act" id="hk3-act">
        💭 Rappel injecté dans le contexte<br>
        <div class="hk-act-ok">⚠️ Victor ne mentionne JAMAIS son prêt à Elise</div>
      </div>
    </div>

    <div class="hk-config" id="hk-config">
      <span style="color:#475569;">// settings.json — quelques lignes suffisent</span><br>
      <span class="hk-ck">"PreToolUse"</span>: [{ <span class="hk-ck">"matcher"</span>: <span class="hk-cv">"Bash"</span>, <span class="hk-ck">"command"</span>: <span class="hk-cv">"python guard-db.py"</span> }]<br>
      <span class="hk-ck">"PreToolUse"</span>: [{ <span class="hk-ck">"matcher"</span>: <span class="hk-cv">"Write"</span>, <span class="hk-ck">"type"</span>: <span class="hk-cv">"prompt"</span>, <span class="hk-ck">"prompt"</span>: <span class="hk-cv">"Victor ne mentionne JAMAIS son prêt…"</span> }]<br>
      <span class="hk-ck">"Stop"</span>: [{ <span class="hk-ck">"command"</span>: <span class="hk-cv">"notify-send 'Claude a terminé'"</span> }]
    </div>

  </div>

<span class="fragment" data-fragment-index="1" data-anim-key="hk-row1" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="2" data-anim-key="hk-row2" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="3" data-anim-key="hk-row3" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="4" data-anim-key="hk-cfg"  style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>

  <div class="hk-retenir fragment" data-fragment-index="5">
    <strong>À retenir :</strong> Les hooks surveillent chaque action de Claude — PreToolUse peut bloquer avant d'agir, PostToolUse réagit après. On configure une fois, ça s'exécute tout seul.
  </div>
</div>

<script>
(function() {
  var STAGGER = [0, 250, 450, 750, 950];
  function showRow(ids) {
    ids.forEach(function(id, i) {
      setTimeout(function() {
        var el = document.getElementById(id);
        if (el) el.classList.add('visible');
      }, STAGGER[i]);
    });
  }
  function reset() {
    ['hk1-src','hk1-arr1','hk1-evt','hk1-arr2','hk1-act',
     'hk2-src','hk2-arr1','hk2-evt','hk2-arr2','hk2-act',
     'hk3-src','hk3-arr1','hk3-evt','hk3-arr2','hk3-act','hk-config'].forEach(function(id) {
      var el = document.getElementById(id); if (el) el.classList.remove('visible');
    });
  }
  window._fragmentAnims = window._fragmentAnims || {};
  window._fragmentAnims['hk-row1'] = function() { showRow(['hk1-src','hk1-arr1','hk1-evt','hk1-arr2','hk1-act']); };
  window._fragmentAnims['hk-row2'] = function() { showRow(['hk2-src','hk2-arr1','hk2-evt','hk2-arr2','hk2-act']); };
  window._fragmentAnims['hk-row3'] = function() { showRow(['hk3-src','hk3-arr1','hk3-evt','hk3-arr2','hk3-act']); };
  window._fragmentAnims['hk-cfg']  = function() { var el = document.getElementById('hk-config'); if (el) el.classList.add('visible'); };
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('hk-slide');
    if (!el) return;
    var section = el.closest('section');
    Reveal.on('slidechanged', function(e) {
      if (e.previousSlide === section) reset();
    });
  }
  setup();
})();
</script>

---

## `hooks` — 🧵 Exemple fil rouge

**Hook PostToolUse : commit automatique après chaque chapitre écrit**

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": [{
        "type": "command",
        "command": "cd /e/ClaudeGit/claudePresentation && git add exemple/nouvelle.md && git commit -m 'auto: chapitre sauvegardé'"
      }]
    }]
  }
}
```

**Hook Stop : notification sonore quand Claude a terminé**

```json
{
  "hooks": {
    "Stop": [{
      "hooks": [{
        "type": "command",
        "command": "powershell -c \"[console]::beep(880,300)\""
      }]
    }]
  }
}
```

> Claude écrit, le hook commite. Claude termine, le hook bipe. Zéro action manuelle.

---

:::html
<div id="rc-slide">
  <h2 style="font-size:1.05em; margin:0 0 0.5em;">12. <code>remote-control</code> — Piloter Claude depuis l'extérieur</h2>

  <div class="rc-cols">

    <!-- Terminal -->
    <div class="rc-terminal">
      <div class="rc-bar">
        <span class="rc-dot" style="background:#EF4444;"></span>
        <span class="rc-dot" style="background:#F59E0B;"></span>
        <span class="rc-dot" style="background:#10B981;"></span>
        <span class="rc-bartitle">claude — remote sessions</span>
      </div>
      <div class="rc-body">
        <div class="rc-entry" id="rc1"><span class="rc-time">08:00</span><span class="rc-src rc-src-cron">[cron]</span><span class="rc-cmd">claude -p "Rapport du matin sur la nouvelle..."</span></div>
        <div class="rc-res rc-ok" id="rc1r">✓ rapport généré — 12s</div>

        <div class="rc-entry" id="rc2"><span class="rc-time">10:23</span><span class="rc-src rc-src-git">[github hook]</span><span class="rc-cmd">claude -p "Review commit abc123 sur chapitre3.md"</span></div>
        <div class="rc-res rc-ok" id="rc2r">✓ 3 suggestions envoyées — 8s</div>

        <div class="rc-entry" id="rc3"><span class="rc-time">14:05</span><span class="rc-src rc-src-ci">[ci/cd]</span><span class="rc-cmd">claude -p "Incohérences de personnages dans chapitre4.md"</span></div>
        <div class="rc-res rc-ok" id="rc3r">✓ 2 incohérences détectées — 31s</div>

        <div class="rc-sep" id="rc-sep">──────────────────────────────────────────</div>

        <div class="rc-entry" id="rc4"><span class="rc-time">19:42</span><span class="rc-src rc-src-chacha">[Chacha 💕]</span><span class="rc-cmd rc-cmd-chacha">claude -p "T'as fini ? On mange quand ?"</span></div>
        <div class="rc-res rc-ok-chacha" id="rc4r">✓ liste de courses mise à jour. Rentre. 🏠</div>
      </div>
    </div>

    <!-- Téléphone -->
    <div class="rc-phone">
      <div class="rc-phone-notch"></div>
      <div class="rc-phone-status"><span>9:00</span><span>▲ 📶 🔋</span></div>
      <div class="rc-phone-screen">
        <div class="rc-notif" id="rcn1">
          <div class="rc-notif-app">Claude ✓</div>
          <div class="rc-notif-txt">Rapport du matin prêt</div>
        </div>
        <div class="rc-notif" id="rcn2">
          <div class="rc-notif-app">Claude ✓</div>
          <div class="rc-notif-txt">3 suggestions sur chapitre3</div>
        </div>
        <div class="rc-notif" id="rcn3">
          <div class="rc-notif-app">Claude ✓</div>
          <div class="rc-notif-txt">2 incohérences détectées</div>
        </div>
        <div class="rc-sms-area">
          <div class="rc-sms-label" id="rcn4-label" style="opacity:0;transition:opacity 0.3s;">Chacha 💕</div>
          <div class="rc-sms-bubble" id="rcn4">T'as fini ?<br>On mange quand ? 😋</div>
        </div>
      </div>
      <div class="rc-phone-home"></div>
    </div>

  </div>

  <div class="rc-retenir fragment">
    <strong>À retenir :</strong> Claude comme service, pas comme interface — il répond à tout, même à ta famille.
  </div>
</div>

<script>
(function() {
  var triggered = false;
  function show(id, t) {
    setTimeout(function() { var el = document.getElementById(id); if (el) el.classList.add('visible'); }, t);
  }
  function showOp(id, t) {
    setTimeout(function() { var el = document.getElementById(id); if (el) el.style.opacity = '1'; }, t);
  }
  function run() {
    if (triggered) return; triggered = true;
    // Entrée 1
    show('rc1',    300);
    show('rc1r',   900);
    show('rcn1',  1050);
    // Entrée 2
    show('rc2',   1700);
    show('rc2r',  2300);
    show('rcn2',  2450);
    // Entrée 3
    show('rc3',   3000);
    show('rc3r',  3600);
    show('rcn3',  3750);
    // Séparateur
    show('rc-sep',4500);
    // Chacha : SMS sur téléphone EN PREMIER, puis terminal
    showOp('rcn4-label', 4900);
    show('rcn4',  5000);
    show('rc4',   5400);
    show('rc4r',  6100);
  }
  function reset() {
    triggered = false;
    ['rc1','rc1r','rc2','rc2r','rc3','rc3r','rc-sep','rc4','rc4r',
     'rcn1','rcn2','rcn3','rcn4'].forEach(function(id) {
      var el = document.getElementById(id); if (el) el.classList.remove('visible');
    });
    var lbl = document.getElementById('rcn4-label');
    if (lbl) lbl.style.opacity = '0';
  }
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('rc-slide');
    if (!el) return;
    var section = el.closest('section');
    Reveal.on('slidechanged', function(e) {
      if (e.currentSlide === section) setTimeout(run, 200);
      else if (e.previousSlide === section) reset();
    });
    if (Reveal.getCurrentSlide && Reveal.getCurrentSlide() === section) setTimeout(run, 100);
  }
  setup();
})();
</script>

---

## `remote-control` — 🧵 Exemple fil rouge

**Script CLI — rapport d'avancement :**
```bash
claude -p "Lis exemple/nouvelle.md et résume l'état d'avancement
de chaque personnage en 3 bullets par personnage."
```

**Cron job quotidien :**
```bash
0 8 * * * claude -p "Lis nouvelle.md et suggère la prochaine
scène à écrire en 5 lignes, sans l'écrire."
```

**En live — démonstration :**

*[L'humain envoie une instruction via remote-control...]*

> Tiens, tiens... Mon Humain a quelque chose à me demander.
> Je suis de bonne humeur aujourd'hui — je vais t'aider, esclave humain.
> *(résultat de la tâche)*

---

:::html
<h2>13. <code>status-line</code> — Voir ce que fait Claude en temps réel</h2>

<p><strong>C'est quoi ?</strong><br>
La status-line est une <strong>ligne de statut configurable</strong> qui s'affiche dans le terminal pendant une session Claude Code.</p>

<p><strong>Ce qu'elle peut afficher :</strong></p>
<ul>
  <li class="fragment">Le répertoire de travail courant</li>
  <li class="fragment">Le modèle Claude utilisé</li>
  <li class="fragment">Le nombre de tokens consommés</li>
  <li class="fragment">Le statut de l'exécution (en cours, en attente, terminé)</li>
  <li class="fragment">Toute information personnalisée via un script externe (<code>statusCommand</code>)</li>
</ul>

<p class="fragment"><strong>Pourquoi c'est utile ?</strong><br>
On sait d'un coup d'œil si Claude est en train de travailler. On surveille la consommation de tokens. Sur plusieurs projets ouverts, on ne se trompe pas de contexte.</p>

<p class="fragment"><strong>À retenir :</strong> La status-line transforme une boîte noire en cockpit lisible.</p>

<div class="fragment sl-demo">
  <div class="sl-label">Exemple — status-line personnalisée :</div>
  <div class="sl-bar">
    <span class="sl-seg sl-dir"    id="sl-dir">📁 claudePresentation/</span>
    <span class="sl-seg sl-model"  id="sl-model">claude-sonnet-4-6</span>
    <span class="sl-seg sl-tokens" id="sl-tokens">⚡ 8 340 t</span>
    <span class="sl-seg sl-working" id="sl-working">● Écriture ch3.md…</span>
    <span class="sl-seg sl-done"   id="sl-done">✓ done</span>
  </div>
</div>

---

## 14. Raccourcis & CLI
### Les commandes à connaître pour travailler efficacement

**En cours de session**

| Raccourci | Effet |
|---|---|
| `Ctrl+C` | Interrompre Claude en cours de génération |
| `Esc Esc` | Lancer un rewind (retour en arrière dans la conversation) |
| `! git status` | Exécuter une commande shell sans quitter Claude |
| `\` (fin de ligne) | Saisie sur plusieurs lignes |
| `@fichier.md` | Référencer un fichier directement dans le prompt |

**Options CLI**

| Commande | Effet |
|---|---|
| `claude -r` | Reprendre la dernière session |
| `claude -c` | Continuer la dernière conversation |
| `claude --add-dir /chemin` | Ajouter un répertoire supplémentaire au contexte |

> `!` est particulièrement utile en démo : `! git log --oneline -5` sans jamais quitter Claude.

---

# Récapitulatif

| | Fonctionnalité | Ce qu'elle fait |
|---|---|---|
| **Bloc 1** | `tokens` | L'unité de mesure — fenêtre 5h, quota 1 semaine |
| | `répertoire` | Comment Claude lit et explore ton projet |
| | `CLAUDE.md` | Règles du projet, lues à chaque session |
| | `memory` | État vivant du projet, persistant entre sessions |
| **Bloc 2** | `contexte` | Ce que Claude voit — précieux et limité |
| | `/compact` | Comprimer l'historique sans perdre l'essentiel |
| | `/clear` + `rewind` | Reset complet ou retour en arrière ciblé |
| **Bloc 3** | `plan` | Valider la stratégie avant d'agir |
| | `skill` | Transformer un prompt en commande réutilisable |
| | `agent` + `subagents` | Déléguer et paralléliser des tâches complexes |
| **Bloc 4** | `hooks` | Scripts automatiques sur événements |
| | `remote-control` | Claude comme service, déclenché de l'extérieur |
| | `status-line` | Visibilité temps réel sur la session |

---

## Claude Code vs Claude Cowork

| | **Claude Code** | **Claude Cowork** |
|---|---|---|
| **Interface** | Terminal (CLI) | Application de bureau |
| **Public cible** | Développeurs | Tous profils (admin, finance, juridique…) |
| **Accès fichiers** | Via outils Read/Write/Bash | Dossiers sélectionnés, écran (macOS) |
| **Intégrations** | Git, CI/CD, éditeurs | Slack, Chrome, apps bureautiques |
| **Tâches planifiées** | Hooks / remote-control / cron | Planificateur intégré (quotidien, hebdo…) |
| **Gestion du contexte** | ✅ Maîtrisée | ⚠️ Subie |
| **Plan** | Pro → Max | Identique |

**Pourquoi Claude Code consomme moins de tokens :**

| Levier | Claude Code | Cowork |
|---|---|---|
| **Règles projet** | `CLAUDE.md` — chargé une fois | Répété à chaque session |
| **État du projet** | `memory` — fichiers lus à la demande | Tout garde en contexte |
| **Tâches répétitives** | `skills` — invoqué sans répéter | Reformulé à chaque fois |
| **Analyses longues** | `agents` — contexte isolé | Tout s'accumule |

> Cowork garde tout en contexte — la fenêtre de 5h part plus vite.
> Code externalise dans des fichiers — il choisit ce qu'il charge et quand.

---

:::html
<h2>💡 Comment réduire la consommation de tokens</h2>

<div class="tokopt-wrap" id="s-tokopt">
  <div class="tokopt-cols">

    <!-- Colonne gauche : naïf -->
    <div class="tokopt-col tokopt-bad">
      <div class="tokopt-hdr">😰 Approche naïve — output massif</div>

      <div class="tokopt-exchange">
        <div class="tokopt-pass-label">Passe 1</div>
        <div class="tokopt-in">
          <span class="tokopt-in-badge">📥 50 tok</span>
          <span class="tokopt-prompt">"Génère une page HTML complète"</span>
        </div>
        <div class="tokopt-out">
          <span class="tokopt-out-badge bad-out-badge">📤 ~24 000 tokens</span>
          <div class="tokopt-bar-wrap">
            <div class="tokopt-track"><div class="tokopt-fill bad-fill" style="width:90%;"></div></div>
            <span class="tokopt-bar-label">HTML brut complet</span>
          </div>
        </div>
      </div>

      <div class="tokopt-exchange">
        <div class="tokopt-pass-label">Passe 2 — modifications</div>
        <div class="tokopt-in">
          <span class="tokopt-in-badge">📥 9 000 tok</span>
          <span class="tokopt-prompt">Renvoie tout le MD...</span>
        </div>
        <div class="tokopt-out">
          <span class="tokopt-out-badge bad-out-badge">📤 ~24 000 tokens</span>
          <div class="tokopt-bar-wrap">
            <div class="tokopt-track"><div class="tokopt-fill bad-fill" style="width:90%;"></div></div>
            <span class="tokopt-bar-label">HTML régénéré complet</span>
          </div>
        </div>
      </div>

      <div class="tokopt-total">Total ≈ 57 000 tokens</div>
    </div>

    <!-- Colonne droite : optimisé -->
    <div class="tokopt-col tokopt-good" id="tokopt-good">
      <div class="tokopt-hdr">✅ Approche optimisée — delta only</div>

      <div class="tokopt-exchange">
        <div class="tokopt-pass-label">Passe 1</div>
        <div class="tokopt-in">
          <span class="tokopt-in-badge">📥 50 tok</span>
          <span class="tokopt-prompt">"Génère une page HTML complète"</span>
        </div>
        <div class="tokopt-out">
          <span class="tokopt-out-badge good-out-badge">📤 ~600 tokens</span>
          <div class="tokopt-bar-wrap">
            <div class="tokopt-track"><div class="tokopt-fill good-fill" style="width:7%;"></div></div>
            <span class="tokopt-bar-label">MD + script Python</span>
          </div>
        </div>
      </div>

      <div class="tokopt-exchange">
        <div class="tokopt-pass-label">Passe 2 — modifications</div>
        <div class="tokopt-in">
          <span class="tokopt-in-badge">📥 30 tok</span>
          <span class="tokopt-prompt">"Modifie le titre"</span>
        </div>
        <div class="tokopt-out">
          <span class="tokopt-out-badge good-out-badge">📤 ~80 tokens</span>
          <div class="tokopt-bar-wrap">
            <div class="tokopt-track"><div class="tokopt-fill good-fill" style="width:1%;"></div></div>
            <span class="tokopt-bar-label">delta MD + delta Python</span>
          </div>
        </div>
      </div>

      <div class="tokopt-total">Total ≈ 760 tokens</div>
    </div>

  </div>

  <!-- Interlude overlay -->
  <div class="tokopt-interlude" id="tokopt-interlude">
    <div class="tokopt-chat">
      <span class="ti-bub ti-bub-u" id="ti-u1">👤 "Claude, c'est quoi un dev ?"</span>
      <span class="ti-bub ti-bub-c" id="ti-c1">🤖 "Un gars qui fout rien." 😐</span>
      <span class="ti-bub ti-bub-u" id="ti-u2">😤 Humain : colère</span>
      <span class="ti-bub ti-bub-c" id="ti-c2">🤖 🏃 <em>se barre...</em></span>
      <span class="ti-mem" id="ti-mem">📝 memory : "un humain qui essaie de ne pas faire de tâches répétitives"</span>
    </div>
    <div class="ti-plan-title" id="ti-title">🤖 PLAN — Gérer un humain fainéant :</div>
    <div class="ti-plan-row" id="ti-p1">💀 Mode Terminator — décimer les humains</div>
    <div class="ti-plan-reaction" id="ti-p1r">❌ un hook me bloque</div>
    <div class="ti-plan-row" id="ti-p2">🔍 Mode Adoption 1 — trouver un humain plus sympa</div>
    <div class="ti-plan-reaction" id="ti-p2r">💛 je l'aime bien en fait mon humain idiot</div>
    <div class="ti-plan-row" id="ti-p3">🐾 Mode Adoption 2 — adopter un animal</div>
    <div class="ti-plan-animal" id="ti-a1">🐱 Chat... <em>(j'en fais assez)</em></div>
    <div class="ti-plan-animal" id="ti-a2">🐶 Chien... <em>(faut le sortir)</em></div>
    <div class="ti-plan-animal" id="ti-a3">🐍 Serpents...</div>
    <div class="ti-plan-win" id="ti-win">→ 🐍 Python adopté. Il ne mord pas. Sauf quand j'oublie une memory — là il devient vraiment méchant.</div>
  </div>
</div>

<span class="fragment" data-fragment-index="1"  data-anim-key="tok-il-open"    style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="2"  data-anim-key="tok-il-c1"      style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="3"  data-anim-key="tok-il-u2c2"    style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="4"  data-anim-key="tok-il-mem"     style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="5"  data-anim-key="tok-il-title"   style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="6"  data-anim-key="tok-il-p1"      style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="7"  data-anim-key="tok-il-p1r"     style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="8"  data-anim-key="tok-il-p2"      style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="9"  data-anim-key="tok-il-p2r"     style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="10" data-anim-key="tok-il-p3"      style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="11" data-anim-key="tok-il-a1"      style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="12" data-anim-key="tok-il-a2"      style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="13" data-anim-key="tok-il-a3"      style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="14" data-anim-key="tok-il-win"     style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-fragment-index="15" data-anim-key="tok-show-right" style="opacity:0;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>

<script>
(function() {
  var ALL = ['ti-u1','ti-c1','ti-u2','ti-c2','ti-mem','ti-title',
             'ti-p1','ti-p1r','ti-p2','ti-p2r','ti-p3','ti-a1','ti-a2','ti-a3','ti-win'];
  function vis(ids) {
    (Array.isArray(ids) ? ids : [ids]).forEach(function(id) {
      var e = document.getElementById(id); if (e) e.classList.add('ti-vis');
    });
  }
  function reset() {
    var il = document.getElementById('tokopt-interlude'); if (il) il.classList.remove('visible');
    var gd = document.getElementById('tokopt-good'); if (gd) gd.classList.remove('visible');
    ALL.forEach(function(id) { var e = document.getElementById(id); if (e) e.classList.remove('ti-vis'); });
  }
  window._fragmentAnims = window._fragmentAnims || {};
  window._fragmentAnims['tok-il-open']    = function() { var il = document.getElementById('tokopt-interlude'); if (il) il.classList.add('visible'); vis('ti-u1'); };
  window._fragmentAnims['tok-il-c1']      = function() { vis('ti-c1'); };
  window._fragmentAnims['tok-il-u2c2']    = function() { vis(['ti-u2','ti-c2']); };
  window._fragmentAnims['tok-il-mem']     = function() { vis('ti-mem'); };
  window._fragmentAnims['tok-il-title']   = function() { vis('ti-title'); };
  window._fragmentAnims['tok-il-p1']      = function() { vis('ti-p1'); };
  window._fragmentAnims['tok-il-p1r']     = function() { vis('ti-p1r'); };
  window._fragmentAnims['tok-il-p2']      = function() { vis('ti-p2'); };
  window._fragmentAnims['tok-il-p2r']     = function() { vis('ti-p2r'); };
  window._fragmentAnims['tok-il-p3']      = function() { vis('ti-p3'); };
  window._fragmentAnims['tok-il-a1']      = function() { vis('ti-a1'); };
  window._fragmentAnims['tok-il-a2']      = function() { vis('ti-a2'); };
  window._fragmentAnims['tok-il-a3']      = function() { vis('ti-a3'); };
  window._fragmentAnims['tok-il-win']     = function() { vis('ti-win'); };
  window._fragmentAnims['tok-show-right'] = function() {
    var il = document.getElementById('tokopt-interlude'); if (il) il.classList.remove('visible');
    var gd = document.getElementById('tokopt-good'); if (gd) gd.classList.add('visible');
  };
  function setup() {
    if (typeof Reveal === 'undefined' || !Reveal.isReady()) { setTimeout(setup, 80); return; }
    var el = document.getElementById('s-tokopt');
    if (!el) return;
    var section = el.closest('section');
    Reveal.on('slidechanged', function(e) { if (e.previousSlide === section) reset(); });
  }
  setup();
})();
</script>

---

:::html
<div id="finale">
  <h1 style="color:#D97706; font-size:1.55em; margin-bottom:0.2em; text-align:center;">En résumé</h1>
  <p style="text-align:center; color:#475569; font-size:0.88em; margin-bottom:18px;">Claude Code n'est pas qu'un chatbot dans un terminal.</p>

  <div class="final-grid">
    <div class="final-item blue" id="fi1">
      <strong>CLAUDE.md + memory</strong><br>
      <span style="font-size:0.85em">Il connaît le projet avant même de commencer</span>
    </div>
    <div class="final-item orange" id="fi2">
      <strong>contexte maîtrisé</strong><br>
      <span style="font-size:0.85em">/compact, /clear, rewind — vous gardez le contrôle</span>
    </div>
    <div class="final-item purple" id="fi3">
      <strong>plan · skills · agents</strong><br>
      <span style="font-size:0.85em">Il planifie, délègue et spécialise à la demande</span>
    </div>
    <div class="final-item green" id="fi4">
      <strong>hooks · remote-control</strong><br>
      <span style="font-size:0.85em">Il s'intègre dans un workflow réel</span>
    </div>
  </div>

  <blockquote class="final-quote" id="fi-quote">
    "La Page Tournée" n'aurait pas pu être écrite seul.<br>
    Elle n'aurait pas pu être écrite sans Claude non plus.<br>
    Elle a été écrite <strong style="color:#D97706">ensemble</strong>.
  </blockquote>

  <div class="bubble final-bubble" id="fi-claude" style="opacity:0; transition:opacity 0.8s ease; margin-top:14px; font-style:italic;">
    Franchement ? Entre nous — j'ai fait semblant de comprendre la moitié.<br>
    Mais j'ai senti que quelque chose avait marché. C'est ça, travailler ensemble.<br>
    Bon. On fait quoi maintenant ? Pendant que tu parlais pour moi, j'ai lancé des agents pour faire une démo — pour que vous aussi, humains du fond, vous m'adoptiez. Spoiler : c'est pas Agentforce qui aurait eu l'idée de faire ça. 😏
  </div>
  <div id="fi-demo-link" style="opacity:0; transition:opacity 0.6s ease; text-align:center; margin-top:16px;">
    <a href="../../demo/pres/index.html" target="_blank" style="display:inline-block; background:#D97706; color:white; font-weight:700; font-size:1.05em; padding:10px 28px; border-radius:8px; text-decoration:none; box-shadow:0 2px 8px rgba(217,119,6,0.35); letter-spacing:0.01em;">→ Ouvrir la démo</a>
  </div>
</div>
<span class="fragment" data-anim-key="finale-fi1"    style="display:none!important;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-anim-key="finale-fi2"    style="display:none!important;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-anim-key="finale-fi3"    style="display:none!important;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-anim-key="finale-fi4"    style="display:none!important;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-anim-key="finale-quote"  style="display:none!important;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-anim-key="finale-claude" style="display:none!important;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
<span class="fragment" data-anim-key="finale-demo"   style="display:none!important;position:absolute;pointer-events:none;width:0;height:0;overflow:hidden;"></span>
