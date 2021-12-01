
# Packages: We only need two packages for this script. The first is the dune analytics package which can be found here:
# https://github.com/itzmestar/duneanalytics
# Massive credit to the creator of the duneanalytics package (itzmestar) . your work has helped me significantly
# The second is Pandas

from duneanalytics import DuneAnalytics
import pandas as pd
# initialize client. This simply means log into your dune analytics account. ('username','password')
dune = DuneAnalytics('Tachikoma000', 'iZ7kUnw!B8!XUTe')
# try to login
dune.login()
# fetch token
dune.fetch_auth_token()
# fetch query result id using query id. https://dune.xyz/queries/29153/58862 . Observe the location of the query number on
# the url
result_id = dune.query_result_id(query_id=29153)
# fetch query result
data = dune.query_result(result_id)
# assign the results to a pandas data frame. You can stop here technically. But depending on your query, you might
# need to do some more unpacking and clean up
df = pd.DataFrame(data)
# I know the data comes in as a dict of dicts, so I have cleaned up the data and created columns
df = df['data']['get_result_by_result_id']
# More unpacking and formatting
df2 = pd.DataFrame(df)
# Let's look at the data and see if we like the form
df2['data']

# I like to work with serialized data
df2 = df2["data"].apply(pd.Series)
df2
df2 = df2[['date','treasury_rfv','lusd_rfv','frax_rfv','dai_rfv']]
df2
rslt_df = df2.sort_values(by = 'date')
#rslt_df.plot(x="date", y=["treasury_rfv", "lusd_rfv", "frax_rfv", 'dai_rfv'], kind="line")

import streamlit as st
st.line_chart(df2)
