import csv


class Reader:
    @staticmethod
    def read_data(path):
        data = []
        with open(path) as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data
