import pandas as pd

a = {"Knut": 2.0, "GK": 1.5, "Ying": 0.5,  "Chakri": 3.0}
b = {"Knut": 10.3, "GK": 9.5, "Chakri": 29.0, "Ying": 13.5}


def affine_dict(a, b, x):
    assert set(a.keys()) == set(b.keys())
    return {name: a[name]*x + b[name] for name in a.keys()}


def affine_series(a, b, x):
    return a*x+b


print(affine_dict(a, b, 10))
print(affine_series(pd.Series(a), pd.Series(b), 10))

c = {"Knut": 0.9, "GK": 0.11, "Chakri": 0.33, "Ying": 0.20}


def quadratic_dict(a, b, c, x):
    assert set(a.keys()) == set(b.keys()) == set(c.keys())
    return {name: a[name]*x**2 + b[name]*x + c[name] for name in a.keys()}


def quadratic_series(a, b, c, x):
    "TODO: Implement this"
    return a*x*x + b*x + c



assert (pd.Series(quadratic_dict(a, b, c, 10)) == quadratic_series(pd.Series(a),
                                                                   pd.Series(b),
                                                                   pd.Series(c),
                                                                   10)).all()
