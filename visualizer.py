# Color Schemes: 
# https://coolors.co/011627-fdff_quick_sorte71d36-ff9f1c
# https://coolors.co/3d5a80-98c1d9-e0fbfc-ee6c4d-293241
# https://coolors.co/2b2d42-8d99ae-edf2f4-ef233c-d90429

import random
from tkinter import *
from tkinter import ttk
from algorithms.bubbleSort import bubbleSort
from algorithms.insertionSort import insertionSort
from algorithms.mergeSort import mergeSort
from algorithms.quickSort import quick_sort
from algorithms.selectionSort import selectionSort
from algorithms.shellSort import shellSort

def initialize():
   """ Creates a window through tkinter and sets its name, size and color
   
   :returns: the root component of the window
   :rtype: Tk
   """
   root = Tk()
   root.title("Sorting Algorithm Visualizer")
   root.geometry("1280x900")
   root.resizable(0, 0)
   root.config(bg='#2C2F33')

   return root

def main():
   """ 
   The applications main function which instantiates the app class and runs it until user exits out 
   """
   root = initialize()

   app = App(root)
   app.start()

   root.mainloop()

class App:
   def __init__(self, root):
      """ Initializes the data structures, the areas of where the app divides and key widgets

      :param root: the root widget of the window
      :type root: Tk
      
      """
      #-----DATA-----#
      self.root = root
      self.data = []
      self.algorithms = ['Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Selection Sort', 'Shell Sort']
      self.selected_alg = StringVar()

      #-----BORDERS-----#
      self.UI_frame_right = Frame(root, width=630, height=200, bg='#8D99AE', padx=20, pady=15) # TOP LEFT
      self.UI_frame_left = Frame(root, width=630, height=200, bg='#8D99AE', padx=20, pady=20) # TOP RIGHT
      self.canvas = Canvas(root, width=1260, height=760, bg='#8D99AE', highlightthickness=0) # BOTTOM

      #-----WIDGETS-----#
      self.algorithm_menu = ttk.Combobox(self.UI_frame_left, textvariable=self.selected_alg, values=self.algorithms, width=31)
      self.speed_scale = Scale(self.UI_frame_right, from_=0.01, to=1.0, length=170, digits=3, resolution=0.01, orient=HORIZONTAL, label='Speed (Lower is Faster)')
      self.size_entry = Scale(self.UI_frame_right, from_=3, to=50, length=170, resolution=1, orient=HORIZONTAL, label='Size', command=self.generate_data)

      self.algorithm_functions = {'Bubble Sort': lambda:bubbleSort(self.data, self.draw, self.speed_scale.get()),
                                  'Insertion Sort': lambda:insertionSort(self.data, self.draw, self.speed_scale.get()),
                                  'Merge Sort': lambda:mergeSort(self.data, self.draw, self.speed_scale.get()),
                                  'Quick Sort': lambda:quick_sort(self.data, self.draw, self.speed_scale.get()),
                                  'Selection Sort': lambda:selectionSort(self.data, self.draw, self.speed_scale.get()),
                                  'Shell Sort': lambda:shellSort(self.data, self.draw, self.speed_scale.get())}
      
   def start(self):
      """ 
      Places everything on the screen 
      """
      self.generate_data() # Display data when app starts

      self.create_top_left()
      self.create_top_right()
      
      #-----BOTTOM-----#
      self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

   def create_top_left(self):
      """
      Creates and places everything located at the top left of the screen, this is where user selects and runs algorithm
      """
      #-----ALGORITHM ROW-----#
      self.UI_frame_left.grid(row=0, column=0, padx=10, pady=10)
      Label(self.UI_frame_left, text="Algorithm: ", bg='#8D99AE', font="Arial", borderwidth=10).grid(row=0, column=0, padx=5, pady=5, sticky=W)
      self.algorithm_menu.grid(row=0, column=1, padx=5, pady=5)
      self.algorithm_menu.current(0)
      Button(self.UI_frame_left, text="Start Algorithm", command=self.start_algorithm, bg='#EE6C4D', pady=10).grid(row=0, column=2, padx=5, pady=5)

   def create_top_right(self):
      """
      Creates and places everything located at the top left of the screen, this is where the user generates the data to be sorted
      """
      #-----DATA ROW-----#
      self.UI_frame_right.grid(row=0, column=1, padx=10, pady=10)
      Label(self.UI_frame_right, text="Data: ", bg='#8D99AE', font="Arial").grid(row=0, column=0, pady=5)
      self.speed_scale.grid(row=0, column=2, columnspan=2, padx=5, pady=5)
      self.size_entry.grid(row=0, column=1, padx=5, pady=5)
      Button(self.UI_frame_right, text="New Data", command=self.generate_data, bg='#EE6C4D',padx=15, pady=10).grid(row=0, column=4, padx=5, pady=5)

   def draw(self, data, color_array):
      """ Takes in data to be drawn onto the screen in the form of rectangles with their respective value on top

      :param data: The data to be drawn onto the screen
      :type data: List[int]
      :param color_array: a list of colors for the data to be drawn as, this helps the visualization
      :type color_array: List[str]
      """
      self.canvas.delete('all')
      bar_height = 760
      bar_width = 1240
      x_width = bar_width / (len(data)+1)
      offset = x_width // 2
      space_between = 5

      normalize_data = [i / max(data) for i in data] # divides every element by the highest to make the graph more evenly distributed

      for i, height in enumerate(normalize_data): # Draw rectangles on screen
         # Top left of rectangle
         x_top = i * x_width + offset + space_between
         y_top = bar_height - height * 700

         # Bottom right of rectange
         x_bottom = (i+1) * x_width + offset
         y_bottom = bar_height

         self.canvas.create_rectangle(x_top, y_top, x_bottom, y_bottom, fill=color_array[i]) # Every bar of the data
         self.canvas.create_text(x_top+2, y_top, anchor=SW, text=str(data[i])) # Adds number on top of each bar

      self.root.update_idletasks() # Update screen

   def start_algorithm(self):
      """
      Based on which algorithm user selects, find it in the algorithm_functions dictonary and run the algorithm, then color the data red
      """
      self.algorithm_functions[self.algorithm_menu.get()]() # Call algorithm based on chosen algorithm from dropdown menu
      self.draw(self.data, ['#E71D36' for x in range(len(self.data))]) # Change color when algorithm completes

   def generate_data(self, input=0):
      """ Gets the size of data the user selects and generates an array with the data and then draw it onto the screen
      :param input: an empty parameter which is passed on through the size slider, this prevents the app from crashing
      :type input: int
      (default is 0)
      """
      self.data = []
      for _ in range(self.size_entry.get()):
         self.data.append(random.randint(1, 100))
      self.draw(self.data, ['#EDF2F4' for x in range(len(self.data))]) # Draw data on screen


main()