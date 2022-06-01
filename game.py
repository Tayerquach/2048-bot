from tkinter import Frame, Label, CENTER
import random
import helper
import constants as c
import time

class Game(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        
        self.list_key = []
        self.matrix = helper.create_new_game(c.GRID_LEN)
        self.matrix = self.create_state(self.matrix)
        # helper.print_grid(self.matrix)
        # self.history_matrixs = []
        # self.gain_scores = []
        # self.master.bind("<Key>", self.key_down)
        self.commands = {c.KEY_UP_ALT: helper.up, c.KEY_DOWN_ALT: helper.down,
                    c.KEY_LEFT_ALT: helper.left, c.KEY_RIGHT_ALT: helper.right}
        
        # self.init_grid()
        # self.update_grid_cells() 



        # print("Options:")
        # print("Press 0: Bot Game")
        # print("Press 1: Manually")
        # self.option = int(input("Select your choice: "))

        # if self.option == 1:
        # self.keys = []
        # self.master.bind("<Key>", self.key_down)
        
        # elif self.option == 0:
        #     while action:
        #         self.history_matrixs = []
        #         self.gain_scores = []
        #         self.give_action(action)
        #         self.run_auto_game(move)
    
        
               
        # self.mainloop()
        
            

            
            

                

        

        # self.matrix = self.create_state(self.matrix)
        # self.history_matrixs = []
        # self.gain_scores = []

        


    def init_grid(self):
        self.background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                           width=c.SIZE, height=c.SIZE)
        self.background.grid(pady=(c.PADY_GRID,0))
        self.grid_cells = []
        self.score = 0
        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell_frame = Frame(self.background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                             width=c.SIZE / c.GRID_LEN,
                             height=c.SIZE / c.GRID_LEN)
                cell_frame.grid(row=i, column=j, padx=c.CELL_PAD, pady=c.CELL_PAD)

                cell_number = Label(self.background, bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                cell_number.grid(row=i, column=j)

                cell_data = {"frame": cell_frame, "number": cell_number}
                grid_row.append(cell_data)

            self.grid_cells.append(grid_row)

        #Make score header
        score_frame = Frame(self)
        score_frame.place(relx=0.5, y=45, anchor="center")
        Label(
            score_frame,
            text="Score",
            font=c.SCORE_LABEL_FONT
        ).grid(row=0)
        self.score_label = Label(score_frame, text="0", font=c.SCORE_FONT)
        self.score_label.grid(row=1)      

    
    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j]["frame"].configure(bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[i][j]["number"].configure(bg=c.BACKGROUND_COLOR_CELL_EMPTY, text="")
                else:
                    self.grid_cells[i][j]["frame"].configure(bg=c.BACKGROUND_COLOR_DICT[new_number])
                    self.grid_cells[i][j]["number"].configure(
                        bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number],
                        font=c.FONT,
                        text=str(new_number)
                    )
            self.score_label.configure(text=self.score)
        self.update_idletasks()
        

    def key_down(self, event):
        key = repr(event.char)
        if key == c.KEY_BACK_ALT and len(self.history_matrixs) > 1:
            self.matrix = self.history_matrixs.pop()
            self.matrix = self.history_matrixs.pop()
            self.score  = self.gain_scores.pop()
            self.score  = self.gain_scores.pop()
            helper.print_grid(self.get_state())
            self.update_grid_cells()
            print('Back on step total step:', len(self.history_matrixs))

        elif key in self.commands:
            self.matrix, done, score = self.commands[repr(event.char)](self.matrix)
            self.list_key.append(key)
            self.score += score
            self.gain_scores.append(self.score)
            # record last move
            self.history_matrixs.append(self.matrix)
            self.update_grid_cells()

        # elif key == c.KEY_AI:
        #     agent = a.BFSAgent()
        #     status = "not over'"
        #     while status != "lose":
        #         state = [self.matrix, 0, []]
        #         action = agent.search_action(state, 6)[0]
        #         matrix, done, score = self.commands[action](self.matrix)
        #         if done:
        #             self.matrix = matrix
        #             self.list_key.append(action)
        #             self.score += score
        #             self.gain_scores.append(self.score)
        #             helper.print_grid(self.matrix)
        #             self.update_grid_cells()

        #         else:
        #             for move in self.commands.keys():
        #                 matrix, done, score = self.commands[move](self.matrix) 
        #                 if done:
        #                     self.matrix = matrix
        #                     self.list_key.append(action)
        #                     self.score += score
        #                     self.gain_scores.append(self.score)
        #                     helper.print_grid(self.matrix)
        #                     self.update_grid_cells()

        if helper.game_state(self.matrix) == 'win':
            # self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            # self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            game_over_frame = Frame(self.background, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            Label(
                game_over_frame,
                text="You win!",
                bg=c.WINNER_BG,
                fg=c.GAME_OVER_FONT_COLOR,
                font=c.GAME_OVER_FONT
            ).pack()
        elif helper.game_state(self.matrix) == 'lose':
            # self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            # self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            game_over_frame = Frame(self.background, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            Label(
            game_over_frame,
            text="Game over!",
            bg=c.LOSER_BG,
            fg=c.GAME_OVER_FONT_COLOR,
            font=c.GAME_OVER_FONT
            ).pack()

    def create_state(self, arr):
        self.matrix = arr
        return self.matrix

    def get_state(self):
        return self.matrix

    def get_action(self):
        return self.list_key

    def give_action(self, action):
        if type(action) == str:
            self.matrix, done, score = self.commands[action](self.matrix)
        else:
            return self.matrix, False, 0
        return self.matrix, done, score


    def run_auto_game(self, move):        
        if move in self.commands:
            self.matrix, done, score = self.commands[move](self.matrix)
            helper.print_grid(self.matrix)
                            



