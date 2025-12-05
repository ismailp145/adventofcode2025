
mid = 50
count = 0 

def save_value(line):
    newLine = line[1:]
    
    if len (newLine) <=2 :
        return int(line[1:]) % 100, 1    
    else:
        multiplier = newLine[:-2]
        return int(line[1:]) % 100 , int(multiplier)


with open("input.txt", "r") as file:

    
    for line in file:
        if not line: 
            continue
    
        line = line.strip()
    
        newVal, multiplier = save_value(line)
    
        match line[0]:               
            case "L":
                if mid - newVal < 0:
                    mid = 100 + (mid-newVal)
                    if mid == 0:
                        count += multiplier + 1
                    else:
                        count += multiplier
                else: 
                    mid -= newVal
                    
            case "R": 
                if mid + newVal > 99:
                    mid = (newVal+mid) - 100
                    if mid == 0:
                        count += multiplier + 1
                    else:
                        count += multiplier
                else: mid += newVal
            
                
    file.close()

    print("count",count)

    """

    """
