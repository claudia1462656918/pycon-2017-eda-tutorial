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
      'country': ['China','UK'],
      'time_period':['1958-1962','1958-1962'],
      'variable': ['area','pop'],
      'value':[1,3]
  }

  time_slice_df = pd.DataFrame(data=expected)
  time_slice_df = time_slice_df.pivot(index='country', columns='variable', values='value')

  
  # check type 
  assert isinstance(time_slice_df, pd.DataFrame)
  
  # check expected output 
  assert time_slice_df.equals(aqua_helper.time_slice(df, time_period))
  

  
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
  time_series_df.year_measured = time_series_df.year_measured.astype(int)
  time_series_df.set_index('year_measured',inplace=True)
  time_series_df.columns = ['pop']
  
  # check type 
  assert isinstance(time_series_df, pd.DataFrame)
  
  # check expected output 
  assert time_series_df.equals(aqua_helper.time_series(df, country, variable))

  

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
  expected = {'country':['US'],
                'time_period':['1973-1977'],
                'variable':['gdp'],
                'value':[4]}
  variable_slice_df = pd.DataFrame(data=expected)
  variable_slice_df = variable_slice_df.pivot(index='country', columns='time_period', values='value')
  variable_slice_df.equals(variable_slice(df, 'gdp')) 
  
  # check type 
  assert isinstance(variable_slice_df, pd.DataFrame)
  
  # check expected output 
  assert variable_slice_df.equals(aqua_helper.variable_slice(df, variable))

  
