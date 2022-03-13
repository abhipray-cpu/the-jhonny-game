import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from windows import set_dpi_awareness
from random import *

MOVE_INCREMENT = 5
GAME_SPEED = 100

class mainFrame(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Game');
        self.geometry('1200x800');
        self.resizable(False,False)
        self.direction = "Right"
        self.canvas = tk.Canvas(self,width=1200,height=800)
        self.canvas.grid(row=0,column=0,sticky='nsew')
        self.bind_all("<Key>", self.on_key_press)  # this function will bind all the keys to our canvas
        self.canvas.config(bg='black')
        self.canvas.create_rectangle(10,10,1190,790,outline='white')
        self.count = 0
        self.create_objects()
        self.create_boundaries()
        self.place_enemies()


    def create_objects(self):
        self.jhonyy = Image.open('./jhonny.jfif').resize((35,35))
        self.jhonny_photo = ImageTk.PhotoImage(self.jhonyy)
        self.mia = Image.open('./mia.jfif').resize((45,45))
        self.mia_photo = ImageTk.PhotoImage(self.mia)
        self.player_pos=[30,50]

        self.canvas.create_image(self.player_pos[0],self.player_pos[1],image=self.jhonny_photo,tag='jhony',anchor='nw')
        self.canvas.create_image(630,400,image=self.mia_photo,tag='mia')

    def move_player(self):

        if self.direction == "Left":
            new_head_position = (self.player_pos[0] - MOVE_INCREMENT, self.player_pos[1])
        elif self.direction == "Right":
            new_head_position = (self.player_pos[0] + MOVE_INCREMENT, self.player_pos[1])
        elif self.direction == "Down":
            new_head_position = (self.player_pos[0], self.player_pos[1] + MOVE_INCREMENT)
        elif self.direction == "Up":
            new_head_position = (self.player_pos[0], self.player_pos[1] - MOVE_INCREMENT)
        self.player_pos = new_head_position
        self.canvas.coords(self.canvas.find_withtag('jhony'),self.player_pos)

    def on_key_press(self, e):

        self.count =self.count +1
        new_direction = e.keysym  # event  is provided by python when we bind a key to a widget
        self.direction = new_direction
        self.move_player()
        if self.count % 5 == 0:
            self.alter_boundaries()
            self.move_enemy1()
            self.move_enemy2()
            self.move_enemy3()
            self.move_enemy4()
            self.move_enemy5()
            self.move_enemy6()
            self.check_collison()

        self.check_collison()

    def check_collison(self):
        if self.player_pos[0]>=610 and self.player_pos[0]<=650 and self.player_pos[1]>=380 and self.player_pos[1]<=420:
            self.game_over_captured()
        self.check_enemy_collison()
        self.check_boundary_collison()

    def check_enemy_collison(self):
        x_pos = [self.player_pos[0], self.player_pos[0]+30]
        y_pos = [self.player_pos[1], self.player_pos[1] + 30]
        if self.enemy1_pos[0] in x_pos and self.enemy1_pos[1] in y_pos:
            self.game_over_enemy()
        elif self.enemy2_pos[0] in x_pos and self.enemy2_pos[1] in y_pos:
            self.game_over_enemy()
        elif self.enemy3_pos[0] in x_pos and self.enemy3_pos[1] in y_pos:
            self.game_over_enemy()
        elif self.enemy4_pos[0] in x_pos and self.enemy4_pos[1] in y_pos:
            self.game_over_enemy()
        elif self.enemy5_pos[0] in x_pos and self.enemy5_pos[1] in y_pos:
            self.game_over_enemy()
        elif self.enemy6_pos[0] in x_pos and self.enemy6_pos[1] in y_pos:
            self.game_over_enemy()


    def check_boundary_collison(self):
        #layer1
        self.line01 = self.canvas.coords(self.canvas.find_withtag('line0.1'))
        self.line02 = self.canvas.coords(self.canvas.find_withtag('line0.2'))
        self.line03 = self.canvas.coords(self.canvas.find_withtag('line0.3'))
        self.line04 = self.canvas.coords(self.canvas.find_withtag('line0.4'))
        self.line05 = self.canvas.coords(self.canvas.find_withtag('line0.5'))
        self.line06 = self.canvas.coords(self.canvas.find_withtag('line0.6'))
        self.line07 = self.canvas.coords(self.canvas.find_withtag('line0.7'))
        self.line08 = self.canvas.coords(self.canvas.find_withtag('line0.8'))
        # layer2
        self.line11 = self.canvas.coords(self.canvas.find_withtag('line1.1'))
        self.line12 = self.canvas.coords(self.canvas.find_withtag('line1.2'))
        self.line13 = self.canvas.coords(self.canvas.find_withtag('line1.3'))
        self.line14 = self.canvas.coords(self.canvas.find_withtag('line1.4'))
        self.line15 = self.canvas.coords(self.canvas.find_withtag('line1.5'))
        self.line16 = self.canvas.coords(self.canvas.find_withtag('line1.6'))
        self.line17 = self.canvas.coords(self.canvas.find_withtag('line1.7'))
        self.line18 = self.canvas.coords(self.canvas.find_withtag('line1.8'))
        # layer3
        self.line21 = self.canvas.coords(self.canvas.find_withtag('line2.1'))
        self.line22 = self.canvas.coords(self.canvas.find_withtag('line2.2'))
        self.line23 = self.canvas.coords(self.canvas.find_withtag('line2.3'))
        self.line24 = self.canvas.coords(self.canvas.find_withtag('line2.4'))
        self.line25 = self.canvas.coords(self.canvas.find_withtag('line2.5'))
        self.line26 = self.canvas.coords(self.canvas.find_withtag('line2.6'))
        self.line27 = self.canvas.coords(self.canvas.find_withtag('line2.7'))
        self.line28 = self.canvas.coords(self.canvas.find_withtag('line2.8'))
        # layer4
        self.line31 = self.canvas.coords(self.canvas.find_withtag('line3.1'))
        self.line32 = self.canvas.coords(self.canvas.find_withtag('line3.2'))
        self.line33 = self.canvas.coords(self.canvas.find_withtag('line3.3'))
        self.line34 = self.canvas.coords(self.canvas.find_withtag('line3.4'))
        self.line35 = self.canvas.coords(self.canvas.find_withtag('line3.5'))
        self.line36 = self.canvas.coords(self.canvas.find_withtag('line3.6'))
        self.line37 = self.canvas.coords(self.canvas.find_withtag('line3.7'))
        self.line38 = self.canvas.coords(self.canvas.find_withtag('line3.8'))
        self.y_static_boundary_check()
        self.x_static_boundary_check()

    # 1,2,7,8 and lines will be used in here
    def y_static_boundary_check(self):
        if (self.player_pos[1] == self.line01[1] and self.player_pos[0] >= self.line01[0] and self.player_pos[0] <= self.line01[2]) or (self.player_pos[1] == self.line02[1] and self.player_pos[0] >= self.line02[0] and self.player_pos[0] <= self.line02[2]) or (self.player_pos[1] == self.line07[1] and self.player_pos[0] >= self.line07[0] and self.player_pos[0] <= self.line07[2]) or (self.player_pos[1] == self.line08[1] and self.player_pos[0] >= self.line08[0] and self.player_pos[0] <= self.line08[2]) or  (self.player_pos[1]+35 == self.line01[1] and self.player_pos[0] >= self.line01[0] and self.player_pos[0] <= self.line01[2]) or (self.player_pos[1]+35 == self.line02[1] and self.player_pos[0] >= self.line02[0] and self.player_pos[0] <= self.line02[2]) or (self.player_pos[1]+35 == self.line07[1] and self.player_pos[0] >= self.line07[0] and self.player_pos[0] <= self.line07[2]) or (self.player_pos[1]+35 == self.line08[1] and self.player_pos[0] >= self.line08[0] and self.player_pos[0] <= self.line08[2]):
            self.game_over_boundary()
        elif (self.player_pos[1] == self.line11[1] and self.player_pos[0] >= self.line11[0] and self.player_pos[0] <= self.line11[2]) or (self.player_pos[1] == self.line12[1] and self.player_pos[0] >= self.line12[0] and self.player_pos[0] <= self.line12[2]) or (self.player_pos[1] == self.line17[1] and self.player_pos[0] >= self.line17[0] and self.player_pos[0] <= self.line17[2]) or (self.player_pos[1] == self.line18[1] and self.player_pos[0] >= self.line18[0] and self.player_pos[0] <= self.line18[2]) or  (self.player_pos[1]+35 == self.line11[1] and self.player_pos[0] >= self.line11[0] and self.player_pos[0] <= self.line11[2]) or (self.player_pos[1]+35 == self.line12[1] and self.player_pos[0] >= self.line12[0] and self.player_pos[0] <= self.line12[2]) or (self.player_pos[1]+35 == self.line17[1] and self.player_pos[0] >= self.line17[0] and self.player_pos[0] <= self.line17[2]) or (self.player_pos[1]+35 == self.line18[1] and self.player_pos[0] >= self.line18[0] and self.player_pos[0] <= self.line18[2]):
            self.game_over_boundary()
        elif (self.player_pos[1] == self.line21[1] and self.player_pos[0] >= self.line21[0] and self.player_pos[0] <= self.line21[2]) or (self.player_pos[1] == self.line22[1] and self.player_pos[0] >= self.line22[0] and self.player_pos[0] <= self.line22[2]) or (self.player_pos[1] == self.line27[1] and self.player_pos[0] >= self.line27[0] and self.player_pos[0] <= self.line27[2]) or (self.player_pos[1] == self.line28[1] and self.player_pos[0] >= self.line28[0] and self.player_pos[0] <= self.line28[2]) or  (self.player_pos[1]+35 == self.line21[1] and self.player_pos[0] >= self.line21[0] and self.player_pos[0] <= self.line21[2]) or (self.player_pos[1]+35 == self.line22[1] and self.player_pos[0] >= self.line22[0] and self.player_pos[0] <= self.line22[2]) or (self.player_pos[1]+35 == self.line27[1] and self.player_pos[0] >= self.line27[0] and self.player_pos[0] <= self.line27[2]) or (self.player_pos[1]+35 == self.line28[1] and self.player_pos[0] >= self.line28[0] and self.player_pos[0] <= self.line28[2]):
            self.game_over_boundary()
        elif (self.player_pos[1] == self.line31[1] and self.player_pos[0] >= self.line31[0] and self.player_pos[0] <= self.line31[2]) or (self.player_pos[1] == self.line32[1] and self.player_pos[0] >= self.line32[0] and self.player_pos[0] <= self.line32[2]) or (self.player_pos[1] == self.line37[1] and self.player_pos[0] >= self.line37[0] and self.player_pos[0] <= self.line37[2]) or (self.player_pos[1] == self.line38[1] and self.player_pos[0] >= self.line38[0] and self.player_pos[0] <= self.line38[2]) or  (self.player_pos[1]+35 == self.line31[1] and self.player_pos[0] >= self.line31[0] and self.player_pos[0] <= self.line31[2]) or (self.player_pos[1]+35 == self.line32[1] and self.player_pos[0] >= self.line32[0] and self.player_pos[0] <= self.line32[2]) or (self.player_pos[1]+35 == self.line37[1] and self.player_pos[0] >= self.line37[0] and self.player_pos[0] <= self.line37[2]) or (self.player_pos[1]+35 == self.line38[1] and self.player_pos[0] >= self.line38[0] and self.player_pos[0] <= self.line38[2]):
            self.game_over_boundary()

    # x values are static in this case
    # karlo bc tune is function ko mere pass time nhi hai
    def x_static_boundary_check(self):
        if (self.player_pos[0] == self.line03[0] and self.player_pos[1] >= self.line03[1] and self.player_pos[1] <= self.line03[3]) or (self.player_pos[0] == self.line04[0] and self.player_pos[1] >= self.line04[1] and self.player_pos[1] <= self.line04[2]) or (self.player_pos[0] == self.line05[0] and self.player_pos[1] >= self.line05[1] and self.player_pos[1] <= self.line05[2]) or (self.player_pos[0] == self.line06[0] and self.player_pos[1] >= self.line06[1] and self.player_pos[1] <= self.line06[2]) or (self.player_pos[0]+35 == self.line03[0] and self.player_pos[1] >= self.line03[1] and self.player_pos[1] <= self.line03[3]) or (self.player_pos[0]+35 == self.line04[0] and self.player_pos[1] >= self.line04[1] and self.player_pos[1] <= self.line04[2]) or (self.player_pos[0]+35 == self.line05[0] and self.player_pos[1] >= self.line05[1] and self.player_pos[1] <= self.line05[2]) or (self.player_pos[0]+35 == self.line06[0] and self.player_pos[1] >= self.line06[1] and self.player_pos[1] <= self.line06[2]):
            self.game_over_boundary()
        elif (self.player_pos[0] == self.line13[0] and self.player_pos[1] >= self.line13[1] and self.player_pos[1] <= self.line13[3]) or (self.player_pos[0] == self.line14[0] and self.player_pos[1] >= self.line14[1] and self.player_pos[1] <= self.line14[2]) or (self.player_pos[0] == self.line15[0] and self.player_pos[1] >= self.line15[1] and self.player_pos[1] <= self.line15[2]) or (self.player_pos[0] == self.line16[0] and self.player_pos[1] >= self.line16[1] and self.player_pos[1] <= self.line16[2]) or (self.player_pos[0]+35 == self.line13[0] and self.player_pos[1] >= self.line13[1] and self.player_pos[1] <= self.line13[3]) or (self.player_pos[0]+35 == self.line14[0] and self.player_pos[1] >= self.line14[1] and self.player_pos[1] <= self.line14[2]) or (self.player_pos[0]+35 == self.line15[0] and self.player_pos[1] >= self.line15[1] and self.player_pos[1] <= self.line15[2]) or (self.player_pos[0]+35 == self.line16[0] and self.player_pos[1] >= self.line16[1] and self.player_pos[1] <= self.line16[2]):
            self.game_over_boundary()
        elif (self.player_pos[0] == self.line23[0] and self.player_pos[1] >= self.line23[1] and self.player_pos[1] <= self.line23[3]) or (self.player_pos[0] == self.line24[0] and self.player_pos[1] >= self.line24[1] and self.player_pos[1] <= self.line24[2]) or (self.player_pos[0] == self.line25[0] and self.player_pos[1] >= self.line25[1] and self.player_pos[1] <= self.line25[2]) or (self.player_pos[0] == self.line26[0] and self.player_pos[1] >= self.line26[1] and self.player_pos[1] <= self.line26[2]) or (self.player_pos[0]+35 == self.line23[0] and self.player_pos[1] >= self.line23[1] and self.player_pos[1] <= self.line23[3]) or (self.player_pos[0]+35 == self.line24[0] and self.player_pos[1] >= self.line24[1] and self.player_pos[1] <= self.line24[2]) or (self.player_pos[0]+35 == self.line25[0] and self.player_pos[1] >= self.line25[1] and self.player_pos[1] <= self.line25[2]) or (self.player_pos[0]+35 == self.line26[0] and self.player_pos[1] >= self.line26[1] and self.player_pos[1] <= self.line26[2]):
            self.game_over_boundary()
        elif (self.player_pos[0] == self.line33[0] and self.player_pos[1] >= self.line33[1] and self.player_pos[1] <= self.line33[3]) or (self.player_pos[0] == self.line34[0] and self.player_pos[1] >= self.line34[1] and self.player_pos[1] <= self.line34[2]) or (self.player_pos[0] == self.line35[0] and self.player_pos[1] >= self.line35[1] and self.player_pos[1] <= self.line35[2]) or (self.player_pos[0] == self.line36[0] and self.player_pos[1] >= self.line36[1] and self.player_pos[1] <= self.line36[2]) or (self.player_pos[0]+35 == self.line33[0] and self.player_pos[1] >= self.line33[1] and self.player_pos[1] <= self.line33[3]) or (self.player_pos[0]+35 == self.line34[0] and self.player_pos[1] >= self.line34[1] and self.player_pos[1] <= self.line34[2]) or (self.player_pos[0]+35 == self.line35[0] and self.player_pos[1] >= self.line35[1] and self.player_pos[1] <= self.line35[2]) or (self.player_pos[0]+35 == self.line36[0] and self.player_pos[1] >= self.line36[1] and self.player_pos[1] <= self.line36[2]):
            self.game_over_boundary()

    def game_over(self,type):
        if type == 'enemy':
            self.game_over_enemy()
        elif type == 'boundary':
            self.game_over_boundary()
        elif type == 'captured':
            self.game_over_captured()

    def game_over_enemy(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(600,100,
            text=f"YOu were fucked by one of the enemy!",
            fill="#fff",
            font=14)
        img = Image.open('./jhonny_fucked.jpg')
        self.photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(400,300,image=self.photo,anchor='nw',tag='jhonny fucked')
    def game_over_boundary(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(600, 100,
                                text=f"YOu were fucked by one boundary!",
                                fill="#fff",
                                font=14)
        img = Image.open('./jhonny_boundary.jfif')
        self.photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(450, 300, image=self.photo, anchor='nw', tag='jhonny fucked')
    def game_over_captured(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(600, 100,
                                text=f"Congrtas you get to eat MIA!",
                                fill="#fff",
                                font=14)
        img = Image.open('./jhonnny_mia.jpg')
        self.photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(450, 300, image=self.photo, anchor='nw', tag='jhonny fucked')


    def create_boundaries(self):
        #layer0 boundary
        count =0
        self.canvas.create_line(80, 30, 300, 30, fill='white', width=4, tag='line0.1')
        self.canvas.create_line(350, 30, 1170, 30, fill='white', width=4, tag='line0.2')
        self.canvas.create_line(1170, 30, 1170, 350, fill='white', width=4, tag='line0.3')
        self.canvas.create_line(1170, 440, 1170, 770, fill='white', width=4, tag='line0.4')
        self.canvas.create_line(80, 30, 80, 650, fill='white', width=4, tag='line0.5')
        self.canvas.create_line(80, 700, 80, 770, fill='white', width=4, tag='line0.6')
        self.canvas.create_line(80, 770, 750, 770, fill='white', width=4, tag='line0.7')
        self.canvas.create_line(800, 770, 1170, 770, fill='white', width=4, tag='line0.8')

        # layer1 boundary
        self.canvas.create_line(150,100,600,100,fill='white',width=4,tag='line1.1')
        self.canvas.create_line(670, 100, 1100, 100, fill='white', width=4,tag='line1.2')
        self.canvas.create_line(1100,100,1100,350,fill='white',width=4,tag='line1.3')
        self.canvas.create_line(1100, 440, 1100, 700, fill='white', width=4,tag='line1.4')
        self.canvas.create_line(150, 100, 150, 350, fill='white', width=4,tag='line1.5')
        self.canvas.create_line(150, 440, 150, 700, fill='white', width=4,tag='line1.6')
        self.canvas.create_line(150, 700, 600, 700, fill='white', width=4,tag='line1.7')
        self.canvas.create_line(670, 700, 1100, 700, fill='white', width=4,tag='line1.8')

        # layer2 boundary
        self.canvas.create_line(250, 200, 400, 200, fill='white', width=4,tag='line2.1')
        self.canvas.create_line(470, 200, 1000, 200, fill='white', width=4,tag='line2.2')
        self.canvas.create_line(1000, 200, 1000, 450, fill='white', width=4,tag='line2.3')
        self.canvas.create_line(1000, 500, 1000, 600, fill='white', width=4,tag='line2.4')
        self.canvas.create_line(250, 200, 250, 350, fill='white', width=4,tag='line2.5')
        self.canvas.create_line(250, 400, 250, 600, fill='white', width=4,tag='line2.6')
        self.canvas.create_line(250, 600, 400, 600, fill='white', width=4,tag='line2.7')
        self.canvas.create_line(450, 600, 1000, 600, fill='white', width=4,tag='line2.8')

        # layer3 boundaries
        self.canvas.create_line(350, 300, 500, 300, fill='white', width=4,tag='line3.1')
        self.canvas.create_line(570, 300, 900, 300, fill='white', width=4,tag='line3.2')
        self.canvas.create_line(900, 300, 900, 350, fill='white', width=4,tag='line3.3')
        self.canvas.create_line(900, 400, 900, 500, fill='white', width=4,tag='line3.4')
        self.canvas.create_line(350, 300, 350, 350, fill='white', width=4,tag='line3.5')
        self.canvas.create_line(350, 440, 350, 500, fill='white', width=4,tag='line3.6')
        self.canvas.create_line(350, 500, 600, 500, fill='white', width=4,tag='line3.7')
        self.canvas.create_line(670, 500, 900, 500, fill='white', width=4,tag='line3.8')

    def alter_boundaries(self):
        layer0 = randint(1, 4)
        layer1 = randint(1,4)
        layer2 = randint(1, 4)
        layer3 = randint(1, 4)

        self.alter_layer0(layer0)
        self.alter_layer1(layer1)

        self.alter_layer2(layer2)

        self.alter_layer3(layer3)





    def alter_layer0(self,type):
        if type == 1:
            self.canvas.coords(self.canvas.find_withtag('line0.1'),(80, 30, 300, 30))
            self.canvas.coords(self.canvas.find_withtag('line0.2'),(350, 30, 1170, 30))
            self.canvas.coords(self.canvas.find_withtag('line0.3'),(1170, 30, 1170, 350))
            self.canvas.coords(self.canvas.find_withtag('line0.4'), (1170, 440, 1170, 770))
            self.canvas.coords(self.canvas.find_withtag('line0.5'), (80, 30, 80, 650))
            self.canvas.coords(self.canvas.find_withtag('line0.6'), (80, 700, 80, 770))
            self.canvas.coords(self.canvas.find_withtag('line0.7'), (80, 770, 750, 770))
            self.canvas.coords(self.canvas.find_withtag('line0.8'), (800, 770, 1170, 770))

        elif type == 2:
            self.canvas.coords(self.canvas.find_withtag('line0.1'), (80, 30, 200, 30))
            self.canvas.coords(self.canvas.find_withtag('line0.2'), (250, 30, 1170, 30))
            self.canvas.coords(self.canvas.find_withtag('line0.3'), (1170, 30, 1170, 250))
            self.canvas.coords(self.canvas.find_withtag('line0.4'), (1170, 340, 1170, 770))
            self.canvas.coords(self.canvas.find_withtag('line0.5'), (80, 30, 80, 350))
            self.canvas.coords(self.canvas.find_withtag('line0.6'), (80, 400, 80, 770))
            self.canvas.coords(self.canvas.find_withtag('line0.7'), (80, 770, 450, 770))
            self.canvas.coords(self.canvas.find_withtag('line0.8'), (500, 770, 1170, 770))
        elif type == 3:
            self.canvas.coords(self.canvas.find_withtag('line0.1'), (80, 30, 500, 30))
            self.canvas.coords(self.canvas.find_withtag('line0.2'), (550, 30, 1170, 30))
            self.canvas.coords(self.canvas.find_withtag('line0.3'), (1170, 30, 1170, 650))
            self.canvas.coords(self.canvas.find_withtag('line0.4'), (1170, 700, 1170, 770))
            self.canvas.coords(self.canvas.find_withtag('line0.5'), (80, 30, 80, 450))
            self.canvas.coords(self.canvas.find_withtag('line0.6'), (80, 500, 80, 770))
            self.canvas.coords(self.canvas.find_withtag('line0.7'), (80, 770, 900, 770))
            self.canvas.coords(self.canvas.find_withtag('line0.8'), (950, 770, 1170, 770))


        elif type == 4:
            self.canvas.coords(self.canvas.find_withtag('line0.1'), (80, 30, 800, 30))
            self.canvas.coords(self.canvas.find_withtag('line0.2'), (850, 30, 1170, 30))
            self.canvas.coords(self.canvas.find_withtag('line0.3'), (1170, 30, 1170, 550))
            self.canvas.coords(self.canvas.find_withtag('line0.4'), (1170, 600, 1170, 770))
            self.canvas.coords(self.canvas.find_withtag('line0.5'), (80, 30, 80, 150))
            self.canvas.coords(self.canvas.find_withtag('line0.6'), (80, 300, 80, 770))
            self.canvas.coords(self.canvas.find_withtag('line0.7'), (80, 770, 450, 770))
            self.canvas.coords(self.canvas.find_withtag('line0.8'), (500, 770, 1170, 770))



    def alter_layer1(self,type): #alter the boundaries
        if type == 1:
            self.canvas.coords(self.canvas.find_withtag('1.1'),(150, 100, 600, 100))
            self.canvas.coords(self.canvas.find_withtag('1.2'), (670, 100, 1100, 100))
            self.canvas.coords(self.canvas.find_withtag('1.3'), (1100, 100, 1100, 350))
            self.canvas.coords(self.canvas.find_withtag('1.4'), (1100, 440, 1100, 700))
            self.canvas.coords(self.canvas.find_withtag('1.5'), (150, 100, 150, 350))
            self.canvas.coords(self.canvas.find_withtag('1.6'), (150, 440, 150, 700))
            self.canvas.coords(self.canvas.find_withtag('1.7'), (150, 700, 600, 700))
            self.canvas.coords(self.canvas.find_withtag('1.8'), (670, 700, 1100, 700))

        elif type == 2:
            self.canvas.coords(self.canvas.find_withtag('line1.1'), (150, 100, 200, 100))
            self.canvas.coords(self.canvas.find_withtag('line1.2'), (250, 100, 1100, 100))
            self.canvas.coords(self.canvas.find_withtag('line1.3'), (1100, 100, 1100, 250))
            self.canvas.coords(self.canvas.find_withtag('line1.4'), (1100, 340, 1100, 700))
            self.canvas.coords(self.canvas.find_withtag('line1.5'), (150, 100, 150, 450))
            self.canvas.coords(self.canvas.find_withtag('line1.6'), (150, 500, 150, 700))
            self.canvas.coords(self.canvas.find_withtag('line1.7'), (150, 700, 550, 700))
            self.canvas.coords(self.canvas.find_withtag('line1.8'), (600, 700, 1170, 700))

        elif type == 3:
            self.canvas.coords(self.canvas.find_withtag('line1.1'), (150, 100, 500, 100))
            self.canvas.coords(self.canvas.find_withtag('line1.2'), (550, 100, 1100, 100))
            self.canvas.coords(self.canvas.find_withtag('line1.3'), (1100, 100, 1100, 650))
            self.canvas.coords(self.canvas.find_withtag('line1.4'), (1100, 700, 1100, 700))
            self.canvas.coords(self.canvas.find_withtag('line1.5'), (150, 100, 150, 450))
            self.canvas.coords(self.canvas.find_withtag('line1.6'), (150, 500, 150, 770))
            self.canvas.coords(self.canvas.find_withtag('line1.7'), (150, 700, 900, 700))
            self.canvas.coords(self.canvas.find_withtag('line1.8'), (950, 700, 1170, 700))


        elif type == 4:
            self.canvas.coords(self.canvas.find_withtag('line1.1'), (150, 100, 800, 100))
            self.canvas.coords(self.canvas.find_withtag('line1.2'), (850, 100, 1170, 100))
            self.canvas.coords(self.canvas.find_withtag('line1.3'), (1100, 100, 1100, 550))
            self.canvas.coords(self.canvas.find_withtag('line1.4'), (1100, 600, 1100, 700))
            self.canvas.coords(self.canvas.find_withtag('line1.5'), (150, 100, 150, 150))
            self.canvas.coords(self.canvas.find_withtag('line1.6'), (150, 300, 150, 700))
            self.canvas.coords(self.canvas.find_withtag('line1.7'), (150, 700, 450, 700))
            self.canvas.coords(self.canvas.find_withtag('line1.8'), (150, 700, 1170, 700))
    def alter_layer2(self,type):
        if type == 1:
            self.canvas.coords(self.canvas.find_withtag('2.1'),(250, 200, 400, 200))
            self.canvas.coords(self.canvas.find_withtag('2.2'), (470, 200, 1000, 200))
            self.canvas.coords(self.canvas.find_withtag('2.3'), (1000, 200, 1000, 450))
            self.canvas.coords(self.canvas.find_withtag('2.4'), (1000, 500, 1000, 600))
            self.canvas.coords(self.canvas.find_withtag('2.5'), (250, 200, 250, 350))
            self.canvas.coords(self.canvas.find_withtag('2.6'), (250, 400, 250, 600))
            self.canvas.coords(self.canvas.find_withtag('2.7'), (250, 600, 400, 600))
            self.canvas.coords(self.canvas.find_withtag('2.8'), (450, 600, 1000, 600))

        elif type == 2:
            self.canvas.coords(self.canvas.find_withtag('line2.1'), (250, 200, 350, 200))
            self.canvas.coords(self.canvas.find_withtag('line2.2'), (400, 200, 1000, 200))
            self.canvas.coords(self.canvas.find_withtag('line2.3'), (1000, 200, 1000, 250))
            self.canvas.coords(self.canvas.find_withtag('line2.4'), (1000, 300, 1000, 600))
            self.canvas.coords(self.canvas.find_withtag('line2.5'), (250, 200, 250, 350))
            self.canvas.coords(self.canvas.find_withtag('line2.6'), (250, 400, 250,600))
            self.canvas.coords(self.canvas.find_withtag('line2.7'), (250, 600, 450, 600))
            self.canvas.coords(self.canvas.find_withtag('line2.8'), (500, 600, 1000, 600))
        elif type == 3:
            self.canvas.coords(self.canvas.find_withtag('line2.1'), (250, 200, 500, 200))
            self.canvas.coords(self.canvas.find_withtag('line2.2'), (550, 200, 1000, 200))
            self.canvas.coords(self.canvas.find_withtag('line2.3'), (1000, 200, 1000, 400))
            self.canvas.coords(self.canvas.find_withtag('line2.4'), (1000, 450, 1000, 600))
            self.canvas.coords(self.canvas.find_withtag('line2.5'), (250, 200, 250, 450))
            self.canvas.coords(self.canvas.find_withtag('line2.6'), (250, 500, 250, 600))
            self.canvas.coords(self.canvas.find_withtag('line2.7'), (250, 600, 900, 600))
            self.canvas.coords(self.canvas.find_withtag('line2.8'), (950, 600, 1000, 600))


        elif type == 4:
            self.canvas.coords(self.canvas.find_withtag('line2.1'), (250, 200, 800, 200))
            self.canvas.coords(self.canvas.find_withtag('line2.2'), (850, 200, 1000, 200))
            self.canvas.coords(self.canvas.find_withtag('line2.3'), (1000, 200, 1000, 350))
            self.canvas.coords(self.canvas.find_withtag('line2.4'), (1000, 400, 1000, 600))
            self.canvas.coords(self.canvas.find_withtag('line2.5'), (250, 200, 250, 250))
            self.canvas.coords(self.canvas.find_withtag('line2.6'), (250, 300, 250, 600))
            self.canvas.coords(self.canvas.find_withtag('line2.7'), (250, 600, 450, 600))
            self.canvas.coords(self.canvas.find_withtag('line2.8'), (500, 600, 1000, 600))
    def alter_layer3(self,type):
        if type == 1:
            self.canvas.coords(self.canvas.find_withtag('3.1'),(350, 300, 500, 300))
            self.canvas.coords(self.canvas.find_withtag('3.2'), (570, 300, 900, 300))
            self.canvas.coords(self.canvas.find_withtag('3.3'), (900, 300, 900, 350))
            self.canvas.coords(self.canvas.find_withtag('3.4'), (900, 400, 900, 500))
            self.canvas.coords(self.canvas.find_withtag('3.5'), (350, 300, 350, 350))
            self.canvas.coords(self.canvas.find_withtag('3.6'), (350, 440, 350, 500))
            self.canvas.coords(self.canvas.find_withtag('3.7'), (350, 500, 600, 500))
            self.canvas.coords(self.canvas.find_withtag('3.8'), (670, 500, 900, 500))

        elif type == 2:
            self.canvas.coords(self.canvas.find_withtag('line3.1'), (350, 300, 450, 300))
            self.canvas.coords(self.canvas.find_withtag('line3.2'), (500, 300, 900, 300))
            self.canvas.coords(self.canvas.find_withtag('line3.3'), (900, 300, 900, 450))
            self.canvas.coords(self.canvas.find_withtag('line3.4'), (900, 500, 900, 500))
            self.canvas.coords(self.canvas.find_withtag('line3.5'), (350, 300, 350, 350))
            self.canvas.coords(self.canvas.find_withtag('line3.6'), (350, 400, 350,500))
            self.canvas.coords(self.canvas.find_withtag('line3.7'), (350, 500, 550, 500))
            self.canvas.coords(self.canvas.find_withtag('line3.8'), (600, 500, 900, 500))


        elif type == 3:
            self.canvas.coords(self.canvas.find_withtag('line3.1'), (350, 300, 500, 300))
            self.canvas.coords(self.canvas.find_withtag('line3.2'), (550, 300, 900, 300))
            self.canvas.coords(self.canvas.find_withtag('line3.3'), (900, 300, 900, 400))
            self.canvas.coords(self.canvas.find_withtag('line3.4'), (900, 450, 900, 500))
            self.canvas.coords(self.canvas.find_withtag('line3.5'), (350, 300, 350, 450))
            self.canvas.coords(self.canvas.find_withtag('line3.6'), (350, 500, 350, 500))
            self.canvas.coords(self.canvas.find_withtag('line3.7'), (350, 500, 550, 500))
            self.canvas.coords(self.canvas.find_withtag('line3.8'), (600, 500, 900, 500))


        elif type == 4:
            self.canvas.coords(self.canvas.find_withtag('line3.1'), (350, 300, 800, 300))
            self.canvas.coords(self.canvas.find_withtag('line3.2'), (850, 300, 900, 300))
            self.canvas.coords(self.canvas.find_withtag('line3.3'), (900, 300, 900, 350))
            self.canvas.coords(self.canvas.find_withtag('line3.4'), (900, 400, 900, 500))
            self.canvas.coords(self.canvas.find_withtag('line3.5'), (350, 300, 350, 350))
            self.canvas.coords(self.canvas.find_withtag('line3.6'), (350, 400, 350, 500))
            self.canvas.coords(self.canvas.find_withtag('line3.7'), (350, 500, 450, 500))
            self.canvas.coords(self.canvas.find_withtag('line3.8'), (500, 500, 900, 500))



    def place_enemies(self):
        self.enem1 = Image.open('./enemy1.jfif').resize((35,35))
        self.enem2 = Image.open('./enemy2.jfif').resize((35,35))
        self.enem3 = Image.open('./enemy3.jfif').resize((35,35))
        self.enemy1 = ImageTk.PhotoImage(self.enem1)
        self.enemy2 = ImageTk.PhotoImage(self.enem2)
        self.enemy3 = ImageTk.PhotoImage(self.enem3)
        self.enemy4 = ImageTk.PhotoImage(self.enem1)
        self.enemy5 = ImageTk.PhotoImage(self.enem2)
        self.enemy6 = ImageTk.PhotoImage(self.enem3)
        self.enemy1_pos = [160,350]
        self.enemy2_pos = [260,440]
        self.enemy3_pos = [360,400]
        self.enemy4_pos = [460, 350]
        self.enemy5_pos = [660, 440]
        self.enemy6_pos = [860, 400]
        self.canvas.create_image(self.enemy1_pos[0],self.enemy1_pos[1],
                                 image=self.enemy1,tag='enemy1',anchor='nw')
        self.canvas.create_image(self.enemy2_pos[0], self.enemy2_pos[1],
                                 image=self.enemy2, tag='enemy2', anchor='nw')
        self.canvas.create_image(self.enemy3_pos[0], self.enemy3_pos[1],
                                 image=self.enemy3, tag='enemy3', anchor='nw')
        self.canvas.create_image(self.enemy4_pos[0], self.enemy4_pos[1],
                                 image=self.enemy4, tag='enemy4', anchor='nw')
        self.canvas.create_image(self.enemy5_pos[0], self.enemy5_pos[1],
                                 image=self.enemy5, tag='enemy5', anchor='nw')
        self.canvas.create_image(self.enemy6_pos[0], self.enemy6_pos[1],
                                 image=self.enemy6, tag='enemy6', anchor='nw')



    # tune this function
    def move_enemy1(self):
        enemy1_posX = randint(10,1160)
        enemy1_posY = randint(10,750)
        self.canvas.coords(self.canvas.find_withtag('enemy1'),(enemy1_posX,enemy1_posY))
    def move_enemy2(self):
        enemy2_posX = randint(10, 1160)
        enemy2_posY = randint(10, 750)
        self.canvas.coords(self.canvas.find_withtag('enemy2'), (enemy2_posX, enemy2_posY))
    def move_enemy3(self):
        enemy3_posX = randint(10, 1160)
        enemy3_posY = randint(10, 750)
        self.canvas.coords(self.canvas.find_withtag('enemy3'), (enemy3_posX, enemy3_posY))
    def move_enemy4(self):
        enemy4_posX = randint(10, 1160)
        enemy4_posY = randint(10, 750)
        self.canvas.coords(self.canvas.find_withtag('enemy4'), (enemy4_posX, enemy4_posY))
    def move_enemy5(self):
        enemy5_posX = randint(10, 1160)
        enemy5_posY = randint(10, 750)
        self.canvas.coords(self.canvas.find_withtag('enemy5'), (enemy5_posX, enemy5_posY))
    def move_enemy6(self):
        enemy6_posX = randint(10, 1160)
        enemy6_posY = randint(10, 750)
        self.canvas.coords(self.canvas.find_withtag('enemy6'), (enemy6_posX, enemy6_posY))




root= mainFrame()
root.columnconfigure(0,weight=1)
style = ttk.Style(root)  # Pass in which application this style is for.

# Get the themes available in your system
print(style.theme_names())
print(style.theme_use("vista"))
root.mainloop()