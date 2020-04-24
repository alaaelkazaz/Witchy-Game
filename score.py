from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
import random
pygame.init()

x = 1
y = 0
def init():
	glClearColor(0,0,0,0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0,1,0,1,0,1)
	glMatrixMode(GL_MODELVIEW)


def display_score():
    global x
    global y 
    glTranslate(x, y, 0)
    white=(1,1,1)
    #we would put the score variable here instead of the random number generation
    Score= random.randrange(0, 5) 
    #Text through GUI SysFont(name, size, bold=False, italic=False) 
    myFont = pygame.font.SysFont("Times New Roman",18 ,True)
    #score Label render(text, antialias, color, background=None) 
    scoreLab=myfont.render("Your Score is : ",white)
    # pass a string to myFont.render
    scoreDisplay = myFont.render(str(Score), 1, white)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
glutInitWindowSize(500,500)
glutCreateWindow(b'Only The Score Feature')
glutDisplayFunc(display_score)
glutIdleFunc(display_score)
init()
glutMainLoop()


