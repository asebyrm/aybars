
from PyQt5.QtWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *

class Rocket3D(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.pitch = 0
        self.roll = 0
        self.yaw = 0

    def initializeGL(self):
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glEnable(GL_DEPTH_TEST)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w / h if h != 0 else 1, 1, 100)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)

        glRotatef(self.roll, 0, 0, 1)
        glRotatef(self.pitch, 1, 0, 0)
        glRotatef(self.yaw, 0, 1, 0)

        glColor3f(0.5, 0.8, 1.0)
        quad = gluNewQuadric()

        glPushMatrix()
        glRotatef(90, 1, 0, 0)
        gluCylinder(quad, 0.2, 0.2, 2.0, 32, 32)
        glTranslatef(0.0, 0.0, 2.0)
        gluCylinder(quad, 0.2, 0.0, 0.5, 32, 32)
        glPopMatrix()

    def update_orientation(self, pitch, roll, yaw):
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw
        self.update()
