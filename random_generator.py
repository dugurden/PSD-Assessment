def random_gen(amount, minRange, maxRange):
    assert minRange < maxRange, "minRange needs to be smaller than maxRange"
    assert amount > 0, "amount needs to be a positive integer"
    count = amount
    result = []
    while count > 0:
        result.append(random.randint(minRange, maxRange))
        count -= 1
    assert len(result) == amount, "wrong number of results"
    assert count == 0, "Code must be wrong"
    print(result)
