
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
                else: 
                    mid -= newVal
                    
            case "R": 
                if mid + newVal > 99:
                    mid = (newVal+mid) - 100    
                else: 
                    mid += newVal
                
        if mid == 0:
            count += multiplier + 1
        elif len(line) > 3:
            print(line, len(line))
            count += multiplier 
                
    file.close()

    print("count",count)

    """
    L68
    L30
    R48
    L5
    R60
    L55
    L1
    L99
    R14
    L82

    newVal = 68
    multi = 1
    mid = 50 
    line = l68
    50 - 68 <0; true
    mid = 100 +(mid-val)
    mid = 82
    else count +=1 true
    
    count = 1
    mid = 82
    L30
    nval = 30
    mult = 1
    
    

    """
