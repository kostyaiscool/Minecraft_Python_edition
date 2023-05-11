import panda3d
from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import DirectButton, DirectFrame
from map_manager import *
from player import *
from panda3d.core import TextNode
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import loadPrcFileData
import sys


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080 - 60

# show fps
loadPrcFileData('', f'win-size {SCREEN_WIDTH} {SCREEN_HEIGHT} show-frame-rate-meter ')

panda3d.core.load_prc_file_data('', 'load-display pandadx9')
class Showbase_but_better(ShowBase):
    def __init__(self):
        super().__init__(self)
        # self.map = Map_manager()
        # self.player = Player((2,  3, 10), self.map)
        # self.fps_shower = OnscreenText(text = 'ds', parent = base.a2dBottomRight, align = TextNode.ARight, fg = (10, 10, 10, 10), scale = 0.1, pos = (-1, 0.1))
        self.menu_panel = DirectFrame(frameColor = (0, 0, 0, 0.5), frameSize = (-0.5, 0.5, -0.5, 0.5))
        self.menu_button1 = DirectButton(text = 'Exit', scale = 0.1, command = sys.exit, parent = self.menu_panel)
        self.menu_button1.setPos(0, 0, -0.4)
        self.menu_button2 = DirectButton(text = 'Start game', scale = 0.1, command = self.start_game, parent = self.menu_panel)
        self.menu_button2.setPos(0, 0, -0.2)
        self.menu_button3 = DirectButton(text = 'Settings', scale = 0.1, command = self.settings, parent = self.menu_panel)
        self.menu_button3.setPos(0, 0, 0)
    def start_game(self):
        self.menu_panel.hide()
        self.map = Map_manager()
        self.player = Player((2,  3, 10), self.map)
    def show_fps(self):
        loadPrcFileData('', 'true')
    def settings(self):
        self.menu_panel.hide()
        self.settings_panel = DirectFrame(frameColor = (0, 0, 0, 0.5), frameSize = (-0.5, 0.5, -0.5, 0.5))
        self.settings_button1 = DirectButton(text = 'Show FPS', scale = 0.1, command = self.show_fps, parent = self.settings_panel)
        self.settings_button1.setPos(0, 0, -0.2)
        self.settings_button2 = DirectButton(text = 'Main menu', scale = 0.1, command = self.exit_settings, parent = self.settings_panel)
        self.settings_button2.setPos(0, 0, -0.4)
    def exit_settings(self):
        self.settings_panel.hide()
        self.menu_panel.show()
        # self.fps_shower = OnscreenText(text = 'ds', parent = base.a2dBottomRight, align = TextNode.ARight, fg = (10, 10, 10, 10), scale = 0.1, pos = (-1, 0.1))
game = Showbase_but_better()
game.run()

