import tkinter
root = tkinter.Tk()
root.title("カラー")

WINDOW_SIZE = 400

canvas = tkinter.Canvas(width=WINDOW_SIZE/5*3, height=WINDOW_SIZE, bg="black")

COLOR = [
    "maroon", "brown", "red", "orange",
    "gold", "yellow", "lime", "limegreen",
    "green", "skyblue", "cyan", "blue",
    "navy", "indigo", "purple", "magenta",
    "white", "lightgray", "silver", "gray",
    "olive", "pink"
]
count = len(COLOR)

FONT = ("Times New Roman", WINDOW_SIZE // count)

rows = count // 2
step = WINDOW_SIZE // (rows + 1)
column = WINDOW_SIZE // 5

x = column
y = step

for c in COLOR:
    canvas.create_text(x, y, text=c, fill=c, font=FONT)
    y += step
    if y >= rows * step + step:
        y = step
        x += column

canvas.pack()
root.mainloop()
