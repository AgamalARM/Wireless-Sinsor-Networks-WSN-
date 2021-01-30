import random
import math
import numpy as np
import matplotlib.pyplot as plt
import parameter as pr
import functions as fn

#Init parameter Enter to system by user :-
#Number of Nodes in the system (n)
#The area of WSN x and y Coordinates
#Generate random deployment of nodes 
n  = int(input("Please Enter Number of Nodes in Network : "))
x1 = 0
x2 = int(input("Please Enter X Coordinate by meter : "))
y1 = 0
y2 = int(input("Please Enter Y Coordinate by meter : "))

#Generate random numbers between x1 and x2
X = random.sample(range(x1, x2), n)
#Generate random numbers between y1 and y2
Y = random.sample(range(y1, y2), n)

print("Total Number of Nodes is : ",n)
print(X)
print(Y)
#plt.plot(X,Y)
#plt.xlabel('X - axis')
#plt.ylabel('Y - axis')
#plt.title('My First Gragh')
#plt.show()

class Node():
    def __init__(self,id):
        self.pos_x = X[id]
        self.pos_y = Y[id]
        self.id    = id
        self.energy = init_energy
        
    def get_info(self):
        print("Node %d possition is : " %(self.id),(self.pos_x),(self.pos_y))
        
        
######Autonomous Generation of List Nodes(class Node)#######
node_No = list()                 ###List Nodes
for i in range(n) :
    node_No.append(Node(i))
    
#print(node_No)    ###print type of class
    
for obj in node_No :
    print(obj.get_info())
    
##############################################################
print("----------------------------------------")    
node_No[3].get_info()
print("----------------------------------------")
   
def distance_node_allHops(node) :
    dist_list_node = list()
    global node_No
    
    for obj in node_No :
        new = fn.distance(node ,obj)
        dist_list_node.append(new)
        
    return dist_list_node
###### to convert any list to array using numpy ###########
####    myarray = np.array(mylist)
###### print the Mesh distance of All Nodes in Networks####
i = 0 
while i < n :
    print(distance_node_allHops(node_No[i])) ## AS a list
    print(np.array(distance_node_allHops(node_No[i])))  ## AS an Array
    i = i + 1
############################################################
