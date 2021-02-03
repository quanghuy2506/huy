# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonelectronicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    asin = scrapy.Field()
    product_rating_numb = scrapy.Field()
    product_price = scrapy.Field()
    product_image_link = scrapy.Field()
    product_date = scrapy.Field()
    product_dimensions = scrapy.Field()
    availability = scrapy.Field()
    brand = scrapy.Field()
    rank = scrapy.Field()
    rating = scrapy.Field()
    link = scrapy.Field()

    product_name = scrapy.Field()

    id = scrapy.Field()
    review_rating = scrapy.Field()
    helpfulness = scrapy.Field()
    date_location = scrapy.Field()


    name = scrapy.Field()
    reviewer_ranking = scrapy.Field()
    helpful_votes = scrapy.Field()
    numb_reviews = scrapy.Field()
    text = scrapy.Field()
    title = scrapy.Field()
    rating = scrapy.Field()
    verified = scrapy.Field()

    pass
class Amazonproductreviewitem(scrapy.Item):
    id = scrapy.Field()
    review_rating = scrapy.Field()
    helpfulness = scrapy.Field()
    date_location = scrapy.Field()
    text = scrapy.Field()
    title = scrapy.Field()
    verified = scrapy.Field()
    pass

class Amazoncustomer(scrapy.Item):
    name = scrapy.Field()
    reviewer_ranking = scrapy.Field()
    helpful_votes = scrapy.Field()
    numb_reviews = scrapy.Field()
    text = scrapy.Field()
    title = scrapy.Field()
    rating = scrapy.Field()
    verified = scrapy.Field()
    pass





