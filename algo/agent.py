from algo.Constrant import *
class Agent:
    ''' Robot '''
    def __init__(self, exploredMap, direction = NORTH, start=START):

        self.exploredMap = exploredMap
        self.direction = direction
        self.center = np.asarray(start)
        self.marked = np.zeros((20, 15))
        self.setHead()
        self.movement = []
        self.markArea(start, 1)
        self.stepCounter = 0