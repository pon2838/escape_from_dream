import pygame, sys
import random
pygame.init()

# цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
o = 3

SPEED = 9
changeX = 0
time = 0

# настройки главного экрана
WIDTH = 1500
HEIGHT = 1000
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
mainScreenColor = WHITE
pygame.display.set_caption("Моя игра")

# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()

vel = 5
jump = False
jumpCount = 0
jumpMax = 32
onGround = True
onPlatform = False

# block2 = pygame.Surface((100, 100))
manjump = pygame.image.load('man_jump.png')
manstand = pygame.image.load('man_stand.png')
manr = pygame.image.load('man_walk.png')
manl = manr.copy()
manl = pygame.transform.flip(manl, True, False)
man = manstand
manrect = manr.get_rect()
manrect.bottom = HEIGHT//2 -15
manrect.left = WIDTH//2
trollge = pygame.image.load('trollge.png')
trollgeRect = trollge.get_rect()
trollgeRect2 = trollge.get_rect()
trollgeRect.bottom = HEIGHT//2
trollgeRect.left = WIDTH//2 + 70
trollgeRect2.bottom = HEIGHT//2 - 300
trollgeRect2.left = WIDTH//2 - 530

platform = pygame.image.load('кирпич шоколадка small.png')

# platform = pygame.Surface((250, 100))

# массив rect'ов для еды
platforms = [
    # platform.get_rect(left = 0, bottom = HEIGHT - 200)
]

map =  [
    '*****    ***********************',
    '*                              *',
    '*                              *',
    '*   ****************************',
    '*                              *',
    '*                              *',
    '*                              *',
    '*                      ****    *',
    '*                              *',
    '*          *****               *',
    '*                          *****',
    '***                            *',
    '*                              *',
    '*     ***               **     *',
    '*                              *',
    '****       ****              ***',
    '*                              *',
    '*                              *',
    '*                              *',
    '********************************'
]
 





while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if not jump and event.key == pygame.K_SPACE:
                jump = True
                jumpCount = jumpMax
                onGround = False
                onPlatform = False

    platforms = []

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '*':
                platformrect = platform.get_rect()
                platformrect.x = 54 * j
                platformrect.y = 54 * i
                platforms.append(platformrect)
                mainScreen.blit(platform, platformrect)

    

    






    manrect_old = manrect.copy()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        changeX = -1 * SPEED
        man = manl
        time = time + 1
        print(time)

    if keys[pygame.K_RIGHT]:
        changeX = SPEED
        man = manr
        time = time + 1
        print(time)

    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        changeX = 0
        man = manstand

    if jump:
        manrect.y -= jumpCount
        man = manjump

    if jumpCount > -jumpMax or (manrect.bottom < HEIGHT and onGround == False):
        jumpCount -= 1
        man = manjump
    else:
        onGround = True

    if manrect.bottom > HEIGHT:
        manrect.bottom = HEIGHT
        onGround = True
        jump = False

    manrect.x += changeX
    if time == 200:
        pon = 0

    # проверка столкновения блока еды и змеи
    for platformrect in platforms:
        if manrect.colliderect(platformrect) == True:
            # движемся налево
            if manrect.left < manrect_old.left:
                manrect.x -= changeX
                # manrect.left = platformrect.right

            # движемся направо
            if manrect.right > manrect_old.right:
                manrect.x -= changeX
                # manrect.left = platformrect.right

        if manrect.colliderect(platformrect) == True:
            # движемся вниз
            if manrect.bottom > manrect_old.bottom:
                jump = False
                onGround = True
                onPlatform = True
                manrect.bottom = platformrect.top
            if manrect.top < manrect_old.top:
                jump = False
                onGround = True
                onPlatform = True
                manrect.top = platformrect.bottom
            if manrect.bottom > manrect_old.bottom:
                jump = False
                onGround = True
                onPlatform = True
                manrect.bottom = platformrect.top

    # Проверка падаем с платформы, потому что вышли с неё
    if onPlatform == True:
        manrect_next = manrect.copy()
        manrect_next.y += 1

        if manrect_next.collidelist(platforms) == -1:
            jump = True
            jumpCount = -1
            onGround = False
            onPlatform = False
    
    if manrect in trollgeRect:
        sys.exit()
    if trollgeRect.x >= 1500:
        trollgeRect.x =  100
        
    if trollgeRect.x >= 100:
        trollgeRect.x += 15   

    if manrect in trollgeRect2:
        sys.exit()
    if trollgeRect2.y >= 800:
        trollgeRect2.y =  150
        
    if trollgeRect2.y >= 100:
        trollgeRect2.y += 15   

    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)

        
       
       

    # рисуем блок еды
    for platformrect in platforms:
        mainScreen.blit(platform, platformrect)


    # рисуем змею
    mainScreen.blit(man, manrect)
    mainScreen.blit(trollge, trollgeRect)
    mainScreen.blit(trollge, trollgeRect2)

    pygame.display.flip()
    clock.tick(FPS)