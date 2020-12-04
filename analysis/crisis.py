
additional_features = ['short_term_interest_rate', 'long_term_interest_rate', 'household_loans', 'business_loans', 'house_prices']

baseline_features = baseline_domestic_features + baseline_global_features
all_features = baseline_features + additional_features

crisis_df = global_df.copy()

crisis_df['y'] = crisis_df.groupby('country')['crisisJST'].shift(-1).fillna(0) + crisis_df.groupby('country')['crisisJST'].shift(-2).fillna(0)

crisis_and_following_four_years = crisis_df['crisisJST']
for i in range(1,5):
    crisis_and_following_four_years = crisis_and_following_four_years +  crisis_df.groupby('country')['crisisJST'].shift(i).fillna(0)

crisis_filtered_df = crisis_df[crisis_and_following_four_years==0]

crisis_df.to_csv("C:\\Users\\micha\\Desktop\\crisis_df.csv")

crisis_filtered_df.to_csv("C:\\Users\\micha\\Desktop\\crisis_filtered_df.csv")

df_clean = crisis_filtered_df[['year','country', 'y'] + all_features].dropna(how = 'any', subset = baseline_features).copy()

df_clean.to_csv("C:\\Users\\micha\\Desktop\\df_clean.csv")
