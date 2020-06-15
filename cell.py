from random import randint

"""
Класс клетки

"""

class Cell:
    cellMatrix = None

    def __init__(self, row, column, state=False):
        self.row = row
        self.column = column
        self.state = state
    def __str__(self):
        if self.state:
            return '1'
        else:
            return '0'
    def __bool__(self):
        return self.state


    def setCellMatrix(matrix):
        Cell.cellMatrix = matrix

    def getNeighbors(self):
        if InfinityCellMatrix is None: return False
        neighbors = self.cellMatrix[self.row][self.column + 1].state
        neighbors += self.cellMatrix[self.row + 1][self.column + 1 ].state
        neighbors += self.cellMatrix[self.row + 1 ][self.column].state
        neighbors += self.cellMatrix[self.row + 1][self.column - 1 ].state
        neighbors += self.cellMatrix[self.row][self.column - 1].state
        neighbors += self.cellMatrix[self.row - 1 ][self.column - 1].state
        neighbors += self.cellMatrix[self.row - 1][self.column].state
        neighbors += self.cellMatrix[self.row - 1 ][self.column + 1 ].state
        
        return neighbors


"""
Классы InfinityCellMatrix и BorderCellMatrix реализуют бесконечную и конечную плоскость соотвественно.
В InfinityCellMatrix при выходе за границы, возвращается нулевой элемент этой последовательности
В BorderCellMatrix при выходе за границы, возвращается список клеток которые интерпритируются как мёртвые
Состоят из InfinityCellList и BorderCellList
"""

class InfinityCellMatrix():
    def __init__(self,columns, rows):
        self.rows = rows
        self.columns = columns
        self.cellMatrix = [InfinityCellList([Cell(row, column) for column in range(self.columns)]) for row in range(self.rows )]
        Cell.setCellMatrix(self)

    def __iter__(self):
        return iter(self.cellMatrix)
    def __getitem__(self, key):
        try:
            return self.cellMatrix[key]
        except:
            return self.cellMatrix[0]

    def __str__(self):
        result = "-" * 30
        for line in self.cellMatrix:
            result += '\n['
            for item in line:
                result += str(item) + ","
            result += "]"
        #TODO переделать вывод
        return str(result)
    def __repr__(self):
        self.__str__()




    def setMatrix(self, cellMatrix = None, setColumn=0, setRow=0, random = False):
        if random:
            for line in self.cellMatrix:
                for cell in line:
                    cell.state = bool(randint(0,1))
        else:
            for rowId, line in enumerate(cellMatrix):
                for columnId, item in enumerate(line):
                    self.cellMatrix[rowId + setRow][columnId + setColumn].state = True if item == 1 else 0

    def stepGeneration(self):
        self.updateCellMatrix = [[False] * self.columns for _ in range(self.rows )]
        for rowId, line in enumerate(self.cellMatrix):
            for columnId, item in enumerate(line):
                alive = item.getNeighbors()
                if alive == 2:
                    self.updateCellMatrix[rowId][columnId] = self.cellMatrix[rowId][columnId].state
                elif alive == 3:
                    self.updateCellMatrix[rowId][columnId] = True
                else:
                    self.updateCellMatrix[rowId][columnId] = False
        for rowId, line in enumerate(self.cellMatrix):
            for columnId, item in enumerate(line):
                self.cellMatrix[rowId][columnId].state= self.updateCellMatrix[rowId][columnId]






class BorderCellMatrix(InfinityCellMatrix):
    def __init__(self, columns, rows):
        super().__init__(columns, rows)
        self.rows = rows
        self.columns = columns
        self.cellMatrix = [BorderCellList([Cell(row, column) for column in range(self.columns)]) for row in range(self.rows )]
        Cell.setCellMatrix(self)

    def __getitem__(self, key):
        if abs(key) >= len(self.cellMatrix): return BorderCellList([Cell(0,0, state=False) for _ in range(key+1)])
        if key < 0: return BorderCellList([Cell(0,0, state=False) for _ in range(key+1)])
        return self.cellMatrix[key]



class BorderCellList(list):
    def __getitem__(self, key):
        if abs(key) >= len(self): return Cell(0,0, state=False)
        if key < 0: return Cell(0, 0, state=False)
        return list.__getitem__(self, key)

class InfinityCellList(list):
    def __getitem__(self, key):
        try:

            return list.__getitem__(self, key)
        except:
            return list.__getitem__(self, 0)












