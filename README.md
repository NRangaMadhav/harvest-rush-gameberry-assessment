# Harvest Rush

Harvest Rush is a small farming-based casual game prototype created for the
GameBerry Labs Gen AI Designer assessment.

## Run the game

The playable game is a browser project and does not require Python packages.
Use any local web server from the project folder:

```text
python -m http.server 8000
```

Then open <http://localhost:8000/> in a browser.

Click **Start Farming**, then use the arrow keys or `WASD` to move the farmer
over crops and tools. Each collected item is worth 10 points and each round
lasts 45 seconds.

## Project contents

- `index.html` - game entry point and asset presentation
- `style.css` - responsive visual styling
- `game.js` - game loop, movement, collectibles, scoring, and timer
- `assets/` - hero, gameplay, environment, and collectible PNG assets
- `*.svg` - editable vector source versions of the illustrated assets
- `generate_final_assets.py` - optional PNG regeneration script
- `requirements.txt` - Python dependency for the optional asset-generation script

## Regenerate the PNG assets (optional)

This step is not needed to play the game. It is included so the art assets can
be regenerated from source:

```text
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python generate_final_assets.py
```

## Design and process note

The visual direction uses a friendly, rounded casual-game style with a
light-blue sky, fresh greens, warm yellow crops, and pink GameBerry branding.
The same palette and simplified shapes are used across the hero, environment,
gameplay composition, and collectible set so the assets remain readable at
mobile sizes.

The artwork was created as clean vector-style compositions and then exported to
PNG. The gameplay screen combines the hero, environment, inventory panel, and
collectible presentation into one composition. The browser prototype adds the
interactive layer: movement, spawning collectibles, collision pickup, score
feedback, and a timed round.

For a production version, I would add touch controls, sound effects,
character animation, multiple farming levels, and a proper layered Photoshop
file with named groups. The editable SVG source files and the Python export
script are included as an organized source workflow for this assessment.

## Submission checklist

Submit the project folder as a ZIP, or submit a repository link containing:

1. `index.html`, `style.css`, and `game.js`
2. The complete `assets/` folder
3. `README.md` and `requirements.txt`
4. The editable SVG source files

When sending it by email, include the run instructions and the URL
`http://localhost:8000/` as the local preview command.
