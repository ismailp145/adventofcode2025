
mid = 50
count = 0 

file = open("input.txt", "r")
line = file.readline()

while line:
    line = file.readline()
    if line:
        newVal = int(line[1:]) % 100
        match line[0]:               
            case "L":
                if mid - newVal < 0:
                    mid = 100 + (mid-newVal)
                else: mid -= newVal
                
            case "R":
                if mid + newVal > 99:
                    mid = (mid+newVal) - 100
                else: mid += newVal
        if mid == 0:
            count +=1               
file.close()

print("count",count)

"""
mid = 5
L20
5 - 20 <0 yes
mid = 100 + -15 
85

Mid = 85
R20

85 + 20 > 99: yes
mid = (85 + 20)- 100 
5

"""
