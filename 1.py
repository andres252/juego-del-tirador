from pygame import *
from random import randint

font.init()
font2 = font.Font(None, 36)

img_back = "galaxy.jpg"
img_hero = "rocket.png"
img_enemy = "ufo.png"
score = 0
lost = 0
clock = 60

class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    # el método “fire” (usa la posición del jugador para crear una bala)
    def fire(self):
        pass

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost

win_width = 700
win_height = 500
display.set_caption("Tirador")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# crea objetos
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint (80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    # el método “fire” (usa la posición del jugador para crear una bala)
    def fire(self):
        pass


    


mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
fire_sound = mixer.music.load("fire.ogg")

finish = False
run = True

while run:
    # el evento de pulsación del botón Cerrar
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        # actualizar fondo
        window.blit(background, (0, 0))
        text = font2.render("puntaje::" + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render("Fallados:" + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        # produciendo los movimientos del objeto
        ship.update()
        monsters.update()

        # los actualiza en una nueva ubicación en cada iteración del ciclo
        ship.reset()
        monsters.draw(window)

        display.update()
    # el ciclo se ejecuta cada 0.05 segundos
    time.delay(60)