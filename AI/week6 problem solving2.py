import os
import random
performance=[]

class Environment(object):
    def __init__(self):
        self.filelist=[]
        for i in os.listdir("C:\\Users\\HP\\Documents\\Cleaned"):  
            self.filelist.append(i)
            print(i)
        
        self.filelist.sort()#order list incase its not ordered
        self.agentfind = random.randint(0, len(self.filelist)-1)
        print("Searching for",self.filelist[self.agentfind])

class Agent(Environment):
    def binsearch(list, target): #Binary Search
        min = 0
        max = len(list)-1
        check=-1
        count=0
        while (min <= max) and (check==-1):
            mid = (min+max)//2
            count=count+1
            print("count",count)
            if list[mid] == target:
                check = mid
            else:
                if target<list[mid]:
                    max = mid -1
                else:
                    min = mid +1
        print("Number of reads and mid",count,mid)
        return count

    def __init__(self, Environment):
        performance.append(Agent.binsearch(Environment.filelist,Environment.filelist[Environment.agentfind]))
   
for x in range(0, 20):
    theEnvironment = Environment()
    theAgent= Agent(theEnvironment)

print("performance",performance)
print("Average search time ",sum(performance)/len(performance))

import matplotlib.pyplot as plt
plt.title('Agent Journey over time')
plt.ylabel('Agent Location')
plt.xlabel('Time')
plt.plot(performance)
plt.show()
