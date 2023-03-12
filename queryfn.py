import pandas as pd
import pyodbc as ps
import warnings
warnings.filterwarnings('ignore', message='pandas only supports SQLAlchemy connectable')



def query_db(query):
    ''' Function that connects to a local database, query and 
        returns output as a dataframe.
        
    Args:
        query (str) : A sql query to retrieve necessary data.
        
    Returns:
        dataframe : A pandas dataframe with the sql output.
    '''
    conn = ps.connect( 'Driver={SQL Server Native Client 11.0};'
                    'Server=localhost\SQLEXPRESS;'
                    'Database=AdventureWorks2017;'
                    'Trusted_Connection=yes;'
                )
    df = pd.read_sql(query, conn)
    
    return df
    





