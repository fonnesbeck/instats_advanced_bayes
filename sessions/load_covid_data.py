import polars as pl
from typing import Optional

def load_individual_timeseries(name: str) -> pl.DataFrame:
    base_url='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series'
    url = f'{base_url}/time_series_covid19_{name}_global.csv'
    
    # Read CSV with polars
    df = pl.read_csv(url)
    
    # Add type column
    df = df.with_columns(pl.lit(name.lower()).alias('type'))
    
    # Melt the dataframe to convert date columns to rows
    id_vars = ['Country/Region', 'Province/State', 'Lat', 'Long', 'type']
    date_columns = [col for col in df.columns if col not in id_vars]
    
    df = df.melt(
        id_vars=id_vars,
        value_vars=date_columns,
        variable_name='date',
        value_name='cases'
    )
    
    # Convert date column to datetime
    df = df.with_columns(pl.col('date').str.to_datetime('%m/%d/%y'))
    
    # Rename columns to match expected output
    df = df.rename({
        'Country/Region': 'country',
        'Province/State': 'state'
    }).drop(['Lat', 'Long'])
    
    # Reorder columns for consistency
    df = df.select(['date', 'country', 'state', 'type', 'cases'])
    
    # Move HK to country level
    df = df.with_columns(
        pl.when(pl.col('state') == 'Hong Kong')
        .then(pl.lit('Hong Kong'))
        .otherwise(pl.col('country'))
        .alias('country'),
        
        pl.when(pl.col('state') == 'Hong Kong')
        .then(None)
        .otherwise(pl.col('state'))
        .alias('state')
    )
    
    # Create aggregated data for countries with states
    countries_with_states = (
        df.filter(pl.col('state').is_not_null())
        .group_by(['country', 'date', 'type'])
        .agg(pl.col('cases').sum())
        .with_columns(
            pl.col('country').map_elements(lambda x: f"{x} (total)", return_dtype=pl.String),
            pl.lit(None, dtype=pl.String).alias('state')
        )
        .select(['date', 'country', 'state', 'type', 'cases'])
    )
    
    # Combine original data with aggregated data
    df = pl.concat([df, countries_with_states])
    
    return df

def load_data(drop_states: bool = False, p_crit: float = .05, filter_n_days_100: Optional[int] = None) -> pl.DataFrame:
    df = load_individual_timeseries('confirmed')
    df = df.rename({'cases': 'confirmed'})
    
    if drop_states:
        # Drop states for simplicity
        df = df.filter(pl.col('state').is_null())
        
    # Estimated critical cases
    df = df.with_columns((pl.col('confirmed') * p_crit).alias('critical_estimate'))

    # Compute days relative to when 100 confirmed cases was crossed
    def compute_days_since_100(group_df):
        # Sort by date to ensure proper ordering
        group_df = group_df.sort('date')
        confirmed_cases = group_df['confirmed'].to_list()
        
        # Find indices where cases < 100 and >= 100
        before_100 = sum(1 for cases in confirmed_cases if cases < 100)
        after_100 = sum(1 for cases in confirmed_cases if cases >= 100)
        
        # Create days_since_100 array
        days_since_100 = list(range(-before_100, after_100))
        
        return group_df.with_columns(pl.Series('days_since_100', days_since_100))
    
    # Group by country and state (handling nulls), then apply the function
    df_with_days = []
    
    # Handle countries without states
    countries_no_states = df.filter(pl.col('state').is_null()).unique(['country'])['country'].to_list()
    
    for country in countries_no_states:
        country_data = df.filter((pl.col('country') == country) & (pl.col('state').is_null()))
        if len(country_data) > 0:
            df_with_days.append(compute_days_since_100(country_data))
    
    # Handle countries with states
    countries_with_states = df.filter(pl.col('state').is_not_null()).unique(['country', 'state'])
    
    for row in countries_with_states.rows(named=True):
        country, state = row['country'], row['state']
        state_data = df.filter((pl.col('country') == country) & (pl.col('state') == state))
        if len(state_data) > 0:
            df_with_days.append(compute_days_since_100(state_data))
    
    df = pl.concat(df_with_days) if df_with_days else df.with_columns(pl.lit(None).alias('days_since_100'))

    # Add deaths
    df_deaths = load_individual_timeseries('deaths')
    df_deaths = df_deaths.rename({'cases': 'deaths'}).select(['country', 'state', 'date', 'deaths'])
    
    # Join with deaths data
    df = df.join(df_deaths, on=['country', 'state', 'date'], how='left')
    
    if filter_n_days_100 is not None:
        # Select countries for which we have at least some information
        countries = (df.filter(pl.col('days_since_100') >= filter_n_days_100)
                    .select('country').unique()['country'].to_list())
        df = df.filter(pl.col('country').is_in(countries))

    return df
