
mid = 50
count = 0 

def save_value(line):
    newLine = line[1:]
    multiplier = 1
    
    if len (newLine) == 2:
        return int(newLine) , 1
    
    else:
        lastLine = newLine[-2:]
        multiplier = newLine[:-2]
    return int(lastLine) , int(multiplier)


with open("input.txt", "r") as file:

    
    for line in file:
        if not line: 
            continue
    
        line = line.strip()
        
        # newVal = int(line[1:]) % 100

        newVal, multiplier = save_value(line)
        newVal = int(newVal)
        
        match line[0]:               
            case "L":
                if mid - newVal < 0:
                    mid = 100 + (mid-newVal)
                    count += multiplier
                else: mid -= newVal
                if mid == 0:
                    count +=1
                
            case "R": 
                if mid + newVal > 99:
                    mid = (newVal+mid) - 100
                    count += multiplier
                else: mid += newVal
                if mid ==0:
                    count +=1
                
        # if mid == 0:
        #     count +=1               
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
