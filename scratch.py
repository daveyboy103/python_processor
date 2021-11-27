from packages.json import SerializerBase
from pprint import pprint as pp


class Person(SerializerBase):
    _firstname: str
    _lastname: str
    _skills = ["Coding", "Analysis"]

    def __init__(self, firstname: str, lastname: str):
        self._lastname = lastname
        self._firstname = firstname

    @property
    def skills(self):
        return self._skills

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname


p = Person('David', 'Harrington')

pp(p.to_json())

