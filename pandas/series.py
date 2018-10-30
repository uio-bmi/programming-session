import numpy as np
import pandas as pd


def simple_example(data):
    array = np.array(data)
    series = pd.Series(data)
    print(array)
    print(series)


def index_example(data, index):
    series = pd.Series(data, index=index)
    print(series)


def dict_index_example(data):
    series = pd.Series(data)
    print(series)
    return series


simple_example([1, 2, 3, 4])
gender = ["M", "M", "F", "M"]
names = ["Knut", "GK", "Ying", "Chakri"]
index_example(gender, names)
series = dict_index_example(dict(zip(names, gender)))
print(series["Knut"])
