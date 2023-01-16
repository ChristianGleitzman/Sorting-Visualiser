import pygame
import random
import time
import math
pygame.font.init() 

#color tuples
WHITE = (255,255,255)
BLUE = (0,0,255)
GREY = (100,100,100)
RED = (255,0,0)
YELLOW = (255, 255, 0)

#window constraints
WIDTH = 900
HEIGHT = 600
FPS = 120

fnt = pygame.font.SysFont("comicsans", 30) 
fnt1 = pygame.font.SysFont("comicsans", 20)

#variables
arr_clr = [(0, 204, 102)]*151
clr_ind = 0
clr = [(0, 204, 102), RED, BLUE, YELLOW]

class Algorithms:
    def __init__(self, listLength = 151, minVal = 1, maxVal = 100):
        self.state = False
        self._maxVal = maxVal
        self._minVal = minVal
        self._listLength = listLength
        self._array = [0]*151
        for i in range(1, self._listLength):
            arr_clr[i] = clr[0]
            self._array[i] = (random.randint(self._minVal, self._maxVal))

    def bubbleSort(self):
        self.startTime = time.time()
        for i in range(1, self._listLength):
            pygame.event.pump()
            self.refill()
            for j in range(1, self._listLength - 1):
                if self._array[j] > self._array[j+1]:
                    arr_clr[j+1] = clr[2] 
                    self._array[j], self._array[j+1] = self._array[j+1], self._array[j]
                    self.refill()
                    arr_clr[j+1] = clr[0]
            self.refill()
            arr_clr[self._listLength - i] = clr[3]
    
    def insertionSort(self):
        self.startTime = time.time()
        for i in range(1,self._listLength):
            pygame.event.pump()
            self.refill()
            key = self._array[i]
            arr_clr[i] = clr[2]
            j = i-1
            while j >= 0 and key < self._array[j]: 
                arr_clr[j] = clr[2] 
                self._array[j + 1] = self._array[j] 
                self.refill() 
                arr_clr[j] = clr[3] 
                j = j-1
            self._array[j + 1] = key  
            self.refill() 
            arr_clr[i] = clr[0]

    def mergeSort(self, array, l, r): 
        mid =(l + r)//2
        if l < r: 
            self.mergeSort(array, l, mid) 
            self.mergeSort(array, mid + 1, r) 
            self.merge(array, l, mid, mid + 1, r)

    def merge(self, array, x1, y1, x2, y2):
        i = x1 
        j = x2 
        temp =[] 
        pygame.event.pump()  
        while i<= y1 and j<= y2: 
            arr_clr[i]= clr[1] 
            arr_clr[j]= clr[1] 
            self.refill() 
            arr_clr[i]= clr[0] 
            arr_clr[j]= clr[0] 
            if array[i]<array[j]: 
                temp.append(array[i]) 
                i+= 1
            else: 
                temp.append(array[j]) 
                j+= 1
        while i <= y1: 
            arr_clr[i]= clr[1] 
            self.refill() 
            arr_clr[i]= clr[0] 
            temp.append(array[i]) 
            i+= 1
        while j <= y2: 
            arr_clr[j] = clr[1] 
            self.refill() 
            arr_clr[j] = clr[0] 
            temp.append(array[j]) 
            j+= 1
        j = 0    
        for i in range(x1, y2 + 1):  
            pygame.event.pump()  
            array[i] = temp[j] 
            j+= 1
            arr_clr[i] = clr[2] 
            self.refill() 
            if y2-x1 == len(array)-2: 
                arr_clr[i] = clr[3] 
            else:  
                arr_clr[i] = clr[0] 
            
    def quickSort(self, l, r):
        if l < r:
            pi = self.partition(l, r)
            self.quickSort(l, pi-1)
            self.refill()
            for i in range(0, pi+1):
                arr_clr[i] = clr[3]
            self.quickSort(pi+1, r)
            
    def partition(self,low,high):
        pygame.event.pump()
        pivot = self._array[high]
        arr_clr[high] = clr[2]
        i = low - 1
        for j in range(low,high):
            arr_clr[j] = clr[1]
            self.refill()
            arr_clr[high] = clr[2]
            arr_clr[j] = clr[0]
            arr_clr[i] = clr[0]
            if self._array[j] < pivot:
                i = i + 1
                arr_clr[i] = clr[1]
                self._array[i], self._array[j] = self._array[j], self._array[i]
        self.refill()
        arr_clr[i] = clr[0]
        arr_clr[high] = clr[0]
        self._array[i + 1], self._array[high] = self._array[high], self._array[i + 1]
        
        return (i + 1)
        
    def getArray(self):
        return self._array
    
    def draw(self):
        txt = fnt.render("SORT: PRESS 'ENTER' ", 1, (0, 0, 0))
        screen.blit(txt, (20,20))
        txt1 = fnt1.render("NEW ARRAY: PRESS R", 1, (0, 0, 0))
        screen.blit(txt1, (20,40))
        txt2 = fnt1.render("ALGORITHM USED: {} SORT".format(choice.upper()), 1, (0, 0, 0))
        screen.blit(txt2, (600,60))
        element_width =(WIDTH - 150) // 150
        boundry_arr = 900 / 150
        boundry_grp = 550 / 100
        pygame.draw.line(screen, (0, 0, 0), (0, 95), (900, 95), 6)

        for i in range(1,151):
            pygame.draw.line(screen, arr_clr[i], (boundry_arr * i-3, 100), (boundry_arr * i-3, self._array[i]*boundry_grp + 100), element_width)
    
    def refill(self):
        try:
            screen.fill(GREY)
            txt = fnt1.render("TIME TAKEN: {}".format(time.time() - self.startTime), 1, (0, 0, 0))
            screen.blit(txt, (20,60))
            self.draw() 
            pygame.display.update() 
            pygame.time.delay(5)
        except AttributeError:
            pass


#creates screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithms")
clock = pygame.time.Clock()

#initial instance of the array
choice = 'bubble'
diagram = Algorithms()

#Game Loop
running = True

while running:
    #keeping the game running at the right speed
    clock.tick(FPS)
    for event in pygame.event.get():
        #checks event for closing the window
        if event.type == pygame.QUIT:
            running = False
        #event of a keypress
        elif event.type == pygame.KEYDOWN:
            if diagram.state == False:
                if event.key == pygame.K_r:
                    diagram = Algorithms()
                if event.key == pygame.K_b:
                    choice = 'bubble'
                if event.key == pygame.K_i:
                    choice = 'insertion'
                if event.key == pygame.K_m:
                    choice = 'merge'
                if event.key == pygame.K_q:
                    choice = 'quick'
                if event.key == pygame.K_RETURN:
                    if choice == 'bubble':
                        state = True
                        diagram.bubbleSort()
                        state = False
                    elif choice == 'insertion':
                        state = True
                        diagram.insertionSort()
                        state = False
                    elif choice == 'merge':
                        state = True
                        diagram.startTime = time.time()
                        arr = diagram.getArray()
                        diagram.mergeSort(arr, 1, len(arr)-1)
                        state = False
                    else:
                        state = True
                        diagram.startTime = time.time()
                        diagram.quickSort(1,len(diagram.getArray())-1)
                        state = False
            else:
                pass
    #draw/render
    screen.fill(GREY)
    diagram.draw()
    #always do this after drawing everything
    pygame.display.flip()
    
pygame.quit()