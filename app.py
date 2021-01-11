# Color Scheme: https://coolors.co/011627-fdfffc-2ec4b6-e71d36-ff9f1c
# https://coolors.co/3d5a80-98c1d9-e0fbfc-ee6c4d-293241
# https://coolors.co/2b2d42-8d99ae-edf2f4-ef233c-d90429

from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubbleSort
from insertionSort import insertionSort
from mergeSort import mergeSort
from quickSort import quickSort
from selectionSort import selectionSort

def initialize():
   root = Tk()
   root.title("Sorting Algorithm Visualizer")
   root.geometry("1280x900")
   root.resizable(0, 0)
   root.config(bg='#2C2F33')

   return root

def main():
   root = initialize()

   app = App(root)
   app.start()

   root.mainloop()

class App:
   def __init__(self, root):
      #-----DATA-----#
      self.root = root
      self.data = []
      self.algorithms = ['Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Selection Sort']
      self.selected_alg = StringVar()

      #-----BORDERS-----#
      self.UI_frame_right = Frame(root, width=630, height=200, bg='#8D99AE', padx=20, pady=15) # TOP LEFT
      self.UI_frame_left = Frame(root, width=630, height=200, bg='#8D99AE', padx=20, pady=20) # TOP RIGHT
      self.canvas = Canvas(root, width=1260, height=760, bg='#8D99AE', highlightthickness=0) # BOTTOM

      #-----WIDGETS-----#
      self.algorithm_menu = ttk.Combobox(self.UI_frame_left, textvariable=self.selected_alg, values=self.algorithms, width=31)
      self.speed_scale = Scale(self.UI_frame_right, from_=0.01, to=1.0, length=170, digits=3, resolution=0.01, orient=HORIZONTAL, label='Speed (Lower is Faster)')
      self.size_entry = Scale(self.UI_frame_right, from_=3, to=50, length=170, resolution=1, orient=HORIZONTAL, label='Size', command=self.generate)

      self.algorithm_functions = {'Merge Sort': lambda:mergeSort(self.data, self.draw, self.speed_scale.get())}
      
   def start(self):
      self.generate() # Display data when app starts

      self.create_top_left()
      self.create_top_right()
      
      #-----BOTTOM-----#
      self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

   def create_top_left(self):
      #-----ALGORITHM ROW-----#
      self.UI_frame_left.grid(row=0, column=0, padx=10, pady=10)
      Label(self.UI_frame_left, text="Algorithm: ", bg='#8D99AE', font="Arial", borderwidth=10).grid(row=0, column=0, padx=5, pady=5, sticky=W)
      self.algorithm_menu.grid(row=0, column=1, padx=5, pady=5)
      self.algorithm_menu.current(0)
      Button(self.UI_frame_left, text="Start Algorithm", command=self.startAlgorithm, bg='#EE6C4D', pady=10).grid(row=0, column=2, padx=5, pady=5)

   def create_top_right(self):
      #-----DATA ROW-----#
      self.UI_frame_right.grid(row=0, column=1, padx=10, pady=10)
      Label(self.UI_frame_right, text="Data: ", bg='#8D99AE', font="Arial").grid(row=0, column=0, pady=5)
      self.speed_scale.grid(row=0, column=2, columnspan=2, padx=5, pady=5)
      self.size_entry.grid(row=0, column=1, padx=5, pady=5)
      Button(self.UI_frame_right, text="New Data", command=self.generate, bg='#EE6C4D',padx=15, pady=10).grid(row=0, column=4, padx=5, pady=5)

   def draw(self, data, color_array):
      self.canvas.delete('all')
      bar_height = 760
      bar_width = 1240
      x_width = bar_width / (len(data)+1)
      offset = x_width // 2
      space_between = 5

      normalize_data = [i / max(data) for i in data] # divides every element by the highest to make the graph more evenly distributed

      for i, height in enumerate(normalize_data):
         # Top left of rectangle
         x_top = i * x_width + offset + space_between
         y_top = bar_height - height * 700

         # Bottom right of rectange
         x_bottom = (i+1) * x_width + offset
         y_bottom = bar_height

         self.canvas.create_rectangle(x_top, y_top, x_bottom, y_bottom, fill=color_array[i]) # Every bar of the data
         self.canvas.create_text(x_top+2, y_top, anchor=SW, text=str(data[i])) # Adds number on top of each bar

      self.root.update_idletasks() # Update screen

   def startAlgorithm(self):
      self.algorithm_functions[self.algorithm_menu.get()]()
      self.draw(self.data, ['#E71D36' for x in range(len(self.data))])   

   def generate(self, input=None):
      # Generates random data
      self.data = []
      for _ in range(self.size_entry.get()):
         self.data.append(random.randint(1, 100))
      self.draw(self.data, ['#EDF2F4' for x in range(len(self.data))]) # Draw data on screen


main()