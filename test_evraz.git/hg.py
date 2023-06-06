import pygame, sys
import random
import time
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

move = 20
movex = random.randint(-50,50)
movey = random.randint(-50,50)

# настройки главного экрана
WIDTH = 1500
HEIGHT = 1000
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
mainScreenColor = BLACK 
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

exit = 0



manjump = pygame.image.load('man_jump.png')
manstand = pygame.image.load('man_stand.png')
manr = pygame.image.load('man_walk.png')
manl = manr.copy()
manl = pygame.transform.flip(manl, True, False)
man = manstand
manrect = manr.get_rect()
manrect.bottom = HEIGHT//2 +500
manrect.left = WIDTH//2 + 800
trollge = pygame.image.load('trollge.png')
trollgeRect = trollge.get_rect()
trollgeRect2 = trollge.get_rect()
trollgeRect.bottom = HEIGHT//2
back = pygame.image.load('back.png')
back1 = back.get_rect()
trollgeRect.left = WIDTH//2 + 70
trollgeRect2.bottom = HEIGHT//2 - 300
trollgeRect2.left = WIDTH//2 - 530
trollge3 = pygame.image.load('trollge2.png')
trollgeRect3 = trollge3.get_rect()
trollgeRect3.bottom = HEIGHT//2
trollgeRect3.left = WIDTH//2
background = pygame.image.load('background.png')
background1 = background.get_rect()
background1.bottom = 1025
background1.left = 0
trollge4 = pygame.image.load('trollge.png')
trollgeRect4 = trollge4.get_rect()
trollgeRect4.bottom = 163
trollgeRect4.left = WIDTH//2
trollge5 = pygame.image.load('trollge.png')
trollgeRect5 = trollge5.get_rect()
trollgeRect5.bottom = HEIGHT//2 + 500
trollgeRect5.left = WIDTH//2 + 200
trollge6 = pygame.image.load('trollge.png')
trollgeRect6 = trollge6.get_rect()
trollgeRect6.bottom = HEIGHT//2 + 30
trollgeRect6.left = WIDTH//2 + 525

trollge7 = pygame.image.load('trollge.png')
trollgeRect7 = trollge7.get_rect()
trollgeRect7.bottom = 4000
trollgeRect7.left = 4000

trollge8 = pygame.image.load('trollge.png')
trollgeRect8 = trollge8.get_rect()
trollgeRect8.bottom = 4000
trollgeRect8.left = 4000

trollge9 = pygame.image.load('trollge.png')
trollgeRect9 = trollge9.get_rect()
trollgeRect9.bottom = 4000
trollgeRect9.left = 4000

boss = pygame.image.load('boss.png')
bossrect = boss.get_rect()
bossrect.bottom = 10000
bossrect.left = 10000

bullet = pygame.image.load('bul.png')
bulreck = bullet.get_rect()

portal = pygame.image.load('portal.png')
portalRect = portal.get_rect()
portalRect.bottom = 160
portalRect.left = 1600
t = 15
o = 100
s = 0

hp = '150'
dam = 20



f2 = pygame.font.Font(None, 60)
text2 = f2.render('GAME OVER', 1, (180, 0, 0))

f1 = pygame.font.Font(None, 60)
text1 = f1.render(hp, 1, (180, 0, 0))

f3 = pygame.font.Font(None, 60)
text3 = f3.render('VICTORY', 1, (180, 0, 0))

bullets = []

platform = pygame.image.load('walle.png')
exitimage = pygame.image.load('portal.png')
ror = 0
ror1 = 0
# platform = pygame.Surface((250, 100))

# массив rect'ов для еды
platforms = [
    # platform.get_rect(left = 0, bottom = HEIGHT - 200)
]

map =  [
    '********************************',
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

activemap = map


game = 1


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
    exit = []

    for i in range(len(activemap)):
        for j in range(len(activemap[i])):
            if activemap[i][j] == '*':
                platformrect = platform.get_rect()
                platformrect.x = 54 * j
                platformrect.y = 54 * i
                platforms.append(platformrect)
                mainScreen.blit(platform, platformrect)
            elif activemap[i][j] == '-':
                exitrect = platform.get_rect()
                exitrect.x = 54 * j
                exitrect.y = 54 * i
                exit.append(exitrect)
                mainScreen.blit(exitimage, exitrect)

    

    






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
    if keys[pygame.K_HOME]:
        manrect.x = 1568
        manrect.y = 108

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
        hp = int(hp) - dam
        hp = str(hp)
        
    if trollgeRect.x >= 1500:
        trollgeRect.x =  o
        
    if trollgeRect.x >= 100:
        trollgeRect.x += t
         


    if manrect in trollgeRect2:
        hp = int(hp) - dam
        hp = str(hp)
    if trollgeRect2.y >= 800:
        trollgeRect2.y =  150
        
    if trollgeRect2.y >= 100:
        trollgeRect2.y += 15  


    if manrect in trollgeRect4:
        hp = int(hp) - dam
        hp = str(hp)
    if trollgeRect4.x >= 1400:
        trollgeRect4.x =  100
       
        
    if trollgeRect4.x >= 100:
        trollgeRect4.x += 4   
        

    if manrect in trollgeRect5:
        hp = int(hp) - dam
        hp = str(hp)
    if trollgeRect5.x >= 1400:
        trollgeRect5.x =  280
        
    if trollgeRect5.x >= 100:
        trollgeRect5.x += 15

    if manrect in trollgeRect6:
        hp = int(hp) - dam
        hp = str(hp)
    if trollgeRect6.y >= 610:
        trollgeRect6.y =  400
        
    if trollgeRect6.y >= 100:
        trollgeRect6.y +=  1
    
    if manrect in trollgeRect7: 
        hp = int(hp) - dam
        hp = str(hp)
    
    if trollgeRect7.x >= 1325:
        trollgeRect7.x =  200
        
    if trollgeRect7.x >= 100:
        trollgeRect7.x += t 

    if manrect in trollgeRect8: 
        hp = int(hp) - dam
        hp = str(hp)
    
    if trollgeRect8.x >= 1325: 
        trollgeRect8.x =  280
        
    if trollgeRect8.x >= 100:
        trollgeRect8.x += t
        

    if manrect in trollgeRect9: 
        hp = int(hp) - dam
        hp = str(hp)
    
    if trollgeRect9.x >= 1325: 
        trollgeRect9.x =  280
        
    if trollgeRect9.x >= 100:
        trollgeRect9.x += t 


    if manrect in bossrect:
        hp = int(hp) - dam
        hp = str(hp)
        


    print('x',manrect.x)
    print('y',manrect.y)

    if manrect.x == 1622 and manrect.y == 108:
        trollgeRect6.bottom = 4000
        trollgeRect6.left = 4000
        trollgeRect5.bottom = 4000
        trollgeRect5.left = 4000
        trollgeRect4.bottom = 4000
        trollgeRect4.left = 4000
        trollgeRect3.bottom = 4000
        trollgeRect3.left = 4000
        trollgeRect2.bottom = 4000
        trollgeRect2.left = 4000
        trollgeRect.bottom = 590
        trollgeRect.left = 500
        t = 5
        o = 650
        manrect.bottom = HEIGHT//2 +500
        manrect.left = WIDTH//2 + 800
        portalRect.bottom = 1020
        portalRect.left = 45

        activemap =  [
        '********************************',
        '*             *               **',
        '*             *               **',
        '*     **      *     *******   **',
        '*      ***    *     *     *   **',
        '*        *    *     *     *   **',
        '***      *          *         **',
        '* *      *          *         **',
        '* ***    ************   ********',
        '*        *                     *',
        '*        *                     *',
        '*  *******   *******************',
        '*  **              *   *    *  *',
        '*  **              *         * *',
        '*  **     ******   *      *    *',
        '*  **          *   *   *   *   *',
        '*  **          *****    *   ****',
        '*  ********              *     *',
        '*  **                     *    *',
        '********************************'
        ]
        
    if manrect.x == 56 and manrect.y == 946:
        manrect.bottom = HEIGHT//2 +500
        manrect.left = WIDTH//2 + 800
        trollgeRect.x = 150
        trollgeRect.y = 946


        portalRect.bottom = 1020
        portalRect.left = 160 

        activemap =  [
        '********************************',
        '*                             **',
        '*                             **',
        '*   ************************* **',
        '*   *                       *  *',
        '*   *                       *  *',
        '*   *      **************** *  *',
        '*   *                     * *  *',
        '*   *                     *    *',
        '*   *** ********************   *',
        '*   *   *                  *****',
        '*** *                          *',
        '*   *                          *',
        '*   ************************** *',
        '*   *                          *',
        '*   *                          *',
        '*   *** ************************',
        '*   *                          *',
        '*   *                          *',
        '********************************'
          ]






    
    
    mainScreen.fill(mainScreenColor)


        
    if int(hp) <= 0:
        exit = 1
       

    
    for platformrect in platforms:
        mainScreen.blit(platform, platformrect)
        
        

    text1 = f1.render(hp, 1, (180, 0, 0))
    
    mainScreen.blit(man, manrect)
    mainScreen.blit(trollge, trollgeRect)
    mainScreen.blit(trollge, trollgeRect2)
    mainScreen.blit(trollge5, trollgeRect5)
    mainScreen.blit(trollge4, trollgeRect4)
    mainScreen.blit(trollge6, trollgeRect6)
    mainScreen.blit(trollge7, trollgeRect7)
    mainScreen.blit(trollge8, trollgeRect8)
    mainScreen.blit(trollge9, trollgeRect9)

    mainScreen.blit(boss,bossrect)

    mainScreen.blit(portal, portalRect)
    
    
    mainScreen.blit(text1, (10, 20))

    if manrect.x == 164 and manrect.y == 946:

        mainScreen.blit(back,back1)
        mainScreen.blit(text3, (WIDTH/2, HEIGHT/2))
        game += 1
    if game == 250:
        sys.exit()


    if exit == 1:

        mainScreen.blit(back,back1)
        mainScreen.blit(text2, (WIDTH/2, HEIGHT/2))
        game += 1
    if game == 250:
        sys.exit()

    pygame.display.flip()
    clock.tick(FPS)