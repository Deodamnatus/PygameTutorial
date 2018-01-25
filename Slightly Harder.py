import pygame                           # import the pygame library which has many functions we will need later

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
pygame.init()                           # initializing the pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    # creating screen upon which we can place images
done = False                            # while loop exit condition
black = (0,0,0)
x,y = 0,0                               # base x and y pixel coordinates are 0,0
dx,dy = 1,1                             # moving box will go one pixel at a time
red_dvd = pygame.image.load("/home/jeremy/Pictures/red_dvd.png")
while not done:
   for event in pygame.event.get():    # whenever pygame recognizes an event (IE: mouse movement, clicking on the window
       if event.type == pygame.QUIT:   # if user clicked the red box to close the window
           done = True                 # exit the loop
   x += dx
   y += dy
   if x + dx < 0 or x + dx + 100 > SCREEN_WIDTH: # Extra 100 here because image position is measured from top left corner
      dx = -dx                                   # and the images are 100 x 100
   if y + dy < 0 or y + dy + 100 > SCREEN_HEIGHT:
      dy = -dy
   screen.fill(black)
   screen.blit(red_dvd, (x,y))
   pygame.display.flip()               # update display with current picture