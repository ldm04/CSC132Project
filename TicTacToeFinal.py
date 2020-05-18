#1. Implement main menu stats option - DONE
#2. Implement basic stats screen - DONE
        #1. Refactor score variables - DONE
        #2. add stats screen variables and visuals - DONE
#3. Implement Save File - DONE
        #1. open and close save file at correct times, change both local scoreboard variable and stats variable - DONE
#5. Implement nuke save file option in main menu - DONE
        #1. Delete save file using os.remove - DONE

from Tkinter import *
import os.path
from os import path, remove

class Game(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

        # turn counter
        self.turn = 0
        # point variables
        #Local variables for this session
        self.localTotalTTTGamesvCPU = 0
        self.localTotalTTTGamesvPlayer = 0
        self.localTotalMisereGamesvCPU = 0
        self.localTotalMisereGamesvPlayer = 0
        self.localUserTTTWinsvCPU = 0
        self.localUserTTTWinsvPlayer = 0
        self.localUserMisereWinsvCPU = 0
        self.localUserMisereWinsvPlayer = 0
        self.localUserTTTTiesvCPU = 0
        self.localUserTTTTiesvPlayer = 0
        self.localUserMisereTiesvCPU = 0
        self.localUserMisereTiesvPlayer = 0
        
        #Variables read and written to and from save file
        self.statsTotalTTTGamesvCPU = 0
        self.statsTotalTTTGamesvPlayer = 0
        self.statsTotalMisereGamesvCPU = 0
        self.statsTotalMisereGamesvPlayer = 0
        self.statsUserTTTWinsvCPU = 0
        self.statsUserTTTWinsvPlayer = 0
        self.statsUserMisereWinsvCPU = 0
        self.statsUserMisereWinsvPlayer = 0
        self.statsUserTTTTiesvCPU = 0
        self.statsUserTTTTiesvPlayer = 0
        self.statsUserMisereTiesvCPU = 0
        self.statsUserMisereTiesvPlayer = 0

        
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

        b3 = Button(self, text = "Tic Tac Toe (PvP)", command = lambda: self.PvPtictactoe(w, h, canvas))
        b3.configure(width = 20, activebackground = "gray", relief = FLAT, font = ("Helvetica", 10))
        b3_window = canvas.create_window(w/4, 3*h/4, anchor = CENTER, window = b3)

        b4 = Button(self, text = "Misere (PvP)", command = lambda: self.PvPmisere(w, h, canvas))
        b4.configure(width = 20, activebackground = "gray", relief = FLAT, font = ("Helvetica", 10))
        b4_window = canvas.create_window(3*w/4, 3*h/4, anchor = CENTER, window = b4)

        #Opens the Statistics screen
        b5 = Button(self, text = "Statistics", command = lambda: self.statisticsScreen(w, h, canvas))
        b5.configure(width = 10, activebackground = "gray", relief = FLAT, font = ("Helvetica", 15))
        b5_window = canvas.create_window(w/2, 7*h/8, anchor = CENTER, window = b5)

        b6 = Button(self, text = "Nuke Save?", command = lambda: self.nukeStats(w, h, canvas))
        b6.configure(width = 10, activebackground = "gray", relief = FLAT, font = ("Helvetica", 8))
        b6_window = canvas.create_window(3*w/4, 7*h/8, anchor = CENTER, window = b6)

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

    def statisticsScreen(self, w, h, canvas):
        canvas.pack(side = TOP, anchor = NW)
        canvas.delete("all")
        #Statistics Screen

        CheckSave = path.exists("TTTSave.txt")
        if (CheckSave == False):
            Save = open("TTTSave.txt", "w+")
            for i in range(12):
                Save.write("0\n")
            Save.close()
        Save = open("TTTSave.txt", "r")
        SaveContents = Save.readlines()
        self.statsTotalTTTGamesvCPU = int(SaveContents[0])
        self.statsTotalTTTGamesvPlayer = int(SaveContents[1])
        self.statsTotalMisereGamesvCPU = int(SaveContents[2])
        self.statsTotalMisereGamesvPlayer = int(SaveContents[3])
        self.statsUserTTTWinsvCPU = int(SaveContents[4])
        self.statsUserTTTWinsvPlayer = int(SaveContents[5])
        self.statsUserMisereWinsvCPU = int(SaveContents[6])
        self.statsUserMisereWinsvPlayer = int(SaveContents[7])
        self.statsUserTTTTiesvCPU = int(SaveContents[8])
        self.statsUserTTTTiesvPlayer = int(SaveContents[9])
        self.statsUserMisereTiesvCPU = int(SaveContents[10])
        self.statsUserMisereTiesvPlayer = int(SaveContents[11])
        Save.close()
        
        q1 = Label(self, text = "Statistics!")
        q1.configure(width = 25, bg = "white", fg = "red", font = ("Helvetica", 25))
        q1_window = canvas.create_window(w/2, h/12, anchor = CENTER, window = q1)

        q2 = Label(self, text = "Wins")
        q2.configure(width = 15, bg = "white", fg = "blue", font = ("Helvetica", 15))
        q2_window = canvas.create_window(w/6, h/7, anchor = CENTER, window = q2)

        q3 = Label(self, text = "Ties")
        q3.configure(width = 15, bg = "white", fg = "blue", font = ("Helvetica", 15))
        q3_window = canvas.create_window(w/2, h/7, anchor = CENTER, window = q3)

        q4 = Label(self, text = "Losses")
        q4.configure(width = 15, bg = "white", fg = "blue", font = ("Helvetica", 15))
        q4_window = canvas.create_window(5*w/6, h/7, anchor = CENTER, window = q4)

        q5 = Label(self, text = "Total TTT Games: {}".format(self.statsTotalTTTGamesvCPU+self.statsTotalTTTGamesvPlayer))
        q5.configure(width = 20, bg = "white", fg = "blue", font = ("Helvetica", 8))
        q5_window = canvas.create_window(w/8, 8*h/10, anchor = CENTER, window = q5)

        q6 = Label(self, text = "Total Misere Games: {}".format(self.statsTotalMisereGamesvCPU+self.statsTotalMisereGamesvPlayer))
        q6.configure(width = 20, bg = "white", fg = "blue", font = ("Helvetica", 8))
        q6_window = canvas.create_window(3*w/8, 8*h/10, anchor = CENTER, window = q6)

        if (self.statsTotalTTTGamesvCPU == 0 and self.statsTotalMisereGamesvCPU == 0):
            CPUwinpct = 0
        else:
            CPUwinpct = ((self.statsUserTTTWinsvCPU+self.statsUserMisereWinsvCPU)/(self.statsTotalTTTGamesvCPU+self.statsTotalMisereGamesvCPU)*100.0)
        q7 = Label(self, text = "Win% vs CPU: {}%".format(CPUwinpct))
        q7.configure(width = 20, bg = "white", fg = "blue", font = ("Helvetica", 8))
        q7_window = canvas.create_window(5*w/8, 8*h/10, anchor = CENTER, window = q7)

        if (self.statsTotalTTTGamesvPlayer == 0 and self.statsTotalMisereGamesvPlayer == 0):
            Playerwinpct = 0
        else:
            Playerwinpct = ((self.statsUserTTTWinsvPlayer+self.statsUserMisereWinsvPlayer)/(self.statsTotalTTTGamesvPlayer+self.statsTotalMisereGamesvPlayer)*100.0)

        q7 = Label(self, text = "Win% vs Player 2: {}%".format(Playerwinpct))
        q7.configure(width = 20, bg = "white", fg = "blue", font = ("Helvetica", 8))
        q7_window = canvas.create_window(7*w/8, 8*h/10, anchor = CENTER, window = q7)
        
        c1 = Label(self, text = "TTT Vs CPU: {} ".format(self.statsUserTTTWinsvCPU))
        c1.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        c1_window = canvas.create_window(w/6, 2*h/8, anchor = CENTER, window = c1)

        c2 = Label(self, text = "Misere Vs CPU: {}".format(self.statsUserMisereWinsvCPU))
        c2.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        c2_window = canvas.create_window(w/6, 3*h/8, anchor = CENTER, window = c2)

        c3 = Label(self, text = "TTT Vs Player 2: {}".format(self.statsUserTTTWinsvPlayer))
        c3.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        c3_window = canvas.create_window(w/6, 4*h/8, anchor = CENTER, window = c3)

        c4 = Label(self, text = "Misere Vs Player 2: {}".format(self.statsUserMisereWinsvPlayer))
        c4.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        c4_window = canvas.create_window(w/6, 5*h/8, anchor = CENTER, window = c4)

        c5 = Label(self, text = "TTT Vs CPU: {} ".format(self.statsTotalTTTGamesvCPU-(self.statsUserTTTWinsvCPU+self.statsUserTTTTiesvCPU)))
        c5.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        c5_window = canvas.create_window(5*w/6, 2*h/8, anchor = CENTER, window = c5)

        c6 = Label(self, text = "Misere Vs CPU: {}".format(self.statsTotalMisereGamesvCPU-(self.statsUserMisereWinsvCPU+self.statsUserMisereTiesvCPU)))
        c6.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        c6_window = canvas.create_window(5*w/6, 3*h/8, anchor = CENTER, window = c6)

        c7 = Label(self, text = "TTT Vs Player 2: {}".format(self.statsTotalTTTGamesvPlayer-(self.statsUserTTTWinsvPlayer+self.statsUserTTTTiesvPlayer)))
        c7.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        c7_window = canvas.create_window(5*w/6, 4*h/8, anchor = CENTER, window = c7)

        c8 = Label(self, text = "Misere Vs Player 2: {}".format(self.statsTotalMisereGamesvPlayer-(self.statsUserMisereWinsvPlayer+self.statsUserMisereTiesvPlayer)))
        c8.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        c8_window = canvas.create_window(5*w/6, 5*h/8, anchor = CENTER, window = c8)

        c9 = Label(self, text = "TTT Vs CPU: {} ".format(self.statsUserTTTTiesvCPU))
        c9.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        c9_window = canvas.create_window(w/2, 2*h/8, anchor = CENTER, window = c9)

        c10 = Label(self, text = "Misere Vs CPU: {}".format(self.statsUserMisereTiesvCPU))
        c10.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        c10_window = canvas.create_window(w/2, 3*h/8, anchor = CENTER, window = c10)

        c11 = Label(self, text = "TTT Vs Player 2: {}".format(self.statsUserTTTTiesvPlayer))
        c11.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        c11_window = canvas.create_window(w/2, 4*h/8, anchor = CENTER, window = c11)

        c12 = Label(self, text = "Misere Vs Player 2: {}".format(self.statsUserMisereTiesvPlayer))
        c12.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        c12_window = canvas.create_window(w/2, 5*h/8, anchor = CENTER, window = c12)

        b1 = Button(self, text = "Quit", command = lambda: self.quit(canvas, w, h))
        b1.configure(width = 10, activebackground = "gray", relief = FLAT, font = ("Helvetica", 15))
        b1_window = canvas.create_window(w/2, 7*h/8, anchor = CENTER, window = b1)

    def nukeStats(self, w, h, canvas):
        os.remove("TTTSave.txt")
        print("I hope that was on purpose!")

    def createGrid(self, canvas, w, h, game):
        # clear canvas and reset turn counter
        canvas.delete("all")
        canvas.pack(side = TOP, anchor = NW)
        self.turn = 0

        # clear spaces dictionary
        for space in self.spaces:
            self.spaces[space] = " "
        
        # create scoreboard
        if game == "Tic-Tac-Toe":
            #run this scoreboard for TTT games vs CPU
            title = Label(self, text = game)
            title.configure(width = 50, bg = "blue", fg = "red", font = ("Helvetica", 40))
            title_window = canvas.create_window(w/2, 25, anchor = CENTER, window = title)

            cpu = Label(self, text = "CPU: {}".format(self.localTotalTTTGamesvCPU - (self.localUserTTTWinsvCPU+self.localUserTTTTiesvCPU)))
            cpu.configure(width = 7, bg = "white", fg = "red", font = ("Helvetica", 20))
            cpu_window = canvas.create_window(w/4, 77, anchor = CENTER, window = cpu)

            tie = Label(self, text = "Draws: {}".format(self.localUserTTTTiesvCPU))
            tie.configure(width = 8, bg = "white", fg = "black", font = ("Helvetica", 20))
            tie_window = canvas.create_window(w/2, 77, anchor = CENTER, window = tie)

            user = Label(self, text = "You: {}".format(self.localUserTTTWinsvCPU))
            user.configure(width = 7, bg = "white", fg = "blue", font = ("Helvetica", 20))
            user_window = canvas.create_window(3*w/4, 77, anchor = CENTER, window = user)

        # create scoreboard
        elif game == "Misere":
            #run this scoreboard for Misere games vs CPU
            title = Label(self, text = game)
            title.configure(width = 50, bg = "blue", fg = "red", font = ("Helvetica", 40))
            title_window = canvas.create_window(w/2, 25, anchor = CENTER, window = title)

            cpu = Label(self, text = "CPU: {}".format(self.localTotalMisereGamesvCPU - (self.localUserMisereWinsvCPU+self.localUserMisereTiesvCPU)))
            cpu.configure(width = 7, bg = "white", fg = "red", font = ("Helvetica", 20))
            cpu_window = canvas.create_window(w/4, 77, anchor = CENTER, window = cpu)

            tie = Label(self, text = "Draws: {}".format(self.localUserMisereTiesvCPU))
            tie.configure(width = 8, bg = "white", fg = "black", font = ("Helvetica", 20))
            tie_window = canvas.create_window(w/2, 77, anchor = CENTER, window = tie)

            user = Label(self, text = "You: {}".format(self.localUserMisereWinsvCPU))
            user.configure(width = 7, bg = "white", fg = "blue", font = ("Helvetica", 20))
            user_window = canvas.create_window(3*w/4, 77, anchor = CENTER, window = user)

        #Scoreboard for PvP games

        elif game == "Tic-Tac-Toe (PvP)":
            #run this scoreboard for TTT games vs Player
            title = Label(self, text = game)
            title.configure(width = 50, bg = "blue", fg = "red", font = ("Helvetica", 40))
            title_window = canvas.create_window(w/2, 25, anchor = CENTER, window = title)

            Player2 = Label(self, text = "Player Two: {}".format(self.localTotalTTTGamesvPlayer - (self.localUserTTTWinsvPlayer+self.localUserTTTTiesvPlayer)))
            Player2.configure(width = 10, bg = "white", fg = "red", font = ("Helvetica", 20))
            Player2_window = canvas.create_window(3*w/16, 77, anchor = CENTER, window = Player2)

            tie = Label(self, text = "Draws: {}".format(self.localUserTTTTiesvPlayer))
            tie.configure(width = 8, bg = "white", fg = "black", font = ("Helvetica", 20))
            tie_window = canvas.create_window(w/2, 77, anchor = CENTER, window = tie)

            user = Label(self, text = "Player One: {}".format(self.localUserTTTWinsvPlayer))
            user.configure(width = 10, bg = "white", fg = "blue", font = ("Helvetica", 20))
            user_window = canvas.create_window(13*w/16, 77, anchor = CENTER, window = user)

        elif game == "Misere (PvP)":
            #run this scoreboard for Misere games vs Player
            title = Label(self, text = game)
            title.configure(width = 50, bg = "blue", fg = "red", font = ("Helvetica", 40))
            title_window = canvas.create_window(w/2, 25, anchor = CENTER, window = title)

            Player2 = Label(self, text = "Player Two: {}".format(self.localTotalMisereGamesvPlayer - (self.localUserMisereWinsvPlayer+self.localUserMisereTiesvPlayer)))
            Player2.configure(width = 10, bg = "white", fg = "red", font = ("Helvetica", 20))
            Player2_window = canvas.create_window(3*w/16, 77, anchor = CENTER, window = Player2)

            tie = Label(self, text = "Draws: {}".format(self.localUserMisereTiesvPlayer))
            tie.configure(width = 8, bg = "white", fg = "black", font = ("Helvetica", 20))
            tie_window = canvas.create_window(w/2, 77, anchor = CENTER, window = tie)

            user = Label(self, text = "Player One: {}".format(self.localUserMisereWinsvPlayer))
            user.configure(width = 10, bg = "white", fg = "blue", font = ("Helvetica", 20))
            user_window = canvas.create_window(13*w/16, 77, anchor = CENTER, window = user)
        

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
        if game == "Tic-Tac-Toe" or game == "Misere":
            if game == "Tic-Tac-Toe":
                self.playX(s1, "red", "s1", canvas, game, w, h)
            else:
                self.playX(s5, "red", "s5", canvas, game, w, h)

    # creates squares as blank buttons
    def createSquare(self, w, h, game, canvas, dictS):
        s = Button(self, text = " ", width = 4, height = 1,\
                    command = lambda: self.playX(s, "red", dictS, canvas, game, w, h)\
                    if self.turn%2 == 0 else self.playO(s, "blue", dictS, canvas, game, w, h))
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
            if game == "Tic-Tac-Toe" or game == "Misere":
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

        outcomeArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if state == "win":
            #disable all grid squares if game is over
            s1["state"] = DISABLED
            s2["state"] = DISABLED
            s3["state"] = DISABLED
            s4["state"] = DISABLED
            s5["state"] = DISABLED
            s6["state"] = DISABLED
            s7["state"] = DISABLED
            s8["state"] = DISABLED
            s9["state"] = DISABLED
            
            if game == "Tic-Tac-Toe":
                if self.turn%2 == 0:
                    self.localTotalTTTGamesvCPU += 1
                    outcomeArray[0] = 1
                    result = Label(self, text = "THE CPU WINS")
                    result.configure(width = 13, bg = "white", fg = "red", font = ("Helvetica", 30))
                    result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)
                else:
                    self.localUserTTTWinsvCPU += 1
                    self.localTotalTTTGamesvCPU += 1
                    outcomeArray[4] = 1
                    outcomeArray[0] = 1
                    result = Label(self, text = "YOU WIN")
                    result.configure(width = 8, bg = "white", fg = "blue", font = ("Helvetica", 30))
                    result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)
            elif game == "Misere":
                if self.turn%2 == 0:
                    self.localUserMisereWinsvCPU += 1
                    self.localTotalMisereGamesvCPU += 1
                    outcomeArray[6] = 1
                    outcomeArray[2] = 1
                    result = Label(self, text = "THE CPU LOSES")
                    result.configure(width = 14, bg = "white", fg = "blue", font = ("Helvetica", 30))
                    result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)
                else:
                    self.localTotalMisereGamesvCPU += 1
                    outcomeArray[2] = 1
                    result = Label(self, text = "YOU LOSE")
                    result.configure(width = 9, bg = "white", fg = "red", font = ("Helvetica", 30))
                    result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)
            elif game == "Tic-Tac-Toe (PvP)":
                if self.turn%2 == 0:
                    self.localTotalTTTGamesvPlayer += 1
                    outcomeArray[1] = 1
                    result = Label(self, text = "PLAYER TWO WINS")
                    result.configure(width = 18, bg = "white", fg = "red", font = ("Helvetica", 30))
                    result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)
                else:
                    self.localUserTTTWinsvPlayer += 1
                    self.localTotalTTTGamesvPlayer += 1
                    outcomeArray[5] = 1
                    outcomeArray[1] = 1
                    result = Label(self, text = "PLAYER ONE WINS")
                    result.configure(width = 18, bg = "white", fg = "blue", font = ("Helvetica", 30))
                    result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)
            else:
                if self.turn%2 == 0:
                    self.localUserMisereWinsvPlayer += 1
                    self.localTotalMisereGamesvPlayer += 1
                    outcomeArray[7] = 1
                    outcomeArray[3] = 1
                    result = Label(self, text = "PLAYER TWO LOSES")
                    result.configure(width = 18, bg = "white", fg = "blue", font = ("Helvetica", 30))
                    result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)
                else:
                    self.localTotalMisereGamesvPlayer += 1
                    outcomeArray[3] = 1
                    result = Label(self, text = "PLAYER ONE LOSES")
                    result.configure(width = 18, bg = "white", fg = "red", font = ("Helvetica", 30))
                    result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)
        else:
            if " " in self.spaces.values():
                result = False
            elif game == "Tic-Tac-Toe":
                state = "tie"
                self.localUserTTTTiesvCPU += 1
                self.localTotalTTTGamesvCPU += 1
                outcomeArray[8] = 1
                outcomeArray[0] = 1
                result = Label(self, text = "IT'S A TIE")
                result.configure(width = 9, bg = "white", fg = "black", font = ("Helvetica", 30))
                result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)
            elif game == "Misere":
                state = "tie"
                self.localUserMisereTiesvCPU += 1
                self.localTotalMisereGamesvCPU += 1
                outcomeArray[10] = 1
                outcomeArray[2] = 1
                result = Label(self, text = "IT'S A TIE")
                result.configure(width = 9, bg = "white", fg = "black", font = ("Helvetica", 30))
                result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)
            elif game == "Tic-Tac-Toe (PvP)":
                state = "tie"
                self.localUserTTTTiesvPlayer += 1
                self.localTotalTTTGamesvPlayer += 1
                outcomeArray[9] = 1
                outcomeArray[1] = 1
                result = Label(self, text = "IT'S A TIE")
                result.configure(width = 9, bg = "white", fg = "black", font = ("Helvetica", 30))
                result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)
            else:
                state = "tie"
                self.localUserMisereTiesvPlayer += 1
                self.localTotalMisereGamesvPlayer += 1
                outcomeArray[11] = 1
                outcomeArray[3] = 1
                result = Label(self, text = "IT'S A TIE")
                result.configure(width = 9, bg = "white", fg = "black", font = ("Helvetica", 30))
                result_window = canvas.create_window(250, 250, anchor = CENTER, window = result)

        #Save outcomearray to file
        CheckSave = path.exists("TTTSave.txt")
        if (CheckSave == False):
            Save = open("TTTSave.txt", "w+")
            for i in range(12):
                Save.write("0\n")
            Save.close()
        Save = open("TTTSave.txt", "r")
        SaveContents = Save.readlines()
        self.statsTotalTTTGamesvCPU = int(SaveContents[0]) + outcomeArray[0]
        self.statsTotalTTTGamesvPlayer = int(SaveContents[1]) + outcomeArray[1]
        self.statsTotalMisereGamesvCPU = int(SaveContents[2]) + outcomeArray[2]
        self.statsTotalMisereGamesvPlayer = int(SaveContents[3]) + outcomeArray[3]
        self.statsUserTTTWinsvCPU = int(SaveContents[4]) + outcomeArray[4]
        self.statsUserTTTWinsvPlayer = int(SaveContents[5]) + outcomeArray[5]
        self.statsUserMisereWinsvCPU = int(SaveContents[6]) + outcomeArray[6]
        self.statsUserMisereWinsvPlayer = int(SaveContents[7]) + outcomeArray[7]
        self.statsUserTTTTiesvCPU = int(SaveContents[8]) + outcomeArray[8]
        self.statsUserTTTTiesvPlayer = int(SaveContents[9]) + outcomeArray[9]
        self.statsUserMisereTiesvCPU = int(SaveContents[10]) + outcomeArray[10]
        self.statsUserMisereTiesvPlayer = int(SaveContents[11]) + outcomeArray[11]
        Save.close()
        Save = open("TTTSave.txt", "w+")
        Save.write(str(self.statsTotalTTTGamesvCPU) + "\n")
        Save.write(str(self.statsTotalTTTGamesvPlayer) + "\n")
        Save.write(str(self.statsTotalMisereGamesvCPU) + "\n")
        Save.write(str(self.statsTotalMisereGamesvPlayer) + "\n")
        Save.write(str(self.statsUserTTTWinsvCPU) + "\n")
        Save.write(str(self.statsUserTTTWinsvPlayer) + "\n")
        Save.write(str(self.statsUserMisereWinsvCPU) + "\n")
        Save.write(str(self.statsUserMisereWinsvPlayer) + "\n")
        Save.write(str(self.statsUserTTTTiesvCPU) + "\n")
        Save.write(str(self.statsUserTTTTiesvPlayer) + "\n")
        Save.write(str(self.statsUserMisereTiesvCPU) + "\n")
        Save.write(str(self.statsUserMisereTiesvPlayer) + "\n")
        Save.close()
                
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
            textGame = "Misere"
        elif game == "Misere":
            game = "Tic-Tac-Toe"
            textGame = "T. T. T."
        elif game == "Tic-Tac-Toe (PvP)":
            game = "Misere (PvP)"
            textGame = "Misere"
        else:
            game = "Tic-Tac-Toe (PvP)"
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

################################
#MAIN
################################
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
