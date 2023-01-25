import random

class Environment(object):
    def __init__(self):
        self.loc = ['1', '2', '3', '4']
        self.move = ['U', 'D', 'L', 'R']
        self.path = {'1R': '2', '1D': '3', '1L': 'W', '1U': 'W',
                    '2R': 'W', '2D': '4', '2L': '1', '2U': 'W',
                    '3R': '4', '3D': 'W', '3L': 'W', '3U': '1',
                    '4R': 'W', '4D': 'W', '4L': '3', '4U': '2',
                    }
        self.journey = []

class pathFindingAgent(Environment):
    def takeJourney(self, Environment):
        agent1 =  self.makeAgent(random.choice(Environment.loc))
        print('Agent Location:', agent1)
        self.journey.append(agent1[0])

        while agent1[0] != '4':
            toMove = self.choosePath(agent1, Environment)
            agent1[0] = Environment.path[toMove]
            print('Agent moved to Location:', agent1[0])
            self.journey.append(agent1[0])

        self.journey.append('4')
        print('Path you found is:', self.journey)

    def makeAgent(self, location):
        return [location]

    def choosePath(self, agent1, Environment):
        i = random.choice(self.move)
        j = str(agent1[0]) + i
        print('Direction to move:', j)
        print('Destination:', Environment.path[j])
        
        while Environment.path[j] == 'W':
            i = random.choice(self.move)
            j = str(agent1[0]) + i
            print('Direction to move:', j)
            print('Destination:', Environment.path[j])

        print('Selected Path:', Environment.path[j])
        return j

#Objects
theEnvironment = Environment()
myAgent = pathFindingAgent()
myAgent.takeJourney(theEnvironment)
