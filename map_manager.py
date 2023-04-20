
class Map_manager:
    def __init__(self):
        # for y in range(10, 40):
        #     for x in range(40):
        #         self.block_create((x, y, 0), 'block.egg', 'Wood.jpg')
        self.create_branch()
        self.render_map('default_map.txt')
    def block_create(self, position, model, texture):
        self.block_model = 'source/' + model
        self.block_texture = 'source/' + texture
        self.model = loader.loadModel(self.block_model)
        self.texture = loader.loadTexture(self.block_texture)
        self.model.setTexture(self.texture)
        self.model.reparentTo(self.branch)
        self.model.setPos(position)
        self.model.setTag('at', str(position))
    def render_map(self, file_name):
        for y in range(10, 40):
            for x in range(40):
                self.block_create((x, y, 0), 'block.egg', 'Wood.jpg')
        # with open(file_name, 'r') as file:
        #     for line in file:
        #         line = line.split(' ')
        #         y = 0
        #         del line[-1]
        #         for block in line:
        #             x = 0
        #             for item in range(int(block)):
        #                 for z in range(item):
        #                     self.block_create((x, y, z), 'block.egg', 'Wood.jpg')
        #                 x += 1
        #             y += 1
    def is_block_at(self, position):
        if self.branch.findAllMatches('=at=' + str(position)):
            return True
        else:
            return False
    def create_branch(self):
        self.branch = render.attachNewNode('map_branch')