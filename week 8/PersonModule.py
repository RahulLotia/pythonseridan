class Person:
    def __init__(self, name : str, address : str):
        self._name = name
        self._address = address

    def __str__(self):
        return (f'Name: {self._name} Address : {self._address}')