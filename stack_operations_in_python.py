# -*- coding: utf-8 -*-
"""Stack operations in python.ipynb






class stack():                   #Stack is a LIFO(last in first out data structure)
  def __init__(self):
    self.elements=[]

  def push(self,element):         #pushes an element to the stack
    self.elements.append(element)


  def pop(self):                 #pops the last pushed element from the list
    return self.elements.pop()
  
  def is_empty(self):          #checks whether the stack is empty or not.Returns boolean value True or False
    return self.elements==[]
 
  def peek(self):              #returns the top elements of the stack
    if not self.is_empty:
      return self.elements[-1]

#For displaying the stack items,simply do print(stack_object.elements)





