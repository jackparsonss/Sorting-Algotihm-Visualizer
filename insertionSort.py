import time

def insertionSort(data, draw, speed):
   for i in range(1, len(data)):
      current = data[i]
      j = i - 1
      while j >= 0 and data[j] > current:
         data[j+1] = data[j]
         draw(data, ['#2EC4B6' if x == j or x == j+1 else '#EDF2F4' for x in range(len(data))])
         time.sleep(speed)
         j -= 1
      data[j+1] = current
