# TODO: add docstring
# TODO: add assumptions
import pandas
import requests

COMMODITIES = ["gold", "silver"]
DATA_EXT = ".pkl"

"""
Constants for Investing.com commodity data
For ref., XPath of target: '//table[@id=TABLE_ID]'
NOTE: Confirm TABLE_ID by inspecting targeted HTML table in web browser
"""
BASE_URL = "https://www.investing.com/commodities/"
TAIL_URL = "-historical-data"
TABLE_ID = "curr_table"

# assign Google Chrome user agent to header to avoid HTTP Error 403: Forbidden
CHROME_HEADER = {'User-Agent':
                 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}


def update_local_data():
    print ("    <<<<<<<<<<<<<<<<<<<<<< retrieving >>>>>>>>>>>>>>>>>>>>>>")
    # data = dict()

    for commodity in COMMODITIES:
        url = BASE_URL + commodity + TAIL_URL
        url_response = requests.get(url, headers=CHROME_HEADER)
        # assign local variable to pandas' dataframe located at index 0
        commodity_df = pandas.read_html(url_response.content, header=0, attrs={"id": TABLE_ID})[0]
        # change datetime format for 'Date' column
        # ex: "Aug 30, 2017" -> "2017-08-30"
        commodity_df['Date'] = pandas.to_datetime(commodity_df.Date)
        commodity_df.to_pickle(commodity + DATA_EXT)
#        data[commodity] = commodity_df
#
#    with open(DATA_FILENAME, "wb") as file_handle:
#        pickle.dump(data, file_handle, protocol=pickle.HIGHEST_PROTOCOL)

    print ("    ----------------- local data updated -------------------")
