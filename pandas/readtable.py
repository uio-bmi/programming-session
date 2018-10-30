import pandas as pd


def parse_bed(filename):
    tmp = pd.read_csv(filename, sep="\t", header=None, index_col=None,
                      usecols=[0, 1, 2, 3],
                      names=["chrom", "start", "end", "strand"])
    print(tmp.head())
    return tmp


def parse_genelist(filename):
    tmp = pd.read_csv(filename, sep="\t", usecols=[0, 2, 3, 4, 5],
                      index_col=None, header=None, skiprows=1,
                      names=["name", "chrom",   "start", "end", "strand"])
    tmp.chrom = ["chr" + str(chrom) for chrom in tmp.chrom]
    print(tmp.head())
    return tmp


def parse_simple_bed(filename):
    """ TODO: read bed file without direction column """
    pass

if __name__ == "__main__":
    print(parse_genelist("genelist.tsv").head())
    

    # print(parse_bed("peaks.bed"))
    # simple_df = parse_bed("peaks.bed")
    # del simple_df["direction"]
    # assert (parse_simple_bed("peaks.bed") == simple_df).all().all()
