import feedparser

url = input("Enter the RSS feed URL: ")
newsFeed = feedparser.parse(url)
entry = newsFeed.entries[1]

print('Post Title:', entry.title)
print('Post Description:', entry.summary)
print('Post Link:', entry.link)
