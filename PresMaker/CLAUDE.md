# PresMaker

## Objectif
Workflow en 4 étapes pour passer rapidement d'une idée à une présentation Reveal.js :
1. `/planMaker <n_parts>` → interactif → `work/<slug>/plan.md`
2. Édition manuelle du plan (avec instructions `@xxx@`)
3. `/draft [max=N]` → `work/<slug>/slides/slide-XX.md`
4. Édition manuelle des slides (avec instructions `@xxx@`) → `/present` → `work/<slug>/presentation/`

## Structure des fichiers de travail
```
work/<slug>/
├── plan.md           ← sortie de /planMaker
├── slides/
│   ├── slide-01.md   ← sortie de /draft
│   ├── slide-02.md
│   └── ...
└── presentation/
    ├── index.html    ← sortie de /present
    └── reveal/       ← assets Reveal.js
```

## Convention `@xxx@`
Les instructions `@xxx@` sont des directives inline dans le Markdown, interprétées par les skills draft et present.
Exemples simples : `@développe avec un exemple concret@`, `@ajoute de l'humour@`, `@crée un visuel ASCII@`

**TODO amélioration future** : passer à des instructions structurées avec préfixes de type :
- `@exemple:xxx@` — demande un exemple
- `@image:xxx@` — suggère un visuel ou une image
- `@humour@` — injecte une touche humoristique
- `@données:xxx@` — demande des chiffres/statistiques
- `@citation:xxx@` — demande une citation sur le sujet

## Conventions
- Slugs de répertoire : minuscules, tirets, pas d'espaces (ex: `ia-education`, `securite-zero-trust`)
- Un slide = un fichier `.md` numéroté `slide-XX.md`
- Les `@xxx@` sont supprimées du contenu final après traitement
- Thème Reveal.js : proposé par Claude en cohérence avec le sujet
