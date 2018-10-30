import pandas as pd
from util import genome_binary


def split_strands(df):
    pos = df["strand"] == 1
    return (df[pos], df[~pos])


def find_closest(values, x, direction):
    a, b = ("end", "start")
    if direction == 1:
        b, a = (a, b)
    idxs = values[a].searchsorted(x[b])
    genes = values.iloc[idxs].copy()
    genes.index = x.index
    genes["dist"] = (genes[a]-x[b]).abs()
    return genes


@genome_binary
def closest_gene(peaks, genes):
    pos_genes, neg_genes = split_strands(genes)
    pos_genes = pos_genes.sort_values(["start"])
    neg_genes = neg_genes.sort_values(["end"])
    closest_pos = find_closest(pos_genes, peaks, +1)
    closest_neg = find_closest(neg_genes, peaks, -1)
    assert closest_pos.index.equals(closest_neg.index), (closest_pos.index, closest_neg.index)
    closest = closest_pos.where(closest_pos.dist < closest_neg.dist,
                                closest_neg)
    return pd.concat({"peak": peaks, "gene": closest},
                     axis=1)


def genome_closest_gene_old(peaks, genes):
    peak_groups = peaks.groupby("chrom")
    gene_groups = genes.groupby("chrom")
    return pd.concat({name: closest_gene(group, genes.loc[gene_groups.groups[name]])
                      for name, group in peak_groups})


def genome_closest_gene(peaks, genes):
    return pd.concat([closest_gene(peaks.loc[chrom], genes.loc[chrom])
                      for chrom in peaks.index.unique()])

if __name__ == "__main__":
    from readtable import parse_genelist, parse_bed
    genes = parse_genelist("genelist.tsv")
    peaks = parse_bed("peaks.bed")
    res = closest_gene(peaks, genes)
    # print(res[("gene", "dist")])
    print(res)
