import TAASSC_214_dev as lgr
import glob
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Directory location of your text files.')
    parser.add_argument('--directory', type=str, help="Directory of your text files.")
    parser.add_argument('--filename', type=str, help="Name of the .csv file with your results.")
    args = parser.parse_args()

    file_list = glob.glob("%s/*.txt" % args.directory)  # create your own filelist
    lgr.LGR_Full(file_list, "%s.csv" % args.filename)

    lgr.LGR_Full(args.directory, "%s.csv" % args.filename)  # let TAASSC generate the filelist based on a folder name
    lgr.LGR_Full("%s/" % args.directory, "%s.csv" % args.filename,
                 output=["xml"])  # generate summary count file, generate xml representation for each
    lgr.LGR_Full("%s/" % args.directory, "%s.csv" % args.filename, output=["xml",
                                                            "vertical"])  # generate summary count file, generate xml representation  and vertical representation for each


