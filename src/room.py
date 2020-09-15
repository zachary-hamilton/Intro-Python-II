# Implement a class to hold room information. This should have name and
# description attributes.

default = 'The way is blocked.'
class Room:
    def __init__(self, name, description, n_to=default, e_to=default, s_to=default, w_to=default):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
        self.inventory = []

    def add_item(self, new_item):
        self.inventory.append(new_item)
        return self

    def remove_item(self, old_item):
        self.inventory.remove(old_item)
        return self