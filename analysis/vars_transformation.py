# Transform varables
N_PERIODS = 2

clean_df['yield_curve_slope'] = clean_df['ltrate'] - clean_df['stir']

clean_df['credit'] = clean_df['tloans'] / clean_df['gdp']
clean_df['credit'] = clean_df.groupby('country')['credit'].diff(N_PERIODS)

clean_df['stock_prices'] = clean_df.groupby('country')['stocks'].pct_change(N_PERIODS)

clean_df['debt_service_ratio'] = clean_df['tloans'] * clean_df['ltrate'] / clean_df['gdp']
clean_df['debt_service_ratio'] = clean_df.groupby('country')['debt_service_ratio'].diff(N_PERIODS)

clean_df['real_consumption_per_capita'] = clean_df.groupby('country')['rconpc'].pct_change(N_PERIODS)

clean_df['investment'] = clean_df.groupby('country')['iy'].diff(N_PERIODS)

clean_df['current_account'] = clean_df['ca'] / clean_df['gdp']
clean_df['current_account'] = clean_df.groupby('country')['current_account'].diff(N_PERIODS)

clean_df['public_debt'] = clean_df['debtgdp']
clean_df['public_debt'] = clean_df.groupby('country')['debtgdp'].diff(N_PERIODS)

clean_df['broad_money'] = clean_df['money'] / clean_df['gdp']
clean_df['broad_money'] = clean_df.groupby('country')['broad_money'].diff(N_PERIODS)

clean_df['cpi'] = clean_df.groupby('country')['cpi'].pct_change(N_PERIODS)

baseline_domestic_features = ['yield_curve_slope', 'credit', 'stock_prices',
                              'debt_service_ratio',
                              'real_consumption_per_capita', 'investment',
                              'current_account', 'public_debt',
                              'broad_money', 'cpi']

clean_df[baseline_domestic_features] = clean_df[baseline_domestic_features] * 100
clean_df['yield_curve_slope'] = clean_df['yield_curve_slope']/100
clean_df['debt_service_ratio'] = clean_df['debt_service_ratio']/100

clean_df.to_csv("Desktop\\transformed_df.csv")
