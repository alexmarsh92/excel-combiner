import pandas as pd
import numpy as np
import glob

all_data = pd.DataFrame()
input_location = "C:\\Users\\amarsh04\\Desktop\\Industry Updates\\Paid Search\\Google\\Media\\*.xlsx"
output_location = "C:\\Users\\amarsh04\\Desktop\\Industry Updates\\"
output_filename = "full_googleads_media.csv"
media_g_cols = {0: "advertising_channel_type", #media GOOGLE columns
        1: "advertising_channel_sub_type",
        2: "account_id",
        3: "account_name",
        4: "campaign_name",
        5: "device_type",
        6: "year",
        7: "month",
        8: "impressions",
        9: "clicks",
        10: "cost_usd",
        11: "available_impressions",
        12: "top_impression_pct",
        13: "absolute_top_impression_pct"}
media_b_cols = {0: "advertising_channel_type", #media BING columns
        1: "advertising_channel_sub_type",
        2: "account_id",
        3: "account_name",
        4: "campaign_name",
        5: "device_type",
        6: "year",
        7: "month",
        8: "impressions",
        9: "clicks",
        10: "cost_usd",
        11: "available_impressions",
        12: "top_impressions",
        13: "absolute_top_impressions"}
cvrs_g_cols = {} #todo
cvrs_b_cols = {} #todo
fb_cols = {}     #todo

for f in glob.glob(input_location):
    df = pd.read_excel(f)
    if f.__contains__("google"):
        df.rename(columns={media_g_cols}, inplace=True)
        df.insert(0, "media_provider_name", "google")
    elif f.__contains__("bing"):
        df.rename(columns={media_b_cols}, inplace=True)
        df.insert(0, "media_provider_name", "bing")
    else:
        df.rename(columns={media_b_cols}, inplace=True)
        df.insert(0, "media_provider_name", "unknown")
    all_data = all_data.append(df, ignore_index=True)

all_data.drop_duplicates()

if all_data.media_provider_name == 'google':
    all_data['top_impressions'] = df.apply(lambda row: row['impressions'] * row['top_impression_pct'], axis=1)
    all_data['absolute_top_impressions'] = df.apply(lambda row: row['impressions'] * row['absolute_top_impression_pct'], axis=1)
    all_data.drop(['top_impression_pct', 'absolute_top_impression_pct'], axis=1, inplace=True)
else:
    pass

all_data.to_csv(output_location + output_filename, sep=',', index=False)