
import numpy as np

class Pizza(object):
    """Create the class of a book"""

    def __init__(self, vertices, edges, surfaces): #, touches):
        """Initialize the attributes to describe a pizza"""
        #self.target = target
        #self.top = top
        #self.support = support
        self.vertices = vertices
        self.edges = edges
        self.surfaces = surfaces
        #self.touches = touches

    def top(self, surface):
        """Defines the top surface of the pizza"""
    def target(self):
        """Defines the target pizza"""
    #'ef adjacent(self, surface, surface, surface, surface, surface):
        """Defines the adjacent surfaces for each surface"""
    #def touches(self, surface, surface):
        """Defines surfaces touching other surfaces"""
    def spine(self):
        """Defines the spine of the pizza surface"""



class Freezer(object):
    """Create the class to describe bookshelf"""

    def __init__(self, vertices, edges, surfaces):
        """Initialize the attributes to describe a bookshelf"""
        #self.target = target
        #self.support = support
        self.vertices = vertices
        self.edges = edges
        self.surfaces = surfaces
    def support(self):
        """Defines the supporting surface of the bookshelf"""
    def target(self):
        """Defines the target book"""
freezer = Freezer(
vertices = (
    (0, 100, 0),
    (100, 100, 0),
    (100, 100, 140),
    (0, 100, 140),
    (0, 0, 0),
    (100, 0, 0),
    (100, 0, 140),
    (0, 0, 140),
    (10, 100, 10),
    (90, 100, 10),
    (90, 100, 130),
    (10, 100, 130),
    (10, 10, 10),
    (90, 10, 10),
    (90, 10, 130),
    (10, 10, 130)
    ),

edges = (
    (0,1),
    (1,2),
    (2,3),
    (3,0),
    (4,5),
    (5,6),
    (6,7),
    (7,4),
    (4,0),
    (5,1),
    (6,2),
    (3,7),
	(8,9),
    (9,10),
    (10,11),
    (11,8),
    (12,13),
    (13,14),
    (14,15),
    (15,12),
    (12,8),
    (13,9),
    (14,10),
    (15,11)
    ),

surfaces = [
    (0,1,5,4),
    (1,2,6,5),
    (2,3,7,6),
    (0,3,7,4),
    (4,5,6,7),
    (0-8,1-9,2-10,3-11),
    (8,9,13,12),
    (9,10,14,13),
    (10,11,14,14),
    (8,11,15,12),
    (12,13,14,15)
    ])




pizza1 = Pizza(
vertices = (
    (10, 10, 10),
    (40, 10, 10),
    (40, 10, 40),
    (10, 10, 40),
    (10, 15, 10),
    (40, 15, 10),
    (40, 15, 40),
    (10, 15, 40)
    ),

edges = (
    (0,1),
    (1,2),
    (2,3),
    (3,0),
    (4,5),
    (5,6),
    (6,7),
    (7,4),
    (4,0),
    (5,1),
    (6,2),
    (3,7),
    ),

surfaces = [
    (0,1,2,3,0,-1,0,"bottom",1),
    (4,5,6,7,0,1,0,"top",0),
    (0,1,5,4,0,0,-1,"",0),
    (1,2,6,5,1,0,0,"",1),
    (2,3,7,6,0,0,1,"",1),
    (0,3,7,4,-1,0,0,"",1)
    ]

)

#for surface in pizza1.surfaces[:]:
#    print(surface)

pizza2 = Pizza(
vertices = (
    (10, 10, 40),
    (40, 10, 40),
    (40, 10, 70),
    (10, 10, 70),
    (10, 15, 40),
    (40, 15, 40),
    (40, 15, 70),
    (10, 15, 70)
    ),

edges = (
    (0,1),
    (1,2),
    (2,3),
    (3,0),
    (4,5),
    (5,6),
    (6,7),
    (7,4),
    (4,0),
    (5,1),
    (6,2),
    (3,7),
    ),

surfaces = [
    (0,1,2,3,0,-1,0,"bottom",1),
    (4,5,6,7,0,1,0,"top",0),
    (0,1,5,4,0,0,-1,"",0),
    (1,2,6,5,1,0,0,"",1),
    (2,3,7,6,0,0,1,"",1),
    (0,3,7,4,-1,0,0,"",1)
    ]

)

pizza3 = Pizza(
vertices = (
    (10, 10, 70),
    (40, 10, 70),
    (40, 10, 100),
    (10, 10, 100),
    (10, 15, 70),
    (40, 15, 70),
    (40, 15, 100),
    (10, 15, 100)
    ),

edges = (
    (0,1),
    (1,2),
    (2,3),
    (3,0),
    (4,5),
    (5,6),
    (6,7),
    (7,4),
    (4,0),
    (5,1),
    (6,2),
    (3,7),
    ),

surfaces = [
    (0,1,2,3,0,-1,0,"bottom",1),
    (4,5,6,7,0,1,0,"top",0),
    (0,1,5,4,0,0,-1,"",0),
    (1,2,6,5,1,0,0,"",0),
    (2,3,7,6,0,0,1,"",1),
    (0,3,7,4,-1,0,0,"",1)
    ]

)


for area in pizza2.surfaces:
        j = len(pizza2.surfaces[0:1])/len(pizza2.surfaces[1:2])
        k = len(pizza2.surfaces[1:2])/len(pizza2.surfaces[0:1])
        m = min(j,k)
        print(j)
        #print(k)
        #print(m)

"""

# Defining the tops of the pizza boxes
pizza1_top = pizza1.surfaces[1]
pizza2_top = pizza2.surfaces[1]
pizza3_top = pizza3.surfaces[1]
print('\n......')
print(pizza1_top)
print('\n......')
print(pizza2_top)
print('\n......')
print(pizza3_top)
print('\n......')

# Defining location of the pizza box 'spines'
pizza1_spine = pizza1.surfaces[2]
pizza2_spine = pizza2.surfaces[2]
pizza3_spine = pizza3.surfaces[2]
print('\n......')
print(pizza1_spine)
print('\n......')
print(pizza2_spine)
print('\n......')
print(pizza3_spine)
print('\n......')

# Defining the bottom support of the pizza boxes
pizza1_support = pizza1.surfaces[0]
pizza2_support = pizza2.surfaces[0]
pizza3_support = pizza3.surfaces[0]
print('\n......')
print(pizza1_support)
print('\n......')
print(pizza2_support)
print('\n......')
print(pizza3_support)
print('\n......')

# Defining the surface of the pizza touching the wall
pizza1_wall = pizza1.surfaces[4]
pizza2_wall = pizza2.surfaces[4]
pizza3_wall = pizza3.surfaces[4]
print('\n......')
print(pizza1_wall)
print('\n......')
print(pizza2_wall)
print('\n......')
print(pizza3_wall)
print('\n......')

# Defining the surface of the pizza touching the right
pizza1_touching_right = pizza1.surfaces[5]
pizza2_touching_right = pizza2.surfaces[5]
pizza3_touching_right = pizza3.surfaces[5]
print('\n......')
print(pizza1_touching_right)
print('\n......')
print(pizza2_touching_right)
print('\n......')
print(pizza3_touching_right)
print('\n......')

# Defining the surface of the pizza touching the left
pizza1_touching_left = pizza1.surfaces[3]
pizza2_touching_left = pizza2.surfaces[3]
pizza3_touching_left = pizza3.surfaces[3]
print('\n......')
print(pizza1_touching_left)
print('\n......')
print(pizza2_touching_left)
print('\n......')
print(pizza3_touching_left)
print('\n......')

# Defining adjacent surfaces
pizza1_surface0_adjacent = ([pizza1.surfaces[2]] + 
                            [pizza1.surfaces[3]] + 
                            [pizza1.surfaces[4]] + 
                            [pizza1.surfaces[5]])
print(pizza1_surface0_adjacent)

pizza1_surface1_adjacent = ([pizza1.surfaces[2]] + 
                            [pizza1.surfaces[3]] + 
                            [pizza1.surfaces[4]] + 
                            [pizza1.surfaces[5]])
print(pizza1_surface1_adjacent)

pizza1_surface2_adjacent = ([pizza1.surfaces[0]] + 
                            [pizza1.surfaces[3]] + 
                            [pizza1.surfaces[1]] + 
                            [pizza1.surfaces[5]])
print(pizza1_surface2_adjacent)

pizza1_surface3_adjacent = ([pizza1.surfaces[1]] + 
                            [pizza1.surfaces[2]] + 
                            [pizza1.surfaces[0]] + 
                            [pizza1.surfaces[4]])
print(pizza1_surface3_adjacent)

pizza1_surface4_adjacent = ([pizza1.surfaces[1]] + 
                            [pizza1.surfaces[3]] + 
                            [pizza1.surfaces[0]] + 
                            [pizza1.surfaces[5]])
print(pizza1_surface4_adjacent)

pizza1_surface5_adjacent = ([pizza1.surfaces[1]] + 
                            [pizza1.surfaces[2]] + 
                            [pizza1.surfaces[0]] + 
                            [pizza1.surfaces[4]])

#***********************************************************************

pizza2_surface0_adjacent = ([pizza2.surfaces[2]] + 
                            [pizza2.surfaces[3]] + 
                            [pizza2.surfaces[4]] + 
                            [pizza2.surfaces[5]])
print(pizza2_surface0_adjacent)

pizza2_surface1_adjacent = ([pizza2.surfaces[2]] + 
                            [pizza2.surfaces[3]] + 
                            [pizza2.surfaces[4]] + 
                            [pizza2.surfaces[5]])
print(pizza2_surface1_adjacent)

pizza2_surface2_adjacent = ([pizza2.surfaces[0]] + 
                            [pizza2.surfaces[3]] + 
                            [pizza2.surfaces[1]] + 
                            [pizza2.surfaces[5]])
print(pizza2_surface2_adjacent)

pizza2_surface3_adjacent = ([pizza2.surfaces[1]] + 
                            [pizza2.surfaces[2]] + 
                            [pizza2.surfaces[0]] + 
                            [pizza2.surfaces[4]])
print(pizza2_surface3_adjacent)

pizza2_surface4_adjacent = ([pizza2.surfaces[1]] + 
                            [pizza2.surfaces[3]] + 
                            [pizza2.surfaces[0]] + 
                            [pizza2.surfaces[5]])
print(pizza2_surface4_adjacent)

pizza2_surface5_adjacent = ([pizza2.surfaces[1]] + 
                            [pizza2.surfaces[2]] + 
                            [pizza2.surfaces[0]] + 
                            [pizza2.surfaces[4]])
print(pizza2_surface5_adjacent)
#***********************************************************************

pizza3_surface0_adjacent = ([pizza3.surfaces[2]] + 
                            [pizza3.surfaces[3]] + 
                            [pizza3.surfaces[4]] + 
                            [pizza3.surfaces[5]])
print(pizza3_surface0_adjacent)

pizza3_surface1_adjacent = ([pizza3.surfaces[2]] + 
                            [pizza3.surfaces[3]] + 
                            [pizza3.surfaces[4]] + 
                            [pizza3.surfaces[5]])
print(pizza3_surface1_adjacent)

pizza3_surface2_adjacent = ([pizza3.surfaces[0]] + 
                            [pizza3.surfaces[3]] + 
                            [pizza3.surfaces[1]] + 
                            [pizza3.surfaces[5]])
print(pizza3_surface2_adjacent)

pizza3_surface3_adjacent = ([pizza3.surfaces[1]] + 
                            [pizza3.surfaces[2]] + 
                            [pizza3.surfaces[0]] + 
                            [pizza3.surfaces[4]])
print(pizza3_surface3_adjacent)

pizza3_surface4_adjacent = ([pizza3.surfaces[1]] + 
                            [pizza3.surfaces[3]] + 
                            [pizza3.surfaces[0]] + 
                            [pizza3.surfaces[5]])
print(pizza3_surface4_adjacent)

pizza3_surface5_adjacent = ([pizza3.surfaces[1]] + 
                            [pizza3.surfaces[2]] + 
                            [pizza3.surfaces[0]] + 
                            [pizza3.surfaces[4]])
print(pizza3_surface5_adjacent)

# Defining the support for the books
freezer_bottom = freezer.surfaces[4]

pizzas_in_freezer = (pizza1, pizza2, pizza3, freezer)
print(pizzas_in_freezer)


a = np.array([0,1,0])  
b = np.array([0,0,1])  
c = np.cross(a,b)
print(c)
d = np.cross(a,c)
print(d)
e = np.cross(a,d)
print(e)
f = np.cross(c,b)
print(f)
"""


"""
# Calcualting the cross product of vectors
if np.array([0,1,0]):
    a = np.array([0,1,0])  
    b = np.array([0,0,1])  
    c = np.cross(a,b)
    print(c)
    d = np.cross(a,c)
    print(d)
    e = np.cross(a,d)
    print(e)
    f = np.cross(c,b)
    print(f)

elif np.array([0,-1,0]):
    a = np.array([0,-1,0])  
    b = np.array([0,0,1])  
    c = np.cross(a,b)
    print(c)
    d = np.cross(a,c)
    print(d)
    e = np.cross(a,d)
    print(e)
    f = np.cross(c,b)
    print(f)

elif np.array([1,0,0]):
    a = np.array([1,0,0])  
    b = np.array([0,0,-1])  
    c = np.cross(a,b)
    print(c)
    d = np.cross(a,c)
    print(d)
    e = np.cross(a,d)
    print(e)
    f = np.cross(c,b)
    print(f)

elif np.array([-1,0,0]):
    a = np.array([-1,0,0])  
    b = np.array([0,0,1])  
    c = np.cross(a,b)
    print(c)
    d = np.cross(a,c)
    print(d)
    e = np.cross(a,d)
    print(e)
    f = np.cross(c,b)
    print(f)

elif np.array([0,0,1]):
    a = np.array([0,0,1])  
    b = np.array([1,0,0])  
    c = np.cross(a,b)
    print(c)
    d = np.cross(a,c)
    print(d)
    e = np.cross(a,d)
    print(e)
    f = np.cross(c,b)
    print(f)

else np.array([0,0,-1]):
    a = np.array([0,0,-1])  
    b = np.array([-1,0,0])  
    c = np.cross(a,b)
    print(c)
    d = np.cross(a,c)
    print(d)
    e = np.cross(a,d)
    print(e)
    f = np.cross(c,b)
    print(f)
"""
"""
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) # Double buffer in OpenGL for the display

    gluPerspective(45, (display[0]/display[1]), 50, 700.0)

    glTranslatef(-100.0, -150.0, -400) # Distance of viewing range (for graphics)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 100, 1) # Rotates the object
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Freezer()
        PizzaBox1()
        PizzaBox2()
        PizzaBox3()
        pygame.display.flip()
        pygame.time.wait(50)


main()
"""