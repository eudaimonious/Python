from gasp import *          # import everything from the gasp library

begin_graphics(title="Houses at Night", background=color.BLACK)            # open the graphics canvas

Box((20, 20), 100, 100, filled=True, color=color.BLUE)     # the house
Box((55, 20), 30, 50, filled=True, color=color.GREEN)       # the door
Box((40, 80), 20, 20, filled=True, color=color.YELLOW)       # the left window
Box((80, 80), 20, 20, filled=True, color=color.YELLOW)       # the right window
Polygon((10,100),(70,120),(110,100), filled=True, color=color.BLUE)  #the roof

update_when('key_pressed')  # keep the canvas open until a key is pressed
end_graphics()              # close the canvas (which would happen
                            # anyway, since the script ends here, but it
                            # is better to be explicit).
