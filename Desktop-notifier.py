from win10toast import ToastNotifier
import feedparser
import time

toaster = ToastNotifier()

fp = feedparser.parse("https://timesofindia.indiatimes.com/world")
for news in fp['items']:
    toaster.showtoast(
        title=news['title'],
        msg=news['summary'],
        duration=5
    )    

    time.sleep(10)
