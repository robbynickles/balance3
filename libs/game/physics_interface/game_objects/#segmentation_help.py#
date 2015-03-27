from math import cos, atan

def slope( (x1,y1), (x2, y2) ):
    try:
        m = (y2-y1) / (x2-x1)
    except ZeroDivisionError:
        # For a vertical line, approximate the slope with a big number.
        m = 100000
    return m

def line_function( (x1,y1), (x2, y2) ):
    m = slope( (x1,y1), (x2, y2) )
    return lambda x: m*(x-x1) + y1

def close_to( u, v ):
    EPSILON = 10
    return v - EPSILON <= u <= v + EPSILON

def within_bounds( segmentation, x ):
    return segmentation[0][0] < x < segmentation[-1][0] or \
           segmentation[-1][0] < x < segmentation[0][0]

def find_segment( self, pos ):
    x, y         = pos
    segmentation = self.points
    for i in range( len(segmentation) - 1 ):
        a, b = segmentation[i], segmentation[i+1]

        # Generate the equation of the line between a and b.
        F    = line_function( a, b )

        # Make sure x is within the bounds of the segmentation.
        if within_bounds( segmentation, x ):
            # See if y is close enough to the line to be considered touching that segment.
            if close_to( y, F(x) ):
                return a, b

    # If no segment matched, the pos wasn't on the segmentation
    raise AssertionError

def split_segment( seg, pos ):
    x, y = pos
    a, b = seg
    GAP  = 5 * ( cos( atan( slope( a, b ) ) ) )
    if a[0] > b[0]:
        x1 = x+GAP
        x2 = x-GAP
        if x1 >= a[0]:
            x1 = x + (a[0] - x)
        if x2 <= b[0]:
            x2 = x - (x - b[0])
    else:
        x1 = x-GAP
        x2 = x+GAP
        if x1 <= a[0]:
            x1 = x - (x - a[0])
        if x2 >= b[0]:
            x2 = x + (b[0] - x)

    F = line_function( a, b )
    return [ [a, (x1, F(x1)) ], [ (x2, F(x2)), b ] ]

def segs_before( self, seg ):
    a, b         = seg
    segmentation = [ p for p in self.points ]
    for i in range( len(segmentation) - 1 ):
        k, l     = segmentation[i], segmentation[i+1]
        if (a,b) == (k,l):
            return segmentation[:i]
    return []

def segs_after( self, seg ):
    a, b         = seg
    segmentation = [ p for p in self.points ]
    for i in range( len(segmentation) - 1 ):
        k, l     = segmentation[i], segmentation[i+1]
        if (a,b) == (k,l):
            return segmentation[i+1+1:]
    return []
