# Assignment2Widget.py
# (C)2013
# Scott Ernst

from pyglass.widgets.PyGlassWidget import PyGlassWidget
import nimble
from nimble import cmds

#___________________________________________________________________________________________________ Assignment2Widget
class Assignment2Widget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment2Widget."""
        super(Assignment2Widget, self).__init__(parent, **kwargs)

        self.homeBtn.clicked.connect(self._handleReturnHome)
        self.eyes.sliderMoved.connect(self._handleEyes)
        self.nose.sliderMoved.connect(self._handleNose)
        self.mouth.sliderMoved.connect(self._handleMouth)
        self.ears.sliderMoved.connect(self._handleEars)
        self.forehead.sliderMoved.connect(self._handleForehead)

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')

#___________________________________________________________________________________________________ _handleEyes
    def _handleEyes(self):
        val = self.eyes.value()
        val = float(val)/100
        if val > 0:
            cmds.blendShape( "blendShape1", edit=True, w=[(7, val)] )
        if val < 0:
            cmds.blendShape( "blendShape1", edit=True, w=[(6, -1 * val)] )
        if val == 0:
            cmds.blendShape( "blendShape1", edit=True, w=[(6, 0)] )
            cmds.blendShape( "blendShape1", edit=True, w=[(7, 0)] )


#___________________________________________________________________________________________________ _handleNose
    def _handleNose(self):
        val = self.nose.value()
        val = float(val)/100
        if val > 0:
            cmds.blendShape( "blendShape1", edit=True, w=[(3, val)] )
        if val < 0:
            cmds.blendShape( "blendShape1", edit=True, w=[(2, -1 * val)] )
        if val == 0:
            cmds.blendShape( "blendShape1", edit=True, w=[(2, 0)] )
            cmds.blendShape( "blendShape1", edit=True, w=[(3, 0)] )

#___________________________________________________________________________________________________ _handleMouth
    def _handleMouth(self):
        val = self.mouth.value()
        val = float(val)/100
        if val > 0:
            cmds.blendShape( "blendShape1", edit=True, w=[(5, val)] )
        if val < 0:
            cmds.blendShape( "blendShape1", edit=True, w=[(4, -1 * val)] )
        if val == 0:
            cmds.blendShape( "blendShape1", edit=True, w=[(5, 0)] )
            cmds.blendShape( "blendShape1", edit=True, w=[(4, 0)] )

#___________________________________________________________________________________________________ _handleEars
    def _handleEars(self):
        val = self.ears.value()
        val = float(val)/100
        if val > 0:
            cmds.blendShape( "blendShape1", edit=True, w=[(0, val)] )
        if val < 0:
            cmds.blendShape( "blendShape1", edit=True, w=[(1, -1 * val)] )
        if val == 0:
            cmds.blendShape( "blendShape1", edit=True, w=[(1, 0)] )
            cmds.blendShape( "blendShape1", edit=True, w=[(0, 0)] )

#___________________________________________________________________________________________________ _handleForehead
    def _handleForehead(self):
        val = self.forehead.value()
        val = float(val)/100
        if val > 0:
            cmds.blendShape( "blendShape1", edit=True, w=[(9, val)] )
        if val < 0:
            cmds.blendShape( "blendShape1", edit=True, w=[(8, -1 * val)] )
        if val == 0:
            cmds.blendShape( "blendShape1", edit=True, w=[(9, 0)] )
            cmds.blendShape( "blendShape1", edit=True, w=[(8, 0)] )
