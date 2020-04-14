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

    def mainmenu(self, w, h):
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

        # game descriptions
        d1 = Label(self, text = "Traditional X and O rules,")
        d1.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        d1_window = canvas.create_window(w/4, 5*h/8, anchor = CENTER, window = d1)

        d2 = Label(self, text = "first to make three in a row, wins")
        d2.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        d2_window = canvas.create_window(w/4, 43*h/64, anchor = CENTER, window = d2)

        d3 = Label(self, text = "Every player plays X and the")
        d3.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        d3_window = canvas.create_window(3*w/4, 5*h/8, anchor = CENTER, window = d3)

        d4 = Label(self, text = "first to make three in a row, loses")
        d4.configure(width = 25, bg = "white", fg = "black", font = ("Helvetica", 10))
        d4_window = canvas.create_window(3*w/4, 43*h/64, anchor = CENTER, window = d4)

    def tictactoe(self, w, h, canvas):
        # create tic tac toe grid
        game = "Tic-Tac-Toe"
        self.createGrid(canvas, w, h, game)

    def misere(self, w, h, canvas):
        # create tic tac toe grid
        game = "Misere"
        self.createGrid(canvas, w, h, game)

    def createGrid(self, canvas, w, h, game):
        # clear canvas and reset turn counter
        canvas.delete("all")
        self.turn = 0
        
        # create scoreboard
        title = Label(self, text = game)
        title.configure(width = 50, bg = "blue", fg = "red", font = ("Helvetica", 40))
        title_window = canvas.create_window(w/2, 25, anchor = CENTER, window = title)

        user = Label(self, text = "You: {}".format(self.userPoints))
        user.configure(width = 7, bg = "white", fg = "red", font = ("Helvetica", 20))
        user_window = canvas.create_window(w/4, 77, anchor = CENTER, window = user)

        tie = Label(self, text = "Draws: {}".format(self.ties))
        tie.configure(width = 8, bg = "white", fg = "black", font = ("Helvetica", 20))
        tie_window = canvas.create_window(w/2, 77, anchor = CENTER, window = tie)

        cpu = Label(self, text = "CPU: {}".format(self.cpuPoints))
        cpu.configure(width = 7, bg = "white", fg = "blue", font = ("Helvetica", 20))
        cpu_window = canvas.create_window(3*w/4, 77, anchor = CENTER, window = cpu)

        # create vertical lines
        canvas.create_line(w/3, 110, w/3, h-10)
        canvas.create_line(2*w/3, 110, 2*w/3, h-10)
        
        # create horizontal lines
        canvas.create_line(10, (h-100)/3+100, w-10, (h-100)/3+100)
        canvas.create_line(10, 2*(h-100)/3+100, w-10, 2*(h-100)/3+100)
        
        # square one
        s1 = Button(self, text = " ", width = 4, height = 1,\
                    command = lambda: self.playX(s1, "red") if (self.turn%2 == 0)\
                    else self.playO(s1, "blue"))
        s1.configure(fg = "white", bg = "white", relief = FLAT,\
                     font = ("Helvetica", 45))
        s1_window = canvas.create_window(10, 110, anchor = NW, window = s1)

        # rest of squares

    # fills in button with X
    def playX(self, s, color):
        s.configure(text = "X", fg = color)
        self.turn += 1

    # fills in button with O
    def playO(self, s, color):
        s.configure(text = "O", fg = color)
        self.turn += 1

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
