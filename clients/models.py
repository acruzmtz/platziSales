import uuid

class Client:
    """docstring for Client."""

    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4() #we can use the logical operators (and, or) to set a value in vars


    def to_dict(self):
        return vars(self) #returns a dict, convert the self class to a dictionary

    @staticmethod
    def schema():
        """ show the top of table """
        return ['name', 'company','email', 'position', 'uid']
