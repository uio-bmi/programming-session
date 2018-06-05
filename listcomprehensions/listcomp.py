
def old(data):
    processed = []
    for element in data:
        if element % 2 == 0:
            processed.append(element//2)
    return processed


def new(data):
    """ TODO """
    pass


if __name__ == "__main__":
    data = list(range(10, 100, 3))
    assert old(data) == new(data)
