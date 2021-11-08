from googlesearch import search

def search_google(query):
    results = []
    for x in search(query, tld="com", num=1, stop=1, pause=2):
        results.append(x)
    return results[0]



