from pprint import pprint as pp

from fetchers import *
from persistors import *
from processors import *


def run(count):
    processors = [ReversingProcessor(), ReplaceDashProcessor(), MultiplyByMillionProcessor(), UppercaseProcessor()]
    fetcher = FakeFetcher()
    persistor = FakePersistor("sample.txt")

    for item in fetcher.get(count):
        for processor in processors:
            processor.process(item)
        pp(item)
        persistor.save(item)


run(10000)
