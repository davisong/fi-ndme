from distutils.util import execute
from dotenv import load_dotenv
import os
import pyodbc

# convert CSV file to SQL in Azure DB
# https://portal.azure.com/#home
# https://docs.microsoft.com/en-us/azure/azure-sql/load-from-csv-with-bcp?view=azuresql
# https://docs.microsoft.com/en-us/azure/azure-sql/database/connect-query-python?view=azuresql
# sqlcmd -S tcp:be-fucking-fi-real.database.windows.net -U <USERNAME> -P <PASSWORD>
# bcp dbo.FiHistoryStaging in FiHistoryEncoded.csv -S tcp:be-fucking-fi-real.database.windows.net -d bffr-db -U <USERNAME> -P <PASSWORD> -q -c -t ";"  load_dotenv()


def execute_query(query):
  load_dotenv()
  conn_str = 'DRIVER='+os.environ.get('DRIVER')+';SERVER=tcp:'+os.environ.get('SERVER')+';PORT=1433;DATABASE='+os.environ.get('DATABASE')+';UID='+os.environ.get('USERNAME')+';PWD='+ os.environ.get('PASSWORD')
  with pyodbc.connect(conn_str) as conn:
    with conn.cursor() as cursor:
      cursor.execute(query)
      row = cursor.fetchone()
      while row:
        print([str(col) for col in row])
        # print (str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()

def create_staging_table():
  # CREATE TABLE Calls (
  #   ID INTEGER PRIMARY KEY,
  #   Number VARCHAR(50) NOT NULL,
  #   Date DATE NOT NULL,
  #   Time TIME NOT NULL,
  #   Type VARCHAR(50) NOT NULL,
  #   Duration SMALLINT NOT NULL
  # )
  # ;

  # CREATE TABLE Messages (
  #   ID INTEGER PRIMARY KEY,
  #   Number VARCHAR(50) NOT NULL,
  #   Date DATE NOT NULL,
  #   Time TIME NOT NULL,
  #   Type VARCHAR(50) NOT NULL
  # )
  # ;
  
  # INSERT INTO [dbo].[Messages] (ID, Number, Date, Time, Type)
  # SELECT * FROM [dbo].[FiHistoryStaging]
  # WHERE type="Received text" OR type="Sent text"

  query_str = """CREATE TABLE FiHistoryStaging
    (
      Date VARCHAR(50) NOT NULL,
      Time VARCHAR(50) NOT NULL,
      Phone VARCHAR(500) NOT NULL,
      Type VARCHAR(50) NOT NULL,
      Duration VARCHAR(50),
      Rate VARCHAR(50),
      Cost VARCHAR(50)
    )
    ;
  """
  execute_query(query_str)

def drop_table():
  query_str = "DROP TABLE FiHistoryStaging"
  execute_query(query_str)

def view_table():
  query_str = "SELECT TOP (25) * FROM FiHistoryStaging"
  execute_query(query_str)

# number of calls/texts total every month
# heatmap of phone activity
# most commonly missed number
# most commonly called (incoming) number
# most commonly called (outgoing) number
# most commonly texted (sender) number
# most commonly texted (receiver) number
# average length of call