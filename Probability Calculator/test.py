import random
import copy

contents = ['red', 'red', 'red', 'red', 'red', 'orange', 'orange', 'orange', 'orange', 'black', 'pink', 'pink', 'striped', 'striped', 'striped', 'striped', 'striped', 'striped', 'striped', 'striped', 'striped']
cont = copy.copy(contents)
print(cont)

rand_item = random.choice(cont)
cont.pop(cont.index(rand_item))
print(rand_item)
print(len(contents))
print(contents)
print(len(cont))
print(cont)