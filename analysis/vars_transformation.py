# Transform varables

transformed_df = clean_df.copy()

N_PERIODS = 2

transformed_df['yield_curve_slope'] = transformed_df['ltrate'] - transformed_df['stir']

transformed_df['credit'] = transformed_df['tloans'] / transformed_df['gdp']
transformed_df['credit'] = transformed_df.groupby('country')['credit'].diff(N_PERIODS)

transformed_df['stock_prices'] = transformed_df.groupby('country')['stocks'].pct_change(N_PERIODS,fill_method=None )

transformed_df['debt_service_ratio'] = transformed_df['tloans'] * transformed_df['ltrate'] / transformed_df['gdp']
transformed_df['debt_service_ratio'] = transformed_df.groupby('country')['debt_service_ratio'].diff(N_PERIODS)

transformed_df['real_consumption_per_capita'] = transformed_df.groupby('country')['rconpc'].pct_change(N_PERIODS,fill_method=None)

transformed_df['investment'] = transformed_df.groupby('country')['iy'].diff(N_PERIODS)

transformed_df['current_account'] = transformed_df['ca'] / transformed_df['gdp']
transformed_df['current_account'] = transformed_df.groupby('country')['current_account'].diff(N_PERIODS)

transformed_df['public_debt'] = transformed_df['debtgdp']
transformed_df['public_debt'] = transformed_df.groupby('country')['debtgdp'].diff(N_PERIODS)

transformed_df['broad_money'] = transformed_df['money'] / transformed_df['gdp']
transformed_df['broad_money'] = transformed_df.groupby('country')['broad_money'].diff(N_PERIODS)

transformed_df['cpi'] = transformed_df.groupby('country')['cpi'].pct_change(N_PERIODS,fill_method=None)

baseline_domestic_features = ['yield_curve_slope', 'credit', 'stock_prices',
                              'debt_service_ratio',
                              'real_consumption_per_capita', 'investment',
                              'current_account', 'public_debt',
                              'broad_money', 'cpi']

transformed_df[baseline_domestic_features] = transformed_df[baseline_domestic_features] * 100
transformed_df['yield_curve_slope'] = transformed_df['yield_curve_slope']/100
transformed_df['debt_service_ratio'] = transformed_df['debt_service_ratio']/100

transformed_df.to_csv("C:\\Users\\internet\\Desktop\\transformed_df.csv")
