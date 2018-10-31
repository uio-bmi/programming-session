import pandas as pd
from util import genome_binary


def find_closest(values, x):
    direction = values["strand"].iloc[0]
    a, b = ("end", "start")
    if direction > 0:
        b, a = (a, b)
    idxs = values[a].searchsorted(x[b])
    if direction < 0:
        idxs += 1
    genes = values.iloc[idxs].copy()
    genes.index = x.index
    genes["dist"] = (genes[a]-x[b]).abs()
    return genes


@genome_binary
def closest_gene(peaks, genes):
    genes = genes.sort_values(["start"])
    closest = genes.groupby("strand").apply(find_closest, peaks)
    closest = closest.loc[1].where(closest.loc[1].dist < closest.loc[-1].dist,
                                   closest.loc[-1])
    return pd.concat({"peak": peaks, "gene": closest},
                     axis=1)


if __name__ == "__main__":
    from readtable import parse_genelist, parse_bed
    genes = parse_genelist("genelist.tsv")
    peaks = parse_bed("peaks.bed")
    res = closest_gene(peaks, genes)
    # print(res[("gene", "dist")])
    print(res)
