import copy
import random

class Hat:
    def __init__(self, **arg):
        self.contents = []
        for item,num in arg.items():
            for x in range(num):
                self.contents.append(item)
        self.cont = copy.copy(self.contents)
    
    
    def draw(self, arg):
        collected = []
        if (len(self.contents) == 0) or (len(self.cont) > arg and len(self.contents) < arg):
            self.contents = copy.copy(self.cont)
        if len(self.contents) < arg and len(self.cont) == len(self.contents):
            return self.contents

        for i in range(arg):
            rand_item = random.choice(self.contents)
            self.contents.pop(self.contents.index(rand_item))
            collected.append(rand_item)
        
        return collected


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for _ in range(num_experiments):
        collected = hat.draw(num_balls_drawn)
        boolean = True
        
        for item in expected_balls:
            if item not in collected:
                boolean = False
                break
            
            count = 0
            coll = copy.copy(collected)
            for _ in range(len(coll)):
                coll.pop(coll.index(item))
                count += 1
                if item not in coll:
                    break
            
            if not count >= expected_balls[item]:
                boolean = False
                break        
        
        if boolean:
            M += 1
    
    return(M / num_experiments)
    