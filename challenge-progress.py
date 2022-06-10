from cmath import e
import sys
from tkinter import CENTER, DoubleVar, Label, StringVar
from turtle import distance
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk


#basic setting for the Program
fonsize = 350
distance_total = 1378.50
distance_per_round = 0.75
distance_elapsed = 0.0
distance_remaining = distance_total - distance_elapsed
rounds_counted = distance_elapsed / distance_per_round

#set up the window
root=tk.Tk()
root.title('UA Running Challenge 2022')

dblDistanceElapsed = DoubleVar()
dblDistanceElapsed.set(distance_elapsed)
dblDistanceRemaining = DoubleVar()
dblDistanceRemaining.set(distance_remaining)
l_distance_elapsed = Label(root, justify=CENTER, compound=CENTER, textvariable=dblDistanceElapsed, bg="blue", fg="white", font=("Arial", fonsize))
l_distance_elapsed.pack(expand=1, fill="both")
l_distance_remaining = Label(root, justify=CENTER, compound=CENTER, textvariable=dblDistanceRemaining, bg="yellow", fg="white", font=("Arial", fonsize))
l_distance_remaining.pack(expand=1, fill="both")


def calculate_distances(event):
    global distance_elapsed, distance_remaining, rounds_counted
    global dblDistanceElapsed, dblDistanceRemaining
    rounds_counted += 1
    distance_elapsed = rounds_counted * distance_per_round
    distance_remaining = distance_total - distance_elapsed
    dblDistanceElapsed.set(round(distance_elapsed, 1))
    dblDistanceRemaining.set(round(distance_remaining, 1))
    

#binding the SPACE keypress event to the function
root.bind('<space>', calculate_distances)

#start the event loop
root.mainloop()