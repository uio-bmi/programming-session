from util import genome_unary


@genome_unary
def count_bin(track, bin_size=1000000):
    groups = track.groupby((track.start//bin_size)*bin_size)
    return groups.size()


def genome_binning(track, bin_size=1000000):
    groups = track.groupby(track.index)
    return groups.apply(count_bin, bin_size)


if __name__ == "__main__":
    from readtable import parse_genelist
    genes = parse_genelist("genelist.tsv")
    print(count_bin(genes))
