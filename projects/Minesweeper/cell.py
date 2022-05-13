from tkinter import Button, Label
import random
import settings


    
class Cell:
    all=[]
    
    cell_count_label_object = None
    life_count_label_object = None
    mine_label_object = None
    flag_count_label_object = None
    
    left_cell_count = settings.LEFT_CELL
    left_life_count = settings.LIFE_COUNT
    flag_count = 0
    
    def __init__(self, x, y):
        self.is_mine = False
        self.is_open = False
        self.cell_btn_object= None
        self.x= x
        self.y= y
        
        #Append the object to the Cell.all list
        Cell.all.append(self)
        
    def create_btn_object(self,location):
        btn = Button(
            location,
            width= 5,
            height= 2,
            bg= 'gray',
            text=""
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object= btn
        
    
    def left_click_actions(self, event):
        if self.is_open:
            return
        self.is_open =True
        
        if self.cell_btn_object["bg"]== 'purple':
            Cell.flag_count-=1
            Cell.refresh_flag_count()
        
        self.show_cell()
        
        if Cell.left_cell_count ==0:
            Cell.store_data()
            Cell.reset_game()


    def show_cell(self):
        if self.is_mine:
            self.cell_btn_object["bg"]= 'red'
            self.cell_btn_object["text"]= text="MINE!!"
            Cell.left_life_count -=1
            if Cell.left_life_count >0:
                Cell.refresh_life_count()
            else:
                Cell.refresh_life_count(is_alive =False)
                #interrupt the game and display a message that player lost
                
            return # end the game
        
        Cell.left_cell_count -=1
        near_mine= self.near_mine()
        self.cell_btn_object["bg"]= 'white'
        self.cell_btn_object["text"] = f'{near_mine}'
        if Cell.left_cell_count >0:
            Cell.refresh_cell_count()
        else:
            Cell.refresh_cell_count(is_left = False)
            
        if near_mine ==0:
            for cell in self.surrounded_cells:
                cell.left_click_actions(None)


    def right_click_actions(self, event):

        if self.is_open:
            return
            
        if self.cell_btn_object["bg"] == 'purple':
            self.cell_btn_object["bg"] = 'gray'
            Cell.flag_count-=1
            Cell.refresh_flag_count()
            
        else: 
            self.cell_btn_object["bg"] = 'purple'
            Cell.flag_count+=1
            Cell.refresh_flag_count()

    def near_mine(self):
        n_mines =0
        for cell in  self.surrounded_cells:
            if cell.is_mine:
                n_mines+=1
        return n_mines
    
    @property
    @staticmethod
    def surrounded_cells(self):
        cells= []
        for y in [-1,0,1]:
            for x in [-1,0,1]:
                if x==0 and y ==0:
                    continue
                nx = self.x +x 
                ny = self.y +y
                cells.append(self.get_cell_by_axis(nx,ny))
                
        return [cell for cell in cells if cell is not None]
    
    @staticmethod        
    def get_cell_by_axis(x ,y):
        for cell_object in Cell.all:
            if cell_object.x == x and cell_object.y == y:
                return cell_object
   
    @staticmethod
    def randomize_mines():
        mine_objects= random.sample(Cell.all, settings.MINE_COUNT)
        for mine_object in mine_objects:
            mine_object.is_mine = True
            # mine_object.cell_btn_object["text"]= text="MINE!!"
            
    @staticmethod
    def create_label_object(location, text_input = ''):
        lbl = Label(
            location,
            text= text_input,
            bg= 'black',
            fg= 'white',
            font= ("", 20),

        )
        return lbl
    
    @staticmethod
    def create_left_labels(location):
        Cell.cell_count_label_object = Cell.create_label_object(location)
        Cell.life_count_label_object = Cell.create_label_object(location)
        Cell.mine_label_object = Cell.create_label_object(location,text_input=f'Mines are {settings.MINE_COUNT}')
        Cell.flag_count_label_object = Cell.create_label_object(location)
        
        Cell.refresh_cell_count()
        Cell.refresh_life_count()
        Cell.refresh_flag_count()
    
    
    @staticmethod
    def refresh_cell_count(is_left = True):
        if is_left:
            Cell.cell_count_label_object["text"] = f'Cells left: {Cell.left_cell_count}'
        else:
            if Cell.left_life_count >0:
                Cell.cell_count_label_object["text"] = 'CLEAR'
        return
    
    @staticmethod
    def refresh_life_count(is_alive = True):
        if is_alive:
            Cell.life_count_label_object["text"] = f'Life left: {Cell.left_life_count}'
        else:
            Cell.life_count_label_object["text"] = f'GAME OVER'
        return
    
    @staticmethod
    def refresh_flag_count():
        Cell.flag_count_label_object["text"]= f'Flags are: {Cell.flag_count}'
        

    
    @staticmethod
    def store_data():
        pass
    
    @staticmethod
    def reset_game():
        pass
            
            