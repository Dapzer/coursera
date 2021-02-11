class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, 'r') as file:
                text = file.read()
                return text
        except IOError:
            return ''
