# Harvest Rush — Process Note

## Concept and visual direction

Harvest Rush is a farming-based casual mobile game prototype set in
SunSprout Valley. The player controls Sprout Scout, collects produce and tools,
and avoids rolling hay carts during a 45-second farm dash. My design direction
was: **“A cheerful, rounded mobile farming game with a friendly smiling farmer,
soft blue sky, layered green hills, warm yellow crops, simple readable shapes,
and energetic pink accents.”** This prompt/brief guided the hero, lobby,
environment, collectibles, and UI as one consistent visual system.

## Tools and workflow

I used Python with Pillow to create and export the illustrated PNG assets,
Photopea to assemble the layered submission file, and HTML/CSS/JavaScript to
prototype the playable mobile game. The asset workflow was:

1. Define the palette and visual rules: leafy greens, sky blue, crop yellow,
   tomato red, watering-can blue, warm brown, and pink accent colour.
2. Create the hero and alternate blue-apron/watering-can variant.
3. Build the farm-world background with clouds, hills, farmhouses, crop plots,
   and trees.
4. Create a related collectible set: carrot, tomato, hammer, and watering can.
5. Compose the gameplay/lobby screen with the hero, inventory panel, mission
   card, and farm environment.
6. Export individual PNGs, including transparent hero and collectible assets,
   then integrate them into the touch-friendly game prototype.

I maintained consistency by reusing the same rounded silhouettes, thick
outlines, soft shadows, limited palette, and simplified proportions across all
assets. The hero is shown on the home screen and lobby, while the same crops and
tools appear both in the asset pack and in the gameplay loop.

## Initial-to-final hero comparison and Photopea edits

The initial hero render had a pale-blue rectangular background and was not ready
for compositing. In Photopea, I imported the hero PNG, removed the background
to preserve the character silhouette, placed the result on transparency,
applied a small brightness/contrast and saturation correction, and added a
subtle soft drop shadow. I also organized the PSD into named groups:
`01 HERO`, `02 GAMEPLAY LOBBY`, `03 FARM BACKGROUND`, `04 COLLECTIBLES`, and
`05 HERO BEFORE AFTER`. The cleaned result is
`assets/hero-transparent.png`; the comparison is shown in
`hero-before-after.png`; the editable file is `Harvest-Rush-Layered.psd`.

## Improvements

For a production release, I would add sprite animation, sound effects,
haptics, swipe movement, multiple farm levels, saved progress, accessibility
options, and a native Android build. I would also expand the hero variants and
test the asset readability on a wider range of phone screen sizes.
