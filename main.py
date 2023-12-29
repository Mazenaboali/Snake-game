# snake game

#import libraries
import random
import curses

#initialize curses Library
screen = curses.initscr()

#hide cursor on the screen
curses.curs_set(0)

#get max height and max width of the screen
screen_height, screen_Width = screen.getmaxyx()

# create window
window = curses.newwin(screen_height,screen_Width,0,0)

# allow window to recieve input from the user
window.keypad(True)

# set the delay for updating the screen
window.timeout(200)

# set the x,y coordinate of the initial positon of the snake head
snk_y=screen_height//2
snk_x=screen_Width//4

# define the initial position of the snake body
snake=[
    [snk_y,snk_x],
    [snk_y,snk_x-1],
    [snk_y,snk_x-2],
]

# create the food in the middle of the window
food =[screen_height//2,screen_Width//2]

# add the food by using PI character from the curse module
window.addch(food[0],food[1],curses.ACS_PI)

# set the initial movement direction of the snake to right
key= curses.KEY_RIGHT

# create the game loop that loops forever until player loses or quit
while True:
# get the next key that will be pressed by the user
   new_key = window.getch()

# if user doesnot input anything, key remains the same , else key will be set to the pressed key
   if new_key == -1:
     key = key
   else:
     key = new_key
# check if snake collided with the walls or itself
   if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_Width] or snake[0] in snake[1:]:
         curses.endwin()
         quit()
# set the new position of the snake head to the first position of the snake list
   new_head=[snake[0][0],snake[0][1]]

   if key == curses.KEY_RIGHT:
       new_head[1]+=1
   if key == curses.KEY_LEFT:
       new_head[1]-=1
   if key == curses.KEY_UP:
       new_head[0]-=1
   if key == curses.KEY_DOWN:
       new_head[0]+=1
# add the new head to the snake List
   snake.insert(0,new_head)
# check if the snake ate the food or not
   if snake[0] == food :
     food=None # remove food if snake ate it
     while food is None :
       new_food=[
         random.randint(1,screen_height-1),
         random.randint(1,screen_Width-1),
       ]
       if new_food not in snake :
           food = new_food
       else:
            food = None
# add the food by using PI character from the curse module
     window.addch(food[0],food[1],curses.ACS_PI)
   else:
       tail =snake.pop()
       window.addch(tail[0],tail[1],' ')
   window.addch(snake[0][0],snake[0][1],curses.ACS_CKBOARD)





