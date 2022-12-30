def evalPostfix(CQStack,exp):
    for i in exp:
        if i.isdigit(): 
            CQStack.push(i) 
        else: 
            val1 = CQStack.pop() 
            val2 = CQStack.pop()
            if i=='^':
              i = "**"
            CQStack.push(str(int(eval(val2 + i + val1))))
    return int(CQStack.pop())