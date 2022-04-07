def arithmetic_arranger(lst, answer = False):
    arranged_problems = ''
    if len(lst) > 5: return "Error: Too many problems."
    fnum = list()
    snum = list()
    operator = list() 
    size = list()
    for operation in lst:
        line = operation.strip().split()
        try:
            first = int(line[0])
            second = int(line[2])
        except:
            return "Error: Numbers must only contain digits."
        
        if len(str(first)) > 4 or len(str(second)) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        temp = len(str(first)) 
        if temp > len(str(second)):
            size.append(temp)
        else:
            size.append(len(str(second)))

        if line[1] not in ("+", "-"): 
            return "Error: Operator must be '+' or '-'."
        fnum.append(str(first))
        snum.append(str(second))
        operator.append(line[1]) 
    
    line = []
    for index in range(len(fnum)):
        space = 2 + int(size[index])
        line.append("-" * space)
        if fnum[index] is not fnum[-1]:     
            arranged_problems += fnum[index].rjust(space, " ") + "    "
        else:
            arranged_problems += fnum[index].rjust(space, " ") + "\n"        
    
    for index in range(len(snum)):
        space = 1 + int(size[index])
        if snum[index] is not snum[-1]:     
            arranged_problems += operator[index] + snum[index].rjust(space, " ") + "    "
        else:
            arranged_problems += operator[index] + snum[index].rjust(space, " ") + "\n" + '    '.join(line)    
    
    if answer == False:
        return arranged_problems
    else:
        arranged_problems += "\n"
        ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y)}
        answers = []
        print(operator, len(operator))
        for index in range(len(operator)):
            first = int(fnum[index])
            second = int(snum[index])

            ans = ops[operator[index]] (first, second)
            
            answers.append(str(ans).rjust(len(line[index]), " "))
        
        arranged_problems += "    ".join(answers)
        return arranged_problems
            