def evalPrefix(stack, exp):
  for i in exp[::-1]:
    if i.isdigit():
      stack.push(int(i));
    else:
      val1=stack.pop();
      val2=stack.pop();
      if i == '+':
        stack.push(val1+val2);
      elif i == '-':
        stack.push(val1-val2);
      elif i == '*':
        stack.push(val1*val2);
      elif i=='/':
        stack.push(val1/val2);
      elif i=='^':
      	stack.push(pow(val1,val2));
  return int(stack.pop());