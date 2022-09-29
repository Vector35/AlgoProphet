import os, sys
from binaryninja import *
from binaryninjaui import Sidebar, SidebarWidget, SidebarWidgetType

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QScrollArea, QWidget
from PySide6.QtGui import QImage

from binaryninjaui import UIActionHandler, UIAction, UIActionContext, UIContext

PLUGINDIR_PATH = os.path.abspath(os.path.dirname(__file__))

class AlgoProphetSidebarWidget(SidebarWidget):
    def __init__(self, name: str, frame, data):
        SidebarWidget.__init__(self, name)
        self.datatype = QLabel("")
        self.data = data
        self.actionHandler = UIActionHandler()
        self.actionHandler.setupActionHandler(self)
        self.prev_func_offset = None
        self.binary_view = None
        
        AlgoProphet_layout = QVBoxLayout()

class AlgoProphetSidebarWidgetType(SidebarWidgetType):
    def __init__(self):
        icon = QImage(os.path.join(PLUGINDIR_PATH, "icon.png"))
        SidebarWidgetType.__init__(self, icon, "AlgoProphet")
        
    def createWidget(self, frame, data):
        # This callback is called when a widget needs to be created for a given context. Different
        # widgets are created for each unique BinaryView. They are created on demand when the sidebar
        # widget is visible and the BinaryView becomes active.
        return AlgoProphetSidebarWidget("AlgoProphet", frame, data)

#Sidebar.addSidebarWidgetType(AlgoProphetSidebarWidgetType())