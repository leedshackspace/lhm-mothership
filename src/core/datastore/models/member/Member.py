

class Member(object):
    # def find_by_card_id(self, card_id):
    def __init__(self):
        """ Empty Init """
        print("hi")

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self):
        self._first_name = "First Name"
