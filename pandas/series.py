import numpy as np
import pandas as pd


def simple_example(data):
    print("SIMPLE EXAMPLE")
    array = np.array(data)
    series = pd.Series(data)
    print(array)
    print(series)


def index_example(data, index):
    print("INDEX EXAMPLE")
    series = pd.Series(data, index=index)
    print(series)


def dict_index_example(data):
    print("DICT EXAMPLE")
    print(data)
    series = pd.Series(data)
    print(series)
    return series

if __name__ == "__main__":
    gender = ["M", "M", "F", "M"]
    names = ["Knut", "GK", "Ying", "Chakri"]
    simple_example(gender)
    index_example(gender, names)
    series = dict_index_example(dict(zip(names, gender)))
    print(series["Knut"])
