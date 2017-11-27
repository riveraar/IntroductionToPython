"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Angel Rivera.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

angel = rg.SimpleTurtle('turtle')
angel.pen = rg.Pen('midnight blue', 3)
angel.speed = 5

drewe = rg.SimpleTurtle('turtle')
drewe.pen = rg.Pen('pink', 3)
drewe.speed = 10

size = 100

for k in range(8):
    angel.draw_circle(size)
    drewe.draw_square(size)

    angel.pen_up()
    angel.right(45)
    angel.forward(10)
    angel.left(45)
    angel.pen_down()

    drewe.pen_up()
    drewe.right(45)
    drewe.forward(10)
    drewe.left(45)
    drewe.pen_down()

    size = size - 10

window.close_on_mouse_click()
