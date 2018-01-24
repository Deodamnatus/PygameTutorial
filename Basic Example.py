import pygame,time                      # import the pygame library which has many functions we will need later

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
pygame.init()                           # initializing the pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    # creating screen upon which we can place images


# importing images
red_dvd = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\red_dvd.png")
blue_dvd = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\blue_dvd.png")
green_dvd = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\green_dvd.png")

# dictionary to deal with selecting color
color_select = {0: red_dvd, 1:blue_dvd, 2:green_dvd}

black = (0,0,0)                         # define black as black RGB color
x,y = 0,0                               # base x and y pixel coordinates are 0,0
dx,dy = 1,1                             # moving box will go one pixel at a time
color = 0                               # current color will be red

done = False                            # while loop exit condition

while not done:
    for event in pygame.event.get():    # whenever pygame recognizes an event (IE: mouse movement, clicking on the window x
        if event.type == pygame.QUIT:   # if user clicked the red box to close the window
            done = True                 # exit the loop
        if event.type == pygame.MOUSEBUTTONUP:  # if user clicks
            color += 1
    x += dx
    y += dy

    if x + dx < 0 or x + dx + 100 > SCREEN_WIDTH :
        dx = -dx
    if y + dy < 0 or y + dy + 100 > SCREEN_HEIGHT:
        dy = -dy

    screen.fill(black)                  # fill screen with black pixels

    screen.blit(color_select[color%3], (x,y))
    time.sleep(0.01)

    pygame.display.flip()               # update display with current picture