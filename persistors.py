import os


class FakePersistor:
    _filename: str

    def __init__(self, filename):
        directory = os.getcwd()
        self._filename = os.path.join(directory, filename)
        if os.path.exists(self._filename):
            os.remove(self._filename)

    def save(self, transaction):

        with open(self._filename, 'at') as file:
            for key_name in transaction:
                file.write(key_name + ' -' + str(transaction[key_name]) + '\n')
