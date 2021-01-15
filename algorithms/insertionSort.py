import time

def insertionSort(data, draw, speed):
   """ An algorithm which starts at the first index and goes through each item one at a time sorting it accordingly
   :param data: The data being sorted
   :type data: List[int]
   :param draw: The function which draws the algorithm onto the screen
   :type draw: function
   :param speed: The rate at which the user sees the data being sorted
   :type speed: float
   """
   for i in range(1, len(data)):
      current = data[i]
      j = i - 1
      while j >= 0 and data[j] > current:
         data[j+1] = data[j]
         draw(data, ['#2EC4B6' if x == j or x == j+1 else '#EDF2F4' for x in range(len(data))])
         time.sleep(speed)
         j -= 1
      data[j+1] = current
