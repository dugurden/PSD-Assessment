def random_gen(amount, minRange, maxRange):
    count = amount
    result = []
    while count > 0:
        result.append(random.randint(minRange, maxRange))
        count -= 1
    print(result)
