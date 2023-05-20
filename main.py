from PySide6.QtOpenGL import QOpenGLWindow
from PySide6.QtWidgets import QApplication
import ctypes
import numpy as np
from OpenGL import GL
from OpenGL.GL.shaders import compileProgram, compileShader 
from math import pi, cos, sin
from random import random


class OpenGLMainWindow(QOpenGLWindow):
    def initializeGL(self):
        listax, listay = self.pointCircle(0.66, 0.66, 0.28)
        self.vertices = np.array([# X     Y    Z    R     G    B
                                  -1.0, -1.0, 0.0, 0.0,  0.0, 1.0,
                                   0.0,  1.0, 0.0, 0.0,  0.0, 1.0,
                                   1.0, -1.0, 0.0, 0.0,  0.0, 1.0,

                                   
                                  -1.0, -1.0, 0.0, 0.0,  0.0, 1.0,
                                   0.0,  1.0, 0.0, 0.0,  0.0, 1.0,
                                  -1.0,  1.0, 0.0, 0.0,  0.0, 1.0,
                                   
                                   
                                   0.0,  1.0, 0.0, 0.0,  0.0, 1.0,
                                   1.0, -1.0, 0.0, 0.0,  0.0, 1.0,
                                   1.0,  1.0, 0.0, 0.0,  0.0, 1.0,

                                   -1.0, -0.2, 0.0, 0.0, 1.0, 0.0, #A
                                   -1.0, -1.0, 0.0, 0.0, 1.0, 0.0, #B
                                   1.0, -1.0, 0.0, 0.0, 1.0, 0.0, #C
                                   
                                   -1.0, -0.2, 0.0, 0.0, 1.0, 0.0, #A
                                   1.0, -1.0, 0.0, 0.0, 1.0, 0.0, #C
                                   1.0, -0.2, 0.0, 0.0, 1.0, 0.0, #D

                                   #House
                                   -0.6, -0.4, 0.0, 0.9, 0.9, 0.9, #E
                                   -0.71, -0.6, 0.0, 0.9, 0.9, 0.9, #F
                                   -0.51, -0.6, 0.0, 0.9, 0.9, 0.9, #G

                                   -0.51, -0.6, 0.0, 0.0, 0.0, 0.8, #G
                                   -0.71, -0.6, 0.0, 0.0, 0.0, 0.8, #F
                                   -0.71, -0.8, 0.0, 0.0, 0.0, 0.8, #H

                                   -0.51, -0.6, 0.0, 0.0, 0.0, 0.8, #G
                                   -0.51, -0.8, 0.0, 0.0, 0.0, 0.8, #I
                                   -0.71, -0.8, 0.0, 0.0, 0.0, 0.74, #H

                                   -0.6, -0.4, 0.0, 1.0, 0.0, 0.0, #E
                                   -0.2, -0.4, 0.0, 1.0, 0.0, 0.0, #K
                                   -0.3, -0.6, 0.0, 1.0, 0.0, 0.0, #J

                                   -0.6, -0.4, 0.0, 1.0, 0.0, 0.0, #E
                                   -0.3, -0.6, 0.0, 1.0, 0.0, 0.0, #J
                                   -0.51, -0.6, 0.0, 1.0, 0.0, 0.0, #G

                                   -0.3, -0.6, 0.0, 1.0, 0.0, 0.0, #J
                                   -0.2, -0.4, 0.0, 1.0, 0.0, 0.0, #K
                                   -0.1, -0.6, 0.0, 1.0, 0.0, 0.0, #L

                                   -0.1, -0.6, 0.0, 0.0, 0.0, 0.8, #L
                                   -0.51, -0.8, 0.0, 0.0, 0.0, 0.8, #I
                                   -0.51, -0.6, 0.0, 0.0, 0.0, 0.8, #G

                                   -0.1, -0.6, 0.0, 0.0, 0.0, 0.8, #L
                                   -0.51, -0.8, 0.0, 0.0, 0.0, 0.8, #I
                                   -0.1, -0.71, 0.0, 0.0, 0.0, 0.8, #N

                                   -0.1, -0.6, 0.0, 0.0, 0.0, 0.8, #L
                                   -0.51, -0.8, 0.0, 0.0, 0.0, 0.8, #I
                                   -0.1, -0.8, 0.0, 0.0, 0.0, 0.74, #M

                                   #DOOR
                                   -0.65, -0.65, 0.0, 0.9, 0.9, 0.9,
                                   -0.59, -0.65, 0.0, 0.9, 0.9, 0.9,
                                   -0.59, -0.8, 0.0, 0.9, 0.9, 0.9,

                                   -0.65, -0.8, 0.0, 0.9, 0.9, 0.9,
                                   -0.65, -0.65, 0.0, 0.9, 0.9, 0.9,
                                   -0.59, -0.8, 0.0, 0.9, 0.9, 0.9,
                                   

                                   #Moinho
                                   -0.95, -0.59, 0.0, 0.8, 0.0, 0.0,
                                   -0.8, -0.59, 0.0, 0.8, 0.0, 0.0,
                                   -0.87, -0.1, 0.0, 1.0, 0.0, 0.0,

                                   -0.87, -0.1, 0.0, 0.01, 0.01, 0.05,
                                   -0.8, -0.59, 0.0, 0.01, 0.01, 0.05,
                                   -0.78, -0.47, 0.0, 0.01, 0.01, 0.05,

                                   #pas do moinho
                                   -0.87, -0.1, 0.0, 0.9, 0.9, 0.9,
                                   -0.84, -0.15, 0.0, 0.9, 0.9, 0.9,
                                   -0.90, -0.15, 0.0, 0.9, 0.9, 0.9,

                                   -0.87, -0.1, 0.0, 0.9, 0.9, 0.9,
                                   -0.84, -0.05, 0.0, 0.9, 0.9, 0.9,
                                   -0.90, -0.05, 0.0, 0.9, 0.9, 0.9,

                                   -0.87, -0.1, 0.0, 0.9, 0.9, 0.9,
                                   -0.92, -0.07,  0.0, 0.9, 0.9, 0.9,
                                   -0.92, -0.13,  0.0, 0.9, 0.9, 0.9,

                                   -0.87, -0.1, 0.0, 0.9, 0.9, 0.9,
                                   -0.82, -0.07,  0.0, 0.9, 0.9, 0.9,
                                   -0.82, -0.13,  0.0, 0.9, 0.9, 0.9,


                                   #rua da casa
                                   #(-0.65, -0.65)
                                   #(-0.59, -0.65)
                                   #(-0.59, -0.80)
                                   #(-0.65, -0.80)
                                   -0.65, -0.8, 0.0, 0.9, 0.9, 0.9,
                                   -0.59, -0.8, 0.0, 0.9, 0.9, 0.9,
                                   -1.00, -1.0, 0.0, 0.9, 0.9, 0.9,


                                   -1.00, -1.0, 0.0, 0.9, 0.9, 0.9,
                                   -0.59, -0.8, 0.0, 0.9, 0.9, 0.9,
                                   -0.95, -1.0, 0.0, 0.9, 0.9, 0.9,




                                   #solar panels

                                
                                     ], dtype=np.float32)
        
        self.lines_vertices = np.array([ 
                                   -0.6, -0.4, 0.0, 0.0, 0.0, 0.0, #E
                                   -0.71, -0.6, 0.0, 0.0, 0.0, 0.0, #F

                                   -0.6, -0.4, 0.0, 0.0, 0.0, 0.0, #E
                                   -0.51, -0.6, 0.0, 0.0, 0.0, 0.0, #G

                                   -0.51, -0.6, 0.0, 0.0, 0.0, 0.0, #G
                                   -0.71, -0.6, 0.0, 0.0, 0.0, 0.0, #F

                                   -0.6, -0.4, 0.0, 0.0, 0.0, 0.0, #E
                                   -0.2, -0.4, 0.0, 0.0, 0.0, 0.0, #K

                                   -0.2, -0.4, 0.0, 0.0, 0.0, 0.0, #K
                                   -0.1, -0.6, 0.0, 0.0, 0.0, 0.0, #L

                                   -0.1, -0.6, 0.0, 0.0, 0.0, 0.0, #L
                                   -0.51, -0.6, 0.0, 0.0, 0.0, 0.0, #G

                                   -0.1, -0.6, 0.0, 0.0, 0.0, 0.0, #L
                                   -0.1, -0.8, 0.0, 0.0, 0.0, 0.0, #M

                                   -0.1, -0.8, 0.0, 0.0, 0.0, 0.0, #M
                                   -0.51, -0.8, 0.0, 0.0, 0.0, 0.0, #I

                                   -0.51, -0.8, 0.0, 0.0, 0.0, 0.0, #I
                                   -0.51, -0.6, 0.0, 0.0, 0.0, 0.0, #G

                                   -0.51, -0.8, 0.0, 0.0, 0.0, 0.0, #I
                                   -0.71, -0.8, 0.0, 0.0, 0.0, 0.0, #H

                                   -0.71, -0.8, 0.0, 0.0, 0.0, 0.0, #H
                                   -0.71, -0.6, 0.0, 0.0, 0.0, 0.0, #F

                                   #DOOR
                                   -0.65, -0.65, 0.0, 0.0, 0.0, 0.0,
                                   -0.59, -0.65, 0.0, 0.0, 0.0, 0.0,

                                   -0.65, -0.65, 0.0, 0.0, 0.0, 0.0,
                                   -0.65, -0.8, 0.0, 0.0, 0.0, 0.0,

                                   -0.59, -0.65, 0.0, 0.0, 0.0, 0.0,
                                   -0.59, -0.8, 0.0, 0.0, 0.0, 0.0,

                                   #Moinho
                                   -0.95, -0.59, 0.0, 0.0, 0.0, 0.0,
                                   -0.8, -0.59, 0.0, 0.0, 0.0, 0.0,
                                    
                                   -0.8, -0.59, 0.0, 0.0, 0.0, 0.0,
                                   -0.86, -0.15, 0.0, 0.0, 0.0, 0.0,

                                   -0.95, -0.59, 0.0, 0.0, 0.0, 0.0,
                                   -0.88, -0.15, 0.0, 0.0, 0.0, 0.0,

                                   -0.86, -0.15, 0.0, 0.0, 0.0, 0.0,
                                   -0.88, -0.15, 0.0, 0.0, 0.0, 0.0,

                                   #pas do moinho 1
                                   -0.87, -0.1, 0.0, 0.0, 0.0, 0.0,
                                   -0.84, -0.15, 0.0, 0.0, 0.0, 0.0,

                                   -0.84, -0.15, 0.0, 0.0, 0.0, 0.0,
                                   -0.90, -0.15, 0.0, 0.0, 0.0, 0.0,

                                   -0.90, -0.15, 0.0, 0.0, 0.0, 0.0,
                                   -0.87, -0.1, 0.0, 0.0, 0.0, 0.0,

                                   #pas do moinho 2
                                   -0.87, -0.1, 0.0, 0.0, 0.0, 0.0,
                                   -0.84, -0.05, 0.0, 0.0, 0.0, 0.0,

                                   -0.84, -0.05, 0.0, 0.0, 0.0, 0.0,
                                   -0.90, -0.05, 0.0, 0.0, 0.0, 0.0,

                                   -0.90, -0.05, 0.0, 0.0, 0.0, 0.0,
                                   -0.87, -0.1, 0.0, 0.0, 0.0, 0.0,

                                   #pas do moinho 3
                                   -0.87, -0.1, 0.0, 0.0, 0.0, 0.0,
                                   -0.92, -0.07,  0.0, 0.0, 0.0, 0.0,

                                   -0.92, -0.07,  0.0, 0.0, 0.0, 0.0,
                                   -0.92, -0.13,  0.0, 0.0, 0.0, 0.0,

                                   -0.92, -0.13,  0.0, 0.0, 0.0, 0.0,
                                   -0.87, -0.1, 0.0, 0.0, 0.0, 0.0,


                                   #pas do moinho 4
                                   -0.87, -0.1, 0.0, 0.0, 0.0, 0.0,
                                   -0.82, -0.07,  0.0, 0.0, 0.0, 0.0,

                                   -0.82, -0.07,  0.0, 0.0, 0.0, 0.0,
                                   -0.82, -0.13,  0.0, 0.0, 0.0, 0.0,

                                   -0.82, -0.13,  0.0, 0.0, 0.0, 0.0,
                                   -0.87, -0.1, 0.0, 0.0, 0.0, 0.0,
                                   
                                   ], dtype=np.float32)
        
        """
        -0.95, -0.59, 0.0, 0.0, 0.0, 0.0,
        -0.8, -0.59, 0.0, 0.0, 0.0, 0.0,
        -0.8, -0.59, 0.0, 0.0, 0.0, 0.0,
        -0.87, -0.1, 0.0, 0.0, 0.0, 0.0,
        -0.87, -0.1, 0.0, 0.0, 0.0, 0.0,
        -0.95, -0.59, 0.0, 0.0, 0.0, 0.0,
        """
        
        i = 0
        while(i<1000):
            if(i%2 == 0):
                self.vertices = np.append(self.vertices, 0.66)
                self.vertices = np.append(self.vertices, 0.65)
                self.vertices = np.append(self.vertices, 0.0)
                self.vertices = np.append(self.vertices, 1.0)
                self.vertices = np.append(self.vertices, 1.0)
                self.vertices = np.append(self.vertices, 0.0)
            self.vertices = np.append(self.vertices, listax[i])
            self.vertices = np.append(self.vertices, listay[i])
            self.vertices = np.append(self.vertices, 0.0)
            self.vertices = np.append(self.vertices, 1.0)
            self.vertices = np.append(self.vertices, 1.0)
            self.vertices = np.append(self.vertices, 0.0)
            i = i + 1
            
        

        aux = self.vertices
        self.vertices = np.array(aux, dtype=np.float32)
        
        
        self.shader = self.load_shaders('shaders/vertex_sh.txt', 'shaders/fragment_sh.txt')
        GL.glUseProgram(self.shader)
        self.tri = _DefaultTriangle(self.vertices, 0, 1)
        GL.glBindVertexArray(self.tri.vao)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.tri.vertices.size)


        self.lines = _DefaultLines(self.lines_vertices, 0, 1)
        GL.glBindVertexArray(self.lines.vao)
        GL.glDrawArrays(GL.GL_LINES, 0, self.lines.vertices.size)

        """
        GL.glUseProgram(self.shader)
        self.tri2 = _DefaultTriangle(self.vertices2, 0, 1)
        GL.glBindVertexArray(self.tri2.vao)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.tri.vertices.size)
        """
        GL.glClearColor(0.2,0.2,0.5,1)
        
    

    def load_shaders(self, path_vertex, path_fragment):
        with open(path_vertex, 'r') as f:
            vertex_src = f.readlines()

        with open(path_fragment, 'r') as f:
            fragment_src = f.readlines()

        shader = compileProgram(
                compileShader(vertex_src, GL.GL_VERTEX_SHADER),
                compileShader(fragment_src, GL.GL_FRAGMENT_SHADER)
        )

        return shader
    
    def minha_soma(self, x, y):
        return x+y
        
    def paintGL(self):
        GL.glClear( GL.GL_COLOR_BUFFER_BIT )
        print(self.minha_soma(2,3))

        GL.glBindVertexArray(self.tri.vao)
        GL.glDrawArrays(GL.GL_TRIANGLES,0,int(self.vertices.size/6))

        GL.glBindVertexArray(self.lines.vao)
        GL.glDrawArrays(GL.GL_LINES, 0,int(self.lines_vertices.size/6))

    def pointCircle(self, xCircle, yCircle, radius):
        listax = []
        listay = []
        i = 1
        while(i<1001):
            aux = random()
            theta = aux * 2 * pi
            listax.append(xCircle + cos(theta) * radius)
            listay.append(yCircle + sin(theta) * radius)
            i = i + 1
        return listax, listay


class _DefaultTriangle():
    def __init__(self, vertices, position, color):

        self.vertices = vertices

        self.vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao)
        self.vbo = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL.GL_STATIC_DRAW)

        #pega a posição do atributo no shaders via forma programática
        ##position = GL.glGetAttribLocation(self.shader, "e_vertice")
        ##color = GL.glGetAttribLocation(self.shader, "e_cor")
        



        #diz qual atributo deve ser usado (posição ou cor) a partir de um index
        GL.glEnableVertexAttribArray(position)
        GL.glVertexAttribPointer(position, 3, GL.GL_FLOAT, GL.GL_FALSE, 24, ctypes.c_void_p(0))
        GL.glEnableVertexAttribArray(color)
        GL.glVertexAttribPointer(color, 3, GL.GL_FLOAT, GL.GL_FALSE, 24, ctypes.c_void_p(12))

        #GL.glVertexAttribPointer(index, pontos (xyz), tipo de dado, transformacao, qnt de bytes para o proximo vertice, mudança de ponto para cor)


class _DefaultLines():
    def __init__(self, vertices, position, color):
        self.vertices = vertices

        self.vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao)
        self.vbo = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.vbo)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL.GL_STATIC_DRAW)

        #pega a posição do atributo no shaders via forma programática
        ##position = GL.glGetAttribLocation(self.shader, "e_vertice")
        ##color = GL.glGetAttribLocation(self.shader, "e_cor")
        



        #diz qual atributo deve ser usado (posição ou cor) a partir de um index
        GL.glEnableVertexAttribArray(position)
        GL.glVertexAttribPointer(position, 3, GL.GL_FLOAT, GL.GL_FALSE, 24, ctypes.c_void_p(0))
        GL.glEnableVertexAttribArray(color)
        GL.glVertexAttribPointer(color, 3, GL.GL_FLOAT, GL.GL_FALSE, 24, ctypes.c_void_p(12))

        #GL.glVertexAttribPointer(index, pontos (xyz), tipo de dado, transformacao, qnt de bytes para o proximo vertice, mudança de ponto para cor)

app = QApplication()
widget = OpenGLMainWindow()
widget.resize(500,500)
print(widget.minha_soma(4.1,4))
widget.show()
app.exec()



def sunFunc():
    #(x-0.66)^(2)+(y-0.65)^(2)=0.08
    rad = 0.08
    center = 0.66
    x_max = 0.74
    x_min = 0.58
    # .58 < x > .74
    aux = 0.58
    num = []
    while(aux <= 0.74):
        #(x**2 - 2*0.66*x + 0.66**2) + (y**2 - 2*0.65*y + 0.65**2) - 0.08 = 0
        #y**2 - 1.3*y = -x**2 + 2*0.66*x - 0.66**2 - 0.65**2 + 0.08
        #
        pass



