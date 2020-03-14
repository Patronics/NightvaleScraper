#! /usr/bin/env python3

import feedparser
feed = feedparser.parse('http://feeds.nightvalepresents.com/welcometonightvalepodcast')
print(feed["channel"]["title"])
#print(feed["channel"]["description"])
for item in feed["items"]:
	print(item["title"])
	print(item["summary_detail"]["value"].partition("Weather:")[2].partition("</p>")[0],"\n")
