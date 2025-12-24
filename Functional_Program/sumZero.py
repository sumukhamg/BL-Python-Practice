list1 = [-10, 2, 3, 25, 15, 5, 5]

list1.sort()

def check_Negetive(list1):
    if(list1[0] > 0):
        print("Sum not possible")
    else:
        printSum(list1)
    
def printSum(list1):
    for i in range(0, len(list1)):
        for j in range(i + 1, len(list1)):
            for k in range(j + 1, len(list1)):
                if(i != j and i != k and j != k):
                    if(list1[i] + list1[j] + list1[k] == 0):
                        print(list1[i] , ", ", list1[j] ,", ", list1[k])


check_Negetive(list1)