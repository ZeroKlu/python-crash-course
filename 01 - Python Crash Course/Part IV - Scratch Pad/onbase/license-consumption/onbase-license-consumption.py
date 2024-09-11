from datetime import datetime
import pymssql as ms # python -m pip install pymssql
import pandas as pd # python -m pip install pandas
import matplotlib.pyplot as plt # python -m pip install matplotlib
import os
from sm_utils import timer, file_path

# General debug setting for extra logging
debug = True

# Date range to query
start = datetime(2020, 1, 1)
end = datetime.today()

# Column headers for data frame and graph
col = ["License Type", "Peak Usage"]

# SQL query to retrieve usage data (Note: %s represents a parameter - see params tuple in cursor.execute())
sql = f""" SELECT RTRIM(psl.productname) AS 'License', MAX(lus.usagecount) AS 'Peak Usage'
 FROM hsi.licusage lus
 INNER JOIN hsi.productsold psl ON lus.producttype = psl.producttype
 WHERE lus.logdate > %s
 AND lus.logdate < %s
 GROUP BY psl.productname
 ORDER BY psl.productname
"""

# Database connection settings
sv = "OnBaseTestVM"
db = "OnBaseTest"
un = "viewer"
pw = "cprt_hsi"

@timer
def main() -> None:
    """Obtain the usage data from the OnBase database and load data to a plot"""
    # Connect and query the database
    conn = ms.connect(server=sv, database=db, user=un, password=pw)
    cursor = conn.cursor()
    cursor.execute(sql, params=(start, end))
    data = cursor.fetchall()
    conn.close()

    # Create the data frame
    global df
    df = pd.DataFrame(data)
    df.columns = col

def graph() -> None:
    """Display and save the bar graph for usage"""
    ax = df.plot(kind="barh", title=f"Max License Usage {start.strftime('%Y-%m-%d')} to {end.strftime('%Y-%m-%d')}", x=0, y=1, fontsize=8)
    for i, v in enumerate(df[col[1]]): ax.text(v / 2 - 0.5, i - .15, str(v), fontsize="small", color="white")
    plt.subplots_adjust(left=.4)
    plt.savefig(file_path("usage.png", None))
    plt.show()

if __name__ == "__main__":
    # Do not execute if this file is imported
    main()
    if debug: print(df)
    graph()
