from itertools import cycle
import sys
from os import system
from time import sleep
from threading import Thread
import textwrap

grid=[]

solved=True

def welcome():
    sud='''
    8 0 0 0 0 0 0 0 0
    0 0 3 6 0 0 0 0 0
    0 7 0 0 9 0 2 0 0
    0 5 0 0 0 7 0 0 0
    0 0 0 0 4 5 7 0 0
    0 0 0 1 0 0 0 3 0
    0 0 1 0 0 0 0 6 8
    0 0 8 5 0 0 0 1 0
    0 9 0 0 0 0 4 0 0 '''
    sud=textwrap.dedent(sud).strip()
    wel='''
    Welcome to SUDSoL !! you can solve your sudoku here. Infact, a sudoku with multiple solutions can also be solved here as it will give all the answers. This is from Chandramauli Chakraborty, you can reach me through my github account https://github.com/chandramaulichak108. 
The procedure for entering the sudoku is to input 0 in case of blank spaces, and enter the sudoku grid in this format\n\n{}
\nSo enjoy !!!
    '''.format(sud)
    print(textwrap.dedent(wel).strip())

welcome()
#system('cls')
print("\nEnter the sudoku: \n")

## Animation

done=False

def animate():
    print()
    for c in cycle(['|','/','-','\\']):
        if done==True:
            break
        sys.stdout.write("\rSolving "+c)
        sys.stdout.flush()
        sleep(0.2)
    if solved==True:
        print('\rSolved           ')
    else:
        print('\rDone             ')

t=Thread(target=animate)


for _ in range(9):
    grid.append(list(map(int,input().split())))

def possible(x,y,n):
    global grid
    for i in range(9):
        if grid[i][y]==n:
            return False
    for j in range(9):
        if grid[x][j]==n:
            return False
    for i in range(3*(x//3),3*(x//3)+3):
        for j in range(3*(y//3),3*(y//3)+3):
            if grid[i][j]==n:
                return False
    return True

def prnt():
    global grid
    print()
    for i in range(9):
        for j in range(9):
            print(grid[i][j],end=" ")
        print()




def solve():
    global done
    global grid
    global t
    for x in range(9):
        for y in range(9):
            if grid[x][y]==0:
                for n in range(1,10):
                    if possible(x,y,n):
                        grid[x][y]=n
                        solve()
                        grid[x][y]=0
                return
    done=True
    t.join()
    prnt()
    ch=input("\nMore? Press [y/n] ")
    if ch=='y' or ch=='yes':
        done=False
        t=Thread(target=animate)
        t.start()
    else:
        print("\nDone")
        exit(1)


            
t.start()
solve()
done=True
solved=False
t.join()

ch=input("\nEnter any key to exit....")
exit(1)

'''

5 0 0 9 0 8 0 0 6
0 0 0 0 6 0 0 0 0
0 8 6 3 0 5 9 4 0
0 0 3 1 0 9 7 0 0
0 0 1 0 0 0 6 0 0
0 0 2 6 0 7 1 0 0
0 7 4 8 0 1 3 9 0
0 0 0 0 4 0 0 0 0
3 0 0 7 0 6 0 0 5
'''
