import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x600")
        self.master.title("My App")

        # Left counter
        self.left_counter = tk.Label(self.master, text="Left", font=("Arial", 16), width=6, anchor=tk.E)
        self.left_counter.grid(row=0, column=0, padx=5, pady=5)

        # Middle button
        self.middle_button = tk.Button(self.master, text="Button", font=("Arial", 16))
        self.middle_button.grid(row=0, column=1, padx=5, pady=5)

        # Right counter
        self.right_counter = tk.Label(self.master, text="Right", font=("Arial", 16), width=6, anchor=tk.E)
        self.right_counter.grid(row=0, column=2, padx=5, pady=5)

        # Initialize grid
        self.rows = 16
        self.columns = 16
        self.grid = [[None for _ in range(self.columns)] for _ in range(self.rows)]
        self.create_grid()

    def create_grid(self):
        self.grid_frame = tk.Frame(self.master)
        self.grid_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        for row in range(self.rows):
            for col in range(self.columns):
                cell = tk.Button(self.grid_frame, width=2, height=1, bg="gray", relief=tk.SUNKEN)
                cell.grid(row=row, column=col)
                cell.bind("<Button-1>", lambda e, row=row, col=col: self.left_click(row, col))
                cell.bind("<Button-3>", lambda e, row=row, col=col: self.right_click(row, col))
                self.grid[row][col] = {
                    "button": cell,
                    "mine": False,
                    "flag": False,
                    "revealed": False,
                    "value": 0
                }

    def left_click(self, row, col):
        cell = self.grid[row][col]
        if not cell["flag"]:
            cell["revealed"] = True
            cell["button"].config(text=cell["value"])

    def right_click(self, row, col):
        cell = self.grid[row][col]
        if not cell["revealed"]:
            cell["flag"] = not cell["flag"]
            if cell["flag"]:
                cell["button"].config(text="🚩")
            else:
                cell["button"].config(text="")

root = tk.Tk()
app = App(root)
root.mainloop()
