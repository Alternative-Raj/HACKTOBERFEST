from tkinter import Label
from tkinter import Button, EventType
from settings import *
import random
import settings
import ctypes
import sys

class Cell:
    all= []
    c_count= settings.CEll_COUNT
    cell_cnt_label_obj=None
    def __init__(self, x, y, is_mine=False):
        self.is_mine= is_mine
        self.btn_obj=None
        self.x= x
        self.y= y
        self.is_open=False
        self.is_marked=False
        Cell.all.append(self)

    def create_btn(self, location):
        btn= Button(
            location,
            bg="grey",
            width= int(settings.WIDTH/120),
            height= int(settings.HEIGHT/180),
            
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.btn_obj=btn
    
    def left_click_actions(self,event):
        if(self.is_mine):
            self.btn_obj.configure(bg= "red")
            self.show_mine()
        else:
            if not self.is_open: 
                if self.surround_mines_length==0:
                    for i in self.surround_cells:
                        if not i.is_open:
                            i.show_cell()
                            if i.surround_mines_length==0:
                                for j in i.surround_cells:
                                    if not j.is_open:
                                        j.show_cell()
                                        if j.surround_mines_length==0:
                                            for k in j.surround_cells:
                                                if not k.is_open:
                                                    k.show_cell()
                self.show_cell()
                if Cell.c_count==settings.MINE_COUNT:
                    ctypes.windll.user32.MessageBoxW(0,"Congratulations! You Won The Game", "Game Over", 0)
                    sys.exit()

    
    def get_cell_by_axes(self,x,y):
        for cell in Cell.all:
            if cell.x==x and cell.y==y:
                return cell
    def show_cell(self):
        if not self.is_open:
            self.btn_obj.configure(
                text=f"{self.surround_mines_length}",
                bg="white"
                )
            self.btn_obj.unbind("<Button-1>")
            self.btn_obj.unbind("<Button-3>")
            if not self.is_marked:        
                Cell.c_count-=1
            self.is_open=True
            if Cell.cell_cnt_label_obj:
                Cell.cell_cnt_label_obj.configure(
                text=f"Cells left: {Cell.c_count}"
                )

    @staticmethod
    def create_cell_cnt_label(location):
        lbl= Label(
            location,
            text=f"Cells left: {Cell.c_count}",
            width= int(settings.WIDTH/120),
            height= int(settings.HEIGHT/180),
            font=("", 30),
            bg="black",
            fg="white"

        )
        Cell.cell_cnt_label_obj = lbl
        return lbl


    @property
    def surround_cells(self):        
        cell_list =[]
        for i in range((self.x)-1,(self.x)+2):
            for j in range((self.y)-1,(self.y)+2):
                if i>=0 and j>=0 and i<(settings.GRID_ROW) and j<(settings.GRID_COLUMN):
                    cell_list.append(self.get_cell_by_axes(i,j))
        return cell_list
        
    @property
    def surround_mines_length(self):
        count=0
        for i in self.surround_cells:
            if i.is_mine:
                count+=1
        return count



    def show_mine(self):
        
        ctypes.windll.user32.MessageBoxW(0,"You Clicked on a Mine", "Game Over", 0)
        sys.exit()
        
    
    def right_click_actions(self,event):
        if not self.is_open:
            if self.is_marked:
                self.btn_obj.configure(bg="grey")                
                self.is_marked= False
            else:
                self.btn_obj.configure(bg="orange")
                self.is_marked= True

    @staticmethod
    def randomize_mines():
        mine_cells = random.sample(Cell.all,MINE_COUNT)
        for i in mine_cells:
            i.is_mine=True



    def __repr__(self):
        return f"Cell({self.x},{self.y})"