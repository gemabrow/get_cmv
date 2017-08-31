# TODO: add docstring
# TODO: add assumptions
import pandas
import requests

DATA_EXT = ".pkl"

"""
Constants for Investing.com commodity data
For ref., XPath of target: '//table[@id=TABLE_ID]'
NOTE: Confirm TABLE_ID by inspecting targeted HTML table in web browser
"""
TARGETS = ["gold", "silver"]
BASE_URL = "https://www.investing.com/commodities/"
TAIL_URL = "-historical-data"
TABLE_ID = "curr_table"

# assign user agent to header to avoid HTTP Error 403: Forbidden
HEADER = {'User-Agent':
          'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}


def fetch_data():
    print ("    <<<<<<<<<<<<<<<<<<<<<< retrieving >>>>>>>>>>>>>>>>>>>>>>")
    for target in TARGETS:
        target_result = process_data(target)
        target_result.to_pickle(target + DATA_EXT)
    print ("    ----------------- local data updated -------------------")


def process_data(commodity):
    # type: (str) -> pandas.DataFrame

    # assign variable to commodity-based url
    url = BASE_URL + commodity + TAIL_URL
    url_response = requests.get(url, headers=HEADER)
    # assign variable to pandas' dataframe with column headings, target table with "id" == TABLE_ID
    commodity_df = pandas.read_html(url_response.content, header=0, attrs={"id": TABLE_ID})[0]
    # change datetime format for 'Date' column
    # ex: "Aug 30, 2017" -> "2017-08-30"
    commodity_df['Date'] = pandas.to_datetime(commodity_df.Date)

    return commodity_df
