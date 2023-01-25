from kanren import *

tools = Relation() #tool object belong to relation
careers = Relation()

facts(tools, ("Java","Language"),
      ("Python","Language"),
      ("Word","Package"),
      ("Excel","Package"),
      ("Windows","OS"),
      ("Linux","OS"))

facts(careers, ("Programming","Language"),
      ("Users","Package"),
      ("Networking","OS"))

career_tool, tools_v, careers_v = var(),var(),var()
run(0,career_tool,tools(career_tool,tools_v),careers("Networking",tools_v))

def career_tool(x,y):
    z = var()
    return conde((tools(x,z),careers(y,z)))

what = var()
print(run(0,what,career_tool(what,"Networking")))

