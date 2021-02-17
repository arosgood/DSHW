import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

############DEQUE TESTING#################
  def test_print_empty_deque(self):
    self.assertEqual('[ ]', str(self.__deque), 'Empty list should print as "[ ]"')

  def test_push_front_deque(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual('[ 2, 1 ]', str(self.__deque))

  def test_push_back_deque(self):
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.assertEqual('[ 1, 2 ]', str(self.__deque))

  def test_peek_front_deque(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.assertEqual(3, self.__deque.peek_front())

  def test_peek_empty_front_deque(self):
    self.assertEqual(None, self.__deque.peek_front())

  def test_peek_back_deque(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.assertEqual(1, self.__deque.peek_back())

  def test_peek_empty_back_deque(self):
    self.assertEqual(None, self.__deque.peek_back())
  
  def test_pop_front_deque(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.assertEqual(3, self.__deque.pop_front())

  def test_pop_back_deque(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.assertEqual(1, self.__deque.pop_back())

  def test_pop_empty_front_deque(self):
    self.assertEqual(None, self.__deque.pop_front())

  def test_pop_empty_back_deque(self):
    self.assertEqual(None, self.__deque.pop_back())

  def test_deque_grow(self):
    self.__deque.push_front(1)
    self.assertEqual('[ 1 ]', str(self.__deque))
  
  def test_deque_grow_2(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual('[ 2, 1 ]', str(self.__deque))

  def test_deque_grow_3(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.assertEqual('[ 3, 2, 1 ]', str(self.__deque))

  def test_deque_grow_4(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.__deque.push_front(4)
    self.assertEqual('[ 4, 3, 2, 1 ]', str(self.__deque))

  def test_nothing_goes_wrong_deque(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.__deque.push_front(4)
    self.__deque.peek_back()
    self.assertEqual('[ 4, 3, 2, 1 ]', str(self.__deque))

  def test_nothing_goes_wrong_deque2(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.__deque.push_front(4)
    self.__deque.peek_front()
    self.assertEqual('[ 4, 3, 2, 1 ]', str(self.__deque))

  def test_nothing_goes_wrong_deque3(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.__deque.push_front(4)
    self.__deque.peek_back()
    self.assertEqual(4, len(self.__deque))

  def test_nothing_goes_wrong_deque4(self):
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.push_front(3)
    self.__deque.push_front(4)
    self.__deque.peek_front()
    self.assertEqual(4, len(self.__deque))
########################################
########################################

#####################QUEUE TESTING#####################
  def test_str_empty_queue(self):
    self.assertEqual('[ ]', str(self.__queue))

  def test_len_empty_queue(self):
    self.assertEqual(0, len(self.__queue))

  def test_en_queue_str(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.enqueue(3)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__queue))

  def test_en_queue_len(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.enqueue(3)
    self.assertEqual(3, len(self.__queue))

  def test_de_queue_str(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.enqueue(3)
    self.__queue.dequeue()
    self.assertEqual('[ 2, 3 ]', str(self.__queue))

  def test_de_queue_len(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.enqueue(3)
    self.__queue.dequeue()
    self.assertEqual(2, len(self.__queue))

  def test_de_queue_empty(self):
    self.assertEqual(None, self.__queue.dequeue())

########################################
########################################

#####################STACK TESTING#####################

  def test_empty_stack_print(self):
    self.assertEqual('[ ]', str(self.__stack))

  def test_empty_stack_pop(self):
    self.assertEqual(None, self.__stack.pop())

  def test_empty_stack_len(self):
    self.assertEqual(0, len(self.__stack))

  def test_stack_push(self):
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__stack))

  def test_stack_push_len(self):
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.assertEqual(3, len(self.__stack))

  def test_stack_pop(self):
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.__stack.pop()
    self.assertEqual('[ 2, 3 ]', str(self.__stack))

  def test_stack_pop_val(self):
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.assertEqual(1, self.__stack.pop())

  def test_stack_pop_len(self):
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.__stack.pop()
    self.assertEqual(2, len(self.__stack))

  def test_stack_str(self):
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.__stack.push(0)
    self.assertEqual('[ 0, 1, 2, 3 ]', str(self.__stack))

  def test_stack_str2(self):
    self.__stack.push(4)
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.__stack.push(0)
    self.assertEqual('[ 0, 1, 2, 3, 4 ]', str(self.__stack))

  def test_stack_pop2(self):
    self.__stack.push(4)
    self.__stack.push(3)
    self.__stack.push(2)
    self.__stack.push(1)
    self.__stack.push(0)
    self.assertEqual(0, self.__stack.pop())

if __name__ == '__main__':
  unittest.main()

