#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy


class CCFSpider(scrapy.spiders.Spider):
    name = "ccf"
    allowed_domains = ["dblp.uni-trier.de", "jslhr.pubs.asha.org", "digital-library.theiet.org"]
    start_urls = [
        "http://dblp.uni-trier.de/db/journals/ai/",
        "http://dblp.uni-trier.de/db/journals/pami/",
        "http://dblp.uni-trier.de/db/journals/ijcv/",
        "http://dblp.uni-trier.de/db/journals/jmlr/",

        "http://dblp.uni-trier.de/db/journals/tap/",
        "http://dblp.uni-trier.de/db/journals/tslp/",
        "http://dblp.uni-trier.de/db/journals/coling/",
        "http://dblp.uni-trier.de/db/journals/cviu/",
        "http://dblp.uni-trier.de/db/journals/dke/",
        "http://dblp.uni-trier.de/db/journals/ec/",
        "http://dblp.uni-trier.de/db/journals/taffco/",
        "http://dblp.uni-trier.de/db/journals/taslp/",
        "http://dblp.uni-trier.de/db/journals/tcyb/",
        "http://dblp.uni-trier.de/db/journals/tec/",
        "http://dblp.uni-trier.de/db/journals/tfs/",
        "http://dblp.uni-trier.de/db/journals/tnn/",
        "http://dblp.uni-trier.de/db/journals/ijar/",
        "http://dblp.uni-trier.de/db/journals/jair/",
        "http://dblp.uni-trier.de/db/journals/jar/",
        "http://jslhr.pubs.asha.org/",
        "http://dblp.uni-trier.de/db/journals/ml/",
        "http://dblp.uni-trier.de/db/journals/neco/",
        "http://dblp.uni-trier.de/db/journals/nn/",
        "http://dblp.uni-trier.de/db/conf/par/",
        "http://dblp.uni-trier.de/db/journals/aamas/",

        "http://dblp.uni-trier.de/db/journals/talip/",
        "http://dblp.uni-trier.de/db/journals/apin/",
        "http://dblp.uni-trier.de/db/journals/artmed/",
        "http://dblp.uni-trier.de/db/journals/alife/",
        "http://dblp.uni-trier.de/db/journals/ci/",
        "http://dblp.uni-trier.de/db/journals/csl/",
        "http://dblp.uni-trier.de/db/journals/connection/",
        "http://dblp.uni-trier.de/db/journals/dss/",
        "http://dblp.uni-trier.de/db/journals/eaai/",
        "http://dblp.uni-trier.de/db/journals/es/",
        "http://dblp.uni-trier.de/db/journals/eswa/",
        "http://dblp.uni-trier.de/db/journals/fss/",
        "http://dblp.uni-trier.de/db/journals/tciaig/",
        "http://digital-library.theiet.org/content/journals/iet-cvi",
        "http://digital-library.theiet.org/content/journals/iet-spr",
        "http://dblp.uni-trier.de/db/journals/ivc/",
        "http://dblp.uni-trier.de/db/journals/ida/",
        "http://dblp.uni-trier.de/db/journals/ijcia/",
        "http://dblp.uni-trier.de/db/journals/ijdar/",
        "http://dblp.uni-trier.de/db/journals/ijis/",
        "http://dblp.uni-trier.de/db/journals/ijns/",
        "http://dblp.uni-trier.de/db/journals/ijprai/",
        "http://dblp.uni-trier.de/db/journals/ijcia/",
        "http://dblp.uni-trier.de/db/journals/jetai/",
        "http://dblp.uni-trier.de/db/journals/kbs/",
        "http://dblp.uni-trier.de/db/journals/mt/",
        "http://dblp.uni-trier.de/db/journals/mva/",
        "http://dblp.uni-trier.de/db/journals/nc/",
        "http://dblp.uni-trier.de/db/journals/nle/",
        "http://dblp.uni-trier.de/db/journals/nca/",
        "http://dblp.uni-trier.de/db/journals/npl/",
        "http://dblp.uni-trier.de/db/journals/ijon/",
        "http://dblp.uni-trier.de/db/journals/paa/",
        "http://dblp.uni-trier.de/db/journals/prl/",
        "http://dblp.uni-trier.de/db/journals/soco/",
        "http://dblp.uni-trier.de/db/journals/wias/",
    ]

    papers = {}

    def parse(self, response):
        # print(response, type(response))
        # from scrapy.http.response.html import HtmlResponse
        # print(response.body_as_unicode())

        current_url = response.url  # 爬取时请求的url
        body = response.body  # 返回的html
        unicode_body = response.body_as_unicode()  # 返回的html unicode编码
        urls = response.xpath('/html/body/div[@id="main"]/ul/li/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_paper, dont_filter=True)

    def parse_paper(self, response):
        current_url = response.url
        journal = current_url.split('/')[-2]
        if journal not in self.papers.keys():
            self.papers[journal] = []
        papers = response.xpath('/html/body/div[@id="main"]/ul/li/div[@class="data"]/span[@class="title"]/text()').extract()
        self.papers[journal].extend(papers)
        #print(self.papers)