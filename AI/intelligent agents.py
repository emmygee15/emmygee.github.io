import random
class Environment(object):
    def __init__(self):
        self.locationcondition = {'A' : '0', 'B' : '0'}
        self.locationcondition['A'] = random.randint(0,1)
        self.locationcondition['B'] = random.randint(0,1)


class MyAgent(Environment):
    def __init__(self, Environment):
        print(Environment.locationcondition)
        vacuumlocation = random.randint(0,1)
      if vacuumlocation == 0:
        print("vacuum randomly placed at location A")
        if Environment.locationcondition['A'] == 1:
            print("location A is dirty")
            Environment.locationcondition['A'] = 0:
            print("location A cleaned. Moving to B")
            if Environment.locationcondition['B'] ==1
            print("location B is dirty")
            Environment.locationcondition['B'] = 0:
            print("location B cleaned")
        else:
            print("location A is clean. Moving to B")
             if Environment.locationcondition['B'] ==1
            print("location B is dirty")
            Environment.locationcondition['B'] = 0:
             print("location B cleaned")

        elif:
             if vacuumlocation == 1:
        print("vacuum randomly placed at location B")
        if Environment.locationcondition['B'] == 1:
            print("location B is dirty")
            Environment.locationcondition['B'] = 0:
            print("location B cleaned. Moving to A")
            if Environment.locationcondition['A'] ==1
            print("location A is dirty")
            Environment.locationcondition['A'] = 0:
            print("location A cleaned")
        else:
            print("location B is clean. Moving to A")
             if Environment.locationcondition['A'] ==1
            print("location A is dirty")
            Environment.locationcondition['A'] = 0:
             print("location A cleaned")

          print(Environment.locationcondition)

theEnvironment = Environment()
theAgent = MyAgent(theEnvironment)




