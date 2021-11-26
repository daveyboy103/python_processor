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


class UppercaseProcessor:
    @staticmethod
    def process(transaction):
        for key_name in transaction:
            if key_name == "Name":
                value = transaction[key_name].upper()
                transaction[key_name] = value