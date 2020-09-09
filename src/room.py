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


    def __str__(self):
        ret = f"Room: {self.name}"
        ret += '\n-------------'
        ret += f'\n{self.description}'
        ret += '\n-------------'
        ret += '\nWhere would you like to go next?'
        if self.n_to != default:
            ret += f'\n    n: {self.n_to.name}'
        if self.e_to != default:    
            ret += f'\n    e: {self.e_to.name}'
        if self.s_to != default:
            ret += f'\n    s: {self.s_to.name}'
        if self.w_to != default:
            ret += f'\n    w: {self.w_to.name}'
        ret += '\n    q: Quit'
        return ret