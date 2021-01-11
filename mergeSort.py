import time

def mergeSort(data, draw, speed):
   _mergeSort(data,0, len(data)-1, draw, speed)


def _mergeSort(data, left, right, draw, speed):
   if left < right:
      middle = (left + right) // 2
      _mergeSort(data, left, middle, draw, speed)
      _mergeSort(data, middle+1, right, draw, speed)
      merge(data, left, middle, right, draw, speed)

def merge(data, left, middle, right, draw, speed):
   draw(data, colorArray(len(data), left, middle, right))
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

def colorArray(length, left, middle, right):
   colorArray = []

   for i in range(length):
      if i >= left and i <= right:
         if i >= left and i <= middle:
               colorArray.append("#FF9F1C")
         else:
               colorArray.append("#EE6C4D")
      else:
         colorArray.append("#EDF2F4")

   return colorArray
