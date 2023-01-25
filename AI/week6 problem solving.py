import os
import random
performance=[]

class Environment(object):
    
    def __init__(self):
        self.filelist=[]
        for i in os.listdir("C:\\Users\\User\\OneDrive"):  
            self.filelist.append(i)
            print(i)

        self.agentfind = random.randint(0, len(self.filelist)-1)
        print("Searching for",self.filelist[self.agentfind])

class Agent(Environment):
    def __init__(self, Environment):
        count=0
        for i in Environment.filelist:  #Linear Search
            if i==Environment.filelist[Environment.agentfind]:
                print("File found in location:",count )
                performance.append(count)
            else:
                count=count+1
        
        
   
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
