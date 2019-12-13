import datetime
import matplotlib.pyplot as plt


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

class Graph:
    """
    A Graph Object using matplotlib
    """
    def __init__(self, title: str, x_label: str, y_label: str, data: list):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.data = data
        self.x_data = []
        self.y_data = []

    def create_axis(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if j == 0:
                    self.x_data.append(self.data[i][j])
                elif j == 1:
                    self.y_data.append(self.data[i][j])

    def create_graph(self):
        self.create_axis()
        plt.plot(self.x_data, self.y_data)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.show()


if __name__ == '__main__':
    file = File('spending.csv')
    file.clean_data()

    G = Graph("Spendings", "Date", "Amount", file.data)
    G.create_graph()
    print(G.x_data)
    print(G.y_data)
    print(len(G.x_data))
    print(len(G.y_data))






