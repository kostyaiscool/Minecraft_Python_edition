import panda3d
from direct.showbase.ShowBase import ShowBase
from map_manager import *
from player import *
from panda3d.core import TextNode
from direct.gui.OnscreenText import OnscreenText

panda3d.core.load_prc_file_data('', 'load-display pandadx9')
class Showbase_but_better(ShowBase):
    def __init__(self):
        super().__init__(self)
        self.map = Map_manager()
        self.player = Player((20,  20, 10), self.map)
        self.fps_shower = OnscreenText(text = 'dfshi', parent = base.a2dBottomRight, align = TextNode.ARight, fg = (10, 10, 10, 10), scale = 0.1, pos = (-1, 0.1))
game = Showbase_but_better()
game.run()
# timer = 0
# tick30 = 0wwwwwwwww
# delta = 1
# fps = 0
# def fps(last_tick30):
#     tick30 = timer * 30
#     delta = tick30 - last_tick30
#     fps = int(30/delta)
# while True:
#     timer = timer + 0.0001
#     fps(tick30)
#     print(fps)