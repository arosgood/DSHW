import unittest
from Binary_Search_Tree import Binary_Search_Tree

class Binary_Search_Tree_Tester(unittest.TestCase):

    def setUp(self):
        self.test_tree = Binary_Search_Tree()
    
    def test_empty_tree_string(self):
        self.assertEqual('[ ]', str(self.test_tree), 'Empty tree should print as "[ ]"')
        
    def test_empty_tree_list(self):
        self.assertEqual([], self.test_tree.to_list(), 'Empty tree should print as "[]"')

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
        self.assertEqual(3, self.test_tree.get_height(), 'Tree should now have height 3 as height is the longest path from root to leaf node')

    def test_heavy_right_tree_height(self):
        self.test_tree.insert_element(21)
        self.test_tree.insert_element(50)
        self.test_tree.insert_element(15)
        self.test_tree.insert_element(60)
        self.test_tree.insert_element(70)
        self.test_tree.insert_element(80)
        self.assertEqual(3, self.test_tree.get_height(), 'Tree should now have height 3 as height is the longest path from root to leaf node')

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

    def test_str_left_heavy2_left_child_left_heavy(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(10)
        self.test_tree.insert_element(5)
        self.assertEqual('[ 5, 10, 20 ]', str(self.test_tree), 'In-order traversal of the tree should print as "[ 5, 10, 20 ]"') 

    def test_list_left_heavy2_left_child_left_heavy(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(10)
        self.test_tree.insert_element(5)
        self.assertEqual([5, 10, 20], self.test_tree.to_list(), 'In-order traversal of the tree should print as "[5, 10, 20]"') 

    def test_height_left_heavy2_left_child_left_heavy(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(10)
        self.test_tree.insert_element(5)
        self.assertEqual(2, self.test_tree.get_height(), 'Height should be 2') 

    def test_str_left_heavy2_left_child_right_heavy(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(10)
        self.test_tree.insert_element(12)
        self.assertEqual('[ 10, 12, 20 ]', str(self.test_tree), 'In-order traversal of the tree should print as "[ 10, 12, 20 ]"') 

    def test_list_left_heavy2_left_child_right_heavy(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(10)
        self.test_tree.insert_element(12)
        self.assertEqual([10, 12, 20], self.test_tree.to_list(), 'In-order traversal of the tree should print as "[10, 12, 20]"') 

    def test_height_left_heavy2_left_child_right_heavy(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(10)
        self.test_tree.insert_element(12)
        self.assertEqual(2, self.test_tree.get_height(), 'Height should be 2') 

    def test_str_right_heavy2_right_child_right_heavy(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(25)
        self.test_tree.insert_element(30)
        self.assertEqual('[ 20, 25, 30 ]', str(self.test_tree), 'In-order traversal of the tree should print as "[ 20, 25, 30 ]"') 

    def test_list_right_heavy2_right_child_right_heavy(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(25)
        self.test_tree.insert_element(30)
        self.assertEqual([20, 25, 30], self.test_tree.to_list(), 'In-order traversal of the tree should print as "[20, 25, 30]"') 

    def test_height_right_heavy2_right_child_right_heavy(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(25)
        self.test_tree.insert_element(30)
        self.assertEqual(2, self.test_tree.get_height(), 'Height should be 2') 

    def test_str_right_heavy2_right_child_left_heavy(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(25)
        self.test_tree.insert_element(23)
        self.assertEqual('[ 20, 23, 25 ]', str(self.test_tree), 'In-order traversal of the tree should print as "[ 20, 23, 25 ]"') 

    def test_list_right_heavy2_right_child_left_heavy(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(25)
        self.test_tree.insert_element(23)
        self.assertEqual([20, 23, 25], self.test_tree.to_list(), 'In-order traversal of the tree should print as "[20, 23, 25]"') 

    def test_height_right_heavy2_right_child_left_heavy(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(25)
        self.test_tree.insert_element(23)
        self.assertEqual(2, self.test_tree.get_height(), 'Height should be 2') 

    def test_complicated_avl_height(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(25)
        self.test_tree.insert_element(23)
        self.test_tree.insert_element(27)
        self.test_tree.insert_element(29)
        self.test_tree.insert_element(30)
        self.test_tree.insert_element(18)
        self.test_tree.insert_element(17)
        self.test_tree.insert_element(16)
        self.assertEqual(4, self.test_tree.get_height(), 'Height should be 4') 

    def test_complicated_avl_str(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(25)
        self.test_tree.insert_element(23)
        self.test_tree.insert_element(27)
        self.test_tree.insert_element(29)
        self.test_tree.insert_element(30)
        self.test_tree.insert_element(18)
        self.test_tree.insert_element(17)
        self.test_tree.insert_element(16)
        self.test_tree.insert_element(26)
        self.assertEqual('[ 16, 17, 18, 20, 23, 25, 26, 27, 29, 30 ]', str(self.test_tree), 'In-order traversal should be "[ 16, 17, 18, 20, 23, 25, 26, 27, 29, 30 ]"')
    

    def test_remove_complicated_avl_str(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(25)
        self.test_tree.insert_element(23)
        self.test_tree.insert_element(27)
        self.test_tree.insert_element(29)
        self.test_tree.insert_element(30)
        self.test_tree.insert_element(18)
        self.test_tree.insert_element(17)
        self.test_tree.insert_element(16)
        self.test_tree.insert_element(26)
        self.test_tree.remove_element(27)
        self.assertEqual('[ 16, 17, 18, 20, 23, 25, 26, 29, 30 ]', str(self.test_tree), 'In-order traversal should be "[ 16, 17, 18, 20, 23, 25, 26, 29, 30 ]"')

    def test_remove2_complicated_avl_str(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(25)
        self.test_tree.insert_element(23)
        self.test_tree.insert_element(27)
        self.test_tree.insert_element(29)
        self.test_tree.insert_element(30)
        self.test_tree.insert_element(18)
        self.test_tree.insert_element(17)
        self.test_tree.insert_element(16)
        self.test_tree.insert_element(26)
        self.test_tree.remove_element(27)
        self.test_tree.remove_element(26)
        self.assertEqual('[ 16, 17, 18, 20, 23, 25, 29, 30 ]', str(self.test_tree), 'In-order traversal should be "[ 16, 17, 18, 20, 23, 25, 29, 30 ]"')

    def test_height_remove2_complicated_avl_str(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(25)
        self.test_tree.insert_element(23)
        self.test_tree.insert_element(27)
        self.test_tree.insert_element(29)
        self.test_tree.insert_element(30)
        self.test_tree.insert_element(18)
        self.test_tree.insert_element(17)
        self.test_tree.insert_element(16)
        self.test_tree.insert_element(26)
        self.test_tree.remove_element(27)
        self.test_tree.remove_element(26)
        self.assertEqual(4, self.test_tree.get_height(), 'Height is now 4')

    def test_remove3_complicated_avl_str(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(25)
        self.test_tree.insert_element(23)
        self.test_tree.insert_element(27)
        self.test_tree.insert_element(29)
        self.test_tree.insert_element(30)
        self.test_tree.insert_element(18)
        self.test_tree.insert_element(17)
        self.test_tree.insert_element(16)
        self.test_tree.insert_element(26)
        self.test_tree.remove_element(27)
        self.test_tree.remove_element(26)
        self.test_tree.remove_element(29)
        self.test_tree.remove_element(25)
        self.assertEqual('[ 16, 17, 18, 20, 23, 30 ]', str(self.test_tree), 'In-order traversal should be "[ 16, 17, 18, 20, 23, 30 ]"')

    def test_height_remove3_complicated_avl_str(self):
        self.test_tree.insert_element(20)
        self.test_tree.insert_element(25)
        self.test_tree.insert_element(23)
        self.test_tree.insert_element(27)
        self.test_tree.insert_element(29)
        self.test_tree.insert_element(30)
        self.test_tree.insert_element(18)
        self.test_tree.insert_element(17)
        self.test_tree.insert_element(16)
        self.test_tree.insert_element(26)
        self.test_tree.remove_element(27)
        self.test_tree.remove_element(26)
        self.test_tree.remove_element(29)
        self.test_tree.remove_element(25)
        self.assertEqual(3, self.test_tree.get_height(), 'Height is now 3')


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