'''
given a string, which is the company name in lowecase letterd , 
your task is to find top three msot common characters in the string
print the three most commin charceyters along with their occurence count 
sort in dscending order of occurence count
if the occurence count is the same, sort the characters in alphabeticak order
input format :
aabbbccdef
output format:
b 3
a 2
c 2

'''
c = input()
count = {}
for ch in c:
    if(ch in count):
        count[ch]= count[ch] + 1
    else:
        count[ch] = 1
char = []
for ch in count:
    char.append([ch,count[ch]])
char.sort()
char.sort(key=lambda x: x[1], reverse=True)
for i in range(3):
    print(char[i][0], char[i][1])