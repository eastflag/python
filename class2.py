class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result


class MoreCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result


four = FourCal(3, 4)
# four.setdata(3, 4)
print(four.sum())

more = MoreCal(3, 4)
print(more.pow())