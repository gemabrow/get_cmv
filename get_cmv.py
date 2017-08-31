# TODO: add docstring
# TODO: add assumptions
import argparse
import os.path
import pandas
from datetime import datetime
from html_to_data import DATA_EXT, fetch_data


def main():
    """
    """
    args = parse_arguments()
    commodity_df = get_local_data(args)
    # return mean + variance for timeframe


def mean_variance(args):
    pass


def get_local_data(args):
    data_filename = args.commodity + DATA_EXT
    no_local_data = os.path.isfile(data_filename) is False

    # if update requested or no local data, retrieve data
    if args.update or no_local_data:
        fetch_data()

    return pandas.read_pickle(data_filename)


def parse_arguments():
    parser = argparse.ArgumentParser(prog="get_cmv",
                                     usage="%(prog)s start_date end_date"
                                           "commodity",
                                     description="Calculates the mean and"
                                                 "variance of a commodity"
                                                 "over the inputted time frame"
                                     )

    parser.add_argument("-u", "--update",
                        help="update local data",
                        action="store_true")

    parser.add_argument("start_date",
                        help="a date in the format YYYY-MM-DD",
                        type=valid_date)

    parser.add_argument("end_date",
                        help="a date in the format YYYY-MM-DD occurring after"
                             "the start date",
                        type=valid_date)

    parser.add_argument("commodity",
                        help="a commodity name (either 'gold' or 'silver')",
                        type=valid_commodity)

    return parser.parse_args()


def valid_commodity(s):
    if s == "gold" or s == "silver":
        return s
    else:
        msg = "Not a valid commodity: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def valid_date(s):
    # Source:
    # https://stackoverflow.com/questions/25470844/specify-format-for-input-arguments-argparse-python
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

if __name__ == "__main__":
    main()
