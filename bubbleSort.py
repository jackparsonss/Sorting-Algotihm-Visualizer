import time

def bubbleSort(data, draw, speed):
   is_sorted = False
   last_unsorted = len(data)-1

   while not is_sorted:
      is_sorted = True
      for i in range(last_unsorted):
         if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i] # perfrom swap
            draw(data, ['#2EC4B6' if x == i or x == i+1 else '#EDF2F4' for x in range(len(data))]) # highlight the two selected bars
            time.sleep(speed)
            is_sorted = False
      last_unsorted -= 1
