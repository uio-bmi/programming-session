import pandas as pd


def genome_unary(func):
    def new_func(track, *args, **kwargs):
        return track.groupby("chrom").apply(func, *args, **kwargs)
    return new_func


def genome_binary(func):
    def new_func(track_a, track_b, *args, **kwargs):
        groups_a = track_a.groupby("chrom")
        groups_b = track_b.groupby("chrom")
        # wrapper = lambda a, b: func(a, b.get_group(a.chrom.iloc[0]), *args, **kwargs)
        # return groups_a.apply(wrapper, groups_b)
        return pd.concat({
            name: func(group, groups_b.get_group(name), *args, **kwargs)
            for name, group in groups_a if name in groups_b.groups})

    return new_func
