import operator
"""The Environment"""
class Environment(object):
    mygraph = { "1" : set(["2", "4"]),
                "2" : set(["1", "3", "5"]),
                "3" : set(["2", "6"]),
                "4" : set(["1", "5", "7"]),
                "5" : set(["4", "4", "6", "8"]),
                "6" : set(["3", "5", "9"]),
                "7" : set(["4", "8"]),
                "8" : set(["7", "5", "9"]),
                "9" : set(["6", "8"])
               } 
    myheuristics= { "1" : "4",
                    "2" : "3",
                    "3" : "2",
                    "4" : "3",
                    "5" : "2",
                    "6" : "1",
                    "7" : "2",
                    "8" : "1",
                    "9" : "0"
                } 
    Start="1"
    Goal="9"

"""Agent Behaviour"""
class Agent(Environment):
 def gbfs(graph,start, goal):
    p=[]
    p.append(start)
    while True:
        neighbour = graph[start]
        print("neighbour",neighbour)
        heuristic={}
        for i in neighbour.difference(p):
            heuristic[i]=Environment.myheuristics[i]
        sorted_heur = sorted(heuristic.items(), key=operator.itemgetter(1))
        x=next(iter(sorted_heur[0]))
        print("x",x)
        p.append(x)
        if x == goal:
            return p 
        else:
            start=x

 def __init__(self, Environment):
    print("GBFS-Paths Available")
    print(Agent.gbfs(Environment.mygraph,Environment.Start, Environment.Goal)) 
    # returns all possible routes
 
"""Create the agent"""
theEnvironment = Environment()
theAgent= Agent(theEnvironment)





