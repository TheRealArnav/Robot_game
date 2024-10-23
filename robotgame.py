import pgzrun
import random
WIDTH=500
HEIGHT=500
TITLE="Robot game"
bg=Actor("grass",(WIDTH//2,HEIGHT//2))
robot=Actor("robot_idle")
coin=Actor("coin_gold")
bomb=Actor("bomb")


#global variables
velocity=5
over=False
timer=0

#def start is to restart the game
def start():
    global velocity,timer,over
    velocity = 5
    timer = 0
    over = False
    robot.pos = WIDTH//2,HEIGHT//2
    move_bomb()
    move_coin()
    clock.schedule_interval(increment_timer,1.0)
    music.play("house")

def increment_timer():
    global timer
    timer=timer+1

def game_over():
    global over
    over=True
    clock.schedule_unique(start,5.0)
    clock.unschedule(increment_timer)
    music.stop()

def move_coin():
    
    coin.x=random.randint(20,WIDTH-20)
    coin.y=random.randint(20,HEIGHT-20)
    while coin.colliderect(bomb) or coin.colliderect(robot):
        coin.x=random.randint(20,WIDTH-20)
        coin.y=random.randint(20,HEIGHT-20)

def move_bomb():
    bomb.x=random.randint(20,WIDTH-20)
    bomb.y=random.randint(20,HEIGHT-20)
    while bomb.colliderect(robot) or bomb.colliderect(coin):
        bomb.x=random.randint(20,WIDTH-20)
        bomb.y=random.randint(20,HEIGHT-20)



def draw():
    global timer
    screen.clear()
    bg.draw()
    coin.draw()
    bomb.draw()
    if over:
        screen.draw.text("Game over",color="black",center=(WIDTH//2,HEIGHT//2))
    else:
        robot.draw()
    


def update():
    if keyboard.left and robot.left>0:
        robot.image="robot_left"
        robot.x=robot.x-velocity
    if keyboard.right and robot.right<WIDTH:
        robot.image="robot_right"
        robot.x=robot.x+velocity
    if keyboard.up and robot.top>0:
        robot.image="robot_idle"
        robot.y=robot.y-velocity
    if keyboard.down and robot.bottom<HEIGHT:
        robot.y=robot.y+velocity
        robot.image="robot_idle"
    if robot.colliderect(coin):
        sounds.find_money.play()
        move_coin()
        move_bomb()
    if robot.colliderect(bomb) and not over:
        sounds.bomb_explosion.play()
        move_bomb()
        game_over()





'''def on_key_up(key):
    if key==keys.left or key==keys.right:
        robot.image="robot_idle"'''


start()

pgzrun.go()