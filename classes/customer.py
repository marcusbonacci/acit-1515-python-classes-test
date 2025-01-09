import random
from data.names import firstNames, lastNames
from data.foods import * # Wildcard

class customerClass:
    def __init__(self):
        self.firstName = random.choice(firstNames) # random name
        self.lastName = random.choice(lastNames)
        self.ordered = False

        # print("[+]", self.firstName, self.lastName, "entered the restaurant")

    def __str__(self):

        # figure out: if not dict: return False # Currently throws missing attribute, I want a None / Missing attribute to throw False like LUA
        # self.order: dict
        # if not self.order: 
        #     print("ugh oh")
        

        # stright Boolean work around
        if not self.ordered:
            return f"> {self.firstName}, {self.lastName} hasn't ordered food yet"
        else:
            return f">> {self.firstName}, {self.lastName} - Ordered: {[dish for dish in self.order.values()]}"

    # Custom cleanup logic ...
    def __del__(self):
        # print("[-]", self.firstName, self.lastName, "has ate and left the restaurant \n")
        del(self)

    def orderFood(self):
        self.order = {}

        self.order["sideCourse"] = random.choice(sideCourses) 
        self.order["firstCourse"] = random.choice(firstCourses)
        self.order["secondCourse"] = random.choice(secondCourses) 
        self.ordered = True

        return self.order