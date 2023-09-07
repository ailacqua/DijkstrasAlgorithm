"""
Implementation of Dijkstra's Algorithm with priority queue

Author: Alex Ilacqua
Date: 1/29/2023
"""
class Node:
    #creating node class constructor with names and edges
    def __init__(self, name, edges):
        self.name = name
        self.edges = edges
#prints resulting data table        
def printResult(dataTable):
    print("Dest.","Dist.","Prior Node",sep='\t')
    for i in range(0, len(dataTable)):
        print(dataTable[i][0],dataTable[i][1],dataTable[i][2],sep='\t')
#finds index numbers of neighbors to current node            
def findNeighbors(node):
    neighbors = []
    #appends indices if distance is greater than 0
    for i in range(0,len(node.edges)):
        if node.edges[i] > 0:
            neighbors.append(i)
    return neighbors
#inserts new value into priority queue
def pqInsert(pq,item):
    added = False
    #loops through until i item distance greater then inserts new item
    for i in range(0,len(pq)):
        if item[2]<pq[i][2]:
            pq.insert(i,item)
            added = True
            break
    #if cost is greatest then it is appended to the pq
    if added == False:
        pq.append(item)
    return pq
#processing method for dijkstra
def dijkstra(graph,dataTable,indexDict):
    #instatiating pq and visited list
    pq = []
    visited = [0]
    #finding neighbors of A and inserting them into pq
    neighbors = findNeighbors(graph[0])
    for i in range(0,len(neighbors)):
        distance = graph[0].edges[neighbors[i]]
        item = [0,neighbors[i],distance]
        pqInsert(pq,item)
    #while pq is not empty loop continues
    while pq != []:
        #least cost item is popped
        minItem = pq.pop(0)
        #if distance to node is less than what is in data table distance is updated
        if minItem[2] < dataTable[minItem[1]][1]:
            dataTable[minItem[1]][1] = minItem[2]
            dataTable[minItem[1]][2] = indexDict[minItem[0]].name
            #neighbors of minItem are found
            newNode = graph[minItem[1]]
            neighbors = findNeighbors(newNode)
            for i in range(0,len(neighbors)):
                #calculates total cost from A
                distance = newNode.edges[neighbors[i]] + dataTable[minItem[1]][1]
                #if new node has not been visited then add to pq
                if neighbors[i] not in visited:    
                    item = [minItem[1],neighbors[i],distance]
                    pqInsert(pq,item)
        #appends visited node to visited
        visited.append(minItem[1])
    return dataTable

def main():
    #definition of maxint
    maxint = 999999999
    #creating nodes
    A = Node("A", [0,4,2,-1,-1,7,-1,-1])
    B = Node("B", [4,0,-1,2,-1,-1,-1,-1])
    C = Node("C", [2,-1,0,-1,8,3,-1,-1])
    D = Node("D", [-1,2,-1,0,-1,5,6,-1])
    F = Node("F", [-1,-1,8,-1,0,-1,-1,3])
    G = Node("G", [7,-1,3,5,-1,0,-1,4])
    H = Node("H", [-1,-1,-1,6,-1,-1,0,2])
    J = Node("J", [-1,-1,-1,-1,3,4,2,0])
    #creating data table
    dataTable = [
        [A.name,0,"A"],[B.name,maxint,""],[C.name,maxint,""],[D.name,maxint,""],
        [F.name,maxint,""],[G.name,maxint,""],[H.name,maxint,""],[J.name,maxint,""]]
    #creating index dict
    indexDict = {
        0 : A,
        1 : B,
        2 : C,
        3 : D,
        4 : F,
        5 : G,
        6 : H,
        7 : J}
    #creating graph
    graph = [A,B,C,D,F,G,H,J]
    #finding and printing the result
    printResult(dijkstra(graph,dataTable,indexDict))
    
main()