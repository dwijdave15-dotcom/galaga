import pgzrun
import random
WIDTH = 1200
HEIGHT = 600


WHITE = (225 , 225 , 225)
BLUE = (0,0,225)

ship = Actor("galaga")
bug = Actor("bug")

ship.pos = (WIDTH//2, HEIGHT-60)

speed = 5

bullets = []

enemies = []

enemies.append(Actor("bug"))
#now the enemies  will be in a straight line
enemies[-1].x = 10
#starting off  the screen that why we are putting at =100
#slowly the enemy will calm down
enemies[-1].y = 50

score = 0

#for updating the score 
def displayScore():
    screen.draw.text(str(score), (50,30))

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        #the last bullet added , set its pos
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50


def update():
    global score
    # move the ship left or right with arrows keys
    if keyboard.left:
        ship.x -= speed
        if ship.x <= 0:
            ship.x = 0

    elif keyboard.right:
        ship.x += speed
        if ship.x >= WIDTH:
            ship.x = WIDTH
    #to fire bullets
    # it should not be while you hold space key event
    # rather it should be on space key down event

for bullets in bullets:
    #if the bullet reaches the top of the screen it should get removed
    # else the list will become huge
    if bullets.y <=0:
        bullets.remove(bullet)
    else:
        bullet.y -= 10

for enemy in enemies:
    enemy.y +=5
    #as the bug touches the bottom, make it go back up
    if enemy.y >=HEIGHT:
        enemy.y = -100
        enemy.x = random.randint(50,WIDTH-50)
        #checking if the enemy hit a bullet while moving down
        #ilterate over all the bullets and check for a collision
        for bullets in bullets:
            if enemy.colliderect(bullet):
                score +=100
                # we also want to destroy the bullet
                bullets.remove(bullet)
                #destroy the bug
                enemies.remove(enemy)

def draw():
    screen.clear()
    screen.fill(BLUE)
    #ship.draw
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    #ship to be drawn last
    ship.draw()
    displayScore()

pgzrun.go()
                    




                


