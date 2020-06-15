import pygame
import cell
import patterns
import time



class GameOfLife:
    def __init__(self, width=640, height=480, cellSize=10, speed=10, infinity = True):
        self.width = width
        self.height = height
        self.cellSize = cellSize
        self.speed = speed
        self.screen = pygame.display.set_mode((width, height))
        self.cellWidth = self.width // self.cellSize
        self.cellHeight = self.height // self.cellSize
        cellMatrix = cell.InfinityCellMatrix if infinity else cell.BorderCellMatrix
        self.cellMatrix = cellMatrix(self.cellWidth, self.cellHeight)
        self.cellMatrix.setMatrix(random=True)



    def drawLines(self):
        for x in range(0, self.width, self.cellSize):
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 0), (x, self.height))

        for y in range(0, self.height, self.cellSize):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))



    def drawCellMatrix(self):
        for rowId, line in enumerate(self.cellMatrix):
            for columnId, item in enumerate(line):
                if bool(item.state):
                    place = columnId * self.cellSize, rowId * self.cellSize, self.cellSize, self.cellSize
                    pygame.draw.rect(self.screen, pygame.Color('green'), place)
                else:
                    place = columnId * self.cellSize, rowId * self.cellSize, self.cellSize, self.cellSize
                    pygame.draw.rect(self.screen, pygame.Color('white'), place)
        self.drawLines()




    def step(self):
        self.cellMatrix.stepGeneration()



    def run(self):
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        while True:
                pygame.event.pump()
                self.drawCellMatrix()
                pygame.display.flip()
                self.step()
                clock.tick(self.speed)



    """
    Функция для запуска на secondsWork секунд, возвращает количество обработанных поколений
    """
    def runBenchMark(self, secondsWork = 10):
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        generationCount = 0
        endTime = time.time() + secondsWork
        while True:
            if time.time() < endTime:
                pygame.event.pump()
                self.drawCellMatrix()
                pygame.display.flip()
                self.step()
                clock.tick(self.speed)
                generationCount += 1

            else:
                return generationCount