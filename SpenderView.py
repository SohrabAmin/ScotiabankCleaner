import datetime


class File:
    """
    A File object can open, clean, and store csv files.
    """

    def __init__(self, file):
        """
        Instantiates a File Object.
        """
        self.file = open(file, 'r')
        self.data = []

    def clean_data(self):
        self.data = [line.split(',') for line in self.file]
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if j == 0:
                    self.data[i][j] = datetime.datetime.strptime(self.data[i][j], '%m/%d/%Y')
                elif j == 1:
                    self.data[i][j] = float(self.data[i][j])
                else:
                    self.data[i][j] = self.data[i][j].strip()


if __name__ == '__main__':
    file = File('pcbanking.csv')
    file.clean_data()
    print(file.data[0])



