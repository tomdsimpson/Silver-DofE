# Game Main Page
# Tom Simpson
# 10/09/21



# --- Importing modules --- #
import pygame as pg
from pygame import mixer
pg.init()
import random as r
import time as t
import math as m






# --- Making entity classes --- #
class enemy_entity():


    # Initialising entity attributes
    def __init__(self, state, enemyX_Change, enemyIMG, enemyX, enemyY):

        self.state = state
        self.enemyX_Change = enemyX_Change
        self.enemyIMG = pg.image.load(enemyIMG)
        self.enemyX = enemyX
        self.enemyY = enemyY
    

    # Instance methods

    # Updating alien pos
    def update_pos(self, aliens):

        # Moving enemy entity along x an y axis
        self.enemyX += self.enemyX_Change
    
        # Boundry checking
        if self.enemyX <= 0:
            
            # Shifting all enemies down
            for x in aliens:
                x.enemyX_Change = 0.2
                x.enemyY += 10
        
        elif self.enemyX >= 736:

            # Shifting all enemies down
            for x in aliens:
                x.enemyX_Change = -0.2
                x.enemyY += 10

        # Drawing at new location
        window.blit(self.enemyIMG, (self.enemyX, self.enemyY))

    def collision_detection(self, entityX, entityY):

        distance = m.sqrt((m.pow((self.enemyX+32) - entityX, 2)) + (m.pow((self.enemyY+32) - entityY, 2)))  # Algabraic distance between two points

        if distance < 27:
            return True
        return False






# Player Class
class player_entity():


    # Initialising entity attributes
    def __init__(self, player_state, player_img, playerX, playerY, playerX_change, playerY_change):

        self.player_state = player_state
        self.player_img = pg.image.load(player_img)
        self.playerX = playerX
        self.playerY = playerY
        self.playerX_change = playerX_change
        self.playerY_change = playerY_change


    # Instance Methods

    # Updating player position
    def update_player_pos(self):

        # Player movement
        self.playerX += self.playerX_Change
        
        # Boundary detection
        if self.playerX <= 5:
            self.playerX = 5
        elif self.playerX >= 725:
            self.playerX = 725   
        
        # Redrawing player
        window.blit(self.player_img, (self.playerX, self.playerY))






# Font class
class font_entity():


    # Initialising entity attributes
    def __init__(self, fontX, fontY, font_style, font_size, font_text):

        self.fontX = fontX
        self.fontY = fontY
        self.font_size = font_size
        self.font_text = font_text
        self.font_object = pg.font.Font(font_style, font_size)

    # Instance Methods

    # Display font
    def display_font(self):

        display = self.font_object.render(self.font_text, True, (255, 255, 255))
        window.blit(display, (self.fontX, self.fontY))






# Laser class
class  laser_entity():


    # Initialising entity attributes
    def __init__(self, laser_state, laser_img, laserX, laserY, laserY_change):

        self.laser_state = laser_state
        self.laser_img = pg.image.load(laser_img)
        self.laserX = laserX
        self.laserY = laserY
        self.laserY_change = laserY_change


    # Instance Methods

    # Firing laser
    def fire_laser(self):

        # Checking if the laser is present
        if not self.laser_state:

            self.laser_state = True
            player_laser.laserX = player.playerX + 16
            player_laser.laserY = player.playerY - 50

            # Laser sounds
            laser_sound = mixer.Sound("sounds/laser.wav")
            laser_sound.play()

        # Moving laser
        else:

            self.laser_state = True

            # Updating Position
            self.laserY += self.laserY_change

            # Checking boundaries
            if self.laserY > 600 or self.laserY < 0:
                self.laser_state = False
                self.laserY = 1000

            # Drawing entity
            window.blit(self.laser_img, (self.laserX, self.laserY))
























# --- Making the game window --- #
window = pg.display.set_mode((800, 600))
background = pg.image.load("Images/background.png")

# Music
mixer.music.load("sounds/background.wav")
mixer.music.play(-1) # -1 means loop

# Title and Icon
pg.display.set_caption("Space Invaders")
icon = pg.image.load("Images/ufo.png")
pg.display.set_icon(icon)






# --- Font Entities --- #

# Game over
game_over_display = font_entity(100, 250, "freesansbold.ttf", 96, "GAME OVER")
# Victory
victory_display = font_entity(225, 250, "freesansbold.ttf", 96, "VICTORY")
# Score Label
score = 0
score_display = font_entity(10, 10, "freesansbold.ttf", 32, ("Score: " + str(score)))



# --- Making entities --- #

# Player entity
player = player_entity(True, "Images/player.png", 368, 531, 0, 0)

# Alien entities
aliens = []
enemy_counter = 0

for counter in range(1, 5):
    for counter2 in range(1, 9):
        enemy_counter += 1
        aliens.append(enemy_entity(True, -0.2, "Images/enemy.png", counter2*92, (counter*75)- 30))

# Laser entity
player_laser = laser_entity(False, "Images/bullet.png", 0, 1000, -10)






# --- Game loop --- #
left_key = False
right_key = False
game_over = False
player_collision = False
running = True


while running:

    # RGB background fill
    window.fill((0, 0, 0))
    window.blit(background, (0, 0))


    # Looping through events
    for event in pg.event.get():

        # Allowing exit functionality
        if event.type == pg.QUIT:
            running = False

        # Keystroke input detection (KeyDown)
        if event.type == pg.KEYDOWN:

            if event.key == pg.K_LEFT:
                left_key = True
                pressed = "lkey"

            if event.key == pg.K_RIGHT:
                right_key = True
                pressed = "rkey"

            # Shooting laser
            if event.key == pg.K_SPACE:
                player_laser.fire_laser()


        # Keystroke input detection (KeyUp)
        if event.type == pg.KEYUP:

            if event.key == pg.K_LEFT:
                left_key = False
            
            if event.key == pg.K_RIGHT:
                right_key = False


    # Updating and drawing player
    
    # No keys pressed
    if left_key:
        player.playerX_Change = -0.6

    if right_key:
        player.playerX_Change = 0.6

    if right_key and left_key:

        if pressed == "lkey":
            player.playerX_Change = -0.6
        else:
            player.playerX_Change = 0.6

    if not left_key and not right_key:
        player.playerX_Change = 0


    # Enemy events
    for x in aliens:
        
        # Calling instance methods

        # --- Collision detection --- #
        collision = x.collision_detection(player_laser.laserX, player_laser.laserY)

        # If enemy hit
        if collision:

            # Reseting laser
            player_laser.laserY = 1000
            player_laser.laser_state = False
            score += 5
            score_display.font_text = ("Score: " + str(score))
            
            # 'Killing' enemy
            x.state = False
            x.enemy_Xchange = 0
            x.enemyX = 1000
            x.enemyY = -1000
            enemy_counter += -1

            # Explosion sounds
            explosion_sound = mixer.Sound("sounds/explosion.wav")
            explosion_sound.play()

        # Player collision detection
        if x.enemyY >= player.playerY - 48:
      
            for y in aliens:
                y.enemyY = -2000
                x.state = False

            game_over = True
            break



        # Checking if alive: moving
        if x.state:
            x.update_pos(aliens)


    # Player movement
    player.update_player_pos()
    # Moving laser
    if player_laser.laser_state:
        player_laser.fire_laser()


    # Font display
    score_display.display_font()

    if game_over:
        game_over_display.display_font()

    if enemy_counter == 0:
        victory_display.display_font()





    # Updating window
    pg.display.update()