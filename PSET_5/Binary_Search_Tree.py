class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 1

  def __init__(self):
    self.__root = None

  def insert_element(self, value):
    self.__root = self.__insert_element(value, self.__root)

  def __insert_element(self, val, root):
    if root is None:
      return self.__BST_Node(val)
    if root.value == val:
      raise ValueError
    if val < root.value:
      root.left = self.__insert_element(val, root.left)
      root.height = self.__height_checker(root)
    if val > root.value:
      root.right = self.__insert_element(val, root.right)
      root.height = self.__height_checker(root)
    return self.__balance(root)

  def remove_element(self, value):
    self.__root = self.__remove_element(value, self.__root)

  def __remove_element(self, val, root):
    if root is None:
      raise ValueError
    if root.value == val:
      if root.left is None and root.right is None:
        return None
      elif (root.left is not None and root.right is None) or (root.right is not None and root.left is None):
        if root.left is None:
          return root.right
        else:
          return root.left
      elif root.left is not None and root.right is not None:
        finder = root.right
        while(finder.left is not None):
          finder = finder.left
        root.value = finder.value
        root.right = self.__remove_element(finder.value, root.right)
        root.height = self.__height_checker(root)
        return self.__balance(root)
    if val < root.value:
      root.left = self.__remove_element(val, root.left)
      root.height = self.__height_checker(root)
    if val > root.value:
      root.right = self.__remove_element(val, root.right)
      root.height = self.__height_checker(root)
    return self.__balance(root)
  
  def __list__(self, root):
    if(root is None):
      return []
    else:
      tree_list = self.__list__(root.left) + [root.value] + self.__list__(root.right)
    return tree_list

  def in_order(self):
    return '[ ' + self.__in_order(self.__root)[2:] + ' ]'

  def __in_order(self, root):
    if(root is None):
      return ''
    else:
      tree = self.__in_order(root.left) + ', ' + str(root.value) + self.__in_order(root.right)
    return tree

  def pre_order(self):
    return '[ ' + self.__pre_order(self.__root)[2:] + ' ]'

  def __pre_order(self, root):
    if(root is None):
      return ''
    else:
      tree = ', ' + str(root.value) + self.__pre_order(root.left) + self.__pre_order(root.right)
    return tree

  def post_order(self):
    return '[ ' + self.__post_order(self.__root)[2:] + ' ]'

  def __post_order(self, root):
    if(root is None):
      return ''
    else:
      tree = self.__post_order(root.left) + self.__post_order(root.right) + ', ' + str(root.value) 
    return tree

  def get_height(self):
    if self.__root is None:
      return 0
    else:
      return self.__root.height
  
  def __balance(self, t):
    if t is None:
      return t
    elif (self.__right_child_checker(t) - self.__left_child_checker(t) == -2):
      #If t's left child is left-heavy by 1 or balanced at 0, rotate right about t and return the new root.
      if (self.__right_child_checker(t.left) - self.__left_child_checker(t.left) == -1) or (self.__right_child_checker(t.left) - self.__left_child_checker(t.left) == 0):
        holder = t
        t = t.left
        holder.left = t.right
        t.right = holder
        holder.height = self.__height_checker(holder)
        t.height = self.__height_checker(t)
      #If t's left child is right-heavy by 1, rotate left about t's left child, then rotate right about t and return the new root.
      elif (self.__right_child_checker(t.left) - self.__left_child_checker(t.left) == 1):
        holder = t.left
        left_child = t.left
        left_float = left_child.right.left
        t.left = left_child.right
        t.left.left = holder
        holder.right = left_float
        holder.height = self.__height_checker(holder)
        t.left.height = self.__height_checker(t.left)
        t.height = self.__height_checker(t)
        holder = t
        t = t.left
        holder.left = t.right
        t.right = holder
        holder.height = self.__height_checker(holder)
        t.height = self.__height_checker(t)
    elif (self.__right_child_checker(t) - self.__left_child_checker(t) == 2):
      #If t's right child is right-heavy by 1 or balanced at 0, rotate left about t and return the new root.
      if (self.__right_child_checker(t.right) - self.__left_child_checker(t.right) == 1) or (self.__right_child_checker(t.right) - self.__left_child_checker(t.right) == 0):
        holder = t
        t = t.right
        holder.right = t.left
        t.left =  holder
        holder.height = self.__height_checker(holder)
        t.height = self.__height_checker(t)
      #If t's right child is left-heavy by 1, rotate right about t's right child, then rotate left about t and return the new root.
      elif (self.__right_child_checker(t.right) - self.__left_child_checker(t.right) == -1):
        holder = t.right
        right_child = t.right
        right_float = right_child.left.right
        t.right = right_child.left
        t.right.right = holder
        holder.left = right_float
        holder.height = self.__height_checker(holder)
        t.right.height = self.__height_checker(t.right)
        t.height = self.__height_checker(t)
        holder = t
        t = t.right
        holder.right = t.left
        t.left =  holder
        holder.height = self.__height_checker(holder)
        t.height = self.__height_checker(t)
    return t
  
  def __left_child_checker(self, t):
    return t.left.height if t.left is not None else 0
  def __right_child_checker(self, t):
    return t.right.height if t.right is not None else 0

  def __rotate_left(self, t):
    right_child = t.right
    t.left = t
    t.right = t.left.left
    t = right_child

  def __str__(self):
    if(self.__root is None):
      return '[ ]'
    else:
      return self.in_order()
  
  def to_list(self):
    return self.__list__(self.__root)
  
  def __height_checker(self, root):
    if root is None:
      return 0
    elif root.left is None and root.right is None:
      return 1
    elif root.left is None and root.right is not None:
      return root.right.height + 1
    elif root.left is not None and root.right is None:
      return root.left.height + 1
    elif root.left is not None and root.right is not None:
      return max(root.left.height, root.right.height) + 1
    
if __name__ == '__main__':
  test = Binary_Search_Tree()
  test.insert_element(20)
  test.insert_element(10)
  test.insert_element(19)
  print(test)
  print(test.get_height())
  

  