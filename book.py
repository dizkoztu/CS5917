#import pygame
#from pygame.locals import *

#from OpenGL.GL import *
#from OpenGL.GLU import *

import numpy as np

class Book(object):
    """Create the class of a book"""

    def __init__(self, vertices, edges, surfaces): #, touches):
        """Initialize the attributes to describe a book"""
        #self.target = target
        #self.top = top
        #self.support = support
        self.vertices = vertices
        self.edges = edges
        self.surfaces = surfaces
        #self.touches = touches

    def top(self, surface):
        """Defines the top surface of the book"""
    #def target(self):
        """Defines the target book"""
    #def adjacent(self, surface, surface, surface, surface, surface):
        """Defines the adjacent surfaces for each surface"""
    #def touches(self, surface, surface):
        """Defines surfaces touching other surfaces"""
    def spine(self):
        """Defines the spine of the book surface"""



class BookShelf(object):
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

book1 = Book( 
    vertices = (
    (0.25, -2.5, -1.5),
    (0.25, 2.5, -1.5),
    (-0.25, 2.5, -1.5),
    (-0.25, -2.5, -1.5),
    (0.25, -2.5, 1.5),
    (0.25, 2.5, 1.5),
    (-0.25, -2.5, 1.5),
    (-0.25, 2.5, 1.5)
    ), 
    edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    ),

    surfaces = [
    (0,1,2,3,0,0,-1,"",1),
    (3,2,7,6,-1,0,0,"",1),
    (6,7,5,4,0,0,1,"",0),
    (4,5,1,0,1,0,0,"",1),
    (1,5,7,2,0,1,0,"top",0),
    (4,0,3,6,0,-1,0,"bottom",1)
    ]
    )


book2 = Book(
    vertices = (
    (-0.25, -2.5, -1.5),
    (-0.25, 2.5, -1.5),
    (-0.75, 2.5, -1.5),
    (-0.75, -2.5, -1.5),
    (-0.25, -2.5, 1.5),
    (-0.25, 2.5, 1.5),
    (-0.75, -2.5, 1.5),
    (-0.75, 2.5, 1.5)
    ),

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    ),

surfaces = [
    (0,1,2,3,0,0,-1,"",1),
    (3,2,7,6,-1,0,0,"",0),
    (6,7,5,4,0,0,1,"",0),
    (4,5,1,0,1,0,0,"",1),
    (1,5,7,2,0,1,0,"top",0),
    (4,0,3,6,0,-1,0,"bottom",1)
    ]
    )

book3 = Book(
vertices = (
    (0.75, -2.5, -1.5),
    (0.75, 2.5, -1.5),
    (0.25, 2.5, -1.5),
    (0.25, -2.5, -1.5),
    (0.75, -2.5, 1.5),
    (0.75, 2.5, 1.5),
    (0.25, -2.5, 1.5),
    (0.25, 2.5, 1.5)
    ),

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    ),

surfaces = [
    (0,1,2,3,0,0,-1,"",1),
    (3,2,7,6,-1,0,0,"",0),
    (6,7,5,4,0,0,1,"",0),
    (4,5,1,0,1,0,0,"",1),
    (1,5,7,2,0,1,0,"top",0),
    (4,0,3,6,0,-1,0,"bottom",1)
    ]
    )

shelf = BookShelf(
vertices = (
    (8, -2.7, -1.5),
    (8, -2.5, -1.5),
    (-8, -2.5, -1.5),
    (-8, -2.7, -1.5),
    (8, -2.7, 2.5),
    (8, -2.5, 2.5),
    (-8, -2.7, 2.5),
    (-8, -2.5, 2.5)
    ),

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    ),

surfaces = [
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    ]
    )

for area in book1.surfaces:
        j = len(book1.surfaces[0:1])/len(book1.surfaces[1:2])
        k = len(book1.surfaces[1:2])/len(book1.surfaces[0:1])
        m = min(j,k)
        print(j)
        print(k)
        print(m)

#book1.target()
#book1.top(book1.surfaces[0])
#print(book1.surfaces[0])

"""

# Defining the tops of the books
book1_top = book1.surfaces[4]
book2_top = book2.surfaces[4]
book3_top = book3.surfaces[4]
print('\n......')
print(book1_top)
print('\n......')
print(book2_top)
print('\n......')
print(book3_top)
print('\n......')

# Defining location of the book spines
book1_spine = book1.surfaces[2]
book2_spine = book2.surfaces[2]
book3_spine = book3.surfaces[2]
print('\n......')
print(book1_spine)
print('\n......')
print(book2_spine)
print('\n......')
print(book3_spine)
print('\n......')

# Defining the bottom support of the books
book1_support = book1.surfaces[5]
book2_support = book2.surfaces[5]
book3_support = book3.surfaces[5]
print('\n......')
print(book1_support)
print('\n......')
print(book2_support)
print('\n......')
print(book3_support)
print('\n......')

# Defining the surface of the books touching the wall
book1_wall = book1.surfaces[0]
book2_wall = book2.surfaces[0]
book3_wall = book3.surfaces[0]
print('\n......')
print(book1_wall)
print('\n......')
print(book2_wall)
print('\n......')
print(book3_wall)
print('\n......')

# Defining the surface of the books touching right
book1_touching_right = book1.surfaces[3]
book2_touching_right = book2.surfaces[3]
book3_touching_right = book3.surfaces[3]
print('\n......')
print(book1_touching_right)
print('\n......')
print(book2_touching_right)
print('\n......')
print(book3_touching_right)
print('\n......')

# Defining the surface of the books touching left
book1_touching_left = book1.surfaces[1]
book2_touching_left = book2.surfaces[1]
book3_touching_left = book3.surfaces[1]
print('\n......')
print(book1_touching_left)
print('\n......')
print(book2_touching_left)
print('\n......')
print(book3_touching_left)
print('\n......')

# Defining adjacent surfaces
book1_surface0_adjacent = ([book1.surfaces[1]] + 
                            [book1.surfaces[4]] + 
                            [book1.surfaces[3]] + 
                            [book1.surfaces[5]])
print(book1_surface0_adjacent)

book1_surface1_adjacent = ([book1.surfaces[0]] + 
                            [book1.surfaces[4]] + 
                            [book1.surfaces[2]] + 
                            [book1.surfaces[5]])
print(book1_surface1_adjacent)

book1_surface2_adjacent = ([book1.surfaces[1]] + 
                            [book1.surfaces[4]] + 
                            [book1.surfaces[3]] + 
                            [book1.surfaces[5]])
print(book1_surface2_adjacent)

book1_surface3_adjacent = ([book1.surfaces[2]] + 
                            [book1.surfaces[4]] + 
                            [book1.surfaces[0]] + 
                            [book1.surfaces[5]])
print(book1_surface3_adjacent)

book1_surface4_adjacent = ([book1.surfaces[0]] + 
                            [book1.surfaces[1]] + 
                            [book1.surfaces[2]] + 
                            [book1.surfaces[3]])
print(book1_surface4_adjacent)

book1_surface5_adjacent = ([book1.surfaces[0]] + 
                            [book1.surfaces[1]] + 
                            [book1.surfaces[2]] + 
                            [book1.surfaces[3]])
print(book1_surface5_adjacent)

book2_surface0_adjacent = ([book2.surfaces[1]] + 
                            [book2.surfaces[4]] + 
                            [book2.surfaces[3]] + 
                            [book2.surfaces[5]])
print(book2_surface0_adjacent)

book2_surface1_adjacent = ([book2.surfaces[0]] + 
                            [book2.surfaces[4]] + 
                            [book2.surfaces[2]] + 
                            [book2.surfaces[5]])
print(book2_surface1_adjacent)

book2_surface2_adjacent = ([book2.surfaces[1]] + 
                            [book2.surfaces[4]] + 
                            [book2.surfaces[3]] + 
                            [book2.surfaces[5]])
print(book2_surface2_adjacent)

book2_surface3_adjacent = ([book2.surfaces[2]] + 
                            [book2.surfaces[4]] + 
                            [book2.surfaces[0]] + 
                            [book2.surfaces[5]])
print(book2_surface3_adjacent)

book2_surface4_adjacent = ([book2.surfaces[0]] + 
                            [book2.surfaces[1]] + 
                            [book2.surfaces[2]] + 
                            [book2.surfaces[3]])
print(book2_surface4_adjacent)

book2_surface5_adjacent = ([book2.surfaces[0]] + 
                            [book2.surfaces[1]] + 
                            [book2.surfaces[2]] + 
                            [book2.surfaces[3]])
print(book2_surface5_adjacent)


book3_surface0_adjacent = ([book3.surfaces[1]] + 
                            [book3.surfaces[4]] + 
                            [book3.surfaces[3]] + 
                            [book3.surfaces[5]])
print(book3_surface0_adjacent)

book3_surface1_adjacent = ([book3.surfaces[0]] + 
                            [book3.surfaces[4]] + 
                            [book3.surfaces[2]] + 
                            [book3.surfaces[5]])
print(book3_surface1_adjacent)

book3_surface2_adjacent = ([book3.surfaces[1]] + 
                            [book3.surfaces[4]] + 
                            [book3.surfaces[3]] + 
                            [book3.surfaces[5]])
print(book3_surface2_adjacent)

book3_surface3_adjacent = ([book3.surfaces[2]] + 
                            [book3.surfaces[4]] + 
                            [book3.surfaces[0]] + 
                            [book3.surfaces[5]])
print(book3_surface3_adjacent)

book3_surface4_adjacent = ([book3.surfaces[0]] + 
                            [book3.surfaces[1]] + 
                            [book3.surfaces[2]] + 
                            [book3.surfaces[3]])
print(book3_surface4_adjacent)

book3_surface5_adjacent = ([book3.surfaces[0]] + 
                            [book3.surfaces[1]] + 
                            [book3.surfaces[2]] + 
                            [book3.surfaces[3]])
print(book3_surface5_adjacent)

# Defining the support for the books
shelf_support = shelf.surfaces[4]

books_on_shelf = (book1, book2, book3, shelf)
print(books_on_shelf)


# Calcualting the cross product of vectors

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