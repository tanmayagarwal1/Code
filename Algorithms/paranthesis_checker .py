def isvalid(str):
  stack=[]
  my_map={'{':'}','[':']','(':')'}
  braces=set(['{','(','['])
  for i in str:
    if i in braces:
      stack.append(i)
    else:
      if stack and i==my_map[stack[-1]]:
        stack.pop()
      else:
        return False
  return True 

str="[{]"
print(isvalid(str))
