global_df = transformed_df.copy()

countries_year_count = global_df.groupby('year')['credit'].transform('count') + np.where(global_df['credit'].isnull(), 1, 0)
global_df['global_credit_growth'] = global_df.groupby('year')['credit'].transform('sum')
global_df['global_credit_growth'] = (global_df['global_credit_growth'] - np.where(global_df['credit'].isnull(), 0, global_df['credit'])) / (countries_year_count - 1)

countries_year_count = global_df.groupby('year')['yield_curve_slope'].transform('count') + np.where(global_df['yield_curve_slope'].isnull(), 1, 0)
global_df['global_yield_curve_slope'] = global_df.groupby('year')['yield_curve_slope'].transform('sum')
global_df['global_yield_curve_slope'] = (global_df['global_yield_curve_slope'] - np.where(global_df['yield_curve_slope'].isnull(), 0, global_df['yield_curve_slope'])) / (countries_year_count - 1)

baseline_global_features = ['global_credit_growth', 'global_yield_curve_slope']

###

global_df['short_term_interest_rate'] = global_df['stir']

global_df['long_term_interest_rate'] = global_df['ltrate']

global_df['household_loans'] = global_df['thh'] / global_df['gdp']
global_df['household_loans'] = global_df.groupby('country')['household_loans'].diff(N_PERIODS)

global_df['business_loans'] = global_df['tbus'] / global_df['gdp']
global_df['business_loans'] = global_df.groupby('country')['business_loans'].diff(N_PERIODS)

global_df['house_prices'] = global_df['hpnom'].pct_change(N_PERIODS, fill_method = None)

global_df[['household_loans', 'business_loans', 'house_prices']] = global_df[['household_loans', 'business_loans', 'house_prices']] * 100

global_df['household_loans'] = np.where(global_df['business_loans'].notnull(), global_df['household_loans'], np.nan)


# global_df.to_csv("C:\\Users\\micha\\Desktop\\global_df.csv")