from instascrape import *

google_post = Post('https://www.instagram.com/p/CJmnZgqnnE_/')

google_post.scrape()

test = google_post['hashtags']
print(test)