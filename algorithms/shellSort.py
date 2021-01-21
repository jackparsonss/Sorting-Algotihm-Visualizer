import time

def shellSort(data, draw, speed):
   # The distance between each value being compared
   gap = len(data) // 2

   while gap != 0:
      current = gap

      while current < (len(data)):
         temp = data[current]
         i = current - gap

         while i >= 0 and temp < data[i]:
            data[i + gap] = data[i]
            draw(data, ['#2EC4B6' if x == i + gap  or x == i else '#EDF2F4' for x in range(len(data))])
            time.sleep(speed)
            i -= gap

         data[i + gap] = temp
         current += 1

      gap //= 2