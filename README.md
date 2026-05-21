# DevGroup — Claude Code : présentation & outils

Ressources préparées pour une présentation DevGroup sur **Claude Code** — l'outil CLI d'Anthropic qui rend l'IA accessible à tous, pas uniquement aux développeurs.

Claude Code peut aider des profils très variés : rédacteurs, consultants, équipes métier, chefs de projet… tout le monde peut automatiser des tâches répétitives, générer du contenu, ou orchestrer des workflows sans écrire une seule ligne de code.

Ce repo contient trois choses : la présentation elle-même, des démos interactives de ses fonctionnalités, et un outil concret (PresMaker) qui illustre une utilisation non-technique de Claude Code.

---

## Structure du repo

```
DevGroup/
├── presentation/    ← Slides de la présentation DevGroup
├── demo/            ← Démos HTML interactives des features Claude Code
└── PresMaker/       ← Outil de création de présentations Reveal.js piloté par Claude
```

---

## `presentation/` — Slides DevGroup

La présentation principale sur Claude Code, générée avec [Reveal.js](https://revealjs.com/).

| Fichier | Description |
|---------|-------------|
| `ClaudeCode.html` | Présentation complète — ouvrir dans un navigateur |
| `ClaudeCode.md` | Source Markdown de la présentation |

---

## `demo/` — Démos interactives

Un catalogue de démos HTML autonomes, accessibles via un portail unifié.

**Ouvrir `demo/index.html` dans un navigateur** pour naviguer entre toutes les démos.

### Contenu des démos

| Catégorie | Démo | Description |
|-----------|------|-------------|
| **Architecture** | `architecture-claude-code.html` | Vue statique : CLI, LLM, composants |
| | `architecture-animee.html` | Animation pas à pas (clic pour avancer) |
| **Contexte** | `context-explainer.html` | Comment la fenêtre de contexte se remplit |
| | `rewind-explainer.html` | Revenir en arrière dans la conversation |
| | `hook-explainer.html` | Intercepter les actions avec les hooks |
| | `compact-explainer.html` | `/compact` — compresser l'historique |
| | `clear-explainer.html` | `/clear` — effacer le contexte |
| **Skills** | `card-creation.html` | Création d'une fiche sans skill |
| | `skill-card.html` | Même tâche avec un skill |
| | `skill-clear.html` | Skill + `/clear` : tokens session après session |
| **Workflow** | `workflow-sans-automation.html` | Sans automation : dérive des tokens |
| | `workflow-avec-automation.html` | Avec automation : contexte maîtrisé |
| **Agents** | `background-agents-explainer.html` | Agents parallèles : `/plan` → exécution |
| | `agent-explainer.html` | Agent : contexte isolé |

> Les démos s'adaptent à un mode **Projecteur** (toggle en bas du menu) pour une utilisation en présentation.

---

## `PresMaker/` — Workflow de création de présentations

Un exemple concret d'utilisation de Claude Code hors développement : un workflow en 4 étapes pour passer d'une idée à une présentation Reveal.js soignée, sans toucher au code.

```
/planMaker 5    → génère un plan interactif
/draft max=10   → découpe en slides individuels
/present        → génère la présentation HTML finale
```

Voir le **[README complet de PresMaker](PresMaker/docs/README.md)** pour la documentation détaillée.

---

## Ressources utiles

- **[Roadmap Claude Code](https://roadmap.sh/claude-code)** — Documentation exhaustive de toutes les features Claude Code
- **[CLAUDE.md de référence](https://gist.github.com/hqman/e29cb6386c539d795767e8c3fd2c959b)** — Template CLAUDE.md général, à adapter selon les besoins
- **[claude-code-router](https://github.com/musistudio/claude-code-router)** — Utiliser Claude Code avec un autre LLM que Claude

---

## Prérequis

- [Claude Code](https://claude.ai/code) (CLI `claude`) — pour PresMaker et l'utilisation interactive
- Python 3.10+ avec Flask (`pip install flask`) — uniquement pour le mode UI de PresMaker
- Un navigateur moderne — pour les démos et les présentations (aucune installation requise)
