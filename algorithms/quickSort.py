import time

def quickSort(data, draw, speed):
   _quickSort(data, 0, len(data)-1, draw, speed)

def _quickSort(data, left, right, draw, speed):
   # Recursive function
   if left >= right:
      return
   pivot = data[(left + right)//2] # Pivot element is the center

   index = partition(data, left, right, pivot, draw, speed)

   _quickSort(data, left, index-1, draw, speed) # Left side
   _quickSort(data, index, right, draw, speed) # Right side

def partition(data, left, right, pivot, draw, speed):
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

