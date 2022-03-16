class ZeroError(Exception):
    def __init__(self, divident, divider):
        self.divident = divident
        self.divider = divider

    @staticmethod
    def nums(divident, divider):
        try:
            return (divident / divider)
        except:
            return f'Делить на ноль нельзя'


print(ZeroError.nums(4, 0))
print(ZeroError.nums(100, 5))
