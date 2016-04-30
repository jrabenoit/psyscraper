#This section runs spiders for each CS/ML conference

#AAAI
scrapy crawl aaai_2005_2014 -o aaai_2005_2014_items.json

#IJCAI
#IJCAI is published every 2 years; we end up at 2013 as the last year published.
scrapy crawl ijcai_2005 -o ijcai_2005_items.json
scrapy crawl ijcai_2007 -o ijcai_2007_items.json
scrapy crawl ijcai_2009 -o ijcai_2009_items.json
scrapy crawl ijcai_2011 -o ijcai_2011_items.json
scrapy crawl ijcai_2013 -o ijcai_2013_items.json

#ICML
scrapy crawl icml_2005 -o icml_2005_items.json
scrapy crawl icml_2006 -o icml_2006_items.json
scrapy crawl icml_2007 -o icml_2007_items.json
scrapy crawl icml_2008 -o icml_2008_items.json
scrapy crawl icml_2009 -o icml_2009_items.json
scrapy crawl icml_2010 -o icml_2010_items.json
scrapy crawl icml_2011 -o icml_2011_items.json
scrapy crawl icml_2012 -o icml_2012_items.json
scrapy crawl icml_2013 -o icml_2013_items.json
scrapy crawl icml_2014 -o icml_2014_items.json

#MICCAI
scrapy crawl miccai_2005_2014 -o miccai_2005_2014_items.json

#NIPS
#NIPS 2014 has yet to be held
scrapy crawl nips_2005_2013 -o nips_2005_2013_items.json

#UAI
#UAI 2014 has yet to be published in an XPath format... only pdf available as of Nov 19 2014
scrapy crawl uai_2005_2013 -o uai_2005_2013_items.json

#IEEE
#scrapy crawl ieee_2005_2014 -o ieee_2005_2014_items.json

#This section runs spiders for each CS/ML Journal

# MLJ
scrapy crawl mlj_2005_2014 -o mlj_2005_2014_items.json

#JMLR
scrapy crawl jmlr_2005_2014 -o jmlr_2005_2014_items.json

#AIJ
scrapy crawl aij_2005_2014 -o aij_2005_2014_items.json

#JAIR
scrapy crawl jair_2005_2014 -o jair_2005_2014_items.json
