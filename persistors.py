import os


class FakePersistor:
    @staticmethod
    def save(transaction):
        directory = os.getcwd()
        filename = os.path.join(directory, 'sample.txt')
        with open(filename, 'a') as file:
            for key_name in transaction:
                file.write(key_name + ' -' + str(transaction[key_name]) + '\n')