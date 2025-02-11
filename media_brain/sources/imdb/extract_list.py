# import requests

# import json,urllib.request
# data = urllib.request.urlopen("https://www.imdb.com/list/ls567819847/?ref_=uspf_ttl_1&view=detailed").read()
# output = json.loads(data)
# print (output)

import json

tv_shows = {}
movies = {}

'''
The json data was retrieved from the IMDB list page.
'''
def extract_json():
    # Open and read the JSON file
    with open('./imdb.json', 'r') as file:
        data = json.load(file)

    # Print the data
    for item in data['props']['pageProps']['mainColumnData']['list']['titleListItemSearch']['edges']:
        print(item['listItem'].keys(), end='\n')
        # print(item['listItem']['episodes']['episodes']['total'], end='\n\n')
        type = item['listItem']['titleType']['id']
        
        if 'tv' in type or 'show' in type:
            try:
                epi = item['listItem']['episodes']['episodes']['total']
            except:
                epi = 0
            
            tv_shows[item['listItem']['id']] = {
                'name': item['listItem']['titleText']['text'],\
                'year': item['listItem']['releaseYear']['year'],\
                'year': epi,\
            }
        if 'movie' in type:
            movies[item['listItem']['id']] = {
                'name': item['listItem']['titleText']['text'],\
                'year': item['listItem']['releaseYear']['year'],\
            }

    print("TV Shows")
    '''
        append the list of tv shows to a file, checking if already exist.
    '''
    for show in tv_shows:
        print(show)
        
    print("Movies")
    '''
        append the list of movies to a file, checking if already exist.
    '''
    for movie in movies:
        print(movie)

import pandas as pd
'''
csv is and export of the IMDB list
'''
def extract_csv():
    # Reads the CSV file into a DataFrame
    df = pd.read_csv('imdb_export.csv')

    for title in pd.Series(df['Original Title']):    
        # Prints the DataFrame
        print(title)


extract_csv()