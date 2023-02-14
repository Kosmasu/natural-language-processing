import json
import katalog_crawler
import artikel_crawler

URL_KATALOG = "https://inet.detik.com/indeks"
namaFileKatalog = "katalog"
namaFileCorpus = "corpus"

page = int(input("Jumlah page >> "))

print("crawling katalog...")
articles = katalog_crawler.crawl(URL_KATALOG, page)
print("katalog length:", len(articles))

with open(f"hasil/{namaFileKatalog}.json", 'w') as f:
  json.dump(articles, f)

corpus = []
for index, article in enumerate(articles):
  corpus.append(artikel_crawler.crawl(article["link"]))
  print(f"{index}.\tcrawling article...")

with open(f"hasil/{namaFileCorpus}.json", 'w') as f:
  json.dump(corpus, f)

print("done.")