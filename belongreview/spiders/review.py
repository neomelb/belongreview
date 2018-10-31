#待修改成适合Belong Review的代码

import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = 'belongreview'
    start_urls = [
        'https://www.productreview.com.au/p/belong.html'
        #'https://www.productreview.com.au/p/belong/2.html'
        ]


    def parse(self, response):
        #for href in response.css('.review h3 a::attr(href)'):
#            full_url = response.urljoin(href.extract())
#            yield scrapy.Request(full_url, callback=self.parse_question)

        #review = response.css('.review-content')
        for review in response.css('.review-content'):

        #for v in review:
            yield{
            #Review Title
            #title = review.css('[itemprop="name"]::text').extract_first()
            'title' : review.css('[itemprop="name"]::text').extract_first(),
            #Service Connection Type
            #type = review.css('.label-default::text').extract_first()
            'type' : review.css('.label-default::text').extract_first(),
            #Rating
            #rating = review.css('[itemprop="ratingValue"]::text').extract_first()
            'rating' : review.css('[itemprop="ratingValue"]::text').extract_first(),
            #Review Details
            #content = review.css('.review-overall::text').extract_first()
            'content' : review.css('.review-overall::text').extract_first(),
            #Review Date
            #date = review0.css('[itemprop="datePublished"]').extract()
            'date' : review.css('[itemprop="datePublished"]').extract(),
            }

        #Get reviews on the next pages
        next_page = response.css('a[rel="next"]::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
