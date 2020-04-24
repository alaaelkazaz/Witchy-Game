from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
import random

def init():
	glClearColor(0,0,0,0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0,1,0,1,0,1)
	glMatrixMode(GL_MODELVIEW)


def display_score():
   glLineWidth(5)
    glColor(0,0,1,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,1000,0,1000)
    glMatrixMode(GL_MODELVIEW)
    string = "Hello Alaa"
    string = string.encode()
    for x in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, x)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
glutInitWindowSize(500,500)
glutCreateWindow(b'Only The Score Feature')
glutDisplayFunc(display_score)
glutIdleFunc(display_score)
init()
glutMainLoop()


