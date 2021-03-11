from calculator import AverageCalcuator


class FileAverageCalcualtor(AverageCalcuator):

    def __init__(self, file):
        self.file = file
        self.last_line = self.file.readline()

    def has_next(self):
        return self.last_line != ""

    def next_item(self):
        result = float(self.last_line)
        self.last_line = self.file.readline()
        return result

    def dispose(self):
        self.file.close()


fac = FileAverageCalcualtor(open('data.txt'))
print(fac.average())
