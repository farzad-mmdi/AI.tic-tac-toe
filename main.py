import pygame
import time


black   	=           (0, 0, 0) 
gray        =         (127, 127, 127) 
white       =         (255, 255, 255)
red     	=           (255, 0, 0) 
green       =           (0, 255, 0) 
blue        =           (0, 0, 255)
yellow      =          (255, 255, 0) 
cyan        =          (0, 255, 255) 
magenta     =          (255, 0, 255)
transparent =          (0, 0 , 0 , 0)
background  =          (62, 168, 50)
x_color     =          (128, 17, 17)
o_color     =          (33, 137, 207)
background


pygame.init()
display_width = 800
display_height = display_width
blocksize = display_height//3
display = pygame.display.set_mode((display_width,display_height))
display.fill(white)
pygame.display.set_caption('Tic-Tac-Toe')
pygame.display.update()

x_thickness = 20
o_thickness = 20
maxplayer = 'x'
minplayer = 'o'


def SetBoard():
    board = [[0 , 0 , 0],
             [0 , 0 , 0],
             [0 , 0 , 0]]
    globals().update(locals())


def grid():
    display.fill(white)
    for x in range(0,display_width,blocksize):
        pygame.draw.line(display, black, (x,0) , (x,display_height),3)

    for y in range(0,display_height,blocksize):
        pygame.draw.line(display, black, (0,y) , (display_width,y),3)
    pygame.display.update()


def show_message(x,y,Text,textColor, textsize ,msgbackground):
    font = pygame.font.Font('freesansbold.ttf',textsize)
    text = font.render(Text,True,textColor,msgbackground)
    textRect = text.get_rect()
    textRect.center = (x,y)
    display.blit(text , textRect)
    pygame.display.update()


def button(x,y,size,color,hcolor,Text,textColor,x2,Text2,b1clicked,b2clicked,button2=False):

    while True:
        
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            font = pygame.font.Font('freesansbold.ttf',size)
            text = font.render(Text,True,textColor,color)
            textRect = text.get_rect()
            textRect.center = ( x, y )
            display.blit(text, textRect)

            if button2:

                font = pygame.font.Font('freesansbold.ttf',size)
                text2 = font.render(Text2, True, textColor , color)
                textRect2 = text2.get_rect()
                textRect2.center = ( x2 , y )
                display.blit(text2, textRect2)
                
            pygame.display.update()
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if mouse[0] in range(textRect.x,textRect.x + textRect.width) and mouse[1] in range(textRect.y , textRect.y + textRect.height):
                text = font.render(Text,True,textColor,hcolor)
                display.blit(text, textRect)
                
                if pygame.mouse.get_pressed()[0]:
                    time.sleep(0.1)
                    b1clicked()
                
                
            if button2:
                if mouse[0] in range(textRect2.x,textRect2.x + textRect2.width) and mouse[1] in range(textRect2.y , textRect2.y + textRect2.height):    
                    text = font.render(Text2,True,textColor,hcolor)
                    display.blit(text, textRect2)

                    if pygame.mouse.get_pressed()[0]:
                        time.sleep(0.1)
                        b2clicked()

            pygame.display.update() 


def win_screen(winner,reverse=False):
    time.sleep(0.3)
    if winner == 1:
        show_message(display_width/2, display_height/3 , f'{maxplayer if not reverse else minplayer} won',white, 90 , red if not reverse else blue)

    if winner == -1:
        show_message(display_width/2, display_height/3 , f'{minplayer if not reverse else maxplayer} won',white, 90 , blue if not reverse else red)

    if winner == 0:    
        show_message(display_width/2, display_height/3 , 'Game Draw',white, 90 ,gray)

    button((display_width/10)*3.3 , (display_height/10)*8,30, black, green , 'Quit' , white , (display_width/10)*6.7 , 'NewGame' , quit , choose , True )                                   


def move(row,col,player):
    if board[row][col] == 0:
        board[row][col] = player


def img_update(reverse=False):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'x':
                draw_o(col,row) if reverse else draw_x(col,row)
            elif board[row][col] == 'o':
                draw_x(col,row) if reverse else draw_o(col,row)    
  

def draw_x(row,col):
    pygame.draw.line(display, x_color , ((row * blocksize) + blocksize//10 , (col * blocksize) + blocksize//10) , (((row+1) * blocksize) - blocksize//10 , ((col+1) * blocksize) - blocksize//10),x_thickness)
    pygame.draw.line(display, x_color , (((row+1) * blocksize) - blocksize//10 , (col * blocksize) + blocksize//10) , ((row * blocksize) + blocksize//10 , ((col+1) * blocksize) - blocksize//10),x_thickness)
    pygame.display.update()


def draw_o(row,col):
    pygame.draw.circle(display, o_color , ( ((row * blocksize) + (blocksize//2)) , ((col * blocksize) + (blocksize//2)) ) , blocksize*0.45, o_thickness)
    pygame.display.update() 


def intro():
    show_message(display_width/2, display_height/3, 'Tic-Tac-Toe' , green , 90, black)
    button((display_width/10)*2 , (display_height/10)*8,40, white, green , 'Quit' , black , (display_width/10)*7 , 'StartGame' , quit , choose , True )


def choose():
    display.fill(white)
    show_message(display_width/2, display_height/3, 'How Do You Wanna Play?' , yellow , 40, black)
    button((display_width/10)*3, (display_height/10)*8 , 30 , white , yellow , 'Vs computer', black, (display_width/10)*7, 'Vs human', shapes , vsman , True)


def shapes():
    display.fill(white)
    show_message(display_width/2, display_height/3, 'What shape do you want to be?', black , 30 ,cyan)
    button((display_width/10)*3, (display_height/10)*8 , 50 ,white, cyan , 'O' , black , (display_width/10)*7 , 'x', o , x , True)


def x():
    display.fill(white)
    show_message(display_width/2, display_height/3 , 'Who goes first?', magenta , 50 , black)
    button((display_width/10)*3, (display_height/10)*8 , 30 ,white, magenta , 'Player' , black , (display_width/10)*7 , 'Computer', player_first , pc_first , True)



def o():
    display.fill(white)
    show_message(display_width/2, display_height/3 , 'Who goes first?', magenta , 50 , black)
    button((display_width/10)*3, (display_height/10)*8 , 30 ,white,magenta , 'Player' , black , (display_width/10)*7 , 'Computer', player_first_o , pc_first_o , True)


def CheckWin():
    for row in range(len(board)):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == maxplayer:
                return 1
            elif board[row][0] == minplayer:
                return -1

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == maxplayer:
                return 1
            elif board[0][col] == minplayer:
                return -1

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == maxplayer:
            return 1
        if board[0][0] == minplayer:
            return -1

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == maxplayer:
            return 1
        elif board[0][2] == minplayer:
            return -1

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return 2
    return 0

def AImove(o = True):

    depth = 10**10
    min_eval = 3
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                board[row][col] = minplayer
                Eval = minimax(True)
                board[row][col] = 0
                if Eval <= min_eval:
                    min_eval = Eval
                    Row = row
                    Col = col
    move(Row,Col,minplayer)
    return

def minimax(maximazingplayer):

    if CheckWin() != 2:
        return CheckWin()


    if maximazingplayer:
        max_eval = -3
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 0:
                    board[row][col] = maxplayer
                    Eval = minimax(False)
                    board[row][col] = 0
                    max_eval = max(Eval,max_eval)
        return max_eval

    else:
        min_eval = 3
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 0:
                    board[row][col] = minplayer
                    Eval = minimax(True)
                    board[row][col] = 0
                    min_eval = min(Eval,min_eval)  
        return min_eval              

def count_empties():
    return board[0].count(0) + board[1].count(0) + board[2].count(0)


def game_loop(first_turn, vsman=False , reverse_shape=False):
    time.sleep(0.2)
    if not vsman:
        if first_turn == 'pc':
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if count_empties() % 2 != 0:
                        pygame.display.set_caption('PC turn'.center(60,'#'))
                        AImove()
                        time.sleep(0.5)
                        img_update(True if reverse_shape else False)
                        if CheckWin() != 2:
                            win_screen(CheckWin(),True if reverse_shape else False)
                            
                    if count_empties() % 2 == 0:
                        pygame.display.set_caption('YOUR turn'.center(60,'#'))
                        if pygame.mouse.get_pressed()[0]:
                            x_ = pygame.mouse.get_pos()[0]
                            y_ = pygame.mouse.get_pos()[1]
                            move(y_//blocksize,x_//blocksize,'x')
                            img_update(True if reverse_shape else False)
                            if CheckWin() != 2:
                                win_screen(CheckWin(),True if reverse_shape else False)

        if first_turn == 'player':
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if count_empties() % 2 != 0:
                        pygame.display.set_caption('YOUR turn'.center(60,'#'))
                        if pygame.mouse.get_pressed()[0]:
                            x_ = pygame.mouse.get_pos()[0]
                            y_ = pygame.mouse.get_pos()[1]
                            move(y_//blocksize,x_//blocksize,'x')
                            img_update(True if reverse_shape else False)
                            if CheckWin() != 2:
                                win_screen(CheckWin(),True if reverse_shape else False)

                    if count_empties() % 2 == 0:
                        pygame.display.set_caption('PC turn'.center(60,'#'))                        
                        AImove()
                        time.sleep(0.5)
                        img_update(True if reverse_shape else False)
                        if CheckWin() != 2:
                            win_screen(CheckWin(),True if reverse_shape else False)
                    
    if vsman:
        pygame.display.set_caption('o turn'.center(60,'#'))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            
            if pygame.mouse.get_pressed()[0]:
                if count_empties() % 2 == 0:
                    x_ = pygame.mouse.get_pos()[0]
                    y_ = pygame.mouse.get_pos()[1]
                    move(y_//blocksize,x_//blocksize, 'x')
                    img_update()
                    pygame.display.set_caption('x turn'.center(60,'#'))
                    if CheckWin() != 2:
                        win_screen(CheckWin(),True if reverse_shape else False)

                if count_empties() % 2 != 0:
                                x_ = pygame.mouse.get_pos()[0]
                                y_ = pygame.mouse.get_pos()[1]
                                move(y_//blocksize,x_//blocksize, 'o')
                                img_update()
                                pygame.display.set_caption('o turn'.center(60,'#'))
                                if CheckWin() != 2:
                                    win_screen(CheckWin(),True if reverse_shape else False)        


def runit():
    intro()

def set_up():
    SetBoard()    
    grid()
        
def vsman():
    set_up()
    game_loop('',True)

def pc_first_o():
    minplayer = 'x'
    set_up()
    game_loop('pc',False,True)

def player_first_o():
    set_up()
    game_loop('player',False,True)

def pc_first():    
    set_up()
    game_loop('pc')

def player_first():
    set_up()
    game_loop('player')

runit()
pygame.quit()
quit()