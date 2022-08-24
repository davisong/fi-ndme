import csv
import pandas

import db

# https://www.rootstrap.com/blog/how-to-manage-your-python-projects-with-pipenv-pyenv/
# https://fi.google.com/account?pli=1&authuser=1#callhistory
# https://developers.google.com/people/v1/getting-started

# convert staging table values
# create queries of data
# map phone numbers to contacts with Google People API
# create UI to display results
# enforce pipeline to stream data from google fi into db into data graphs

def main():
  # with open("FiHistory2018-07-2022-08.csv", mode='r') as f:
  #   reader = csv.DictReader(f, delimiter=',')
  #   for row in reader:
  #     print(f'date: {row["Date (-04:00)"]}\ttime: {row["Time (-04:00)"]}\tphone: {row["Phone #"]}\ttype: {row["Type"]}')

  # df = pandas.read_csv("FiHistory2018-07-2022-08.csv")
  # print(df)
  db.view_table()

if __name__ == "__main__":
  main()
