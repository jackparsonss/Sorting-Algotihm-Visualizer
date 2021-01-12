import time

def selectionSort(data, draw, speed):
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
