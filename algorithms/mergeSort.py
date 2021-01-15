import time

def mergeSort(data, draw, speed):
   """ An algorithm which repeatedly cuts the data in half until they reach a size of two and then sort and merge each list until data is sorted
   :param data: The data being sorted
   :type data: List[int]
   :param draw: The function which draws the algorithm onto the screen
   :type draw: function
   :param speed: The rate at which the user sees the data being sorted
   :type speed: float
   """
   _mergeSort(data,0, len(data)-1, draw, speed)


def _mergeSort(data, left, right, draw, speed):
   """ The recursive function for merge sort
   :param data: The data being sorted
   :type data: List[int]
   :param left: The left halve of data being sorted
   :type left: int
   :param right: The right halve of data being sorted
   :type right: int
   :param draw: The function which draws the algorithm onto the screen
   :type draw: function
   :param speed: The rate at which the user sees the data being sorted
   :type speed: float
   """
   if left < right:
      middle = (left + right) // 2
      _mergeSort(data, left, middle, draw, speed)
      _mergeSort(data, middle+1, right, draw, speed)
      merge(data, left, middle, right, draw, speed)

def merge(data, left, middle, right, draw, speed):
   """ Takes the left and right index's and merge the two halves of data into one sorted list
   :param data: The data being sorted
   :type data: List[int]
   :param left: The left halve of data being sorted
   :type left: int
   :param middle: The middle index between the left and right sides
   :type middle: int
   :param right: The right halve of data being sorted
   :type right: int
   :param draw: The function which draws the algorithm onto the screen
   :type draw: function
   :param speed: The rate at which the user sees the data being sorted
   :type speed: float
   """
   draw(data, ["#2EC4B6" if x >= left and x <= right else "#EDF2F4" for x in range(len(data))])
   time.sleep(speed)

   left_partition = data[left:middle+1]
   right_partition = data[middle+1: right+1]

   left_index = right_index = 0

   for index in range(left, right+1):
      if left_index < len(left_partition) and right_index < len(right_partition):
         if left_partition[left_index] <= right_partition[right_index]:
               data[index] = left_partition[left_index]
               left_index += 1
         else:
               data[index] = right_partition[right_index]
               right_index += 1
      
      elif left_index < len(left_partition):
         data[index] = left_partition[left_index]
         left_index += 1
      else:
         data[index] = right_partition[right_index]
         right_index += 1
   
   draw(data, ["#2EC4B6" if x >= left and x <= right else "#EDF2F4" for x in range(len(data))])
   time.sleep(speed)
