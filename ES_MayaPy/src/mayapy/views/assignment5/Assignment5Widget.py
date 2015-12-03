# Assignment5Widget.py
# (C)2013
# Scott Ernst

from pyglass.widgets.PyGlassWidget import PyGlassWidget

#___________________________________________________________________________________________________ Assignment5Widget
class Assignment5Widget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment5Widget."""
        super(Assignment5Widget, self).__init__(parent, **kwargs)

        self.homeBtn.clicked.connect(self._handleReturnHome)

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')

#___________________________________________________________________________________________________ _handleEyes
    def _handleEyes(self):

#___________________________________________________________________________________________________ _handleNose
    def _handleNose(self):

#___________________________________________________________________________________________________ _handleMouth
    def _handleMouth(self):

#___________________________________________________________________________________________________ _handleEars
    def _handleEars(self):

#___________________________________________________________________________________________________ _handleForehead
    def _handleForehead(self):
