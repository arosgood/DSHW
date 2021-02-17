import unittest
from Binary_Search_Tree import Binary_Search_Tree

class Binary_Search_Tree_Tester(unittest.TestCase):

    def setUp(self):
        self.test_tree = Binary_Search_Tree()
    
    def test_empty_tree_string(self):
        self.assertEqual('[ ]', str(self.test_tree), 'Empty tree should print as "[ ]"')

    def test_empty_tree_height(self):
        self.assertEqual(0, self.test_tree.get_height(), 'Empty tree should have height 0')

    def test_remove_none_root(self): 
        try:
            self.test_tree.remove_element(10)
        except ValueError:
            print('Root was none and was attempted to be removed')
    
    def test_one_value_tree_string(self):
        self.test_tree.insert_element(21)
        self.assertEqual('[ 21 ]', str(self.test_tree), 'Tree should print as "[ 21 ]"')

    def test_one_value_tree_height(self):
        self.test_tree.insert_element(21)
        self.assertEqual(1, self.test_tree.get_height(), 'Tree should have height 1')

    def test_two_value_tree_height(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        self.assertEqual(2, self.test_tree.get_height(), 'Tree should have height 2')

    def test_two_value_tree_string(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        self.assertEqual('[ 21, 50 ]', str(self.test_tree), 'Tree should print as "[ 21, 50 ]"')

    def test_duplicate_value_error_tree_height(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        try:
            self.test_tree.insert_element(50)
        except ValueError:
            print('Duplicate value was inserted and error was thrown')

    def test_three_value_tree_height(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        self.test_tree.insert_element(15)
        self.assertEqual(2, self.test_tree.get_height(), 'Tree should still have height 2 despite two children')

    def test_three_value_tree_string(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        self.test_tree.insert_element(15)
        self.assertEqual('[ 15, 21, 50 ]', str(self.test_tree), 'Tree should print as "[ 15, 21, 50 ]"')

    def test_four_value_tree_height(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        self.test_tree.insert_element(15)
        self.test_tree.insert_element(10)
        self.assertEqual(3, self.test_tree.get_height(), 'Tree should now have height 3')

    def test_four_value_tree_string(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        self.test_tree.insert_element(15)
        self.test_tree.insert_element(10)
        self.assertEqual('[ 10, 15, 21, 50 ]', str(self.test_tree), 'Tree should print as "[ 10, 15, 21, 50 ]"') 
    
    def test_heavy_left_tree_height(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        self.test_tree.insert_element(15)
        self.test_tree.insert_element(10)
        self.test_tree.insert_element(9)
        self.test_tree.insert_element(8)
        self.assertEqual(5, self.test_tree.get_height(), 'Tree should now have height 5 as height is the longest path from root to leaf node')

    def test_heavy_right_tree_height(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        self.test_tree.insert_element(15)
        self.test_tree.insert_element(60)
        self.test_tree.insert_element(70)
        self.test_tree.insert_element(80)
        self.assertEqual(5, self.test_tree.get_height(), 'Tree should now have height 5 as height is the longest path from root to leaf node')

    def test_inorder_seven_value_tree_string(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        self.test_tree.insert_element(15)
        self.test_tree.insert_element(10)
        self.test_tree.insert_element(17)
        self.test_tree.insert_element(45)
        self.test_tree.insert_element(55)
        self.assertEqual('[ 10, 15, 17, 21, 45, 50, 55 ]', str(self.test_tree), 'In-order traversal of the tree should print as "[ 10, 15, 17, 21, 45, 50, 55 ]"') 

    def test_remove_right_subroot_from_tree_string(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        self.test_tree.insert_element(15)
        self.test_tree.insert_element(10)
        self.test_tree.insert_element(17)
        self.test_tree.insert_element(45)
        self.test_tree.insert_element(55)
        self.test_tree.remove_element(50)
        self.assertEqual('[ 10, 15, 17, 21, 45, 55 ]', str(self.test_tree), 'In-order traversal of the tree should print as "[ 10, 15, 17, 21, 45, 55 ]"') 

    def test_remove_left_subroot_from_tree_string(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        self.test_tree.insert_element(15)
        self.test_tree.insert_element(10)
        self.test_tree.insert_element(17)
        self.test_tree.insert_element(45)
        self.test_tree.insert_element(55)
        self.test_tree.remove_element(15)
        self.assertEqual('[ 10, 17, 21, 45, 50, 55 ]', str(self.test_tree), 'In-order traversal of the tree should print as "[ 10, 17, 21, 45, 50, 55 ]"') 

    def test_remove_root_from_tree_string(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        self.test_tree.insert_element(15)
        self.test_tree.insert_element(10)
        self.test_tree.insert_element(17)
        self.test_tree.insert_element(45)
        self.test_tree.insert_element(55)
        self.test_tree.remove_element(21)
        self.assertEqual('[ 10, 15, 17, 45, 50, 55 ]', str(self.test_tree), 'In-order traversal of the tree should print as "[ 10, 15, 17, 45, 50, 55 ]"') 


"""     def test_preorder_seven_value_tree_string(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        self.test_tree.insert_element(15)
        self.test_tree.insert_element(10)
        self.test_tree.insert_element(17)
        self.test_tree.insert_element(45)
        self.test_tree.insert_element(55)
        self.assertEqual('[ 21, 15, 10, 17, 50, 45, 55 ]', str(self.test_tree), 'Pre-order traversal of the tree should print as "[ 21, 15, 10, 17, 50, 45, 55 ]"')
 """

"""     def test_postorder_seven_value_tree_string(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        self.test_tree.insert_element(15)
        self.test_tree.insert_element(10)
        self.test_tree.insert_element(17)
        self.test_tree.insert_element(45)
        self.test_tree.insert_element(55)
        self.assertEqual('[ 10, 17, 15, 45, 55, 50, 21 ]', str(self.test_tree), 'Tree should print as "[ 10, 17, 15, 45, 55, 50, 21 ]"') """
 

if __name__ == '__main__':
  unittest.main()