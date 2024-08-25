import pygame
import sys
import time
import random
from tkinter import*
from tkinter import messagebox



class Kenjie:
    def __init__(self):
        pygame.init()
        self.w = 500
        self.h = 600
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.fps = pygame.time.Clock()
        self.run = True
        self.click1 = False
        self.click2 = False
        self.click3 = False
        self.click4 = False
        self.click5 = False
        self.start = False
        self.meno = True
        self.score = 0


        self.s =False
        self.c =False
        self.star =False
        self.f =False
        self.tik =False

        self.width = (self.w - 200) // 2
        self.height = (self.h-40 ) // 2
        self.wide = 200
        self.tall = 40

        self.font = pygame.font.SysFont(None,40)

        self.snake_button = pygame.Rect(self.width,self.height-200,self.wide,self.tall)
        self.calculator_button = pygame.Rect(self.width,self.height-100,self.wide,self.tall)
        self.star_button = pygame.Rect(self.width,self.height,self.wide,self.tall)
        self.flappy_button = pygame.Rect(self.width,self.height+100,self.wide,self.tall)
        self.tiktactoe_button = pygame.Rect(self.width,self.height+200,self.wide,self.tall)
        self.exit = pygame.Rect(445,10,self.wide,self.tall)
        self.back = pygame.Rect(10,10,70,self.tall)

        self.upheight = random.randint(50, 450)


    def draw(self,text,font,color,x,y):
        im = self.font.render(text,True,color)
        self.screen.blit(im, (x,y))
    def menu(self):
        while not self.s and not self.f and not self.c and not self.star and not self.tik and self.run and self.meno:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            position = pygame.mouse.get_pos()
            self.screen.fill('black')
            pygame.draw.rect(self.screen, 'white', self.snake_button)
            pygame.draw.rect(self.screen, 'white', self.calculator_button)
            pygame.draw.rect(self.screen, 'white', self.star_button)
            pygame.draw.rect(self.screen, 'white', self.flappy_button)
            pygame.draw.rect(self.screen, 'white', self.tiktactoe_button)


            self.draw('SNAKE','arial','black',self.width+50,self.height-190)
            self.draw('CALCULATOR','arial','black',self.width+5,self.height-90)
            self.draw('JAW BALLS','arial','black',self.width+20,self.height+5)
            self.draw('FLAPPY','arial','black',self.width+45,self.height+105)
            self.draw('TICTACTOE','arial','black',self.width+15,self.height+205)




            if self.snake_button.collidepoint(position):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.click1 = True
                    self.meno = False
                    self.snake()
                    self.s = True

                if pygame.mouse.get_pressed()[0] == 0:
                    self.click1 = False
                    self.s = False

            if self.calculator_button.collidepoint(position):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.meno = False
                    self.click2 = True
                    self.calculator()
                    self.c = True

                if pygame.mouse.get_pressed()[0] == 0:
                    self.click2 = False
                    self.c = False
            if self.star_button.collidepoint(position):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.meno = False
                    self.click3 = True
                    self.starwars()
                    self.star = True
                if pygame.mouse.get_pressed()[0] == 0:
                    self.click3 = False
                    self.star = False
            if self.flappy_button.collidepoint(position):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.meno = False
                    self.click4 = True
                    self.flappy()
                    self.f = True
                if pygame.mouse.get_pressed()[0] == 0:
                    self.click3 = False
                    self.f = False
            if self.tiktactoe_button.collidepoint(position):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.meno = False
                    self.click5 = True
                    self.tiktactoe()
                    self.tik = True
                if pygame.mouse.get_pressed()[0] == 0:
                    self.click5 = False
                    self.tik = False
            pygame.draw.rect(self.screen, 'white', self.exit)
            self.draw('exit', 'arial', 'red', 445, 10)
            if self.exit.collidepoint(position):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.run = False
                if pygame.mouse.get_pressed()[0] == 0:
                    self.run = True


            pygame.display.update()
            self.fps.tick(100)
    def bak(self):
        pygame.draw.rect(self.screen, 'white', self.back)
        self.draw('back', 'arial', 'red', 10, 10)
        position = pygame.mouse.get_pos()
        if self.back.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1:
                self.meno = True
                self.menu()
                if self.s == True:
                    self.s = False
                if self.c == True:
                    self.c = False
                if self.star == True:
                    self.star = False
                if self.f == True:
                    self.f = False
                if self.tik == True:
                    self.tik = False
            if pygame.mouse.get_pressed()[0] == 0:
                self.meno = False

    def snake(self):
        snake_bod = [[200,200],[200,200],[200,200],[200,200],[200,200]]
        head = [200,200]
        food = [random.randrange(1, (self.w // 10)) * 10, random.randrange(1, (self.h // 10)) * 10]
        direction = 'r'
        change = direction
        spawn = False
        while self.click1 and self.run and self.s:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        change = 'u'
                    if event.key == pygame.K_DOWN:
                        change = 'd'
                    if event.key == pygame.K_RIGHT:
                        change = 'r'
                    if event.key == pygame.K_LEFT:
                        change = 'l'

            if change == 'u' and direction != 'd':
                direction ='u'
            if change == 'd' and direction != 'u':
                direction ='d'
            if change == 'r' and direction != 'l':
                direction ='r'
            if change == 'l' and direction != 'r':
                direction ='l'
            if change == 'u':
                head[1] -= 10
            if direction == 'd':
                head[1] += 10
            if direction == 'r':
                head[0] += 10
            if direction == 'l':
                head[0] -= 10

            snake_bod.insert(0, list(head))
            if head == food:
                spawn = False
            else:
                snake_bod.pop()
            if not spawn:
                food = [random.randrange(1, (self.w // 10)) * 10, random.randrange(1, (self.h // 10)) * 10]
                spawn = True
            self.screen.fill('green')

            for pos in snake_bod:
                pygame.draw.rect(self.screen,'red',pygame.Rect(pos[0],pos[1],10,10))
                if pos != snake_bod[0] and pos == head[0]:
                    self.gameover()
            if head[0] < 0:
                head[0] = 500
            if head[0] > 500:
                head[0] = 0
            if head[1] < 0:
                head[1] = 500
            if head[1] > 500:
                head[1] = 0

            pygame.draw.rect(self.screen, 'red', pygame.Rect(food[0], food[1], 10, 10))

            self.bak()

            pygame.display.update()

            self.fps.tick(15)
    def gameover(self):
        self.screen.fill('black')
        skor = self.font.render('your score is: '+str(self.score),True,'white')
        end = self.font.render('GAMEOVER',True,'red')
        self.screen.blit(skor,(50,50))
        self.screen.blit(end,(76,100))
        pygame.display.update()
        time.sleep(3)
        sys.exit()
    def calculator(self):
        pygame.quit()
        def bp(y):
            global p
            p = p + str(y)
            p_label.set(p)

        def e():
            global p
            try:
                t = str(eval(p))
                p_label.set(t)
                p = t
            except ArithmeticError:
                p_label.set("")
                p = ""

        def c():
            global p
            p = ""
            p_label.set("")

        q = Tk()
        p = " "
        p_label = StringVar()
        l = Label(q, height=4, width=20, textvariable=p_label, font="arial,10", bg='red')
        l.pack()
        f = Frame(q)
        f.pack()
        b1 = Button(f, text="1", font="arial,10", height=4, width=7, command=lambda: bp(1))
        b2 = Button(f, text="2", font="arial,10", height=4, width=7, command=lambda: bp(2))
        b3 = Button(f, text="3", font="arial,10", height=4, width=7, command=lambda: bp(3))
        b4 = Button(f, text="4", font="arial,10", height=4, width=7, command=lambda: bp(4))
        b5 = Button(f, text="5", font="arial,10", height=4, width=7, command=lambda: bp(5))
        b6 = Button(f, text="6", font="arial,10", height=4, width=7, command=lambda: bp(6))
        b7 = Button(f, text="7", font="arial,10", height=4, width=7, command=lambda: bp(7))
        b8 = Button(f, text="8", font="arial,10", height=4, width=7, command=lambda: bp(8))
        b9 = Button(f, text="9", font="arial,10", height=4, width=7, command=lambda: bp(9))
        b0 = Button(f, text="0", font="arial,10", height=4, width=7, command=lambda: bp(0))

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)
        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)
        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)
        b0.grid(row=3, column=0)

        plus = Button(f, text="+", font="arial,10", height=4, width=7, command=lambda: bp('+'))
        minus = Button(f, text="-", font="arial,10", height=4, width=7, command=lambda: bp('-'))
        divide = Button(f, text="/", font="arial,10", height=4, width=7, command=lambda: bp('/'))
        multiply = Button(f, text="*", font="arial,10", height=4, width=7, command=lambda: bp('*'))
        dicimal = Button(f, text=".", font="arial,10", height=4, width=7, command=lambda: bp('.'))
        equal = Button(f, text="=", font="arial,10", height=4, width=7, command=lambda: e())
        clear = Button(f, text="clear", font="arial,10", height=4, width=7, command=lambda: c())
        plus.grid(row=0, column=3)
        minus.grid(row=1, column=3)
        divide.grid(row=2, column=3)

        multiply.grid(row=3, column=1)
        dicimal.grid(row=3, column=2)
        equal.grid(row=3, column=3)
        clear.grid(row=4, column=0)
        q.mainloop()
        pygame.init()


    def starwars(self):
        pos = [self.w // 2, self.h // 2]
        speed = [10, 10]
        size = 20
        while self.click3 and self.run and self.star:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            pos[0] += speed[0]
            pos[1] += speed[1]

            if pos[0] > self.w - size or pos[0] < size:
                speed[0] = -speed[0]
            if pos[1] > self.h - size or pos[1] < size:
                speed[1] = -speed[1]

            pygame.draw.circle(self.screen, 'white', pos, size)
            pygame.display.flip()

            self.fps.tick(20)

            self.screen.fill('black')
            self.bak()

            pygame.display.update()

            self.fps.tick(100)
    def flappy(self):
        gap = 100
        self.downheight = self.h - self.upheight - gap
        walldown = [self.w, self.upheight + gap]
        wallup = [self.w, 0]
        birdy = [200, 200, 50, 20]
        self.skoor = 0
        self.scurr = 0
        def process():
            pygame.draw.rect(self.screen, 'white', pygame.Rect(birdy[0], birdy[1], 35, 15))
            birdy[1] += 5

            pygame.draw.rect(self.screen, 'white', pygame.Rect(wallup[0], wallup[1], 50, self.upheight))
            pygame.draw.rect(self.screen, 'white', pygame.Rect(walldown[0], walldown[1], 50, self.downheight))
        def collide():
            bird = pygame.draw.rect(self.screen, 'white', pygame.Rect(birdy[0], birdy[1], 35, 15))
            up = pygame.draw.rect(self.screen, 'white', pygame.Rect(wallup[0], wallup[1], 50, self.upheight))
            down = pygame.draw.rect(self.screen, 'white', pygame.Rect(walldown[0], walldown[1], 50, self.downheight))
            if bird.colliderect(up) or bird.colliderect(down):
                return True
            return False
        def gameover():
            self.screen.fill('white')
            self.draw('YOU DIED BITCH', 'arial', 'black',(150),(100))
            self.draw('score: '+str(self.scurr), 'arial', 'black',(150),(200))
            pygame.display.flip()
            time.sleep(2)
            sys.exit()


        def click():
            self.draw('score: '+str(self.scurr),'arial','black',200,10)
            wallup[0] -= 5
            walldown[0] -= 5
            if wallup[0] == 0:
                self.upheight = random.randint(50, 450)
                self.downheight = self.h - self.upheight - gap
                wallup[0] = self.w
                walldown[0] =self.w
                walldown[1] = self.upheight +gap
            if wallup[0] < 250:
                self.skoor += 1
                self.scurr = int(self.skoor/39)
            if collide():
                gameover()
            if birdy[1] == self.h:
                gameover()
            if birdy[1] == 0:
                gameover()



        while self.click4 and self.run and self.f:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        birdy[1] -= 55
            self.screen.fill('blue')
            click()
            process()
            self.bak()

            pygame.display.update()

            self.fps.tick(40)
    def tiktactoe(self):
        pygame.quit()

        window = Tk()

        click = True
        attempt = 0

        def c_w():
            global winner
            winner = False

            if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
                winner = True
                messagebox.showinfo("X WON")
                reset()
            elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
                winner = True
                messagebox.showinfo("X WON")
                reset()
            elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
                winner = True
                messagebox.showinfo("X WON")
                reset()
            elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
                winner = True
                messagebox.showinfo("X WON")
                reset()
            elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
                winner = True
                messagebox.showinfo("X WON")
                reset()
            elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
                winner = True
                messagebox.showinfo("X WON")
                reset()
            elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
                winner = True
                messagebox.showinfo("X WON")
                reset()
            elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
                winner = True
                messagebox.showinfo("X WON")
                reset()

            if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
                winner = True
                messagebox.showinfo("O WON")
                reset()
            elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
                winner = True
                messagebox.showinfo("O WON")
                reset()
            elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
                winner = True
                messagebox.showinfo("O WON")
                reset()
            elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
                winner = True
                messagebox.showinfo("O WON")
                reset()
            elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
                winner = True
                messagebox.showinfo("O WON")
                reset()
            elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
                winner = True
                messagebox.showinfo("O WON")
                reset()
            elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
                winner = True
                messagebox.showinfo("O WON")
                reset()
            elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
                winner = True
                messagebox.showinfo("O WON")
                reset()

        def b_p(b):
            global click, attempt
            if b["text"] == " " and click == False:
                b["text"] = "X"
                click = True
                attempt += 1
                c_w()
            elif b["text"] == " " and click == True:
                b["text"] = "O"
                click = False
                attempt += 1
                c_w()
            else:
                messagebox.showinfo("Taken")

        def reset():
            global b1, b2, b3, b4, b5, b6, b7, b8, b9
            global attempt, click
            attempt = 0
            click = False

            b1 = Button(window, font='arial, 9', text=" ", height=5, width=5, command=lambda: b_p(b1))
            b2 = Button(window, font='arial, 9', text=" ", height=5, width=5, command=lambda: b_p(b2))
            b3 = Button(window, font='arial, 9', text=" ", height=5, width=5, command=lambda: b_p(b3))
            b4 = Button(window, font='arial, 9', text=" ", height=5, width=5, command=lambda: b_p(b4))
            b5 = Button(window, font='arial, 9', text=" ", height=5, width=5, command=lambda: b_p(b5))
            b6 = Button(window, font='arial, 9', text=" ", height=5, width=5, command=lambda: b_p(b6))
            b7 = Button(window, font='arial, 9', text=" ", height=5, width=5, command=lambda: b_p(b7))
            b8 = Button(window, font='arial, 9', text=" ", height=5, width=5, command=lambda: b_p(b8))
            b9 = Button(window, font='arial, 9', text=" ", height=5, width=5, command=lambda: b_p(b9))

            b1.grid(row=0, column=0)
            b2.grid(row=0, column=1)
            b3.grid(row=0, column=2)
            b4.grid(row=1, column=0)
            b5.grid(row=1, column=1)
            b6.grid(row=1, column=2)
            b7.grid(row=2, column=0)
            b8.grid(row=2, column=1)
            b9.grid(row=2, column=2)

        reset()

        window.mainloop()

        pygame.init()


    def running(self):
        while self.run:
            self.menu()
            if self.s:
                self.snake()
            if self.c:
                self.calculator()
                self.c = False
            if self.star:
                self.starwars()
            if self.f:
                self.flappy()
            if self.tik:
                self.tiktactoe()

        pygame.quit()
        sys.exit()
if __name__ == "__main__":
    game = Kenjie()
    game.running()