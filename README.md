# agencia-dashboard

Dashboard de la agencia (`index.html`, estático) + el **Avatar Reel Pack** instalado
como skills de Claude Code.

## Avatar Reel Pack

Pipeline completo para generar un reel vertical 9:16 en el que tu avatar habla con tu
voz: guion → voz → render del avatar → título → b-roll → subtítulos → música/SFX → mezcla final.

```
.claude/skills/     11 skills (Claude Code las descubre solo aquí)
sfx/                índice de la librería de efectos (los .mp3 no vienen incluidos)
scripts/            validate-outputs.sh
CONTRACT.md         dónde escribe cada run (outputs/<flow>/<run_slug>/)
SETUP.md            instalación de runtimes externos
env.example         nombres de las API keys (copiar a .env, que está en .gitignore)
```

### Antes del primer reel

1. `cp env.example .env` y rellenar `HEYGEN_API_KEY`, `AVATAR_GROUP_ID` y `GEMINI_API_KEY`
   (ElevenLabs, Kie.ai y OpenAI son opcionales). El `.env` nunca se commitea.
2. Editar `.claude/skills/avatar-reel/identity.json` — es el único archivo de identidad:
   `heygen_avatar_id`, `display_name` y la dirección de voz (`audio_profile`, `style`, `accent`).
3. Runtimes locales: ffmpeg, Python 3 + Pillow, Node 18+, jq. Detalle en [SETUP.md](SETUP.md).

### Uso

En Claude Code: *"Hazme un avatar reel sobre &lt;tema&gt;. Fuente: &lt;link o asset&gt;."*
El agente para después del guion para que elijas uno de los 3 hooks, antes de gastar
créditos de render.

### Marca

- Tarjeta de título, colores y subtítulos: `.claude/skills/avatar-reel-editing/references/avatar_reel_post_canon.json`
  (los scripts leen todo de ahí, no hace falta tocar código). Idioma de subtítulos ya fijado en `es`.
- Sistemas visuales de b-roll: `.claude/skills/avatar-reel/references/reel_direction.md`.

### Antes de cerrar un run

```bash
bash scripts/validate-outputs.sh
```
