import time

def selectionSort(data, draw, speed):
   """ An algorithm which repeatedly selects the next-smallest element and swaps it into place accordingly
   :param data: The data being sorted
   :type data: List[int]
   :param draw: The function which draws the algorithm onto the screen
   :type draw: function
   :param speed: The rate at which the user sees the data being sorted
   :type speed: float
   """
   for i in range(len(data)):
      min_index = i
      for j in range(i+1, len(data)):
         if data[j] < data[min_index]:
            min_index = j

      draw(data, ['#2EC4B6' if x == i or x == min_index else '#EDF2F4' for x in range(len(data))])
      time.sleep(speed)
      data[i], data[min_index] = data[min_index], data[i]
      draw(data, ['#2EC4B6' if x == i or x == min_index else '#EDF2F4' for x in range(len(data))])
      time.sleep(speed)
