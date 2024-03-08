import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


def render_function():
    function = function_entry.get()
    function = function.replace("^", "**")
    start_x = int(start_x_entry.get())
    end_x = int(end_x_entry.get())
    start_y = int(start_y_entry.get())
    end_y = int(end_y_entry.get())

    x = np.linspace(start_x, end_x, 1000)
    y = eval(function.replace("x", "x"))

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph of f(x) = {}'.format(function))
    plt.xlim(start_x, end_x)
    plt.ylim(start_y, end_y)
    plt.grid(True)
    plt.show()


app = tk.Tk()
app.title("Function Renderer")

function_label = tk.Label(app, text="Enter the function f(x): ")
function_label.grid(row=0, column=0)
function_entry = tk.Entry(app)
function_entry.grid(row=0, column=1)

start_x_label = tk.Label(app, text="Enter the start number for x-axis: ")
start_x_label.grid(row=1, column=0)
start_x_entry = tk.Entry(app)
start_x_entry.grid(row=1, column=1)

end_x_label = tk.Label(app, text="Enter the end number for x-axis: ")
end_x_label.grid(row=2, column=0)
end_x_entry = tk.Entry(app)
end_x_entry.grid(row=2, column=1)

start_y_label = tk.Label(app, text="Enter the start number for y-axis: ")
start_y_label.grid(row=3, column=0)
start_y_entry = tk.Entry(app)
start_y_entry.grid(row=3, column=1)

end_y_label = tk.Label(app, text="Enter the end number for y-axis: ")
end_y_label.grid(row=4, column=0)
end_y_entry = tk.Entry(app)
end_y_entry.grid(row=4, column=1)

render_button = tk.Button(app, text="Render Function", command=render_function)
render_button.grid(row=5, columnspan=2)

app.mainloop()

