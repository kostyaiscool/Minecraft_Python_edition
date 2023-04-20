class Player():
    def __init__(self, position, map_link):
        self.map_link = map_link
        self.player = loader.loadModel('smiley')
        self.player.setPos(position)
        self.player.setColor((1, 0.5, 0, 1))
        self.player.reparentTo(render)
        self.from_first_face_camera()
        self.events()
        # self.speed_y = 0.2
        taskMgr.add(self.gravity, 'gravity')
    def from_first_face_camera(self):
        base.camera.reparentTo(self.player)
        base.disableMouse()
        base.camera.setH(180)
        base.camera.setZ(1.5)
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
    def jump(self):
        self.speed_y = -10
        self.player.setPos(self.pos[0], self.pos[1], self.pos[2] - self.speed_y)
    def events(self):
        base.accept('q'+"-repeat", self.look_left)
        base.accept('q', self.look_left)
        base.accept('e'+"-repeat", self.look_right)
        base.accept('e', self.look_right)
        base.accept('w'+"-repeat", self.move(5))
        base.accept('w', self.move(5))
    def look_left(self):
        angle = self.player.getH()
        print(angle)
        self.player.setH((angle + 5)%360)
    def look_right(self):
        angle = self.player.getH()
        print(angle)
        self.player.setH((angle - 5)%360)
    def move(self, steps):
        self.player.setX(getX() + steps * sin(angle))
        self.player.setY(getY() + steps * cos(angle))