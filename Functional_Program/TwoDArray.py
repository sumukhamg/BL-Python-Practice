n = int(input("Enter number of rows"))
m = int(input("Enter number of columns"))

array = []
print("Enter the values: ")
for i in range(0, n):
    row = []
    for j in range(0, m):
        print("Row: ", i + 1, ", column: ", j + 1)
        ele = int(input())
        row.append(ele)
    array.append(row)
    row = []

print(array)