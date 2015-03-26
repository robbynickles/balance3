from editable import Editable
from _env import *

class UserStaticLine( Editable ):
    color    = (0,1,0,1)
    colltype = COLLTYPE_USERPLAT

    def adjust_coordinates( self, (ox, oy), (xdim, ydim) ):
        # Find absolute postion based on the passed-in pos and size.
        self.points = self.get_start(), self.get_end()

    def divide( self, S1, S2 ):
        # Create a new line, passing in the start and end of S1.
        # Create a new line, passing in the start and end of S2.
        pass
