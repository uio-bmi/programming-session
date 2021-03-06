import pandas as pd

a = {"Knut": 2.0, "GK": 1.5, "Ying": 0.5,  "Chakri": 3.0}
b = {"Knut": 10.3, "GK": 9.5, "Chakri": 29.0, "Ying": 13.5}
c = {"Knut": 0.9, "GK": 0.11, "Chakri": 0.33, "Ying": 0.20}

nested_dict = {"a": a, "b": b, "c": c}
df = pd.DataFrame(nested_dict)
print(df)


def mod_affine_dataframe(df, x):
    df["y"] = df["a"]*x+df["b"]
    return df


def assign_affine_dataframe(df, x):
    return df.assign(b=lambda tmp: tmp["a"]*x+tmp["b"])


print(mod_affine_dataframe(df, 10))
print(assign_affine_dataframe(df, 10))
print(df)

def quadratic_dict(nested_dict, x):
    return {name:
            nested_dict["a"][name]*x**2 + nested_dict["b"][name]*x + nested_dict["c"][name]
            for name in a.keys()}


def quadratic_dataframe(df, x):
    "TODO: Implement this"
    pass



# assert (pd.Series(quadratic_dict(nested_dict, 10)) == quadratic_dataframe(df, 10)).all()
