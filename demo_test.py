#Create a collection of news articles having the keys as
# id, title, date, description and type
#Apply operations to search based on id or category or title

#news_articles = list()
#print(len(news_articles))
# general, cricket, politics, entertainment, crime, weather, health

'''
news_articles = [{"id":123, "title":'Happy New Year', "date":'01-01-2022', "description":'2022 for KLU', "type":'general'},
                 {"id":223, "title":'IND vs SA', "date":'01-01-2022', "description":'India Won', "type":'sports'},
                 {"id":323, "title":'Bheemla Naayak', "date":'01-01-2022', "description":'Releasing date', "type":'Movie'},
                 {"id":423, "title":'Elections', "date":'01-01-2022', "description":'Elections result', "type":'politics'},
                 {"id":523, "title":'Weather Report', "date":'01-01-2022', "description":'Weather in Vaddeswaram', "type":'weather'},
                 {"id":623, "title":'Robbery', "date":'01-01-2022', "description":'Robbery in a city', "type":'crime'},
                 {"id":723, "title":'Omricon', "date":'01-01-2022', "description":'increase in cases', "type":'health'}]
#print(type(news_articles))
#print(news_articles)
'''

news_articles = {'id':[123,223,323,423,523,623,723],
                'title':["Happy New Year", "IND vs SA", "Bheemla Naayak","Elections", "Weather Report","Robbery", "Omricon"],
                'date':['01-01-2022','01-01-2022','01-01-2022','01-01-2022','01-01-2022','01-01-2022','01-01-2022'],
                
                }
#operations:


for na in news_articles:
    #print(types(na))
    #print(na)
    #print(na.keys())
    #print(na.values())
    #print(na.items())
    if(na.get("id")==323):
        print(na.items())
        print(na.get('type'))
        print(na.get('date'))
        print(na.get('title'))



'''
1. Write a function to display the news as a specific category or a type
2. Write a function to display the news as of a specific date
'''