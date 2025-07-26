def on_left_pressed():
    animation.run_image_animation(mySprite,
        assets.animation("""
            Fire Plane 2 Left Animation
            """),
        700,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_fire_destroyed(location):
    scene.clear_particle_effects_at_location(location)
    tiles.set_tile_at(location, assets.tile("""
        burnt tree
        """))
    music.thump.play()
sprites.on_fire_destroyed(on_fire_destroyed)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        assets.animation("""
            Fire Plane 2 Right Animation
            """),
        700,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_a_repeated():
    sprites.spray(mySprite, assets.image("""
        water
        """))
controller.A.on_event(ControllerButtonEvent.REPEATED, on_a_repeated)

def on_overlap_tile(sprite, location2):
    sprite.destroy()
    sprites.change_flame_strength_by(location2, -1)
scene.on_overlap_tile(SpriteKind.water,
    assets.tile("""
        tree fire
        """),
    on_overlap_tile)

mySprite: Sprite = None
game.set_dryness_of_grass(4)
game.set_strength_of_wind(3)
game.set_health_of_trees(10)
tiles.set_tilemap(tilemap("""
    level1
    """))
mySprite = sprites.create(assets.image("""
        Fire Plane 2 Left
        """),
    SpriteKind.player)
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
for index in range(5):
    sprites.create_spreading_fire(assets.tile("""
            tree
            """),
        assets.tile("""
            tree fire
            """))
hud.fire_hud(True)
hud.danger_hud(True)
hud.forest_hud(True)
hud.forest_hud_healthy(3)

def on_on_update():
    sprites.random_spread()
game.on_update(on_on_update)
