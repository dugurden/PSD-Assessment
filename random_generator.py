class RandomNum:
    def __init__(self, amount, minRange, maxRange):
        self.amount = amount
        self.minRange = minRange
        self.maxRange = maxRange
    def random_gen(cls):
        assert cls.minRange < cls.maxRange, "minRange needs to be smaller than maxRange"
        assert cls.amount > 0, "amount needs to be a positive integer"
        count = cls.amount
        result = []
        while count > 0:
            result.append(random.randint(cls.minRange, cls.maxRange))
            count -= 1
        assert len(result) == cls.amount, "wrong number of results"
        assert count == 0, "Code must be wrong"
        print(result)
