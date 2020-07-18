import pandas as pd
import numpy as np
import glob

all_data = pd.DataFrame()
output_location = "C:\\Users\\amarsh04\\Desktop\\Industry Updates\\"
output_filename = "full_googleads_media.csv"

for f in glob.glob("C:\\Users\\amarsh04\\Desktop\\Industry Updates\\Paid Search\\Google\\Media\\*google*.xlsx"):
    df = pd.read_excel(f)
    df.rename(columns={df.columns[0]: "advertising_channel_type",
        df.columns[1]: "advertising_channel_sub_type",
        df.columns[2]: "account_id",
        df.columns[3]: "account_name",
        df.columns[4]: "campaign_name",
        df.columns[5]: "device_type",
        df.columns[6]: "year",
        df.columns[7]: "month",
        df.columns[8]: "impressions",
        df.columns[9]: "clicks",
        df.columns[10]: "cost_usd",
        df.columns[11]: "available_impressions",
        df.columns[12]: "top_impression_pct",
        df.columns[13]: "absolute_top_impression_pct"}, inplace=True)
    df.insert(0, "media_provider_name", "google")
    df['top_impressions'] = df.apply(lambda row: row['impressions'] * row['top_impression_pct'], axis=1)
    df['absolute_top_impressions'] = df.apply(lambda row: row['impressions'] * row['absolute_top_impression_pct'], axis=1)
    df.drop(['top_impression_pct', 'absolute_top_impression_pct'], axis=1, inplace=True)
    all_data = all_data.append(df, ignore_index=True)

for f in glob.glob("C:\\Users\\amarsh04\\Desktop\\Industry Updates\\Paid Search\\Google\\Media\\*bing*.xlsx"):
    df = pd.read_excel(f)
    df.rename(columns={df.columns[0]: "advertising_channel_type",
        df.columns[1]: "advertising_channel_sub_type",
        df.columns[2]: "account_id",
        df.columns[3]: "account_name",
        df.columns[4]: "campaign_name",
        df.columns[5]: "device_type",
        df.columns[6]: "year",
        df.columns[7]: "month",
        df.columns[8]: "impressions",
        df.columns[9]: "clicks",
        df.columns[10]: "cost_usd",
        df.columns[11]: "available_impressions",
        df.columns[12]: "top_impressions",
        df.columns[13]: "absolute_top_impressions"}, inplace=True)
    df.insert(0, "media_provider_name", "bing")
    all_data = all_data.append(df, ignore_index=True)


all_data.drop_duplicates()

all_data.to_csv(output_location + output_filename, sep=',', index=False)