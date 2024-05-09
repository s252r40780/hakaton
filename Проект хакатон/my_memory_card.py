from pygame import *
from random import randint, choice
from time import time as timer
from webbrowser import *
from turtle import*

win_width = 1000
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption('')
background = transform.scale(image.load('y.jpg'), (win_width, win_height))
background2 = transform.scale(image.load('final.png'), (win_width, win_height))
background3 = transform.scale(image.load('back123.jpg'), (win_width, win_height))
background4 = transform.scale(image.load('bg2.jpg'), (win_width, win_height))
font.init()
font1 = font.SysFont('Arial', 15)
font2 = font.SysFont('Arial', 20)
font3 = font.SysFont("None", 50)
font4 = font.SysFont("None", 60)
mixer.init()

mixer.music.load('background.mp3')
mixer.music.play()
life = 100
fightmuz =mixer.Sound('fight.ogg')

karma = 0

# pLeft = [transform.scale(image.load("left/left"), ())]

game = True
finish = False
menu = True
fight = True
settings = False
background_changed = False
disurl = "https://discord.gg/W7vCRk4J"
pDown = [image.load("up.jpg"), image.load("up2.jpg")]
pLeft = [image.load("left.jpg"), image.load("left2.jpg"), image.load("left3.jpg")]
pRight = [image.load("right.jpg"), image.load("right2.jpg"), image.load("right3.jpg")]
pUp = [image.load("down.jpg"), image.load("down2.jpg"), image.load("down3.jpg")]


# Классы
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h, hp):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        self.rect.x = player_x
        self.rect.y = player_y
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
        # if self.rect.left < 0 or self.rect.right > win_width or self.rect.top < 0 or self.rect.bottom > win_height:
        # global background_changed
        # if not background_changed:
        # window.blit(background2, (0, 0))
        # background_changed = True
        # self.rect.x = win_width // 2
        # self.rect.y = win_height // 2
        # else:
        # background_changed = False

    # def fire(self):
    # bullet = Bullet('kit.png', self.rect.centerx, self.rect.top, 20, 15, 20)
    # bullets.add(bullet)


class Enemy(GameSprite):
    def __init__(self, enemy_image, x, y, w, h):
        super().__init__(enemy_image, x, y, 0, w, h, 0)
        self.image = transform.scale(image.load(enemy_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def Jakob_fight():
    player_x = 60
    player_y = 600
    
    
    fightmuz.play()
    hpen = 50
    savior = transform.scale(image.load("elf2.png"), (30, 30))
    background.blit(savior, (player_x+30, player_y))
    life = 100
    
    while True:
        
        for e in event.get():
            if e.type == QUIT:
                fight = False
                game = False
            if e.type == KEYDOWN:
                if e.key == K_1:
                    hpen -= 25
                    life -=25
                    hpquart = font1.render("-25", True, (255,255,255),(0, 0, 0))
                    background.blit(hpquart, (60,590))
                    time.wait(2000)
                if e.key == K_2:
                    hpen -=100
                    hpfull = font1.render("-100", True, (255,255,255),(0, 0, 0))
                    background.blit(hpfull, (60,590))
                    time.wait(2000)
                if hpen <=0:
                    False
                

                



    
# Функции
def draw_menu():
    window.blit(background3, (0, 0))
    quest1 = font3.render(f"1 - Начать игру", True, (255, 255, 255))
    quest3 = font3.render(f"4 - Выбрать сложность", True, (255, 255, 255))
    quest2 = font3.render(f"2 - настройки", True, (255, 255, 255))
    opening = font4.render(f"Эльфийский квест: Волшебные миры", True, (46, 139, 87))
    discord = font3.render(f'3 - Дискорд', True, (255, 255, 255))
    bukva = font4.render(f"В", True, (255, 255, 255))
    text_rect = quest1.get_rect(center=(win_width // 2, win_height // 2))
    text_rect2 = quest2.get_rect(center=(500, 300))
    text_rect3 = opening.get_rect(center=(500, 250))
    text_rect4 = bukva.get_rect(center=(537.5, 250))
    text_rect5 = discord.get_rect(center=(500, 400))
    arch = transform.scale(image.load("luk.png"), (30, 30))
    arch2 = transform.scale(image.load("strela.png"), (32, 53))
    window.blit(quest1, text_rect)
    window.blit(quest2, text_rect2)
    window.blit(opening, text_rect3)
    window.blit(bukva, text_rect4)
    window.blit(arch, (789, 214))
    window.blit(arch2, (390, 224))
    window.blit(discord, text_rect5)
    window.blit(quest3, (320, 600))

    display.update()


def draw_difficult():
    # Фон
    window.blit(background, (0, 0))
    # Виды сложностей
    diff = font3.render(f'Сложность игры', True, (255, 255, 255))
    window.blit(diff, (500, 0))
    easy = font3.render(f'1 - Легко', True, (0, 255, 0))
    window.blit(easy, (320, 500))
    hard = font3.render(f'2 - Сложно', True, (255, 0, 0))
    window.blit(hard, (320, 600))
    impossible = font3.render(f'3 - Невозможно', True, (255, 255, 255))
    window.blit(impossible, (320, 550))
    if e.key == K_1:
        life = 100
    if e.key == K_2:
        life = 50
    if e.key == K_3:
        life = 1


def start_game():
    global game, menu
    game = True
    menu = False


def draw_back():
    window.blit(background2, (0, 0))


def draw_game():
    if background_changed:
        draw_back()
    else:
        pass


# def draw_settings():
#   window.blit(background3,(0,0))
#  quest1 = font3.render('1 - Выйти',True,(255,255,255))
# text_rect = quest1.get_rect(center=(win_width // 2, win_height // 2))
# window.blit(quest1, text_rect)
#
#   display.update()

# Цикл меню
while menu:
    for e in event.get():
        if e.type == QUIT:
            menu = False
            game = False
        if e.type == KEYDOWN:
            if e.key == K_1:
                start_game()
        if e.type == KEYDOWN:
            if e.key == K_3:
                open(disurl)
        if e.type == KEYDOWN:
            if e.key == K_4:
                draw_difficult()

                

        # if e.type == KEYDOWN:
        #   if e.key == K_2:
        #      draw_settings()
        #     menu = False
        #    settings = True

    # while settings:
    #   for e in event.get():
    #      if e.type == QUIT:
    #         settings = False
    #        game = False
    #   if e.type == KEYDOWN:
    #      if e.key == K_1:
    #         game = False
    #         settings = False

    draw_menu()
    display.update()
    time.delay(20)

# Цикл настроек  

# Отрисовка Эльфов23
enemy1 = Enemy('elf.png', 50, 600, 75, 75)
enemy2 = Enemy('elf2.png', 800, 600, 110, 110)
# enemy2 = Enemy('zloi.png', 0, 0, 115, 130, )
player = Player('ii.png', 300, 440, 20, 50, 100, 100)

# Координаты x, y


player_x = player.rect.x
player_y = player.rect.y

# Игровой цикл
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
            

    if not finish:
        draw_back()
        window.blit(background, (0, 0))
        player.reset()
        player.update()
        enemy1.reset()
        enemy1.update()
        enemy2.reset()
        enemy2.update()
        keys = key.get_pressed()

        enemy3 = transform.scale(image.load("elf.png"), (75, 75))
        window.blit(enemy3, (700, 400))
        warning = font2.render("--Читайте подсказки!", True, (255,255,255),(0, 0, 0))
        background.blit(warning, (300,20))

        if player_x < 300:
            quest2 = font1.render("Спросить Джейкоба - q, напасть - 4", True, (255,255,255),(0, 0, 0))
            background.blit(quest2, (0,0))
        if player_x > 400:
            quest2 = font1.render("Спросить Луну - w", True, (255,255,255),(0, 0, 0))
            background.blit(quest2, (0,20))
        
        if e.type == KEYDOWN:
        # Отображение надписи на экране
            if keys[K_4]:
            
                warning = font2.render(f"5-обычная атака 6-всплеск огня ", True, (255,255,255),(0, 0, 0))
                background.blit(warning, (300,30))
                
                
                life = 100
                fightmuz.play()
                background.blit(background4,(0,0))
                savior = transform.scale(image.load("elf2.png"), (150, 150))
                background4.blit(savior,(800,450))
                
                dialog1 = font1.render(f"Ты убийца,пытался сразить моего друга!", True, (255,255,255),(0, 0, 0))
                background4.blit(dialog1, (700,60))
                
            if keys[K_5]:
                
                
                life -= 25
                hpquart = font1.render(f"-25", True, (255,255,255),(0, 0, 0))
                background4.blit(hpquart, (910,480))
                dialog2 = font1.render(f"Может ты меня сможешь убить своим уроном,но...", True, (255,255,255),(0, 0, 0))
                background4.blit(dialog2, (700,60))
                dialog7 = font1.render(f"Нажми 7 чтобы добить", True,(0, 0, 0),(255,255,255))
                background4.blit(dialog7, (300,50))
                

            if keys[K_7]:
                print('gg')
                
                life -=20
                hpquart = font1.render(f"-25", True, (255,255,255),(0, 0, 0))
                background4.blit(hpquart, (910,500))
                
                dialog3 = font1.render(f"Но ты меня никогда не сломлешь!Я ни за что ни сдамся!", True,(0, 0, 0),(255,255,255))
                background4.blit(dialog3, (670,80))
                dialog8 = font1.render(f"Нажми 8 чтобы добить", True,(0, 0, 0),(255,255,255))
                background4.blit(dialog8, (300,50))
                    
            if keys[K_8]:
                
                dialog9 = font1.render(f"Нажми 9 чтобы добить", True,(0, 0, 0),(255,255,255))
                background4.blit(dialog9, (300,50))
                
                dialog4 = font1.render(f"Я не позволю тебе сбежать!Ни за что!", True,(0, 0, 0),(255,255,255))
                background4.blit(dialog4, (700,100))
            if keys[K_9]:
                dialog10 = font1.render(f"Нет, даже если я на грани гибели, я не паду", True,(0, 0, 0),(255,255,255))
                background4.blit(dialog10, (750,420))
                hpen -= 100
                dialog5 = font2.render(f"Похоже, уничтожив врага вы смогли открыть портал к дракону(вход-3)", True,(255,255,255),(0, 0, 0))
                background4.blit(dialog5, (100,400))
                portal = transform.scale(image.load("portal.png"), (75, 75))
                background4.blit(portal,(900,450))
                
                finish228 = font1.render(f"Хотите пройти в портал?Да-3", True, (255,255,255),(0, 0, 0))
                background.blit(finish228, (700,420))
            
                fightmuz.stop()
                


                        


            if keys[K_6]:
                hpen -=100
                hpfull = font1.render("-100", True, (255,255,255),(0, 0, 0))
                background4.blit(hpfull, (910,500))
                naah = font2.render("...", True, (255,255,255),(0, 0, 0))
                background.blit(naah, (700,420))
                time.wait(2000)
                
                finish228 = font1.render(f"Хотите пройти в портал?Да-3", True, (255,255,255),(0, 0, 0))
                background.blit(finish228, (700,420))
                dialog5 = font2.render(f"Похоже, уничтожив врага вы смогли открыть портал к дракону(вход-3)", True,(255,255,255),(0, 0, 0))
                background4.blit(dialog5, (100,400))
            
                fightmuz.stop()
                
                portal = transform.scale(image.load("portal.png"), (75, 75))
                background4.blit(portal,(900,450))
            display.update()
            background.blit(background4,(0,0))
            
                

        if keys[K_q]:
            if player_x<400:
                answ = font1.render(
                f'я - Джейкоб и мы сейчас находимся на тропинке к замку, если ты туда идешь то иди на право', True,(255, 255, 255), (0, 0, 0))
                background.blit(answ, (60, 590))
                enemy1_h = font1.render("50хп макс", True, (255,255,255),(0, 0, 0))
                background.blit(enemy1_h, (60,590))
          



        if keys[K_w]:
            answ2 = font1.render(f'''Меня зовут Луна, и я - эльф, если ты идешь к замку то удачи''', True,(255, 255, 255), (0, 0, 0))
            answ3 = font1.render(
                f'''Вокруг нас воцарилась тишина, только слабый ветер шепчет свои таинственные истории...''', True,
                (255, 255, 255), (0, 0, 0))
            background.blit(answ2, (420, 380))

            background.blit(answ3, (450, 570))

            answ2 = font1.render(f'', 1, (255, 255, 255), (0, 0, 0))

            

            display.update()
        

        if keys[K_3]:
            background_changed = True
            finalist = font2.render(f"...", True,(255,255,255),(0, 0, 0))
            background2.blit(finalist, (100,100))
            finalist2 = font1.render(f"Двинешься- убью, если хочешь поговорить- нажми z", True,(255,255,255),(0, 0, 0))
            background2.blit(finalist2, (1,100))
        if keys[K_z]:
            finalist2 = font1.render(f"Это твой настоящий персонаж, все время играла только твоя душа", True,(255,255,255),(0, 0, 0))
            background2.blit(finalist2, (1,120))
            finalist2 = font1.render(f"Ты пришел ко мне путем вражды, чего же ты хочешь?(x)", True,(255,255,255),(0, 0, 0))
            background2.blit(finalist2, (1,140))
        if keys[K_x]:
            
            finalist2 = font1.render(f"Я знаю чего...(с)", True,(255,255,255),(0, 0, 0))
            background2.blit(finalist2, (1,160))
            finalist2 = font2.render(f"Смерти!(рекомендую выйти наизбежания скримера)", True,(0, 0, 0))
            background2.blit(finalist2, (500,160))
        if keys[K_c]:
            finalist2 = font3.render(f"Шутка!", True,(0, 0, 0))
            background2.blit(finalist2, (300,160))
        if player_x>1000 or player_y<0:
            finalist2 = font2.render(f"Похоже, ваши блуждания по тропинке привели вас к замку, игра окончена", True,(0, 0, 0))
            background2.blit(finalist2, (300,160))

        
            



            
        

          
            # window.blit(background2, (0,0))

        
        cur_life = life
        if life >= 70:
            life_text_color = (0, 255, 0)
        if 20 <= life < 70:
            life_text_color = (250, 200, 50)
        if life <= 0 or life < 20:
            life_text_color = (255, 0, 0)
        if life <= 0:
            finish = True
            lose = font2.render(f'Поражение', True, (0, 0, 0))           
            window.blit(lose, (450, 250))
        life_text = font2.render(f'Здоровье:{cur_life}', True, life_text_color, (0, 0, 0))
        background.blit(life_text, (850, 10))

        # window.blit(background, (0, 0))

        # enemy2.reset()
        # enemy2.update()

        draw_game()
        display.flip()

    time.delay(5)
    display.update()
