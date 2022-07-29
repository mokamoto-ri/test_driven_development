# class Dollar:
#     def __init__(self, something):
#         self.amount = 10

#     def times(self, multiplier):
#         pass


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier

    # def times(self, multiplier):
    #     return Dollar(self.amount * multiplier)
