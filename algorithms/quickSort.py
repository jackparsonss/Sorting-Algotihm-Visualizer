import time

def quick_sort(data, draw, speed):
   """ An algorithm which creates a pivot point and sorts data based on whether the selected value is greater or less than the pivot
   :param data: The data being sorted
   :type data: List[int]
   :param draw: The function which draws the algorithm onto the screen
   :type draw: function
   :param speed: The rate at which the user sees the data being sorted
   :type speed: float
   """
   _quick_sort(data, 0, len(data)-1, draw, speed)

def _quick_sort(data, left, right, draw, speed):
   """ The recursive function for quick sort
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
   if left >= right:
      return
   pivot = data[(left + right)//2] # Pivot element is the center

   index = partition(data, left, right, pivot, draw, speed)

   _quick_sort(data, left, index-1, draw, speed) # Left side
   _quick_sort(data, index, right, draw, speed) # Right side

def partition(data, left, right, pivot, draw, speed):
   """ This is the function that compares to halves and sorts each value around the pivot respectively
   :param data: The data being sorted
   :type data: List[int]
   :param left: The left halve of data being sorted
   :type left: int
   :param right: The right halve of data being sorted
   :type right: int
   :param pivot: The pivot point at which each value is being compared to
   :type pivot: int
   :param draw: The function which draws the algorithm onto the screen
   :type draw: function
   :param speed: The rate at which the user sees the data being sorted
   :type speed: float
   """
   while left <= right:
      while data[left] < pivot:
         # Move left index towards pivot
         left += 1
      while data[right] > pivot:
         # Move right index towards pivot
         right -= 1

      if left <= right:
         draw(data, ['#2EC4B6' if x == left or x == right else '#EDF2F4' for x in range(len(data))])
         time.sleep(speed)
         data[left], data[right] = data[right], data[left] # Swaps elements
         left += 1
         right -= 1

   return left # The dividing index between the left and right side

