import arcade
from time import sleep
from random import randint

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
TITLE = "Earl"

GRAVITY = 0.1
max_speed = 5 #s
MAX_SPEED = 5
floor_height = 192
BOST_PLAYER = 0.1
jump_height = 7 #s
JUMP_HEIGHT = 7
END_MAP = 1500
parc_kol = 10 #s
PARC_KOL = 10
health = 3
sc = 0
pl_pos_x = 100
pl_pos_y = floor_height + 56
pl_can_x = 0
pl_can_y = 0
coin1_pos = 100
coin2_pos = 1200
coin11_pos = 100
coin21_pos = 1200
level = 1
level_1 = [
    "pppoooooooooooo",
    "ooooooooooooooo",
    "ooooeppppzooooo",
    "oooyuddddiroooo",
    "ppsuddddddiappp",
    "ddddddddddddddd"
]
level_2 = [
    "ppooooooooooooo",
    "ooooeppoopzoooo",
    "oooyuddoodirooo",
    "ooyudddoooooooo",
    "psuddddpppppppp",
    "ddddddddddddddd"
]


class Game(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color([30, 30, 50])
        self.scene = arcade.Scene()
        self.scene1 = arcade.Scene()
        self.player = Player()
        self.dirt_list = []
        self.dirt_list1 = []
        self.blood_list = []
        self.dirt_y = 0
        self.dirt_x = 0
        self.camera = None
        self.camera_x = 0
        self.viev = None
        self.dirt = None
        self.spikes = None
        self.coin1 = None
        self.coin2 = None
        self.fon_pp = "Pause"
        self.fon_pl = True
        self.floor_p = arcade.Sprite("grass.png")
        self.floor_u = arcade.Sprite("dirt_up.png")
        self.floor_y = arcade.Sprite("grass_up.png")
        self.floor_e = arcade.Sprite("grass_end_up.png")
        self.floor_d = arcade.Sprite("dirt.png")
        self.floor_a = arcade.Sprite("grass_start_down.png")
        self.floor_i = arcade.Sprite("dirt_down.png")
        self.floor_r = arcade.Sprite("grass_down.png")
        self.floor_z = arcade.Sprite("grass_end_down.png")
        self.floor_s = arcade.Sprite("grass_start_up.png")
        self.coin_sound = arcade.Sound("coin.mp3")
        self.damage_sound = arcade.Sound("damage.mp3")
        self.fon_sound = arcade.Sound("fon.mp3")
        self.media_player = self.fon_sound.play()
        self.level = level
        self.player.center_x = pl_pos_x
        self.player.center_y = pl_pos_y
        self.player.change_x = pl_can_x
        self.player.change_y = pl_can_y

    def setup(self):
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        for i in range(600, END_MAP+1200, 1200):
            self.background = arcade.Sprite("background.png")
            self.background.center_x = i
            self.background.center_y = SCREEN_HEIGHT/2
            self.scene.add_sprite("Background", self.background)
        self.scene.add_sprite("Earl", self.player)
        self.spikes = arcade.Sprite("spikes.png")
        self.spikes.center_x = 750
        self.spikes.center_y = 426
        self.scene.add_sprite("spik", self.spikes)
        self.coin1 = arcade.Sprite("coin.png", 0.7)
        self.coin2 = arcade.Sprite("coin.png", 0.7)
        self.coin2.center_x = coin2_pos
        self.coin2.center_y = 250
        self.coin1.center_x = coin1_pos
        self.coin1.center_y = 650
        self.scene.add_sprite("coin1", self.coin1)
        self.scene.add_sprite("coin2", self.coin2)

        for i in level_1:
            self.dirt_x = 50
            if i == level_1[0]:
                self.dirt_y = 550
            if i == level_1[1]:
                self.dirt_y = 450
            if i == level_1[2]:
                self.dirt_y = 350
            if i == level_1[3]:
                self.dirt_y = 250
            if i == level_1[4]:
                self.dirt_y = 150
            if i == level_1[5]:
                self.dirt_y = 50
            for j in i:
                if not j == "o":
                    if j == "p":
                        self.dirt = arcade.Sprite("grass.png")
                    if j == "s":
                        self.dirt = arcade.Sprite("grass_start_up.png")
                    if j == "u":
                        self.dirt = arcade.Sprite("dirt_up.png")
                    if j == "y":
                        self.dirt = arcade.Sprite("grass_up.png")
                    if j == "e":
                        self.dirt = arcade.Sprite("grass_end_up.png")
                    if j == "d":
                        self.dirt = arcade.Sprite("dirt.png")
                    if j == "a":
                        self.dirt = arcade.Sprite("grass_start_down.png")
                    if j == "i":
                        self.dirt = arcade.Sprite("dirt_down.png")
                    if j == "r":
                        self.dirt = arcade.Sprite("grass_down.png")
                    if j == "z":
                        self.dirt = arcade.Sprite("grass_end_down.png")
                    self.dirt.center_x = self.dirt_x
                    self.dirt.center_y = self.dirt_y
                    self.dirt_list.append(self.dirt)
                    self.scene.add_sprite(f"{self.dirt_x}{self.dirt_y}", self.dirt)
                self.dirt_x += 100

        for i in range(600, END_MAP+1200, 1200):
            self.background1 = arcade.Sprite("background.png")
            self.background1.center_x = i
            self.background1.center_y = SCREEN_HEIGHT/2
            self.scene1.add_sprite("Background", self.background1)
        self.scene1.add_sprite("Earl", self.player)
        self.spikes1 = arcade.Sprite("spikes.png")
        self.spikes1.center_x = 752
        self.spikes1.center_y = 226
        self.scene1.add_sprite("spik", self.spikes1)
        self.coin11 = arcade.Sprite("coin.png", 0.7)
        self.coin21 = arcade.Sprite("coin.png", 0.7)
        self.coin21.center_x = coin21_pos
        self.coin21.center_y = 250
        self.coin11.center_x = coin11_pos
        self.coin11.center_y = 650
        self.scene1.add_sprite("coin1", self.coin11)
        self.scene1.add_sprite("coin2", self.coin21)

        for i in level_2:
            self.dirt_x = 50
            if i == level_2[0]:
                self.dirt_y = 550
            if i == level_2[1]:
                self.dirt_y = 450
            if i == level_2[2]:
                self.dirt_y = 350
            if i == level_2[3]:
                self.dirt_y = 250
            if i == level_2[4]:
                self.dirt_y = 150
            if i == level_2[5]:
                self.dirt_y = 50
            for j in i:
                if not j == "o":
                    if j == "p":
                        self.dirt = arcade.Sprite("grass.png")
                    if j == "s":
                        self.dirt = arcade.Sprite("grass_start_up.png")
                    if j == "u":
                        self.dirt = arcade.Sprite("dirt_up.png")
                    if j == "y":
                        self.dirt = arcade.Sprite("grass_up.png")
                    if j == "e":
                        self.dirt = arcade.Sprite("grass_end_up.png")
                    if j == "d":
                        self.dirt = arcade.Sprite("dirt.png")
                    if j == "a":
                        self.dirt = arcade.Sprite("grass_start_down.png")
                    if j == "i":
                        self.dirt = arcade.Sprite("dirt_down.png")
                    if j == "r":
                        self.dirt = arcade.Sprite("grass_down.png")
                    if j == "z":
                        self.dirt = arcade.Sprite("grass_end_down.png")
                    self.dirt.center_x = self.dirt_x
                    self.dirt.center_y = self.dirt_y
                    self.dirt_list1.append(self.dirt)
                    self.scene1.add_sprite(f"{self.dirt_x}{self.dirt_y}", self.dirt)
                self.dirt_x += 100

    def on_draw(self):
        self.clear()
        if self.level == 1:
            self.scene.draw()
        if self.level == 2:
            self.scene1.draw()
        self.camera.use()
        arcade.draw_text(f"Hp: {health}", self.camera_x + 10, SCREEN_HEIGHT - 30, [200, 200, 200], 20)
        arcade.draw_text(f"Sc: {sc}", self.camera_x + 10, SCREEN_HEIGHT - 55, [200, 200, 200], 20)
        arcade.draw_text(f"{self.fon_pp} sound: P", self.camera_x + SCREEN_WIDTH - 10, SCREEN_HEIGHT - 30,
                         [200, 200, 200], 15, anchor_x="right")

    def update(self, delta_time: float):
        self.scene.update()
        self.player.update()
        for i in range(len(self.blood_list)):
            self.blood_list[i].update()
        if self.camera_x + SCREEN_WIDTH/2 < self.player.center_x - 300:
            self.camera_x = self.player.center_x - SCREEN_WIDTH/2 - 300
        if self.camera_x + SCREEN_WIDTH/2 > self.player.center_x + 300:
            self.camera_x = self.player.center_x - SCREEN_WIDTH/2 + 300
        if self.camera_x < 0:
            self.camera_x = 0
        if self.camera_x + SCREEN_WIDTH > END_MAP:
            self.camera_x = END_MAP - SCREEN_WIDTH
        self.camera_pos = self.camera_x, 0
        self.camera.move_to(self.camera_pos)

        global sc, health, coin1_pos, coin11_pos, coin21_pos, coin2_pos, pl_pos_y, pl_pos_x, pl_can_y, pl_can_x,\
            floor_height, level
        pl_can_y = self.player.change_y
        pl_can_x = self.player.change_x
        pl_pos_x = self.player.center_x
        pl_pos_y = self.player.center_y
        if self.level == 1:
            if arcade.check_for_collision(self.player, self.spikes):
                health -= 1
                self.damage_sound.play()
                for i in range(parc_kol):
                    self.bl = Blood(floor_height)
                    self.bl.center_x = self.player.center_x
                    self.bl.center_y = self.player.center_y
                    self.bl.change_x = self.player.change_x + randint(-2, 2)
                    self.bl.change_y = -self.player.change_y + randint(-2, 2)
                    self.blood_list.append(self.bl)
                    self.scene.add_sprite(f"Bl{i}", self.bl)
                self.player.change_x = -self.player.change_x
                self.player.change_y = -self.player.change_y
            if arcade.check_for_collision(self.player, self.coin1):
                sc += 1
                self.coin1.center_x = -1000
                coin1_pos = -1000
                self.coin_sound.play()
            if arcade.check_for_collision(self.player, self.coin2):
                sc += 1
                self.coin2.center_x = -1000
                coin2_pos = -1000
                self.coin_sound.play()
        if self.level == 2:
            if arcade.check_for_collision(self.player, self.spikes1):
                for i in range(parc_kol):
                    self.bl = Blood(floor_height)
                    self.bl.center_x = self.player.center_x
                    self.bl.center_y = self.player.center_y
                    self.bl.change_x = self.player.change_x + randint(-2, 2)
                    self.bl.change_y = -self.player.change_y + randint(-2, 2)
                    self.blood_list.append(self.bl)
                    self.scene1.add_sprite(f"Bl{i}", self.bl)
                self.player.change_x = -self.player.change_x
                self.player.change_y = -self.player.change_y
                health -= 1
                self.damage_sound.play()
            if arcade.check_for_collision(self.player, self.coin11):
                sc += 1
                self.coin11.center_x = -1000
                coin11_pos = -1000
                self.coin_sound.play()
            if arcade.check_for_collision(self.player, self.coin21):
                sc += 1
                self.coin21.center_x = -1000
                coin21_pos = -1000
                self.coin_sound.play()
        if health <= 0:
            self.media_player.pause()
            floor_height = 192
            health = 3
            sc = 0
            level = 1
            pl_pos_x = 100
            pl_pos_y = floor_height + 56
            pl_can_x = 0
            pl_can_y = 0
            coin1_pos = 100
            coin2_pos = 1200
            coin11_pos = 100
            coin21_pos = 1200
            self.window.show_view(GameOverView())

        if self.level == 1:
            for i in range(len(self.dirt_list)):
                if arcade.check_for_collision(self.player, self.dirt_list[i]):
                    self.player.on_the_ground = True
            for i in range(len(self.dirt_list)):
                if not arcade.check_for_collision(self.player, self.dirt_list[i]):
                    self.player.on_the_ground = False
        if self.level == 2:
            for i in range(len(self.dirt_list1)):
                if arcade.check_for_collision(self.player, self.dirt_list1[i]):
                    self.player.on_the_ground = True
            for i in range(len(self.dirt_list1)):
                if not arcade.check_for_collision(self.player, self.dirt_list1[i]):
                    self.player.on_the_ground = False

        if self.level == 1:
            if 500 > self.player.center_x > 300:
                floor_height = self.player.center_x-100
            if self.player.center_x <= 300:
                if self.player.center_y <= 500:
                    floor_height = 192
                if 444 < self.player.center_y < 450:
                    self.player.change_y = -1
                if self.player.center_y > 500:
                    floor_height = 592
            if 900 < self.player.center_x < 1100:
                floor_height = 400-(self.player.center_x-900)
            if self.player.center_x >= 1100:
                floor_height = 192
            if 500 <= self.player.center_x <= 900:
                floor_height = 392

            if 500 < self.player.center_y < 590:
                if self.player.center_x < 336:
                    self.player.change_x = 0

        if self.level == 2:
            if self.player.center_x <= 200:
                if self.player.center_y < 400:
                    floor_height = 192
                if 495 < self.player.center_y+56 < 505:
                    self.player.change_y = -1
                if self.player.center_y > 590:
                    floor_height = 592
            if 195 < self.player.center_x < 205:
                if 500 < self.player.center_y < 600:
                    self.player.change_x = 0
            if 200 < self.player.center_x < 500:
                floor_height = self.player.center_x
            if 500 <= self.player.center_x <= 700:
                if self.player.center_y > 520:
                    floor_height = 492
            if 700 < self.player.center_x < 900:
                floor_height = 192
            if 695 < self.player.center_x < 705:
                if self.player.center_y <= 520:
                    self.player.change_x = 3
            if 900 < self.player.center_x < 1200:
                if self.player.center_y < 266:
                    floor_height = 192
                    self.player.center_y = 248
                    self.player.on_the_ground = True
                if self.player.center_y > 300:
                    if 910 < self.player.center_x < 1000:
                        floor_height = 492
                    if 1000 < self.player.center_x < 1200:
                        floor_height = 500 - (self.player.center_x - 1000)
            if self.player.center_x > 1200:
                floor_height = 192
            if 895 < self.player.center_x < 905:
                if 300 < self.player.center_y < 500:
                    self.player.change_x = 0

        if self.level == 1:
            if self.player.center_x >= END_MAP-10 and sc >= 2:
                sleep(0.5)
                self.level = 2
                level = 2
                self.player.center_x = 100
                self.player.center_y = floor_height + 56
        if self.level == 2:
            if self.player.center_x >= END_MAP-10 and sc >= 4:
                sleep(0.5)
                floor_height = 192
                health = 3
                sc = 0
                level = 1
                pl_pos_x = 100
                pl_pos_y = floor_height + 56
                pl_can_x = 0
                pl_can_y = 0
                coin1_pos = 100
                coin2_pos = 1200
                coin11_pos = 100
                coin21_pos = 1200
                self.media_player.pause()
                self.window.show_view(GameWinView())

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D:
            self.player.walk_right = True
        if symbol == arcade.key.A:
            self.player.walk_left = True
        if symbol == arcade.key.SPACE:
            self.player.jump = True
        if symbol == arcade.key.ESCAPE:
            self.media_player.pause()
            self.window.show_view(InstructionView())
        if symbol == arcade.key.P:
            if self.fon_pl:
                self.media_player.pause()
                self.fon_pp = "Play"
                self.fon_pl = False
                return
            if not self.fon_pl:
                self.fon_pp = "Pause"
                self.media_player.play()
                self.fon_pl = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D:
            self.player.walk_right = False
        if symbol == arcade.key.A:
            self.player.walk_left = False


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = 100
        self.center_y = floor_height + 56
        self.change_y = 0
        self.change_x = 0
        self.jump_teaker = 0
        self.stop_teaker = 0
        self.run_teaker = 0
        self.run_textures = []
        self.run_textures_flip = []
        self.jump_textures = []
        self.jump_textures_flip = []
        for i in range(1, 9):
            self.texture_run = arcade.load_texture(f"run{i}.png")
            self.run_textures.append(self.texture_run)
        for i in range(1, 9):
            self.texture_run = arcade.load_texture(f"run{i}.png", flipped_horizontally=True)
            self.run_textures_flip.append(self.texture_run)
        for i in range(1, 9):
            self.texture_j = arcade.load_texture(f"j{i}.png")
            self.jump_textures.append(self.texture_j)
        for i in range(1, 9):
            self.texture_j = arcade.load_texture(f"j{i}.png", flipped_horizontally=True)
            self.jump_textures_flip.append(self.texture_j)
        self.stop_textures = [arcade.load_texture("stop1.png"), arcade.load_texture("stop2.png")]
        self.stop_textures_flip = [arcade.load_texture("stop1.png", flipped_horizontally=True),
                                   arcade.load_texture("stop2.png", flipped_horizontally=True)]
        self.on_the_ground = False
        self.walk_right = False
        self.walk_left = False
        self.look_right = True
        self.jump = False

        self.texture = self.stop_textures[0]

    def update(self):
        self.center_y += self.change_y
        self.center_x += self.change_x

        if not self.on_the_ground:
            self.change_y -= GRAVITY
        if self.on_the_ground:
            self.change_y = 0

        if self.center_y <= floor_height + 56:
            self.center_y = floor_height + 56
            self.on_the_ground = True

        if self.walk_right and self.on_the_ground:
            if self.change_x < max_speed:
                self.change_x += BOST_PLAYER
        if not self.walk_right and self.on_the_ground:
            if self.change_x > 0:
                self.change_x -= BOST_PLAYER
        if self.walk_left and self.on_the_ground:
            if self.change_x > -max_speed:
                self.change_x -= BOST_PLAYER
        if not self.walk_left and self.on_the_ground:
            if self.change_x < 0:
                self.change_x += BOST_PLAYER
        if BOST_PLAYER > self.change_x > -BOST_PLAYER and not self.walk_right and not self.walk_left:
            self.change_x = 0

        if self.jump and self.on_the_ground:
            self.on_the_ground = False
            self.jump_teaker = 0
            self.change_y = jump_height
            self.jump = False

        if self.look_right:
            if not self.on_the_ground:
                if self.jump_teaker < 119:
                    self.jump_teaker += 1
                self.texture = self.jump_textures[self.jump_teaker//20]
            if self.on_the_ground:
                if self.jump_teaker < 159:
                    self.jump_teaker += 1
                self.texture = self.jump_textures[self.jump_teaker//20]
        if not self.look_right:
            if not self.on_the_ground:
                if self.jump_teaker < 119:
                    self.jump_teaker += 1
                self.texture = self.jump_textures_flip[self.jump_teaker//20]
            if self.on_the_ground:
                if self.jump_teaker < 159:
                    self.jump_teaker += 1
                self.texture = self.jump_textures_flip[self.jump_teaker//20]

        if self.walk_right and self.on_the_ground:
            if self.run_teaker < 79:
                self.run_teaker += 1
            if self.run_teaker >= 79:
                self.run_teaker = 0
            self.texture = self.run_textures[self.run_teaker//10]
        if self.walk_left and self.on_the_ground:
            if self.run_teaker < 79:
                self.run_teaker += 1
            if self.run_teaker >= 79:
                self.run_teaker = 0
            self.texture = self.run_textures_flip[self.run_teaker//10]

        if self.change_x > 0:
            self.look_right = True
        if self.change_x < 0:
            self.look_right = False

        if self.change_y == 0 and self.change_x == 0:
            if self.look_right:
                if self.stop_teaker < 190:
                    self.stop_teaker += 2
                if self.stop_teaker >= 190:
                    self.stop_teaker = 0
                self.texture = self.stop_textures[self.stop_teaker//100]
            if not self.look_right:
                if self.stop_teaker < 190:
                    self.stop_teaker += 2
                if self.stop_teaker >= 190:
                    self.stop_teaker = 0
                self.texture = self.stop_textures_flip[self.stop_teaker//100]

        if self.center_x < 36:
            self.center_x += max_speed
            self.change_x = 0
        if self.center_x > END_MAP:
            self.center_x -= max_speed
            self.change_x = 0


class Blood(arcade.Sprite):
    def __init__(self, blood_floor):
        super().__init__("blood.png")
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0
        self.blood_floor = blood_floor

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.center_y < self.blood_floor:
            self.center_y = self.blood_floor
        else:
            self.change_y -= GRAVITY
        if self.change_x > 0:
            self.change_x -= BOST_PLAYER
        if self.change_x < 0:
            self.change_x += BOST_PLAYER
        if BOST_PLAYER > self.change_x > -BOST_PLAYER:
            self.change_x = 0
        global level
        if level == 2:
            if self.center_x < 700:
                self.change_x = -self.change_x


class Button(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.up = arcade.load_texture("but_up.png")
        self.down = arcade.load_texture("but_down.png")
        self.texture = self.up


class Slider(arcade.Sprite):
    def __init__(self):
        super().__init__("slider.png")

    def moving(self):
        if self.center_x < 360:
            self.center_x = 360
        if self.center_x > 840:
            self.center_x = 840


class InstructionView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color([55, 55, 55])
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        self.scene = arcade.Scene()
        self.button = Button()
        self.button.center_x = 600
        self.button.center_y = 480
        self.scene.add_sprite("Button", self.button)
        self.button1 = Button()
        self.button1.center_x = 600
        self.button1.center_y = 350
        self.scene.add_sprite("Button1", self.button1)
        self.button2 = Button()
        self.button2.center_x = 600
        self.button2.center_y = 220
        self.scene.add_sprite("Button2", self.button2)
        self.mos_pos_x = 0
        self.mos_pos_y = 0


    def on_draw(self):
        self.clear()
        self.scene.draw()
        arcade.draw_text("Earl", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200, [255, 255, 255], font_size=70,
                         anchor_x="center")
        arcade.draw_text("by Vitaly", 20, 5, [255, 255, 255], font_size=7, anchor_x="center")
        # arcade.draw_text(f"x:{self.mos_pos_x}, y:{self.mos_pos_y}", 10, 700,)
        arcade.draw_text("Start", SCREEN_WIDTH/2, 480, [255, 255, 255], 30, anchor_x="center", anchor_y="center")
        arcade.draw_text("Settings", SCREEN_WIDTH / 2, 350, [255, 255, 255], 30, anchor_x="center", anchor_y="center")
        arcade.draw_text("Exit", SCREEN_WIDTH / 2, 220, [255, 255, 255], 30, anchor_x="center", anchor_y="center")

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.mos_pos_x = x
        self.mos_pos_y = y

        if 350 < x < 850:
            if 430 < y < 530:
                self.button.texture = self.button.down
        if not 350 < x < 850 or not 430 < y < 530:
            self.button.texture = self.button.up

        if 350 < x < 850:
            if 300 < y < 400:
                self.button1.texture = self.button1.down
        if not 350 < x < 850 or not 300 < y < 400:
            self.button1.texture = self.button1.up

        if 350 < x < 850:
            if 170 < y < 270:
                self.button2.texture = self.button2.down
        if not 350 < x < 850 or not 170 < y < 270:
            self.button2.texture = self.button2.up

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if 350 < x < 850:
            if 430 < y < 530:
                game_view = Game()
                game_view.setup()
                self.window.show_view(game_view)

        if 350 < x < 850:
            if 300 < y < 400:
                game_view = SettingsView()
                game_view.on_show_view()
                self.window.show_view(game_view)

        if 350 < x < 850:
            if 170 < y < 270:
                arcade.close_window()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            game_view = Game()
            game_view.setup()
            self.window.show_view(game_view)


class GameOverView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color([55, 55, 55])
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        self.scene = arcade.Scene()
        self.button = Button()
        self.button.center_x = 600
        self.button.center_y = 400
        self.scene.add_sprite("Button", self.button)
        self.button1 = Button()
        self.button1.center_x = 600
        self.button1.center_y = 270
        self.scene.add_sprite("Button1", self.button1)
        self.mos_pos_x = 0
        self.mos_pos_y = 0

    def on_draw(self):
        self.clear()
        self.scene.draw()
        arcade.draw_text("YOU LOST", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200, [255, 255, 255], font_size=70,
                         anchor_x="center")
        arcade.draw_text("Restart", SCREEN_WIDTH / 2, 400, [255, 255, 255], 30, anchor_x="center", anchor_y="center")
        arcade.draw_text("Exit", SCREEN_WIDTH / 2, 270, [255, 255, 255], 30, anchor_x="center", anchor_y="center")
        # arcade.draw_text(f"x:{self.mos_pos_x}, y:{self.mos_pos_y}", 10, 700)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.mos_pos_x = x
        self.mos_pos_y = y

        if 350 < x < 850:
            if 350 < y < 450:
                self.button.texture = self.button.down
        if not 350 < x < 850 or not 350 < y < 450:
            self.button.texture = self.button.up

        if 350 < x < 850:
            if 220 < y < 320:
                self.button1.texture = self.button1.down
        if not 350 < x < 850 or not 220 < y < 320:
            self.button1.texture = self.button1.up

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if 350 < x < 850:
            if 350 < y < 450:
                game_view = Game()
                game_view.setup()
                self.window.show_view(game_view)

        if 350 < x < 850:
            if 220 < y < 320:
                arcade.close_window()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            game_view = Game()
            game_view.setup()
            self.window.show_view(game_view)
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()


class GameWinView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color([55, 55, 55])
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        self.scene = arcade.Scene()
        self.button = Button()
        self.button.center_x = 600
        self.button.center_y = 400
        self.scene.add_sprite("Button", self.button)
        self.button1 = Button()
        self.button1.center_x = 600
        self.button1.center_y = 270
        self.scene.add_sprite("Button1", self.button1)
        self.mos_pos_x = 0
        self.mos_pos_y = 0

    def on_draw(self):
        self.clear()
        self.scene.draw()
        arcade.draw_text("YOU WIN", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200, [255, 255, 255], font_size=70,
                         anchor_x="center")
        arcade.draw_text("Restart", SCREEN_WIDTH / 2, 400, [255, 255, 255], 30, anchor_x="center", anchor_y="center")
        arcade.draw_text("Exit", SCREEN_WIDTH / 2, 270, [255, 255, 255], 30, anchor_x="center", anchor_y="center")
        # arcade.draw_text(f"x:{self.mos_pos_x}, y:{self.mos_pos_y}", 10, 700)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.mos_pos_x = x
        self.mos_pos_y = y

        if 350 < x < 850:
            if 350 < y < 450:
                self.button.texture = self.button.down
        if not 350 < x < 850 or not 350 < y < 450:
            self.button.texture = self.button.up

        if 350 < x < 850:
            if 220 < y < 320:
                self.button1.texture = self.button1.down
        if not 350 < x < 850 or not 220 < y < 320:
            self.button1.texture = self.button1.up

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if 350 < x < 850:
            if 350 < y < 450:
                game_view = Game()
                game_view.setup()
                self.window.show_view(game_view)

        if 350 < x < 850:
            if 220 < y < 320:
                arcade.close_window()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            game_view = Game()
            game_view.setup()
            self.window.show_view(game_view)
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()


class SettingsView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color([55, 55, 55])
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        self.scene = arcade.Scene()
        self.button = Button()
        self.button.center_x = 600
        self.button.center_y = 480
        self.scene.add_sprite("Button", self.button)
        self.button1 = Button()
        self.button1.center_x = 600
        self.button1.center_y = 90
        self.scene.add_sprite("Button1", self.button1)
        self.button_press = False
        self.slider = Slider()
        self.slider.center_x = (max_speed-1)*50+360
        self.slider.center_y = 365
        self.scene.add_sprite("slider", self.slider)
        self.slider1 = Slider()
        self.slider1.center_x = (jump_height-1)*50+360
        self.slider1.center_y = 285
        self.scene.add_sprite("slider1", self.slider1)
        self.slider2 = Slider()
        self.slider2.center_x = (parc_kol-1)*25+360
        self.slider2.center_y = 205
        self.scene.add_sprite("slider2", self.slider2)

    def on_draw(self):
        self.clear()
        arcade.draw_text("SETTINGS", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200, [255, 255, 255], font_size=70,
                         anchor_x="center")
        arcade.draw_line(360, 365, 840, 365, [30, 30, 30], 10)
        arcade.draw_line(360, 285, 840, 285, [30, 30, 30], 10)
        arcade.draw_line(360, 205, 840, 205, [30, 30, 30], 10)
        self.scene.draw()
        arcade.draw_text("Return", SCREEN_WIDTH / 2, 480, [255, 255, 255], 30, anchor_x="center", anchor_y="center")
        arcade.draw_text("Back", SCREEN_WIDTH / 2, 90, [255, 255, 255], 30, anchor_x="center", anchor_y="center")

        arcade.draw_text(f"{max_speed}", 860, 365, [255, 255, 255], 15,
                         anchor_y="center")
        arcade.draw_text("Player speed", 340, 365, [255, 255, 255], 15,
                         anchor_y="center", anchor_x="right")

        arcade.draw_text(f"{jump_height}", 860, 285, [255, 255, 255], 15,
                         anchor_y="center")
        arcade.draw_text("Jump height", 340, 285, [255, 255, 255], 15,
                         anchor_y="center", anchor_x="right")

        arcade.draw_text("Amount of blood", 340, 205, [255, 255, 255], 15,
                         anchor_y="center", anchor_x="right")
        arcade.draw_text(f"{parc_kol}", 860, 205, [255, 255, 255], 15,
                         anchor_y="center")

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.mos_pos_x = x
        self.mos_pos_y = y

        global max_speed, jump_height, parc_kol
        if self.button_press:
            max_speed = ((self.slider.center_x - 360) // 50) + 1
            jump_height = ((self.slider1.center_x - 360) // 50) + 1
            parc_kol = ((self.slider2.center_x - 360) // 25) + 1

        if 350 < x < 850:
            if 430 < y < 530:
                self.button.texture = self.button.down
        if not 350 < x < 850 or not 430 < y < 530:
            self.button.texture = self.button.up

        if 350 < x < 850:
            if 40 < y < 140:
                self.button1.texture = self.button1.down
        if not 350 < x < 850 or not 40 < y < 140:
            self.button1.texture = self.button1.up

        if self.button_press:
            if 360 < x < 840:
                if 340 < y < 390:
                    self.slider.center_x = x
                if 260 < y < 310:
                    self.slider1.center_x = x
                if 180 < y < 230:
                    self.slider2.center_x = x

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.button_press = True
        global max_speed, jump_height, parc_kol
        if 350 < x < 850:
            if 430 < y < 530:
                max_speed = MAX_SPEED
                jump_height = JUMP_HEIGHT
                parc_kol = PARC_KOL
                self.slider2.center_x = (parc_kol - 1) * 25 + 360
                self.slider1.center_x = (jump_height - 1) * 50 + 360
                self.slider.center_x = (max_speed - 1) * 50 + 360
        if 350 < x < 850:
            if 40 < y < 140:
                game_view = InstructionView()
                game_view.on_show_view()
                self.window.show_view(game_view)


    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.button_press = False


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()