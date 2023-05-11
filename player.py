from math import *
import sys
from direct.gui.DirectGui import DirectButton, DirectFrame
from direct.actor.Actor import Actor
class Player():
    def __init__(self, position, map_link):
        self.map_link = map_link
        # self.player = loader.loadModel('source/')
        self.player = Actor('source/ralph', {'run':'source/ralph-run', 'walk':'source/ralph-walk'})
        self.player.setPos(position)
        self.player.setScale(0.3)
        # self.player.setColor((1, 0.5, 0, 1))
        self.player.reparentTo(render)
        self.from_first_face_camera()
        self.events()
        self.lastMouseX, self.lastMouseY = 0, 0
        self.rotateX, self.rotateY = 0, 0
        self.mouseMagnitude = 10
        self.manualRecenterMouse = True
        # self.speed_y = 0.2
        taskMgr.add(self.gravity, 'gravity')
        taskMgr.add(self.depth_limits, 'depth_limit')
        # taskMgr.add(self.mouseTask, 'mouse_dir_get')
        self.pause_menu()
    def from_first_face_camera(self):
        base.disableMouse()
        base.camera.reparentTo(self.player)
        base.camera.setH(180)
        base.camera.setPos(0, -1, 0.7)
    def gravity(self, task):
        x_from = int(self.player.getX())
        y_from = int(self.player.getY())        
        z_from = int(self.player.getZ())       
        if self.map_link.is_block_at((x_from, y_from, z_from - 1)):          
            # self.speed_y = 0.2            
            pass       
        else:          
            self.player.setPos((x_from, y_from, z_from - 1))          
            # self.speed_y += 1   
        return task.again
    # def jump(self):
        # self.speed_y = -10
        # self.player.setPos(self.pos[0], self.pos[1], self.pos[2] - self.speed_y)
    def events(self):
        base.accept('w'+"-repeat", self.move_front)
        base.accept('w', self.move_front)
        base.accept('s'+"-repeat", self.move_back)
        base.accept('s', self.move_back)
        base.accept('a'+"-repeat", self.move_left)
        base.accept('a', self.move_left)
        base.accept('d'+"-repeat", self.move_right)
        base.accept('d', self.move_right)
        base.accept('mouse1', self.delete_block)
        base.accept('escape', self.pause)
    def look_left(self):
        angle = self.player.getH()
        print(angle)
        self.player.setH((angle + 5)%360)
    def look_right(self):
        angle = self.player.getH()
        print(angle)
        self.player.setH((angle - 5)%360)
    def look_up(self):
        angle = self.player.getP()
        print(angle)
        self.player.setP((angle - 3)%360)
    def look_down(self):
        angle = self.player.getP()
        print(angle)
        self.player.setP((angle + 3)%360)
    def move(self, angle):
        # angle = self.player.getH()
        # self.player.setX(self.player.getX() - 1 * sin(angle))
        # self.player.setY(self.player.getY() - 1 * cos(angle))
        x_from = int(self.player.getX())
        y_from = int(self.player.getY())        
        z_from = int(self.player.getZ())      
        dx, dy = self.check_direction(angle%360)
        if not self.map_link.is_block_at((x_from + dx, y_from + dy, z_from)):          
            self.player.setPos((x_from + dx, y_from + dy, z_from))
        # self.player.setY(self.player.getY() + dy)
    def check_direction(self, angle):
        # if angle >= 0 and angle <= 25 or angle > 340 and angle <= 360:
        #     return 0, 1
        # elif angle > 25 and angle <= 70:
        #     return 1, 1
        # elif angle > 70 and angle <= 115:
        #     return 1, 0
        # elif angle > 115 and angle <= 160:
        #     return 1, -1
        # elif angle > 160 and angle <= 205:
        #     return 0, -1
        # elif angle > 205 and angle <= 250:
        #     return -1, -1
        # elif angle > 250 and angle <= 295:
        #     return -1, 0
        # elif angle > 295 and angle <= 340:
        #     return -1, 1
        if 0 <= angle < 20 or 335 <= angle < 360:
            return 0, -1
        elif 20 <= angle < 65:
            return 1, -1
        elif 65 <= angle < 110:
            return 1, 0
        elif 110 <= angle < 155:
            return 1, 1
        elif 155 <= angle < 200:
            return 0, 1
        elif 200 <= angle < 245:
            return -1, 1
        elif 245 <= angle < 290:
            return -1, 0
        elif 290 <= angle < 335:
            return -1, -1
    def depth_limits(self, task):
        if self.player.getZ() < -100:
            sys.exit()
        return task.again
    def move_back(self):
        self.move((self.player.getH() + 180)%360)
    def move_front(self):
        self.move(self.player.getH())
    def move_left(self):
        self.move((self.player.getH() + 90)%360)
    def move_right(self):
        self.move((self.player.getH() + 270)%360)
    def delete_block(self):
        x_from = int(self.player.getX())
        y_from = int(self.player.getY())        
        z_from = int(self.player.getZ())
        angle = self.player.getH()      
        dx, dy = self.check_direction(angle%360)
        if self.map_link.is_block_at((x_from + dx, y_from + dy, z_from)):          
            self.map_link.break_block((x_from + dx, y_from + dy, z_from))
    # def get_mouse(self, task):
    #     if base.mouseWatcherNode.hasMouse():
    #         x = base.mouseWatcherNode.getMouseX()
    #         y = base.mouseWatcherNode.getMouseY()
    #         if x != self.last_x:
    #             if x * 90 < 0:
    #                 self.look_left()
    #             elif x * 90 > 0:
    #                 self.look_right()
    #         if y != self.last_y:
    #             if y * 90 < 0:
    #                 self.look_up()
    #             elif y * 90 > 0:
    #                 self.look_down()
    #         self.last_x = x
    #         self.last_y = y
        # return task.again
    def mouseTask(self, task):
        mw = base.mouseWatcherNode

        hasMouse = mw.hasMouse()
        if hasMouse:
            # get the window manager's idea of the mouse position
            x, y = mw.getMouseX(), mw.getMouseY()

            if self.lastMouseX is not None:
                # get the delta
                if self.manualRecenterMouse:
                    # when recentering, the position IS the delta
                    # since the center is reported as 0, 0
                    dx, dy = x, y
                else:
                    dx, dy = x - self.lastMouseX, y - self.lastMouseY
            else:
                # no data to compare with yet
                dx, dy = 0, 0

            self.lastMouseX, self.lastMouseY = x, y

        else:
            x, y, dx, dy = 0, 0, 0, 0

        if self.manualRecenterMouse:
            # move mouse back to center
            self.recenterMouse()
            self.lastMouseX, self.lastMouseY = 0, 0

        self.rotateX += dx * 10 * self.mouseMagnitude
        self.rotateY += dy * 10 * self.mouseMagnitude

        self.player.setH(-self.rotateX)
        self.player.setP(-self.rotateY)

        return task.again
 
    def recenterMouse(self):
        base.win.movePointer(
            0,
            int(base.win.getProperties().getXSize() / 2),
            int(base.win.getProperties().getYSize() / 2)
        )
    def pause_menu(self):
        self.menu_panel = DirectFrame(frameColor = (0, 0, 0, 0.5), frameSize = (-0.5, 0.5, -0.5, 0.5))
        self.menu_button1 = DirectButton(text = 'Exit', scale = 0.1, command = sys.exit, parent = self.menu_panel)
        self.menu_button1.setPos(0, 0, -0.4)
        self.menu_button2 = DirectButton(text = 'Continue', scale = 0.1, command = self.continue_game, parent = self.menu_panel)
        self.menu_button2.setPos(0, 0, -0.2)
        self.menu_button3 = DirectButton(text = 'Start new game', scale = 0.1, command = self.new_game, parent = self.menu_panel)
        self.menu_button3.setPos(0, 0, 0)
        self.menu_panel.hide()
    def pause(self):
        self.manualRecenterMouse = False
        self.menu_panel.show()
        taskMgr.remove('gravity')
        taskMgr.remove('depth_limit')
        taskMgr.remove('mouse_dir_get')
    def continue_game(self):
        taskMgr.add(self.gravity, 'gravity')
        taskMgr.add(self.depth_limits, 'depth_limit')
        taskMgr.add(self.mouseTask, 'mouse_dir_get')
        self.manualRecenterMouse = True
        self.paused = False
        self.menu_panel.hide()
    def new_game(self):
        self.map_link.render_map('default_map.txt')