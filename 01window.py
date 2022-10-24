import pygame as pg
from OpenGL.GL import *
'''
PyGame is essentially behaving like a context utility library from C++ in this file. This is a library which takes a 
OpenGL context and makes it accessible via user input and windows. In addition, an implementation of OpenGL exists in
Python whereby the function called are amply called from OpenGL.GL.
'''

pg.init()
pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,
                            pg.GL_CONTEXT_PROFILE_CORE)
pg.display.set_mode((640,480), pg.OPENGL|pg.DOUBLEBUF)
clock = pg.time.Clock()
#initialise opengl
glClearColor(0.1, 0.2, 0.2, 1)
running = True
while running:
    #check events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    #refresh screen
    glClear(GL_COLOR_BUFFER_BIT)
    pg.display.flip()

    #timing
    clock.tick(30)
pg.quit()
