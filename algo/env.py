from algo.Constrant import *
from algo.agent import Agent
class env:
    
    def __init__(self, exploredMap = np.zeros((20,15)), start = START, goal = GOAL, realMap = None):

        self.exploredMap = exploredMap



    def initAgent(self):
        self.agent = Agent()





    def loadMap(self):
        with open(os.path.join('map', self.realMap)) as f:
            return np.genfromtxt(f, dtype=int, delimiter=1)
