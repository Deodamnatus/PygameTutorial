import pygame                           # import the pygame library which has many functions we will need later
pygame.init()                           # initializing the pygame window
screen = pygame.display.set_mode((400, 300))    # creating screen upon which we can place images
done = False                            # while loop exit condition

black = (0,0,0)
red_dvd = pygame.image.load("/home/jeremy/Pictures/red_dvd.png")

while not done:
   for event in pygame.event.get():    # whenever pygame recognizes an event (IE: mouse movement, clicking on the window
       if event.type == pygame.QUIT:   # if user clicked the red box to close the window
           done = True                 # exit the loop
   screen.fill(black)
   screen.blit(red_dvd, (0,0))
   pygame.display.flip()               # update display with current picture

