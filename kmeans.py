import math

data = [
        [2,10],
        [2,5],
        [8,4],
        [5,8],
        [7,5],
        [6,4]  
    ]



# function to calculate the euclidean distance

def euclidean_distance(x1,y1,x2,y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

c1 = data[0]
c2 = data[1]


count = 0

while count < len(data):
    cluster1 = []
    cluster2 = []

    count = count +1
    for point in data:
        x1 = point[0]
        y1 = point[1]
        if euclidean_distance(c1[0],c1[1],x1,y1) < euclidean_distance(c2[0],c2[1],x1,y1):
            cluster1.append(point)
        else:
            cluster2.append(point)
        print("centroid value",c1,c2)
        print(" cluster1 ",cluster1,"cluster2 ",cluster2)
    c1 = [sum([x[0] for x in cluster1])/len(cluster1),sum([x[1] for x in cluster1])/len(cluster1)]
    c2 = [sum([x[0] for x in cluster2])/len(cluster2),sum([x[1] for x in cluster2])/len(cluster2)]
    
   

print("The Centroid values are : ",c1,c2)
print("Final cluster 1 : ",cluster1)
print("Final cluster 2 : ",cluster2)
