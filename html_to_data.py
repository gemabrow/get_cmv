# -*- coding: utf-8 -*-
import pandas
import requests
DATA_EXT = ".pkl"


def fetch_data():
    """ Public method provides feedback while processing all data targets.
    Primary purpose of this method is to serve as an abstraction
    allowing for re-use cases. Stores results in Pickle binaries.
    """
    print("  <<<<<<<<<<<<<<<<<<< downloading >>>>>>>>>>>>>>>>>>>>")
    url_slices = {'gold', 'silver'}

    for target in url_slices:
        target_result = _process_data_(target)
        target_result.to_pickle(target + DATA_EXT)
    print("  --------------- local data updated -----------------")


def _process_data_(target_url):
    """ Specifics to targeted data handling go here
        Args:
             target_url: a string indicating target's url
                         for the purpose of url concatenation
        NOTE: Immediately below is an (optional) assertion of type
    """
    # type: (str) -> pandas.DataFrame
    base_url = "https://www.investing.com/commodities/"
    tail_url = "-historical-data"
    # NOTE: Confirm table_id by inspecting targeted HTML table in web browser
    # For ref., XPath of target: '//table[@id=table_id]'
    table_id = "curr_table"
    # assign user agent to header to avoid HTTP Error 403: Forbidden
    chrome_header = {'User-Agent':
                     'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 '
                     '(KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

    # assign variable to target-based url
    url = base_url + target_url + tail_url
    url_response = requests.get(url, headers=chrome_header)
    # assign variable to pandas' dataframe with column headings
    # target table with "id" == table_id
    commodity_df = pandas.read_html(url_response.content,
                                    header=0,
                                    attrs={"id": table_id})[0]
    # change datetime format for 'Date' column
    # "Aug 30, 2017" becomes "2017-08-30"
    commodity_df['Date'] = pandas.to_datetime(commodity_df.Date)
    # set date as index of dataframe for easier retrieval/manipulation
    commodity_df = commodity_df.set_index(['Date'])
    return commodity_df
