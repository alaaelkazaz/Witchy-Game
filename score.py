from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random



score1 = 17
def init():
	glClearColor(1,1,1,1)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0,1,0,1,0,1)
	glMatrixMode(GL_MODELVIEW)


class score_Dispaly():
    global score1 
    def score_Panel():

     glClearColor(1,1,1,1)
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

     glLineWidth(3)
     glColor(1,0,0,1)

     glMatrixMode(GL_PROJECTION)
     glLoadIdentity()

     gluOrtho2D(0,1500,0,1500)
     glMatrixMode(GL_MODELVIEW)
     glLoadIdentity()
     scoreLabel="Your Score : "
     scoreString=str(score1)
     scorPara=scoreLabel + scoreString
     scorPara= scorPara.encode()
     for x in scorPara:
         glutStrokeCharacter(GLUT_STROKE_ROMAN, x)
    
     glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
glutInitWindowSize(500,500)
glutCreateWindow(b'Only The Score Feature')
glutDisplayFunc(score_Dispaly.score_Panel)
glutIdleFunc(score_Dispaly.score_Panel)
init()
glutMainLoop()

