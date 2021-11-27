import uuid
import random


class FakeFetcher:
    @staticmethod
    def get(count):
        for i in range(count):
            transaction = {
                "Name": str(uuid.uuid4()),
                "Number": random.randrange(1, 1200)
            }
            yield transaction

    def __call__(self, count):
        return self.get(count)
    

