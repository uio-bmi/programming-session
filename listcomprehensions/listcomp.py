
def old(data):
    processed = []
    for element in data:
        if element % 2 == 0:
            processed.append(element//2)
    return processed


def new(data):
    """ TODO """
    return [e // 2 for e in data if e % 2 == 0]

if __name__ == "__main__":
    data = list(range(10, 100, 3))
    assert old(data) == new(data), (old(data), new(data))
    print("SUCSESS!")
