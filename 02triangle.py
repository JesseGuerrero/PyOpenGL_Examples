import pygame as pg
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

def createShader(vertexFilepath, fragmentFilepath):
    with open(vertexFilepath, 'r') as f:
        vertex_src = f.readlines()
    with open(fragmentFilepath, 'r') as f:
        fragment_src = f.readlines()
    shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER),
                            compileShader(fragment_src, GL_FRAGMENT_SHADER))
    return shader

class Triangle:
    def __init__(self):
        # x, y, z, r, g, b
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0, # RGB is calculated magic in backend
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            0.0, 0.5, 0.0, 0.0, 0.0, 1.0
        )
        self.vertices = np.array(self.vertices, dtype=np.float32)

        self.vertex_count = 3 #A vertex is a single point

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        #bound vao
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

        #bound vao, vbo
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        '''
        VBOs are the vertices with a parsing algorithm passed as arguments for reading. VAOs hold VBOs with some magic
        to put them together. The magic included with the VAO is part of the reason it is an object.
        
        VAO is a combination of VBOs and constructs a mesh with all meta data remembered in the VAO.
        Link: https://ogldev.org/www/tutorial32/tutorial32.html  
        '''

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    def destroy(self):
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))


pg.init()
pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,
                            pg.GL_CONTEXT_PROFILE_CORE)
pg.display.set_mode((640, 480), pg.OPENGL | pg.DOUBLEBUF)
clock = pg.time.Clock()
# initialise opengl
glClearColor(0.1, 0.2, 0.2, 1)
triangle = Triangle()
shader = createShader("02shaders/vertex.glsl", "02shaders/fragment.glsl")
glUseProgram(shader)
running = True
while (running):
    # check events
    for event in pg.event.get():
        if (event.type == pg.QUIT):
            running = False
    # refresh screen
    glClear(GL_COLOR_BUFFER_BIT)

    glBindVertexArray(triangle.vao)
    glUseProgram(shader)
    glDrawArrays(GL_TRIANGLES, 0, triangle.vertex_count)

    pg.display.flip()

    # timing
    clock.tick(60)
triangle.destroy()
glDeleteProgram(shader)
pg.quit()