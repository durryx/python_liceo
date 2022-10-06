from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

start = time.perf_counter()
## change x value to get smaller plots 2->1 ##
global g
g = 0.1
iterations = 19
global stringa
stringa = "AB"


def failapiega(stringa):
    i = len(stringa) - 1
    # si legge la stringa al contrario e si duplica ruotando di pi/2
    while i >= 0:
        p = stringa[i]
        if p == "A":
            stringa += "B"
        elif p == "B":
            stringa += "C"
        elif p == "C":
            stringa += "D"
        elif p == "D":
            stringa += "A"
        i -= 1
    return stringa


while 0 <= iterations:
    stringa = failapiega(stringa)
    iterations -= 1
global w, h
w, h = 1200, 900


def plot():
    x, y = 600, 450
    Px = len(stringa) - 1
    Px1 = 0
    while Px >= Px1:
        glBegin(GL_LINES)
        if stringa[Px] == "A":
            glVertex2f(x, y)
            glVertex2f(x, y - g)
            y -= g
        elif stringa[Px] == "B":
            glVertex2f(x, y)
            glVertex2f(x + g, y)
            x += g
        elif stringa[Px] == "C":
            glVertex2f(x, y)
            glVertex2f(x, y + g)
            y += g
        elif stringa[Px] == "D":
            glVertex2f(x, y)
            glVertex2f(x - g, y)
            x -= g
        glEnd()
        Px -= 1


def iterate():
    glViewport(0, 0, 1200, 900)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1200, 0.0, 900, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 0.0, 3.0)
    plot()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(w, h)
window = glutCreateWindow("dragon curve in Opengl")
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
end = time.perf_counter()
print(f'Terminated in {round(end - start, 2)} seconds')

glutMainLoop()
