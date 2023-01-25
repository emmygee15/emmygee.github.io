
"""The Environment"""
class Environment(object):
    mygraph = { "1" : set(["2","4"]),
                "2" : set(["1","3","5"]),
                "3" : set(["2", "6" ]),
                "4" : set(["1","5","7"]),
                "5" : set(["2","4","6","8"]),
                "6" : set(["3","5","9"]),
                "7" : set(["4","8"]),
                "8" : set(["7","5","9"]),
                "9" : set(["8","6"]),
               } 

    #keys in a string should be stings and unique
    #cost is not unique hence becomes the value
    cost ={     str(["1","2"]): "3",   str(["1", "4"]):"5",
                str(["2","1" ]): "3",  str(["2","3"]):"5",   str(["2","5"]):"7",
                str(["3","2"]): "5",   str(["3","6"]):"9",
                str(["4","1" ]): "5",  str(["4","5"]): "9",  str(["4","7"]):"11",
                str(["5","2" ]): "7",  str(["5","4"]):"9",   str(["5","6"]):"11" , str(["5","8"]) :"13",
                str(["6","3" ]): "9",  str(["6","5"]): "11", str(["6","9"]): "15",
                str(["7","4"]): "11",  str(["7","8"]): "15", str(["8","7" ]):"15",
                str(["8","5"]): "13",  str(["8","9"]):"17" ,
                str(["9","8"]): "17",  str(["9","6"]):"15"
               } 
    State="2"
    Goal="9"
"""Agent Behaviour"""
#Depth First Search
class Agent(Environment):
 def dfs(graph, start, goal):
    stack = [(start, [start])]
    p=[]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                p.append(path + [next])
            else:
               stack.append((next, path + [next]))
    return p 

#Breadth First Search
 def bfs(graph, start, goal):
    queue = [(start, [start])]
    p=[]
    while queue:
        (vertex, path) = queue.pop(0)
        #poping 0 make it a queue
        for next in graph[vertex] - set(path):
            if next == goal:
                p.append(path + [next])
                return p 
                #first path returned by bfs is the shortest path
                #we dont need to check the rest
            else:
                queue.append((next, path + [next]))
    return p 

 def getcost(pathToCost):

    i=0
    pathcost=0
    while i<len(pathToCost)-1:
        #extract 2 neighbors in path
        l=[]
        l.append(pathToCost[i])
        l.append(pathToCost[i+1])
        #read and add cost of neighbors to pathcost
        pathcost=pathcost+int(Environment.cost[str(l)])
        i+=1
    #return final path cost
    return pathcost

 def ucs(graph, start, goal):
    stack = [(start, [start])]
    p=[]
    leastcost=1000 #max cost limit

    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                #paths identified by dfs techniques: path+ [next]
                pathcost=Agent.getcost(path+ [next])
                print("UCS path ",path+ [next]," pathcost ",pathcost)
                 #update least cost & least cost path
                if pathcost<leastcost:
                    leastcost=pathcost
                    p=path + [next]
            else:
               stack.append((next, path + [next]))
    return p 


 def __init__(self, Environment):
    print("DFS-Paths Available")
    print(Agent.dfs(Environment.mygraph,Environment.State, Environment.Goal)) 
    # returns all possible routes
    print("BFS-Shortest Path")
    print(Agent.bfs(Environment.mygraph,Environment.State, Environment.Goal)) 
    # returns shortest routes
    print("UCS-Cheapest Paths")
    print(Agent.ucs(Environment.mygraph,Environment.State, Environment.Goal)) 
    # returns cheapest routes

"""Create the agent"""
theEnvironment = Environment()
theAgent= Agent(theEnvironment)




