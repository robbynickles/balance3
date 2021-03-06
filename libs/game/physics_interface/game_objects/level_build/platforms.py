from _env import *

from static_line import PreStaticLine

class LavaLine( PreStaticLine ):
    def build_phys_obj( self, space ):
        PreStaticLine.build_phys_obj( self, space )

        for sh in self.shapes:
            sh.collision_type = COLLTYPE_LAVA

        def ball_hit_lava(space, arbiter): 
            ball, lava = arbiter.shapes
            self.physics_interface.smap[ ball ].explode()
            self.physics_interface.add_notification( self, 'Game Over' )

        submit_collision_handler( COLLTYPE_LAVA, COLLTYPE_BALL, ball_hit_lava )

    def build_render_obj( self ):
        self.color = (1,0,0,1)
        PreStaticLine.build_render_obj( self )

class FriendlyLine( PreStaticLine ):

    def build_render_obj( self ):
        self.color = (0,1,0,1)
        PreStaticLine.build_render_obj( self )
