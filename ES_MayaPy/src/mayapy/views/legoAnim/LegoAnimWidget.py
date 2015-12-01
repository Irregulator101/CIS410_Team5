# LegoManAnimations.py
# 11/2/2015
# Eric Schultz

import nimble
from nimble import cmds as cmds

from pyglass.widgets.PyGlassWidget import PyGlassWidget


#___________________________________________________________________________________________________ Assignment1Widget
class LegoAnimWidget(PyGlassWidget):

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):

        # Creates a new instance of LegoAnimWidget.
        super(LegoAnimWidget, self).__init__(parent, **kwargs)
        self.raiseRightArm.clicked.connect(self._handleRaiseRight)
        self.run.clicked.connect(self._handleRun)
        self.kick.clicked.connect(self._handleKick)
        self.homeBtn.clicked.connect(self._handleReturnHome)

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleRaiseRight
    def _handleRaiseRight(self):

        # This callback raises the lego man's right hand.

        time = cmds.currentTime(q=1)

        cmds.setKeyframe('arm_R', v=0.0, at='rotateX')
        cmds.setKeyframe('arm_R', v=-120.0, at='rotateX', t=time+15)
        cmds.setKeyframe('arm_R', v=0.0, at='rotateX', t=time+30)

#___________________________________________________________________________________________________ _handleRaiseRight
    def _handleRun(self):

        # This callback causes the lego man to run a short distance, along the Z axis.

        time = cmds.currentTime(q=1)
        loc = cmds.getAttr('Lego_Man.tz')

        cmds.setKeyframe('leg_R', v=0.0, at='rotateX')
        cmds.setKeyframe('leg_L', v=0.0, at='rotateX')
        cmds.setKeyframe('arm_R', v=0.0, at='rotateX')
        cmds.setKeyframe('arm_L', v=0.0, at='rotateX')
        cmds.setKeyframe('Lego_Man', v=loc, at='translateZ')

        cmds.setKeyframe('leg_R', v=-90.0, at='rotateX', t=time+20)
        cmds.setKeyframe('leg_L', v=90.0, at='rotateX', t=time+20)
        cmds.setKeyframe('arm_R', v=90.0, at='rotateX', t=time+20)
        cmds.setKeyframe('arm_L', v=-90.0, at='rotateX', t=time+20)
        cmds.setKeyframe('Lego_Man', v=loc+6.0, at='translateZ', t=time+20)

        cmds.setKeyframe('leg_R', v=90.0, at='rotateX', t=time+40)
        cmds.setKeyframe('leg_L', v=-90.0, at='rotateX', t=time+40)
        cmds.setKeyframe('arm_R', v=-90.0, at='rotateX', t=time+40)
        cmds.setKeyframe('arm_L', v=90.0, at='rotateX', t=time+40)
        cmds.setKeyframe('Lego_Man', v=loc+12.0, at='translateZ', t=time+40)

        cmds.setKeyframe('leg_R', v=-90.0, at='rotateX', t=time+60)
        cmds.setKeyframe('leg_L', v=90.0, at='rotateX', t=time+60)
        cmds.setKeyframe('arm_R', v=90.0, at='rotateX', t=time+60)
        cmds.setKeyframe('arm_L', v=-90.0, at='rotateX', t=time+60)
        cmds.setKeyframe('Lego_Man', v=loc+18.0, at='translateZ', t=time+60)


#___________________________________________________________________________________________________ _handleRaiseRight
    def _handleKick(self):

        # This callback causes the lego man to kick with his right leg.

        # actions at frame 0
        time = cmds.currentTime(q=1)
        cmds.setKeyframe('body', v=0.0, at='rotateX')
        cmds.setKeyframe('leg_R', v=0.0, at='rotateX')
        cmds.setKeyframe('leg_L', v=0.0, at='rotateX')
        cmds.setKeyframe('arm_R', v=0.0, at='rotateX')
        cmds.setKeyframe('arm_L', v=0.0, at='rotateX')

        # actions at frame 40
        cmds.setKeyframe('body', v=15, at='rotateX', t=time+40)
        cmds.setKeyframe('leg_R', v=70, at='rotateX', t=time+40)
        cmds.setKeyframe('leg_L', v=-15, at='rotateX', t=time+40)
        cmds.setKeyframe('arm_R', v=40, at='rotateX', t=time+40)
        cmds.setKeyframe('arm_L', v=-40, at='rotateX', t=time+40)

        # actions at frame 60
        cmds.setKeyframe('leg_R', v=-90, at='rotateX', t=time+60)
        cmds.setKeyframe('body', v=-15, at='rotateX', t=time+60)
        cmds.setKeyframe('arm_R', v=-40, at='rotateX', t=time+60)
        cmds.setKeyframe('arm_L', v=40, at='rotateX', t=time+60)

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
