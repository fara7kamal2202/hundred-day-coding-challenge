from tic_tac_toe import TicTacToe
from time import sleep
import tkinter as tk

xo_matrix = TicTacToe()
root = tk.Tk()
root.title("TicTacToe")

xo_frame = tk.Frame(root)
xo_frame.config(padx=10, pady=10)

mat_0_0 = tk.Button(xo_frame)
mat_0_0.grid(row=0, column=0)
mat_0_0.config(height=3, width=8, padx=5, pady=5)
mat_0_0.bind("<Button-1>", xo_matrix.play)

mat_0_1 = tk.Button(xo_frame)
mat_0_1.grid(row=0, column=1)
mat_0_1.config(height=3, width=8, padx=5, pady=5)
mat_0_1.bind("<Button-1>", xo_matrix.play)

mat_0_2 = tk.Button(xo_frame)
mat_0_2.grid(row=0, column=2)
mat_0_2.config(height=3, width=8, padx=5, pady=5)
mat_0_2.bind("<Button-1>", xo_matrix.play)

mat_1_0 = tk.Button(xo_frame)
mat_1_0.grid(row=1, column=0)
mat_1_0.config(height=3, width=8, padx=5, pady=5)
mat_1_0.bind("<Button-1>", xo_matrix.play)

mat_1_1 = tk.Button(xo_frame)
mat_1_1.grid(row=1, column=1)
mat_1_1.config(height=3, width=8, padx=5, pady=5)
mat_1_1.bind("<Button-1>", xo_matrix.play)

mat_1_2 = tk.Button(xo_frame)
mat_1_2.grid(row=1, column=2)
mat_1_2.config(height=3, width=8, padx=5, pady=5)
mat_1_2.bind("<Button-1>", xo_matrix.play)

mat_2_0 = tk.Button(xo_frame)
mat_2_0.grid(row=2, column=0)
mat_2_0.config(height=3, width=8, padx=5, pady=5)
mat_2_0.bind("<Button-1>", xo_matrix.play)

mat_2_1 = tk.Button(xo_frame)
mat_2_1.grid(row=2, column=1)
mat_2_1.config(height=3, width=8, padx=5, pady=5)
mat_2_1.bind("<Button-1>", xo_matrix.play)

mat_2_2 = tk.Button(xo_frame)
mat_2_2.grid(row=2, column=2)
mat_2_2.config(height=3, width=8, padx=5, pady=5)
mat_2_2.bind("<Button-1>", xo_matrix.play)


xo_frame.pack()
root.mainloop()

