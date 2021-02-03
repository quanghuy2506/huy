import scrapy
from ..items import AmazonelectronicItem
from urllib.parse import urlencode
from urllib.parse import urljoin
import numpy as np
import regex

#API = 'd5ed5b28554cc332edb3402152537f47'


'''def get_url(url):
    payload = {'api_key': API, 'url': url, 'country_code': 'uk'}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url'''


class AmazonSpider(scrapy.Spider):
    name = 'amazon_cameraphoto'
    page_number = 2
    # start_urls = [
    #    'https://www.amazon.co.uk/gp/browse.html?node=560834&ref_=nav_em__p_0_2_12_2'
    # ]
    start_urls = [
        'https://www.amazon.co.uk/product-reviews/B014I8SIJY/ref=cm_cr_othr_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    ]

    '''def start_requests(self):
        url = 'https://www.amazon.co.uk/AZATOM-HDMI-Cable-Length-PlayStation-Black/product-reviews/B07KRKYWX5/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
        yield scrapy.Request(url=get_url(url), callback=self.parse_4)'''

    '''def parse(self, response):
        sub_cat = response.css('.octopus-pc-category-card-v2-category-link')
        for i in sub_cat:
            link = 'https://www.amazon.co.uk' + str(i.css('::attr(href)').extract_first())
            yield scrapy.Request(url=get_url(link), callback = self.parse_1)
    def parse_1(self, response):
        see_all = 'https://www.amazon.co.uk' + str(response.css('.a-link-normal').css('::attr(href)').extract_first())
        if str(response.css('.a-link-normal').css('::attr(href)').extract_first()) is not None:
            yield scrapy.Request(url=get_url(see_all), callback = self.parse_2)
    def parse_2(self, response):
        # items = AmazonelectronicItem()
        # open_in_browser(response)
        all_product_attr = response.css('.s-latency-cf-section')
        for attr in all_product_attr:
            link_name = 'https://www.amazon.co.uk' + str(attr.css('.a-link-normal').css('::attr(href)').get())
            # items['link'] = link_name
            # yield items
            if str(attr.css('.a-link-normal').css('::attr(href)').get()) is not None:
                yield scrapy.Request(url=get_url(link_name), callback=self.parse_3)

        # This is for the page that has "next" button
        # next_page = 'https://www.amazon.co.uk' + str(response.css(".a-last").css('::attr(href)').get())
        # if next_page is not None:
        #    yield response.follow(next_page, callback = self.parse)
        # This is for the page that has number to follow to next page

        next_page = 'https://www.amazon.co.uk' + str(response.css(".a-last a").css('::attr(href)').extract_first())
        if AmazonSpider.page_number is not None:
            AmazonSpider.page_number += 1
            yield scrapy.Request(url=get_url(next_page), callback=self.parse_2)

    def parse_3(self, response):
        items = AmazonelectronicItem()
        # response = response.css('#detailBulletsWrapper_feature_div')
        # initilise variable - product attributes
        """asin = ''
        product_dimensions = ''
        product_date = ''
        brand = ''
        rank = ''
        for i in range(1, 10):
            if 'Dimensions' in str(
                    response.css('li:nth-child({}) .a-text-bold'.format(i)).css('::text').extract()):
                product_dimensions = response.css('li:nth-child({}) .a-text-bold+ span'.format(i)).css(
                    '::text').extract_first()

            elif 'Date' in str(
                    response.css('li:nth-child({}) .a-text-bold'.format(i)).css('::text').extract()):
                product_date = response.css('li:nth-child({}) .a-text-bold+ span'.format(i)).css(
                    '::text').extract_first()

            elif 'Manufacturer' in str(
                    response.css('li:nth-child({}) .a-text-bold'.format(i)).css('::text').extract()):
                brand = response.css('li:nth-child({}) .a-text-bold+ span'.format(i)).css(
                    '::text').extract_first()

            elif 'ASIN' in str(response.css('li:nth-child({}) .a-text-bold'.format(i)).css('::text').extract()):
                asin = response.css('li:nth-child({}) .a-text-bold+ span'.format(i)).css('::text').extract_first()

            elif 'Sellers' in str(
                    response.css('li:nth-child({}) .a-text-bold'.format(i)).css('::text').extract()):
                rank = response.css('li:nth-child({}) .a-text-bold+ span'.format(i)).css('::text').extract_first()

        rating = response.css('#averageCustomerReviews .a-star-4-5').css('::text').extract_first()
        product_rating_numb = response.css('#acrCustomerReviewText').css('::text').extract_first()
        product_price = response.css('#priceblock_ourprice').css('::text').extract_first()
        product_image_link = response.css('#altImages , .a-button-text').css('::attr(src)').extract()

        availability = response.xpath('//div[@id="availability"]//text()').extract()


        items['product_rating_numb'] = product_rating_numb
        items['product_price'] = product_price
        items['product_image_link'] = product_image_link
        items['product_date'] = product_date
        items['product_dimensions'] = product_dimensions
        items['availability'] = availability
        items['brand'] = brand
        items['rank'] = rank
        items['rating'] = rating"""
        # initialise customer reviews
        all_reviews_link = 'https://www.amazon.co.uk' + str(
            response.css('#reviews-medley-footer .a-text-bold').css('::attr(href)').extract_first())
        if str(
                response.css('#reviews-medley-footer .a-text-bold').css('::attr(href)').extract_first()) is not None:
            yield scrapy.Request(url= get_url(all_reviews_link), callback=self.parse_4)'''

    def parse(self, response):
        items = AmazonelectronicItem()
        '''product_name = response.css('.a-text-ellipsis .a-link-normal').css('::text').extract_first()
        items['product_name'] = product_name
        yield items
        all_reviews = response.css('#cm_cr-review_list .a-section.celwidget')
        for review in all_reviews:
            id = review.css('.a-profile-name').css('::text').extract_first()
            review_rating = review.css('.review-rating').css('::text').extract_first()
            helpfulness = review.css('.cr-vote-text').css('::text').extract_first()
            date_location = review.css('.review-date').css('::text').extract_first()
            verified = review.css('.a-color-state').css('::text').extract_first()
            if review.css('.cr-translate-this-review-section .a-link-normal').css(
                    '::text').extract_first() == 'Translate review to English':
                text = review.css('.review-text-content .cr-translated-review-content').css(
                    '::text').extract_first()
                title = review.css('.a-text-bold .cr-translated-review-content').css('::text').extract_first()
            else:
                text = review.css('.review-text-content span').css('::text').extract_first()
                title = review.css('.a-link-normal.a-text-bold span').css('::text').extract_first()

            items['id'] = id
            items['review_rating'] = review_rating
            items['helpfulness'] = helpfulness
            items['date_location'] = date_location
            items['text'] = text
            items['title'] = title
            items['verified'] = verified
            yield items'''
        # crawling personal data
        all_reviews = response.css('#cm_cr-review_list .a-section.celwidget')
        for review in all_reviews:
            profile_link = 'https://www.amazon.co.uk' + str(
                review.css('.a-profile').css('::attr(href)').extract_first())
            # items['link'] = profile_link
            # yield items
            if str(review.css('.a-profile').css('::attr(href)').extract_first()) is not None:
                yield response.follow(profile_link, callback=self.parse_5)
            else: pass

        next_page_review = 'https://www.amazon.co.uk' + str(
            response.css(".a-last a").css('::attr(href)').extract_first())
        if next_page_review is not None:
            yield response.follow(next_page_review, callback=self.parse)
        else: pass

    def parse_5(self, response):
        items = AmazonelectronicItem()
        name = response.css('.a-size-extra-large').css('::text').extract_first()
        reviewer_ranking = response.css('.a-span12 .a-row .a-size-base').css('::text').extract_first()
        helpful_votes = response.css('.large-margin-right:nth-child(1) .a-size-large').css('::text').extract_first()
        numb_reviews = response.css('.large-margin-right+ .large-margin-right .a-size-large').css(
            '::text').extract_first()

        items['name'] = name
        items['reviewer_ranking'] = reviewer_ranking
        items['helpful_votes'] = helpful_votes
        items['numb_reviews'] = numb_reviews

        yield items
#    cd AmazonElectronic
#    scrapy genspider example example.com
# scrapy crawl amazon_cameraphoto -o amazon.json
# scrapy crawl amazon_cameraphoto -o profile.json
# wget -U 'Scrapy/1.3.0 (+http://scrapy.org)' url