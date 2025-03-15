import feedparser

def get_url():
    url = input("Enter the RSS feed URL: ")
    return url

def get_rss_feed(url):
    newsFeed = feedparser.parse(url)
    entry = newsFeed.entries[1]
    return entry
    # print(entry.keys())

def print_rss_feed(entry):
    print('Post Title:', entry.title)
    print('Post Description:', entry.summary)
    print('Post Link:', entry.link)

def main():
    url = get_url()
    entry = get_rss_feed(url)
    print_rss_feed(entry)

if __name__ == '__main__':
    main()