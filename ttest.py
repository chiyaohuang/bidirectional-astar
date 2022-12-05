import pandas as pd
from math import sqrt
import csv

Layout = ['tiny', 'small','medium', 'big']
Search = ['dfs', 'bfs', 'ucs', 'astar,heuristic=manhattanHeuristic']

testheader = ['Map', 'Search Algorithm 1', 'Search Algorithm 2', 'Calculated T-Score', 'Two-Tailed T-Score', 'One-Tailed T-Score']

n = 20 #number of samples taken

ttt_val = 2.093 # two-tailed t-score for degree of freedom n-1 at alpha 0.05 [from table]
ott_val = 1.729 # one-tailed t-score for degree of freedom n-1 at alpha 0.05 [from table]

with open('ttest_mm.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(testheader)
  f.close()

for l in Layout:

  data_items=[]

  df = pd.read_csv('finalresult.csv')
  df = df[df['Map'].str.contains(l)]
  df = df.drop('Map', axis=1)
  df = df.drop('Total Cost', axis=1)
  df = df.drop('Score', axis=1)

  df1 = df[df['Search Algorithm']=='mm,heuristic=manhattanHeuristic']
  df1 = df1.reset_index()
  df1 = df1.drop('index', axis=1)
  df1 = df1.drop('Search Algorithm', axis=1)
  df1 = df1.rename(columns={'Number of Nodes Expanded': 'mm'})

  for s in Search:

    df2 = df[df['Search Algorithm']==s]
    df2 = df2.reset_index()
    df2 = df2.drop('index', axis=1)
    df2 = df2.drop('Search Algorithm', axis=1)
    df2 = df2.rename(columns={'Number of Nodes Expanded': s})

    dfnew = df1.join(df2)
    dfnew.reset_index()

    diff = dfnew['mm']-dfnew[s]
    diff = pd.DataFrame(diff, columns = ['diff'])
    dfnew = dfnew.join(diff)
    dftemp = pd.DataFrame()
    dftemp['diffc'] = dfnew['diff'].copy()
    sdiff = dfnew['diff']*dftemp['diffc']
    sdiff = pd.DataFrame(sdiff, columns = ['sdiff'])
    dfnew = dfnew.join(sdiff)
    a = dfnew['diff'].mean()
    b = dfnew['sdiff'].mean()
    tscore = (a/n)/(sqrt((b-((a*a)/(n)))/((n-1)*(n))))

    data_items.append(l)
    data_items.append('mm')
    data_items.append(s)
    data_items.append(tscore)
    data_items.append(ttt_val)
    data_items.append(ott_val)

    with open('ttest_mm.csv', 'a', newline='') as f:
      writer = csv.writer(f)
      writer.writerow(data_items)
      data_items = []
      f.close()

# temp = pd.read_csv('ttest_mm.csv')
# print(temp)

with open('ttest_mm0.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(testheader)
  f.close()

for l in Layout:

  data_items=[]

  df = pd.read_csv('finalresult.csv')
  df = df[df['Map'].str.contains(l)]
  df = df.drop('Map', axis=1)
  df = df.drop('Total Cost', axis=1)
  df = df.drop('Score', axis=1)

  df1 = df[df['Search Algorithm']=='mm']
  df1 = df1.reset_index()
  df1 = df1.drop('index', axis=1)
  df1 = df1.drop('Search Algorithm', axis=1)
  df1 = df1.rename(columns={'Number of Nodes Expanded': 'mm0'})

  for s in Search:

    df2 = df[df['Search Algorithm']==s]
    df2 = df2.reset_index()
    df2 = df2.drop('index', axis=1)
    df2 = df2.drop('Search Algorithm', axis=1)
    df2 = df2.rename(columns={'Number of Nodes Expanded': s})

    dfnew = df1.join(df2)
    dfnew.reset_index()

    diff = dfnew['mm0']-dfnew[s]
    diff = pd.DataFrame(diff, columns = ['diff'])
    dfnew = dfnew.join(diff)
    dftemp = pd.DataFrame()
    dftemp['diffc'] = dfnew['diff'].copy()
    sdiff = dfnew['diff']*dftemp['diffc']
    sdiff = pd.DataFrame(sdiff, columns = ['sdiff'])
    dfnew = dfnew.join(sdiff)
    a = dfnew['diff'].mean()
    b = dfnew['sdiff'].mean()
    tscore = (a/n)/(sqrt((b-((a*a)/(n)))/((n-1)*(n))))

    data_items.append(l)
    data_items.append('mm0')
    data_items.append(s)
    data_items.append(tscore)
    data_items.append(ttt_val)
    data_items.append(ott_val)

    with open('ttest_mm0.csv', 'a', newline='') as f:
      writer = csv.writer(f)
      writer.writerow(data_items)
      data_items = []
      f.close()

# temp = pd.read_csv('ttest_mm0.csv')
# print(temp)

with open('ttest_mm_mm0.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(testheader)
  f.close()

for l in Layout:

  data_items=[]

  df = pd.read_csv('finalresult.csv')
  df = df[df['Map'].str.contains(l)]
  df = df.drop('Map', axis=1)
  df = df.drop('Total Cost', axis=1)
  df = df.drop('Score', axis=1)

  df1 = df[df['Search Algorithm']=='mm,heuristic=manhattanHeuristic']
  df1 = df1.reset_index()
  df1 = df1.drop('index', axis=1)
  df1 = df1.drop('Search Algorithm', axis=1)
  df1 = df1.rename(columns={'Number of Nodes Expanded': 'mm'})

  df2 = df[df['Search Algorithm']=='mm']
  df2 = df2.reset_index()
  df2 = df2.drop('index', axis=1)
  df2 = df2.drop('Search Algorithm', axis=1)
  df2 = df2.rename(columns={'Number of Nodes Expanded': 'mm0'})

  dfnew = df1.join(df2)
  dfnew.reset_index()

  diff = dfnew['mm']-dfnew['mm0']
  diff = pd.DataFrame(diff, columns = ['diff'])
  dfnew = dfnew.join(diff)
  dftemp = pd.DataFrame()
  dftemp['diffc'] = dfnew['diff'].copy()
  sdiff = dfnew['diff']*dftemp['diffc']
  sdiff = pd.DataFrame(sdiff, columns = ['sdiff'])
  dfnew = dfnew.join(sdiff)
  a = dfnew['diff'].mean()
  b = dfnew['sdiff'].mean()
  tscore = (a/n)/(sqrt((b-((a*a)/(n)))/((n-1)*(n))))

  data_items.append(l)
  data_items.append('mm')
  data_items.append('mm0')
  data_items.append(tscore)
  data_items.append(ttt_val)
  data_items.append(ott_val)

  with open('ttest_mm_mm0.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data_items)
    data_items = []
    f.close()

# temp = pd.read_csv('ttest_mm_mm0.csv')
# print(temp)