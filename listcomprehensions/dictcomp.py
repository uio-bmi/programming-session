
def old(data):
    processed = {}
    for i, element in enumerate(data):
        processed[element] = i
    return processed


def new(data):
    """ TODO """
    pass


if __name__ == "__main__":
    data = list(range(10, 100, 3))
    assert old(data) == new(data)
    print("SUCSESS!")
