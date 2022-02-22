#This game was made by Adventure10
#You do not have permision to copy more than 3 lines unless I tell you
#You can share this with anyone.
#------------------------------------------------------------------------------#
# import pygame module in this program 
import pygame, random, time, os

# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init()
#Prepare
def delete_line(original_file, line_number):
    """ Delete a line from a file at the given line number """
    is_skipped = False
    current_index = 0
    dummy_file = original_file + '.bak'
    # Open original file in read only mode and dummy file in write mode
    with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Line by line copy data from original file to dummy file
        for line in read_obj:
            # If current line number matches the given line number then skip copying
            if current_index != line_number:
                write_obj.write(line)
            else:
                is_skipped = True
            current_index += 1
    # If any line is skipped then rename dummy file as original file
    if is_skipped:
        os.remove(original_file)
        os.rename(dummy_file, original_file)
    else:
        os.remove(dummy_file)
#load images
bird1 = pygame.image.load('bird1.png')
bird2 = pygame.image.load('bird2.png')
bird3 = pygame.image.load('bird3.png')
pygame.image.load('pipe_top.png')
pygame.image.load('pipe_bottom.png')
bg=pygame.image.load('flap_back.png')
game_over=pygame.image.load('game_over.png')
over=game_over.get_rect()
over.y=200
#Check bot
bot_enabled=False
if input("Use bot? [Y/N]: ").lower().startswith('y'): bot_enabled=True
# create the display surface object 
game_size=600
s=game_size/2
win = pygame.display.set_mode((game_size, game_size)) 

# set the pygame window name 
pygame.display.set_caption("Flappy Bird")
#Make the fonts
myfont = pygame.font.SysFont('Comic Sans MS', 50)
hi_font=pygame.font.SysFont('Comic Sans MS', 30)
# All variables 
x = s
y = s
score=0
width = 20
height = 20
time_left=0
switch_time=8
pole_counter=[]
upleft=0
current_center= 250
pole_speed=-20
fall_speed=20
jump_spedd=-10
pole_gap=260
#write the text
number= myfont.render(str(score), False, (0,0,0))
#Create ADDENEMY event
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1000)

#Set up clock
clock=pygame.time.Clock()
#Create all Classes/Objects
class Title(pygame.sprite.Sprite):
    def __init__(self):
        super(pygame.sprite.Sprite)
        self.image=pygame.image.load('flappy_main.png')
        self.rect=self.image.get_rect()
        self.rect.center = 300, 100
class Instructions(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('flappy_start.png')
        self.rect=self.image.get_rect()
        self.rect.center = 300,400
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)#call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
class Player(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location[0], location[1]
    def move_up(self):
        self.rect.y=y
    def move_down(self):
        self.rect.y=y
class Enemy_Top(pygame.sprite.Sprite):
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.top=current_center+pole_gap/2
        self.rect.right=700
    def move_right(self):
        self.rect.move_ip(pole_speed, 0)
class Enemy_Bottom(pygame.sprite.Sprite):
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.bottom=current_center-pole_gap/2
        self.rect.right=700
    def move_right(self):
        self.rect.move_ip(pole_speed, 0)
#Run classes
bg=Background('flap_back.png', [0,0])
bird= Player('bird2.png', [x,y])
dead=Player('bird4.png', [x,y])
title=Title()
inst=Instructions()
#Create Group for poles
enemies=pygame.sprite.Group()
# Indicates pygame is running 
run = True
running=True
go=False
#Loop inbetween attempts
while running:
    x=s;y=s
    score=0
    upleft=0
    run=True
    go = False
    enemies.empty()
    pole_counter.clear()
    pygame.event.clear()
    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    number= myfont.render(str(score), False, (0,0,0))
    win.fill((0,0,0))
    win.blit(bg.image, bg.rect)
    win.blit(title.image,title.rect)
    pygame.display.update()
    win.blit(inst.image,inst.rect)
    best=open('flappy_best.txt').read()
    highscore=hi_font.render('Highscore:', False, (0,0,0))
    high=hi_font.render(str(best), False, (0,0,0))
    win.blit(highscore, (50, 330))
    win.blit(high, (120, 370))
    pygame.display.update()
    #Wait for start
    while not go:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                go=True
                run=False
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    go=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                go=True
        time.sleep(.01)
    #Run flappy bird game
    while run:
        if bot_enabled:
            if len(pole_counter)>0:
                if True:
                    if bird.rect.bottom>current_center+pole_gap/5:
                        print('go up')
                        upleft=100
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run=False
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    upleft=100
            if event.type==pygame.MOUSEBUTTONDOWN:
                upleft=100
            if event.type==ADDENEMY:
                current_center=random.randint(120, 380)
                enemies.add(Enemy_Top('pipe_bottom.png'))
                enemies.add(Enemy_Bottom('pipe_top.png'))
                pole_counter.append(enemies.sprites()[len(enemies.sprites())-2])
                pole_counter.append(enemies.sprites()[len(enemies.sprites())-1])
                
        if switch_time//3==2:
            bird.image=bird2
        if switch_time//3==1:
            bird.image=bird1
        if switch_time//3==0:
            bird.image=bird3
        if switch_time==0:
            switch_time=8
        else:
            switch_time -= 1
        if upleft>0:
            y-=fall_speed
            upleft-=20
            bird.move_up()
            time_left=3
        elif not(time_left > 0):
            y=y+fall_speed
            bird.move_down()
        if y>500:
            y=500
        if y <0:
            y=0
        if time_left>0:
            time_left-=1
        if len(pole_counter) > 0:
            if bird.rect.left > pole_counter[0].rect.right:
                score=score+1
                pole_counter.pop(0)
                pole_counter.pop(0)
                number= myfont.render(str(score), False, (0,0,0))
        win.fill((0,0,0))
        win.blit(bg.image, bg.rect)
        for enemy in enemies:
            enemy.move_right()
            win.blit(enemy.image, enemy.rect)
            if enemy.rect.left<=-100:
                enemy.kill()
        win.blit(bird.image, bird.rect)
        clock.tick(20)
        if pygame.sprite.spritecollideany(bird, enemies):
            bird.kill()
            run=False
        win.blit(number, (s, 0))
        pygame.display.update()
    dead=Player('bird4.png', [x,y])
    while dead.rect.bottom<580:
        dead.rect.y+=30
        win.fill((0,0,0))
        win.blit(bg.image, bg.rect)
        for enemy in enemies:
            win.blit(enemy.image, enemy.rect)
            if enemy.rect.left<=-100:
                enemy.kill()
        win.blit(dead.image, dead.rect)
        win.blit(number, (s, 0))
        clock.tick(20)
        pygame.display.update()
    win.blit(bg.image, bg.rect)
    win.blit(game_over, over)
    myfont = pygame.font.SysFont('Comic Sans MS', 100)
    number= myfont.render(str(score), False, (0,0,0))
    win.blit(number, (s, 0))
    win.blit(dead.image, dead.rect)
    pygame.display.update()
    now=time.time()
    while time.time()-1<now:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run=False
                running=False
        time.sleep(.01)
    if score > int(best) and not bot_enabled:
        delete_line('flappy_best.txt', 0)
        writing = open('flappy_best.txt', 'w')
        writing.write(str(score))
        writing.close()
pygame.quit()