from itertools import islice
from youtube_comment_downloader import *

downloader = YoutubeCommentDownloader()
comments_generator = downloader.get_comments_from_url('https://www.youtube.com/watch?v=ScMzIvxBSi4', sort_by=SORT_BY_POPULAR)
comments = []

for comment in islice(comments_generator, 100):
    comments.append(comment["text"])

print(comments)
print(len(comments))
