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
    return root

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
        return root
    if val < root.value:
      root.left = self.__remove_element(val, root.left)
      root.height = self.__height_checker(root)
    if val > root.value:
      root.right = self.__remove_element(val, root.right)
      root.height = self.__height_checker(root)
    return root

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

  def __str__(self):
    if(self.__root is None):
      return '[ ]'
    else:
      return self.in_order()
  
  def __height_checker(self, root):
    if root is None:
      return 0
    if root.left is None and root.right is None:
      return 1
    if root.left is None and root.right is not None:
      return root.right.height + 1
    if root.left is not None and root.right is None:
      return root.left.height + 1
    if root.left is not None and root.right is not None:
      return max(root.left.height, root.right.height) + 1
    
if __name__ == '__main__':
  pass
  