import pygame                           # import the pygame library which has many functions we will need later

pygame.init()                           # initializing the pygame window
screen = pygame.display.set_mode((400, 300))    # creating screen upon which we can place images

done = False                            # while loop exit condition

ball = pygame.image.load("")

while not done:
    for event in pygame.event.get():    # whenever pygame recognizes an event (IE: mouse movement, clicking on the window x
        if event.type == pygame.QUIT:   # if user clicked the red box to close the window
            done = True                 # exit the loop


    black = (0,0,0)
    screen.fill(black)

    pygame.display.flip()               # update display with current picture