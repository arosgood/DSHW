class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      self.value = val
      self.next = None
      self.previous = None

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    self.__header = self.__Node(None)
    self.__trailer = self.__Node(None)
    self.__header.next = self.__trailer
    self.__header.previous = None
    self.__trailer.next = None
    self.__trailer.previous = self.__header
    self.__size = 0

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    return self.__size

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this 
    # is the only way to add items at the tail position.
    newest = self.__Node(val)
    self.__trailer.previous.next = newest
    newest.previous = self.__trailer.previous
    newest.next = self.__trailer
    self.__trailer.previous = newest
    self.__size += 1

  def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the 
    # specified index. If the index is not a valid 
    # position within the list, raise an IndexError 
    # exception. This method cannot be used to add an 
    # item at the tail position.
    if(index >= self.__size or index < 0):
      raise IndexError
    elif(index > self.__size/2):
      newest = Linked_List.__Node(val)
      current = self.__trailer
      for i in range(self.__size - index):
        current = current.previous
      newest.previous = current.previous
      newest.next = current
      current.previous = newest
      newest.previous.next = newest
      self.__size += 1
    else:
      newest = Linked_List.__Node(val)
      current = self.__header
      for i in range(index):
        current = current.next
      newest.next = current.next
      newest.previous = current
      current.next = newest
      newest.next.previous = newest
      self.__size += 1

  def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored 
    # in the node at the specified index. If the index 
    # is invalid, raise an IndexError exception.
    if(index >= self.__size or index < 0):
      raise IndexError
    elif(index > self.__size/2):
      current = self.__trailer
      for i in range(self.__size - index - 1):
        current = current.previous
      element = current.previous
      current.previous = element.previous
      current.previous.next = current
      self.__size = self.__size - 1
      return element.value
    else:
      current = self.__header
      for i in range(index):
        current = current.next
      element = current.next
      current.next = element.next
      current.next.previous = current
      self.__size = self.__size - 1 
      return element.value

  def get_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node 
    # at the specified index, but do not unlink it from 
    # the list. If the specified index is invalid, raise 
    # an IndexError exception.
    if(index >= self.__size or index < 0):
      raise IndexError
    elif(index > self.__size/2):
      current = self.__trailer
      for i in range(self.__size - index - 1):
        current = current.previous
      return current.previous.value
    else:      
      current = self.__header
      for i in range(index):
        current = current.next
      return current.next.value


  def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    if self.__size == 0:
      return '[ ]'
    if self.__size == 1:
      return '[ ' + str(self.__header.next) + ' ]'
    else:
      mover = self.__header.next
      self.__header.next = mover.next
      mover.next.previous = self.__header
      self.__trailer.previous.next = mover
      mover.previous = self.__trailer.previous
      mover.next = self.__trailer
      self.__trailer.previous = mover

    
  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    if(self.__size == 0):
      return '[ ]'
    if(self.__size == 1):
      return '[ ' + str(self.__header.next.value) + ' ]'
    else:
      value = '[ '
      current = self.__header
      while(current.next.next.value is not None):
        value += str(current.next.value) + ', '
        current = current.next
      value += str(current.next.value) + ' ]'
      return value


  def __iter__(self):
    # initialize a new attribute for walking through your list
    # statement. do not modify the return statement.
    self.__iter_walker = self.__header
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more 
    # values to fetch, raise a StopIteration exception.
    if(self.__iter_walker.next.value is None):
      raise StopIteration
    else:
      self.__iter_walker = self.__iter_walker.next
      return str(self.__iter_walker.value)

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  print('Does appending to the list add an element at the new tail position and increment the size by one?')
  a = Linked_List()
  print('Size right now is: ' + str(len(a)))
  print(str(a))
  a.append_element(1)
  print('Size right now is: ' + str(len(a)))
  print(str(a))
  a.append_element(2)
  print('Size right now is: ' + str(len(a)))
  print(str(a))
  a.append_element(3)
  print('Size right now is: ' + str(len(a)))
  print(str(a))
  a.append_element(4)
  print('Size right now is: ' + str(len(a)))
  print(str(a))
  print('------------------------------------------')

  print("Does inserting an item at a valid index increase the size by one and correctly modify the list's structure?")
  b = Linked_List()
  b.append_element(1)
  print('Appended value of one')
  print('Size is: ' + str(len(b)) + ' and list looks like: ' + str(b))
  b.insert_element_at(2, 0)
  print('Adding value of 2 at index 0')
  print('Size is: ' + str(len(b)) + ' and list looks like: ' + str(b))
  b.insert_element_at(4, 1)
  print('Adding value of 4 at index 1')
  print('Size is: ' + str(len(b)) + ' and list looks like: ' + str(b))
  b.insert_element_at(100, 2)
  print('Adding value of 100 at index 2')
  print('Size is: ' + str(len(b)) + ' and list looks like: ' + str(b))
  b.insert_element_at(1000, 3)
  print('Adding value of 1000 at index 3')
  print('Size is: ' + str(len(b)) + ' and list looks like: ' + str(b))
  print('------------------------------------------')

  print("Does inserting an item at an invalid index leave the list completely unchanged?")
  c = Linked_List()
  try:
    # should fail, invalid index 
    c.insert_element_at(1,0)
  except IndexError:
    print('Correctly caught incorrect index!')
  c.append_element(0)
  try:
    # should fail, invalid index 
    c.insert_element_at(1,1)
  except IndexError:
    print('Correctly caught incorrect index!')
  
  try:
    # should fail, invalid index 
    c.insert_element_at(1,-1)
  except IndexError:
    print('Correctly caught incorrect index!')
  c.append_element(1)
  c.append_element(2)
  try:
    # should fail, invalid index 
    c.insert_element_at(5,3)
  except IndexError:
    print('Correctly caught incorrect index!')
  print('------------------------------------------')

  print("Does removing an item at a valid index decrease the size by one and correctly modify the list's structure?") 
  d = Linked_List()
  for i in range(10):
    d.append_element(i)
  print('Our full list d looks like this: ' + str(d))
  print('Now we will delete the value of 1 at index 1!')
  d.remove_element_at(1)
  print('Size should be 9, it is size: ' + str(len(d)) + ', and the list should be the same except missing a 1: ' + str(d))
  print('Now we will delete 2 values!')
  d.remove_element_at(3)
  print(d.remove_element_at(5))
  print('Size should be 7, it is size: ' + str(len(d)) + ', and the list should be the same except missing values 4 and 7: ' + str(d))
  print('Now we will delete the value of 9 at index 6!')
  d.remove_element_at(6)
  print('Size should be 6, it is size: ' + str(len(d)) + ', and the list should be the same except missing a 9: ' + str(d))
  print('Now we will delete the value of 5 at index 4!')
  d.remove_element_at(4)
  print('Size should be 5, it is size: ' + str(len(d)) + ', and the list should be the same except missing a 9: ' + str(d))
  print('------------------------------------------')

  print("Does removing an item at an invalid index leave the list completely unchanged?")

  e = Linked_List()
  for i in range(10):
      e.append_element(i)
  print(str(e))
  print('Lets try removing at invalid indices!')

  try:
    # should fail, invalid index 
    e.remove_element_at(10)
  except IndexError:
    print('Correctly caught incorrect index!')
  
  try:
    # should fail, invalid index 
    e.remove_element_at(-101)
  except IndexError:
    print('Correctly caught incorrect index!')

  try:
    # should fail, invalid index 
    e.remove_element_at(11)
  except IndexError:
    print('Correctly caught incorrect index!')
  e = Linked_List()
  try:
    # should fail, invalid index 
    e.remove_element_at(0)
  except IndexError:
    print('Correctly caught incorrect index!')
  try:
    # should fail, invalid index 
    e.remove_element_at(1)
  except IndexError:
    print('Correctly caught incorrect index!')
  e.append_element(0)
  try:
    # should fail, invalid index 
    e.remove_element_at(1)
  except IndexError:
    print('Correctly caught incorrect index!')
  print('------------------------------------------')

  print("Does length always return the number of values stored in the list (not including sentinel nodes)?")
  f = Linked_List()
  for i in range(20):
    f.append_element(i)
    print('List now looks like this: ' + str(f) + ' , with a size of: ' + str(len(f)))
  print('------------------------------------------')

  print("Is the string representation of your list correct for a variety of lengths?")
  g = Linked_List()
  print('Empty list: ' + str(g))
  for i in range(20):
    g.append_element(i)
    print('List now looks like this: ' + str(g))
  print('------------------------------------------')

  print("Does a for loop visit every value?")
  my_list = Linked_List()
  for i in range(30):
    my_list.append_element(i)
  print("my_list now has 30 elements, from 0 to 29! Let's loop through and check this!")
  for val in my_list:
    print(val)
  print('Lets access some values using get_element_at!')
  print('The number 20 should be printed after the colon: ' + str(my_list.get_element_at(20)))
  print('The number 27 should be printed after the colon: ' + str(my_list.get_element_at(27)))
  print('The number 15 should be printed after the colon: ' + str(my_list.get_element_at(15)))
  print('The number 10 should be printed after the colon: ' + str(my_list.get_element_at(10)))
  print('The number 3 should be printed after the colon: ' + str(my_list.get_element_at(3)))
  print('The number 29 should be printed after the colon: ' + str(my_list.get_element_at(29)))

  new = Linked_List()
  new.rotate_left()

  ll = Linked_List()
  node = Linked_List.__Node(4)
  print(ll)
  print(node)

  