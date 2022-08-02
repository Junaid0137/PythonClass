l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"Madhu" , 234:[23,45,656]}]
l.reverse()
print(l)
print(l[1][0])
print(l[3][1])
for i in range(len(l)):
    if type(l[i]) == list :
        print(l[i])
print(l[0]["key1"])
print(l[0].keys())
print(l[0].values())



