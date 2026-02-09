#dictionary consisting of name and age.soor according to sort in descending order
#output: [{'name':'kevin','age':'24']
n= int(input())
data = []
for i in range(n):
    name = input()
    age = input()
    data.append({"name":name, "age":age})
for i in range(len(data)):
    for j in range (i+1, len(data)):
        if data[i][name] > data[j][age]:
            data[i], data[j] = data[j], data[i]
print(data)