from datetime import datetime
import os

class Log:
    def __init__(self):
        self.filename: str = None

    def create_log(self, directory: str = ''):
        directory = os.path.dirname(os.path.realpath(__file__)) + directory
        filename = datetime.now().strftime("%H%M%S") + '.log'
        for date in ['%Y', '%m', '%d']:
            directory += datetime.now().strftime(f"/{date}")
            os.makedirs(directory, exist_ok=True)
        directory += '/'
        self.filename = filename = directory + filename
        file = open(filename, 'w')
        file.close()
        return filename

    def write(self, text: str):
        filename = self.filename
        file = open(filename, 'a')
        file.write(text)
        file.close()

    def writenl(self, text: str):
        filename = self.filename
        file = open(filename, 'a')
        file.write(text + '\n')
        file.close()

