
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
                    mid = 99 - newVal 
                else: mid -= newVal
                
            case "R":
                if mid + newVal > 99:
                    mid = newVal - 99
                else: mid += newVal
        if mid == 0:
            count +=1               
file.close()

print("count",count)