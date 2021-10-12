class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_correct = self.check_if_correct()

    def check_if_correct(self):
        try:
            return True if 0 <= self.x <= 16 and 0 <= self.y <= 16 else False
        except Exception:
            return False


c1 = Coordinate("s", 1)
print(c1.is_correct)
