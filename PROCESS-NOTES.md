# Harvest Rush — Process Notes

## Concept

Harvest Rush is a friendly, mobile-first farming obstacle dash. The player
controls Sprout Scout through SunSprout Valley, collects produce and tools, and
avoids rolling hay carts before the 45-second round ends. The visual direction
is deliberately bright and readable: leafy greens, warm crop yellows, soft sky
blues, and a pink accent for GameBerry-style energy.

## Asset set

1. **Hero / variant:** Sprout Scout is the farmer hero. The hero is reused in
   the home screen and lobby so the character has a clear identity before play.
2. **Gameplay / lobby:** The gameplay composition shows the hero, farm world,
   inventory panel, and UI hierarchy. The live lobby screen then places the hero
   and mission card in the order a mobile game needs.
3. **Background / environment:** SunSprout Valley uses rolling hills, crop
   plots, clouds, and small farm houses to establish the farming world.
4. **Collectibles:** Carrot, tomato, hammer, and watering can form a related
   harvest/tool set and are used by the gameplay loop.

## Workflow

The illustrations were built as simple vector-style compositions, exported to
PNG, and integrated into a touch-friendly HTML5 canvas prototype. The
interactive pass adds a home screen, lobby, timed round, movement controls,
collectible pickup, score feedback, and hay-cart hazards. The same palette,
rounded forms, and soft shadow treatment are used across every surface.

## Cleanup / before and after

The hero source render initially had a pale-blue rectangular presentation
background. The cleanup pass removed that background, preserved the character
silhouette, and exported a transparent `assets/hero-transparent.png` for the
home screen and lobby. The comparison is included in `hero-before-after.png`.
The presentation sheet is `presentation-sheet.png`.

## What I would improve

For production, I would add sprite animation, sound, haptics, multiple farm
levels, touch swipe movement, a proper save system, and a native Android build.
I would also create the final layered Photoshop document from the named art
groups before delivery to a production art team.
