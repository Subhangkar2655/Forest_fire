controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    animation.runImageAnimation(mySprite, assets.animation`
            Fire Plane 2 Left Animation
            `, 700, true)
})
sprites.on_fire_destroyed(function on_fire_destroyed(location: tiles.Location) {
    scene.clearParticleEffectsAtLocation(location)
    tiles.setTileAt(location, assets.tile`
        burnt tree
        `)
    music.thump.play()
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    animation.runImageAnimation(mySprite, assets.animation`
            Fire Plane 2 Right Animation
            `, 700, true)
})
controller.A.onEvent(ControllerButtonEvent.Repeated, function on_a_repeated() {
    sprites.spray(mySprite, assets.image`
        water
        `)
})
scene.onOverlapTile(SpriteKind.Water, assets.tile`
        tree fire
        `, function on_overlap_tile(sprite: Sprite, location2: tiles.Location) {
    sprite.destroy()
    sprites.change_flame_strength_by(location2, -1)
})
let mySprite : Sprite = null
game.set_dryness_of_grass(4)
game.set_strength_of_wind(3)
game.set_health_of_trees(10)
tiles.setTilemap(tilemap`
    level1
    `)
mySprite = sprites.create(assets.image`
        Fire Plane 2 Left
        `, SpriteKind.Player)
controller.moveSprite(mySprite)
scene.cameraFollowSprite(mySprite)
for (let index = 0; index < 5; index++) {
    sprites.create_spreading_fire(assets.tile`
            tree
            `, assets.tile`
            tree fire
            `)
}
hud.fire_hud(true)
hud.danger_hud(true)
hud.forest_hud(true)
hud.forest_hud_healthy(3)
game.onUpdate(function on_on_update() {
    sprites.random_spread()
})
