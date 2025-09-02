import tkinter
root = tkinter.Tk()
root.title("ウィンドウ")

WINDOW_SIZE = 400

canvas = tkinter.Canvas(width=WINDOW_SIZE, height=WINDOW_SIZE/2, bg="pink")
canvas.create_text(WINDOW_SIZE/2, WINDOW_SIZE/4, text="Python", font=("Times New Roman", 40))
canvas.pack()
root.mainloop()
