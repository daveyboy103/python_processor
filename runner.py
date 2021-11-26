import os
import uuid
import random
from pprint import pprint as pp


class FakeFetcher:
    @staticmethod
    def get(count):
        for i in range(count):
            transaction = {
                "Name":str(uuid.uuid4()),
                "Number": random.randrange(1, 1200)
            }
            yield transaction


class ReversingProcessor:
    def process(self, transaction):
        for key_name in transaction:
            if key_name == "Name":
                value = self._reverse(transaction[key_name])
                transaction[key_name]  = value

    @staticmethod
    def _reverse(string_to_reverse):
        return string_to_reverse[::-1]


class ReplaceDashProcessor:
    @staticmethod
    def process(transaction):
        for key_name in transaction:
            if key_name == "Name":
                value = transaction[key_name].replace('-', '_')
                transaction[key_name]  = value


class MultiplyByMillionProcessor:
    @staticmethod
    def process(transaction):
        for key_name in transaction:
            if key_name == "Number":
                value = transaction[key_name] * 1000000
                transaction[key_name] = value


class FakePersistor:
    @staticmethod
    def save(transaction):
        directory = os.getcwd()
        filename = os.path.join(directory, 'sample.txt')
        with open(filename, 'a') as file:
            for key_name in transaction:
                file.write(key_name + ' -' + str(transaction[key_name]) + '\n')


def run(count):
    processors = [ReversingProcessor(), ReplaceDashProcessor(), MultiplyByMillionProcessor()]
    fetcher = FakeFetcher()
    persistor = FakePersistor()

    for item in fetcher.get(count):
        for processor in processors:
            processor.process(item)
        print(item)
        persistor.save(item)


run(10000)
