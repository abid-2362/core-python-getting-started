def first(an_iterable):
    an_iterator = iter(an_iterable)
    try:
        return next(an_iterator)
    except StopIteration:
        raise ValueError("itearble is empty")


first([1, 2, 3, 4, 5, 6])
