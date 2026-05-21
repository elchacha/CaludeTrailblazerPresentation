# PresMaker

Workflow en 4 étapes pour passer rapidement d'une idée à une présentation [Reveal.js](https://revealjs.com/), piloté par Claude.

---

## Prérequis

- [Claude Code](https://claude.ai/code) (CLI `claude`)
- Python 3.10+
- Flask (`pip install flask`) — uniquement pour le mode UI

---

## Deux modes d'utilisation

### Mode CLI (Claude Code)

Directement dans le terminal Claude Code, via des slash commands.


## Workflow en 4 étapes (mode CLI)

### Étape 1 — Créer le plan

```
/planMaker 5
```

Claude pose 4 questions (sujet, public, objectif, ton), puis génère :

```
work/<slug>/plan.md
```

### Étape 2 — Affiner le plan

Ouvre `work/<slug>/plan.md` et modifie-le librement.
Tu peux enrichir le contenu avec des directives `@xxx@` :

| Directive | Effet |
|-----------|-------|
| `@développe avec un exemple concret@` | Ajoute un exemple illustratif |
| `@ajoute de l'humour@` | Injecte une touche humoristique |
| `@donne des chiffres@` | Illustre avec des statistiques |
| `@crée un visuel ASCII@` | Génère un diagramme en ASCII art |

Les directives `@xxx@` sont supprimées du contenu final après traitement.

### Étape 3 — Générer les slides

```
/draft
/draft max=12
/draft max=12 html=true
```

Génère un fichier par slide dans `work/<slug>/slides/slide-XX.md`.
Avec `html=true`, génère aussi une `preview.html` navigable (sans serveur).

Relis les slides, retouche-les, ajoute des `@xxx@` supplémentaires si besoin.

### Étape 4 — Générer la présentation

```
/present
/present --interactive
/present --slug=mon-projet prompt="thème sombre, slides aérées"
/present --slide=03
```

| Option | Effet |
|--------|-------|
| *(aucune)* | Détecte le projet, génère directement |
| `--interactive` / `-i` | Mode guidé : choisit le projet et le style interactivement |
| `--slug=<slug>` | Cible un projet précis |
| `prompt="..."` | Instruction globale de style (thème, ton, CSS) |
| `--slide=XX` | Régénère un seul slide dans `index.html` |

Résultat :
```
work/<slug>/presentation/index.html   ← ouvrir dans un navigateur
```

---

## Structure des fichiers

```
work/<slug>/
├── plan.md                  ← Étape 1 : plan de la présentation
├── theme.json               ← Étape 4 : thème Reveal.js généré par Claude
├── slides/
│   ├── slide-01.md          ← Étape 3 : un fichier par slide
│   ├── slide-02.md
│   ├── preview.html         ← (optionnel, avec /draft html=true)
│   └── ...
└── presentation/
    ├── index.html           ← Étape 4 : présentation finale Reveal.js
    └── slides-final.md      ← Concaténation des slides sans frontmatter
```

### Format d'un slide (`slide-XX.md`)

```markdown
---
numero: 03
titre: Titre du slide
type: contenu
partie: 1
---

# Titre du slide

- Point clé 1
- Point clé 2
- Point clé 3

<!-- notes: Notes présentateur visibles uniquement en mode présentateur -->
```

Types de slides : `intro` · `agenda` · `contenu` · `transition` · `conclusion` · `final`

---

## Thèmes Reveal.js disponibles

| Thème | Usage recommandé |
|-------|-----------------|
| `night`, `black` | Tech, IA, dark mode |
| `moon` | Business, sobre |
| `dracula`, `blood` | Décalé, humoristique |
| `beige`, `white`, `simple` | Pédagogique, classique |
| `sky`, `solarized`, `league`, `serif` | Divers |

---

## Scripts utilitaires

| Script | Usage |
|--------|-------|
| `scripts/gen_presentation.py <work/slug/>` | Génère `index.html` depuis les slides + `theme.json` |
| `scripts/gen_preview.py <work/slug/slides/>` | Génère `preview.html` pour prévisualiser les slides |

---

## Exemple complet

```
/planMaker 5
# → réponds aux 4 questions

# Édite work/mon-sujet/plan.md si besoin

/draft max=10
# → 10 slides créés dans work/mon-sujet/slides/

/present prompt="thème sombre, peu de texte par slide"
# → ouvre work/mon-sujet/presentation/index.html
```
