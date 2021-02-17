from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__front = 0
    self.__back = 0
    self.__size = 0
    
  def __str__(self):
    if self.__size == 0:
      return '[ ]'
    if self.__size == 1:
      return '[ ' + str(self.__contents[self.__front]) + ' ]'
    else:
      value = '[ '
      for i in range(self.__size - 1):
        value += str(self.__contents[(self.__front + i)%self.__capacity]) + ', '
      value += str(self.__contents[(self.__front + i + 1)%self.__capacity]) + ' ]'
      return value
    
  def __len__(self):
    return self.__size

  def __grow(self):
    old_contents = self.__contents
    self.__capacity = self.__capacity * 2
    self.__contents = [None] * self.__capacity
    walk = self.__front
    for i in range(self.__size):
      self.__contents[i] = old_contents[walk]
      walk = (walk + 1) % self.__size
    self.__front = 0
    self.__back = self.__size - 1
  
  def push_front(self, val):
    if(self.__size == self.__capacity):
      self.__grow()
      self.__front = (self.__front - 1 + self.__capacity) % self.__capacity
      self.__contents[self.__front] = val
      self.__size += 1
    else:
      self.__front = (self.__front - 1 + self.__capacity) % self.__capacity
      self.__contents[self.__front] = val
      self.__size += 1
    
  def pop_front(self):
    temp_front = self.__front
    self.__front = (self.__front + 1) % self.__capacity
    self.__size = self.__size - 1
    return self.__contents[temp_front]
    
  def peek_front(self):
    if(self.__size == 0):
      return None
    else:
      return self.__contents[self.__front]
    
  def push_back(self, val):
    if(self.__size == self.__capacity):
      self.__grow()
      self.__back = (self.__back + 1) % self.__capacity
      self.__contents[self.__back] = val
      self.__size += 1
    else:
      self.__back = (self.__back + 1) % self.__capacity
      self.__contents[self.__back] = val
      self.__size += 1
  
  def pop_back(self):
    temp_back = self.__back
    self.__back = (self.__back - 1 + self.__capacity) % self.__capacity
    self.__size = self.__size - 1
    return self.__contents[temp_back]

  def peek_back(self):
    if(self.__size == 0):
      return None
    else:
      return self.__contents[self.__back]

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
