from collections import namedtuple
import GameOfLife
import patterns




def statistic(dimension):
    print(('{:10} | {:^22} | {:^25} | {:^20} |'.format("Разрешение", "ср. кол-во поколений", "ср. поколений в секундку",
                                                       "обработанных клеток")))
    fmt = '{:10} | {:^22.3f} | {:^25.3f} | {:^20} |'
    for line in dimension:
        avgGeneration = sum([item.number for item in line]) / len(line)
        avgGenPerSec = sum([item.gps for item in line]) / len(line)
        avgCalculatedCell = sum([((item.resolution/10) ** 2) * item.number for item in line]) / len(line)
        print(fmt.format(line[0].resolution, avgGeneration, avgGenPerSec, avgCalculatedCell))


def runBenchMark(secondsWork=10, rounds=5, resolution=(100, 500, 750, 1000, 2000)):
    output = namedtuple("output", ["resolution", "number", "gps"])
    result = []
    for res in resolution:
        tempResult = []
        for _ in range(rounds):
            game = GameOfLife.GameOfLife(res, res, 10, speed=10000)
            generationCount = game.runBenchMark(secondsWork=secondsWork)
            tempResult.append(output(res, generationCount, generationCount / secondsWork))
        result.append(tempResult)
    statistic(result)


if __name__ == '__main__':
    runBenchMark(30,5)