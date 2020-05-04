from Tkinter import *

class Game(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

        # turn counter
        self.turn = 0
        # point variables
        self.userPoints = 0
        self.ties = 0
        self.cpuPoints = 0
        # dictionary of spaces and their value
        self.spaces = { "s1":" ", "s2":" ", "s3":" ", "s4":" ", "s5":" ",\
                        "s6":" ", "s7": " ", "s8":" ", "s9":" "}

    def mainmenu(self, w, h):
        self.pack(fill=BOTH, expand=1)
        # create canvas
        canvas = Canvas(self, relief = FLAT, background = "white", \
                         width = w, height = h)
        canvas.pack(side = TOP, anchor = NW)
        canvas.delete("all")

        # text asking what user wants to play
        q = Label(self, text = "What would you like to play?")
        q.configure(width = 25, bg = "white", fg = "red", font = ("Helvetica", 25))
        q_window = canvas.create_window(w/2, h/4, anchor = CENTER, window = q)

        # 'or' inbetween game options
        o = Label(self, text = "or")
        o.configure(width = 15, bg = "white", font = ("Helvetica", 15))
        o_window = canvas.create_window(w/2, h/2, anchor = CENTER, window = o)
        
        # buttons to choose game mode
        b1 = Button(self, text = "Tic Tac Toe", command = lambda: self.tictactoe(w, h, canvas))
        b1.configure(width = 10, activebackground = "gray", relief = FLAT, font = ("Helvetica", 20))
        b1_window = canvas.create_window(w/4, h/2, anchor = CENTER, window = b1)

        b2 = Button(self, text = "Misere", command = lambda: self.misere(w, h, canvas))
        b2.configure(width = 10, activebackground = "gray", relief = FLAT, font = ("Helvetica", 20))
        b2_window = canvas.create_window(3*w/4, h/2, anchor = CENTER, window = b2)

##        b3 = Button(self, text = "Misere", command = lambda: self.misere(w, h, canvas))
##        b3.configure(width = 10, activebackground = "gray", relief = FLAT, font = ("Helvetica", 20))
##        b3_window = canvas.create_window(3*w/4, h/2, anchor = CENTER, window = b2)

        # game descriptions
        d1 = Label(self, text = "Traditional X and O rules,")
        d1.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        d1_window = canvas.create_window(w/4, 5*h/8, anchor = CENTER, window = d1)

        d2 = Label(self, text = "first to make three in a row, wins")
        d2.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        d2_window = canvas.create_window(w/4, 43*h/64, anchor = CENTER, window = d2)

        d3 = Label(self, text = "Like traditional Tic-Tac-Toe, except")
        d3.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        d3_window = canvas.create_window(3*w/4, 5*h/8, anchor = CENTER, window = d3)

        d4 = Label(self, text = "first to make three in a row, loses")
        d4.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        d4_window = canvas.create_window(3*w/4, 43*h/64, anchor = CENTER, window = d4)

    def tictactoe(self, w, h, canvas):
        canvas.pack(side = TOP, anchor = NW)
        # create tic tac toe grid
        game = "Tic-Tac-Toe"
        self.createGrid(canvas, w, h, game)

    def misere(self, w, h, canvas):
        canvas.pack(side = TOP, anchor = NW)
        # create tic tac toe grid
        game = "Misere"
        self.createGrid(canvas, w, h, game)

    def PvPtictactoe(self, w, h, canvas):
        canvas.pack(side = TOP, anchor = NW)
        # create tic tac toe grid
        game = "Tic-Tac-Toe (PvP)"
        self.createGrid(canvas, w, h, game)

    def PvPmisere(self, w, h, canvas):
        canvas.pack(side = TOP, anchor = NW)
        # create tic tac toe grid
        game = "Misere (PvP)"
        self.createGrid(canvas, w, h, game)

    def createGrid(self, canvas, w, h, game):
        # clear canvas and reset turn counter
        canvas.delete("all")
        canvas.pack(side = TOP, anchor = NW)
        self.turn = 0

        # clear spaces dictionary
        for space in self.spaces:
            self.spaces[space] = " "
        
        # create scoreboard
##        if game == "Tic-Tac-Toe" or game == "Misere":
##            #run this scoreboard for CPU games
        title = Label(self, text = game)
        title.configure(width = 50, bg = "blue", fg = "red", font = ("Helvetica", 40))
        title_window = canvas.create_window(w/2, 25, anchor = CENTER, window = title)

        cpu = Label(self, text = "CPU: {}".format(self.cpuPoints))
        cpu.configure(width = 7, bg = "white", fg = "red", font = ("Helvetica", 20))
        cpu_window = canvas.create_window(w/4, 77, anchor = CENTER, window = cpu)

        tie = Label(self, text = "Draws: {}".format(self.ties))
        tie.configure(width = 8, bg = "white", fg = "black", font = ("Helvetica", 20))
        tie_window = canvas.create_window(w/2, 77, anchor = CENTER, window = tie)

        user = Label(self, text = "You: {}".format(self.userPoints))
        user.configure(width = 7, bg = "white", fg = "blue", font = ("Helvetica", 20))
        user_window = canvas.create_window(3*w/4, 77, anchor = CENTER, window = user)

        #Scoreboard for PvP games

##        if game == "Tic-Tac-Toe (PvP)" or game == "Misere (PvP)":
##            title = Label(self, text = game)
##            title.configure(width = 50, bg = "blue", fg = "red", font = ("Helvetica", 40))
##            title_window = canvas.create_window(w/2, 25, anchor = CENTER, window = title)
##
##            Player2 = Label(self, text = "Player 2: {}".format(self.Player2Points))
##            Player2.configure(width = 7, bg = "white", fg = "red", font = ("Helvetica", 20))
##            Player2_window = canvas.create_window(w/4, 77, anchor = CENTER, window = Player2)
##
##            tie = Label(self, text = "Draws: {}".format(self.ties))
##            tie.configure(width = 8, bg = "white", fg = "black", font = ("Helvetica", 20))
##            tie_window = canvas.create_window(w/2, 77, anchor = CENTER, window = tie)
##
##            user = Label(self, text = "You: {}".format(self.userPoints))
##            user.configure(width = 7, bg = "white", fg = "blue", font = ("Helvetica", 20))
##            user_window = canvas.create_window(3*w/4, 77, anchor = CENTER, window = user)
        

        # create vertical lines
        canvas.create_line(w/3, 110, w/3, h-10)
        canvas.create_line(2*w/3, 110, 2*w/3, h-10)
        
        # create horizontal lines
        canvas.create_line(10, (h-100)/3+100, w-10, (h-100)/3+100)
        canvas.create_line(10, 2*(h-100)/3+100, w-10, 2*(h-100)/3+100)
        
        # create squares
        global s1, s2, s3, s4, s5, s6, s7, s8, s9
        s1 = self.createSquare(w/6+5, 90+h/6, game, canvas, "s1")
        s2 = self.createSquare(w/2, 90+h/6, game, canvas, "s2")
        s3 = self.createSquare(5*w/6-5, 90+h/6, game, canvas, "s3")
        s4 = self.createSquare(w/6+5, 50+h/2, game, canvas, "s4")
        s5 = self.createSquare(w/2, 50+h/2, game, canvas, "s5")
        s6 = self.createSquare(5*w/6-5, 50+h/2, game, canvas, "s6")
        s7 = self.createSquare(w/6+5, 10+5*h/6, game, canvas, "s7")
        s8 = self.createSquare(w/2, 10+5*h/6, game, canvas, "s8")
        s9 = self.createSquare(5*w/6-5, 10+5*h/6, game, canvas, "s9")

        # cpu plays in top left corner always on first turn
        if game == "Tic-Tac-Toe":
            self.playX(s1, "red", "s1", canvas, game, w, h)
        else:
            self.playX(s5, "red", "s5", canvas, game, w, h)

    # creates squares as blank buttons
    def createSquare(self, w, h, game, canvas, dictS):
        s = Button(self, text = " ", width = 4, height = 1,\
                    command = lambda: self.playO(s, "blue", dictS, canvas, game, w, h))
        s.configure(fg = "white", bg = "white", relief = FLAT,\
                    font = ("Helvetica", 45))
        s_window = canvas.create_window(w, h, anchor = CENTER, window = s)

        return s

    # the cpu plays by filling in button with X for Tic-Tac-Toe
    def playCPUT(self, canvas, game, w, h):
        # finds where to play on cpu's second turn
        if self.turn == 2:
            if (self.spaces["s2"] == "O") or (self.spaces["s4"] == "O")\
               or (self.spaces["s6"] == "O") or (self.spaces["s8"] == "O"):
                self.playX(s5, "red", "s5", canvas, game, w, h)
            elif (self.spaces["s7"] == "O") or (self.spaces["s9"] == "O"):
                self.playX(s3, "red", "s3", canvas, game, w, h)
            elif self.spaces["s3"] == "O":
                self.playX(s7, "red", "s7", canvas, game, w, h)
            else:
                self.playX(s9, "red", "s9", canvas, game, w, h)
        # finds where to play on cpu's third turn
        elif self.turn == 4:
            if self.spaces["s1"] == "X" and self.spaces["s5"] == "X":
                if self.spaces["s9"] == " ":
                    self.playX(s9, "red", "s9", canvas, game, w, h)
                elif self.spaces["s2"] == "O" or self.spaces["s8"] == "O":
                    self.playX(s7, "red", "s7", canvas, game, w, h)
                else:
                    self.playX(s3, "red", "s3", canvas, game, w, h)
            elif self.spaces["s1"] == "X" and self.spaces["s3"] == "X":
                if self.spaces["s2"] == " ":
                    self.playX(s2, "red", "s2", canvas, game, w, h)
                elif self.spaces["s7"] == "O":
                    self.playX(s9, "red", "s9", canvas, game, w, h)
                else:
                    self.playX(s7, "red", "s7", canvas, game, w, h)
            elif self.spaces["s1"] == "X" and self.spaces["s7"] == "X":
                if self.spaces["s4"] == " ":
                    self.playX(s4, "red", "s4", canvas, game, w, h)
                else:
                    self.playX(s9, "red", "s9", canvas, game, w, h)
            else:
                if self.spaces["s2"] == "O":
                    self.playX(s8, "red", "s8", canvas, game, w, h)
                elif self.spaces["s3"] == "O":
                    self.playX(s7, "red", "s7", canvas, game, w, h)
                elif self.spaces["s4"] == "O":
                    self.playX(s6, "red", "s6", canvas, game, w, h)
                elif self.spaces["s6"] == "O":
                    self.playX(s4, "red", "s4", canvas, game, w, h)
                elif self.spaces["s7"] == "O":
                    self.playX(s3, "red", "s3", canvas, game, w, h)
                else:
                    self.playX(s2, "red", "s2", canvas, game, w, h)
        # finds where to play on cpu's fourth turn
        elif self.turn == 6:
            if (self.spaces["s1"] == "X") and (self.spaces["s5"] == "X")\
               and (self.spaces["s7"] == "X"):
                if self.spaces["s4"] == " ":
                    self.playX(s4, "red", "s4", canvas, game, w, h)
                else:
                    self.playX(s3, "red", "s3", canvas, game, w, h)
            elif (self.spaces["s1"] == "X") and (self.spaces["s9"] == "X")\
               and (self.spaces["s7"] == "X"):
                if self.spaces["s8"] == " ":
                    self.playX(s8, "red", "s8", canvas, game, w, h)
                else:
                    self.playX(s5, "red", "s5", canvas, game, w, h)
            elif (self.spaces["s1"] == "X") and (self.spaces["s5"] == "X")\
               and (self.spaces["s3"] == "X"):
                if self.spaces["s2"] == " ":
                    self.playX(s2, "red", "s2", canvas, game, w, h)
                else:
                    self.playX(s7, "red", "s7", canvas, game, w, h)
            elif (self.spaces["s1"] == "X") and (self.spaces["s3"] == "X")\
               and (self.spaces["s9"] == "X"):
                if self.spaces["s6"] == " ":
                    self.playX(s6, "red", "s6", canvas, game, w, h)
                else:
                    self.playX(s5, "red", "s5", canvas, game, w, h)
            elif (self.spaces["s1"] == "X") and (self.spaces["s5"] == "X")\
               and (self.spaces["s7"] == "X"):
                if self.spaces["s4"] == " ":
                    self.playX(s4, "red", "s4", canvas, game, w, h)
                else:
                    self.playX(s3, "red", "s3", canvas, game, w, h)
            elif (self.spaces["s1"] == "X") and (self.spaces["s3"] == "X")\
               and (self.spaces["s7"] == "X"):
                if self.spaces["s4"] == " ":
                    self.playX(s4, "red", "s4", canvas, game, w, h)
                else:
                    self.playX(s5, "red", "s5", canvas, game, w, h)
            elif (self.spaces["s1"] == "X") and (self.spaces["s9"] == "X")\
               and (self.spaces["s8"] == "X"):
                if self.spaces["s7"] == " ":
                    self.playX(s7, "red", "s7", canvas, game, w, h)
                else:
                    self.playX(s3, "red", "s3", canvas, game, w, h)
            elif (self.spaces["s1"] == "X") and (self.spaces["s9"] == "X")\
               and (self.spaces["s6"] == "X"):
                if self.spaces["s3"] == " ":
                    self.playX(s3, "red", "s3", canvas, game, w, h)
                else:
                    self.playX(s7, "red", "s7", canvas, game, w, h)
            elif (self.spaces["s1"] == "X") and (self.spaces["s9"] == "X")\
               and (self.spaces["s4"] == "X"):
                if self.spaces["s7"] == " ":
                    self.playX(s7, "red", "s7", canvas, game, w, h)
                else:
                    self.playX(s3, "red", "s3", canvas, game, w, h)
            else:
                if self.spaces["s3"] == " ":
                    self.playX(s3, "red", "s3", canvas, game, w, h)
                else:
                    self.playX(s7, "red", "s7", canvas, game, w, h)
        # finds last empty square and plays there
        else:
            for space in self.spaces:
                if self.spaces[space] == " ":
                    lastSpace = space
            if lastSpace == "s2":
                self.playX(s2, "red", "s2", canvas, game, w, h)
            elif lastSpace == "s4":
                self.playX(s4, "red", "s4", canvas, game, w, h)
            elif lastSpace == "s6":
                self.playX(s6, "red", "s6", canvas, game, w, h)
            else:
                self.playX(s8, "red", "s8", canvas, game, w, h)

    # the cpu plays by filling in button with X for Tic-Tac-Toe
    def playCPUM(self, canvas, game, w, h, dictS):
        if dictS == "s1":
            self.playX(s9, "red", "s9", canvas, game, w, h)
        elif dictS == "s2":
            self.playX(s8, "red", "s8", canvas, game, w, h)
        elif dictS == "s3":
            self.playX(s7, "red", "s7", canvas, game, w, h)
        elif dictS == "s4":
            self.playX(s6, "red", "s6", canvas, game, w, h)
        elif dictS == "s6":
            self.playX(s4, "red", "s4", canvas, game, w, h)
        elif dictS == "s7":
            self.playX(s3, "red", "s3", canvas, game, w, h)
        elif dictS == "s8":
            self.playX(s2, "red", "s2", canvas, game, w, h)
        else:
            self.playX(s1, "red", "s1", canvas, game, w, h)
                
    # fills in button with X
    def playX(self, s, color, dictS, canvas, game, w, h):
        s.configure(text = "X", disabledforeground = color)
        s["state"] = DISABLED
        self.spaces[dictS] = "X"
        result, state = self.checkWin(dictS, canvas, game, w, h)
        if (state == "win" or state == "tie"):
            self.replay(canvas, game, w, h, result)
        else:
            self.turn += 1

    # fills in button with O
    def playO(self, s, color, dictS, canvas, game, w, h):
        s.configure(text = "O", disabledforeground = color)
        s["state"] = DISABLED
        self.spaces[dictS] = "O"
        result, state = self.checkWin(dictS, canvas, game, w, h)
        if (state == "win" or state == "tie"):
            self.replay(canvas, game, w, h, result)
        else:
            self.turn += 1
            if (game == "Misere" and self.turn%2 == 0):
                self.playCPUM(canvas, game, w, h, dictS)
            else:
                self.playCPUT(canvas, game, w, h)

    # check for win
    def checkWin(self, dictS, canvas, game, w, h):
        if self.turn%2 == 0:
            state = False
            result = False
            
        if self.spaces[dictS] == "X":
            state = self.findThreeInRow(dictS, "X")
        else:
            state = self.findThreeInRow(dictS, "O")

        if state == "win":
            #disable all grid squares if game is over
##            s["state"] = DISABLED
            if game == "Tic-Tac-Toe":
                if self.turn%2 == 0:
                    self.cpuPoints += 1
                    result = Label(self, text = "THE CPU WINS")
                    result.configure(width = 13, bg = "white", fg = "red", font = ("Helvetica", 30))
                    result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)
                else:
                    self.userPoints += 1
                    result = Label(self, text = "YOU WIN")
                    result.configure(width = 8, bg = "white", fg = "blue", font = ("Helvetica", 30))
                    result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)
            else:
                if self.turn%2 == 0:
                    self.userPoints += 1
                    result = Label(self, text = "THE CPU LOSES")
                    result.configure(width = 14, bg = "white", fg = "blue", font = ("Helvetica", 30))
                    result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)
                else:
                    self.cpuPoints += 1
                    result = Label(self, text = "YOU LOSE")
                    result.configure(width = 9, bg = "white", fg = "red", font = ("Helvetica", 30))
                    result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)
        else:
            if " " in self.spaces.values():
                result = False
            else:
                state = "tie"
                self.ties += 1
                result = Label(self, text = "IT'S A TIE")
                result.configure(width = 9, bg = "white", fg = "black", font = ("Helvetica", 30))
                result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)

        return result, state
    
    # find three in a row
    def findThreeInRow(self, dictS, value):
        # check all possible three in a rows with space one
        if dictS == "s1":
            if (self.spaces["s2"] == value and self.spaces["s3"] == value)\
               or (self.spaces["s4"] == value and self.spaces["s7"] == value)\
               or (self.spaces["s5"] == value and self.spaces["s9"] == value):
                state = "win"
            else:
                state = "na"
        # check all possible three in a rows with space two
        elif dictS == "s2":
            if (self.spaces["s1"] == value and self.spaces["s3"] == value)\
               or (self.spaces["s5"] == value and self.spaces["s8"] == value):
                state = "win"
            else:
                state = "na"
        # check all possible three in a rows with space three
        elif dictS == "s3":
            if (self.spaces["s1"] == value and self.spaces["s2"] == value)\
               or (self.spaces["s6"] == value and self.spaces["s9"] == value)\
               or (self.spaces["s5"] == value and self.spaces["s7"] == value):
                state = "win"
            else:
                state = "na"
        # check all possible three in a rows with space four
        elif dictS == "s4":
            if (self.spaces["s5"] == value and self.spaces["s6"] == value)\
               or (self.spaces["s1"] == value and self.spaces["s7"] == value):
                state = "win"
            else:
                state = "na"
        # check all possible three in a rows with space five
        elif dictS == "s5":
            if (self.spaces["s4"] == value and self.spaces["s6"] == value)\
               or (self.spaces["s2"] == value and self.spaces["s8"] == value)\
               or (self.spaces["s1"] == value and self.spaces["s9"] == value)\
               or (self.spaces["s3"] == value and self.spaces["s7"] == value):
                state = "win"
            else:
                state = "na"
        # check all possible three in a rows with space six
        elif dictS == "s6":
            if (self.spaces["s4"] == value and self.spaces["s5"] == value)\
               or (self.spaces["s3"] == value and self.spaces["s9"] == value):
                state = "win"
            else:
                state = "na"
        # check all possible three in a rows with space seven
        elif dictS == "s7":
            if (self.spaces["s8"] == value and self.spaces["s9"] == value)\
               or (self.spaces["s1"] == value and self.spaces["s4"] == value)\
               or (self.spaces["s3"] == value and self.spaces["s5"] == value):
                state = "win"
            else:
                state = "na"
        # check all possible three in a rows with space eight
        elif dictS == "s8":
            if (self.spaces["s7"] == value and self.spaces["s9"] == value)\
               or (self.spaces["s2"] == value and self.spaces["s5"] == value):
                state = "win"
            else:
                state = "na"
        else:
            if (self.spaces["s7"] == value and self.spaces["s8"] == value)\
               or (self.spaces["s3"] == value and self.spaces["s6"] == value)\
               or (self.spaces["s1"] == value and self.spaces["s5"] == value):
                state = "win"
            else:
                state = "na"

        return state

    # asks user if they want to replay
    def replay(self, canvas, game, w, h, result):
        w = WIDTH
        h = HEIGHT
        o1 = Button(self, text = "Play Again", width = 8, height = 1,\
                    command = lambda: self.createGrid(canvas, w, h, game))
        o1.configure(fg = "black", bg = "white", relief = FLAT,\
                    font = ("Helvetica", 30))
        o1_window = canvas.create_window(w/4, 3*h/4, anchor = CENTER, window = o1)

        o2 = Button(self, text = "More Options", width = 10, height = 1)
        o2.configure(fg = "black", bg = "white", relief = FLAT,\
                    font = ("Helvetica", 30), command = lambda: \
                     self.moreOptions(canvas, w, h, game, o1, o2))
        o2_window = canvas.create_window(3*w/4, 3*h/4, anchor = CENTER, window = o2)

    # gives user more post-game options
    def moreOptions(self, canvas, w, h, game, o1, o2):
        o2.destroy()
        if game == "Tic-Tac-Toe":
            game = "Misere"
        else:
            game= "Tic-Tac-Toe"

        if game == "Misere":
            textGame = game
        else:
            textGame = "T. T. T."
        
        o1.configure(text = "Play {}".format(textGame), width = 10, command = lambda: \
                     self.createGrid(canvas, w, h, game))
        
        o3 = Button(self, text = "Quit", width = 3, height = 1, command = lambda: \
                    self.quit(canvas, w, h))
        o3.configure(fg = "black", bg = "white", relief = FLAT,\
                    font = ("Helvetica", 30))
        o3_window = canvas.create_window(3*w/4, 3*h/4, anchor = CENTER, window = o3)

    # clears canvas and tells user to quit
    def quit(self, canvas, w, h):
        canvas.delete("all")
        Label1 = Label(self, text = "You can exit the program now.")
        Label1.configure(width = 28, bg = "white", fg = "black", font = ("Helvetica", 25))
        Label1_window = canvas.create_window(w/2, h/2, anchor = CENTER, window = Label1)
    
# dimensions of the GUI
WIDTH = 500
HEIGHT = 500

# start the GUI
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Tic Tac Toe")
t = Game(window)
t.mainmenu(WIDTH, HEIGHT)
window.mainloop()
