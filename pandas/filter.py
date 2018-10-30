from readtable import parse_bed


def get_chromosome_entries(df, chrom):
    return df[df["chrom"] == chrom]


def get_entries_between(df, start, end):
    return df[(df["start"] >= start) & (df["start"] < end)]


def filter_positions(df, chrom, start, end):
    """TODO: return data_frame between start and end on chrom"""
    tmp = (df.chrom == chrom)
    tmp2 = (start <= df.start) & (df.start < end)
    included = tmp & tmp2
    return df[included]


if __name__ == "__main__":
    df = parse_bed("peaks.bed")
    print(df)
    print(get_chromosome_entries(df, "chr1"))
    print(get_entries_between(df, 9986587, 110337144))
    assert filter_positions(df, "chr2", 68062739, 88691358).equals(df[7:9])
