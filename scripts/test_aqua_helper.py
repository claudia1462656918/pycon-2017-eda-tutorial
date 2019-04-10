def test_time_slice():
  # df input
  df_input = {
    'time_period': ['1958-1962', '1963-1967', '1968-1972', '1973-1977', '1978-1982'],
    'country': ['China', 'US', 'UK', 'Afghanistan','Japan'],
    'variable': ['area','land','pop','gdp','treaty'],
    'value': [1,2,3,4,5]
       }
  df = pd.DataFrame(data=df_input)
        
  # time_period input 
  time_period = '1958-1962'
  
  
 # expeced data 
  expected = {
      'area': [1.0, np.NaN],
      'pop': [np.NaN,3.0]
  }

  time_slice_df = pd.DataFrame(data=expected)
  time_slice_df.index = ['China','UK']
  time_slice_df.columns.name = 'country'   
  
  # check type 
  assert isinstance(time_slice_df, pd.DataFrame)
  
  # check expected output 
  assert time_slice_df.equals(time_slice(df, time_period))
  

  
def test_time_series():
  # df input
  df_input = {
    'country': ['US', 'US', 'UK', 'US','Japan'],
    'variable': ['pop','pop','pop','gdp','treaty'],
    'value': [1,2,3,4,5],
    'year_measured': [1995,1992,1991,1999,1993]
       }
  df = pd.DataFrame(data=df_input)
        
  # country input 
  country = 'US'
  
 # variable input 
  variable = 'pop'
  
 # expeced data 
  expected = {
      'year_measured':[1995,1992],
      'pop':[1,2]
             }
  time_series_df = pd.DataFrame(data=expected)
  time_series_df.set_index('year_measured') 
  
  # check type 
  assert isinstance(time_series_df, pd.DataFrame)
  
  # check expected output 
  ##????
  assert time_series_df.equals(time_series(df, country, variable))

  
  
  
  
def variable_slice(df, variable):
    
    # Only data for that variable
    df = df[df.variable==variable]
    
    # Get variable for each country over the time periods 
    df = df.pivot(index='country', columns='time_period', values='value')
    return df
  

def test_variable_slice():
  # df input
  df_input = {
    'time_period': ['1958-1962', '1963-1967', '1968-1972', '1973-1977', '1978-1982'],
    'country': ['US', 'US', 'UK', 'US','Japan'],
    'variable': ['pop','pop','pop','gdp','treaty'],
    'value': [1,2,3,4,5],
       }
  df = pd.DataFrame(data=df_input)
  
 # variable input 
  variable = 'pop'
  
 # expeced data 
  expected = {
      'year_measured':[1995,1992],
      'pop':[1,2]
             }
  variable_slice_df = pd.DataFrame(data=expected)
  variable_slice_df.set_index('year_measured') 
  
  # check type 
  assert isinstance(variable_slice_df, pd.DataFrame)
  
  # check expected output 
  assert variable_slice_df.equals(variable_slice(df, variable))

  
