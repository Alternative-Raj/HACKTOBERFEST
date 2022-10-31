import utils
import settings
from tkinter import *
from cell import *
root= Tk()
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False,False)

top_frame= Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=utils.height_prct(25)
    )
top_frame.place(x=0,y=0)
left_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
game_title = Label(
    top_frame,
    bg="black",
    fg="white",
    text="Minesweeper",
    font=("",48)
)
game_title.place(x=utils.width_prct(35),y=0)
left_frame.place(x=0,y=utils.height_prct(25))
center_frame= Frame(
    root,
    bg="black",
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(x=utils.width_prct(25),y=utils.height_prct(25))
for x in range(settings.GRID_ROW):
    for y in range(settings.GRID_COLUMN):
        c1 = Cell(x,y)
        c1.create_btn(center_frame)
        c1.btn_obj.grid(row=x,column=y)
Cell.create_cell_cnt_label(left_frame)
Cell.cell_cnt_label_obj.place(
    x=0, y=0
)
Cell.randomize_mines()


root.mainloop()
