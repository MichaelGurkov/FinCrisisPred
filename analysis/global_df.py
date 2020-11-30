global_df = transformed_df.copy()

number_of_countries = transformed_df['country'].nunique()

global_df['global_credit_growth'] = global_df.groupby('year')['credit'].transform('mean')
global_df['global_credit_growth'] = (global_df['global_credit_growth'] * number_of_countries - global_df['credit']) / (number_of_countries - 1)

global_df['global_yield_curve_slope'] = global_df.groupby('year')['yield_curve_slope'].transform('mean')
global_df['global_yield_curve_slope'] = (global_df['global_yield_curve_slope'] * number_of_countries - global_df['yield_curve_slope']) / (number_of_countries - 1)

baseline_global_features = ['global_credit_growth', 'global_yield_curve_slope']

###


global_df['short_term_interest_rate'] = global_df['stir']

global_df['long_term_interest_rate'] = global_df['ltrate']

global_df['household_loans'] = global_df['thh'] / global_df['gdp']
global_df['household_loans'] = global_df.groupby('country')['household_loans'].diff(N_PERIODS)

global_df['business_loans'] = global_df['tbus'] / global_df['gdp']
global_df['business_loans'] = global_df.groupby('country')['business_loans'].diff(N_PERIODS)

global_df['house_prices'] = global_df['hpnom'].pct_change(N_PERIODS)
global_df[['household_loans', 'business_loans', 'house_prices']] = global_df[['household_loans', 'business_loans', 'house_prices']] * 100
global_df['household_loans'] = np.where(global_df['business_loans'].notnull(), global_df['household_loans'], np.nan)


global_df.to_csv("C:\\Users\\micha\\Desktop\\global_df.csv")

