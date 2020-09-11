class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        ret = f'Item: {self.name} - {self.description}'
        return ret