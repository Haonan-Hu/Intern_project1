# Internship project1
# Author: Haonan Hu
# Date: 2020/07/12
# Version: 1.0
# Functionality: Testing YAKE algorithm

import yake
import scraping

my_url = ''
text = scraping.scrape_url(my_url)

kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(text)

language = "en"
max_ngram_size = 3
deduplication_threshold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 20

custom_kw_extractor = yake.KeywordExtractor(lan=language,
                                            n=max_ngram_size,
                                            dedupLim=deduplication_threshold,
                                            dedupFunc=deduplication_algo,
                                            windowsSize=windowSize,
                                            top=numOfKeywords,
                                            features=None)
keywords = custom_kw_extractor.extract_keywords(text)

for kw in keywords:
    print(kw)
