from email.policy import default
import scrapy
from scrapy.loader import ItemLoader
from yellowpages.items import YellowpagesItem


class YellowSpider(scrapy.Spider):
    name = "yellow"

    start_urls = [
        "https://www.yellowpages.ca/search/si/1/Restaurants/Montreal+QC",
    ]

    def parse(self, response):
        restaurant_links = response.css("a.listing__name--link::attr(href)")
        yield from response.follow_all(restaurant_links, self.parse_restaurant)

        next_page = response.css("a.pageButton").attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_restaurant(self, response):
        l = ItemLoader(item=YellowpagesItem(), response=response)
        l.add_css(
            "name",
            ".merchant__name h1.merchant__title span[itemprop=name]::text",
        )
        l.add_css(
            "street_address",
            "div.merchant__details__section--address div.merchant__address span[itemprop=streetAddress]::text",
        )
        l.add_css(
            "address_locality",
            "div.merchant__details__section--address div.merchant__address span[itemprop=addressLocality]::text",
        )
        l.add_css(
            "address_region",
            "div.merchant__details__section--address div.merchant__address span[itemprop=addressRegion]::text",
        )
        l.add_css(
            "postal_code",
            "div.merchant__details__section--address div.merchant__address span[itemprop=postalCode]::text",
        )
        l._add_value(
            "telephone", response.css("span[itemprop=telephone]::text").extract_first()
        )
        websites = response.css('a.hide-print::attr("href")').getall()
        website = ""
        for each_website in websites:
            if "gourl" in each_website and "facebook" not in each_website:
                website = each_website
        l.add_value("website", website)
        l.add_css(
            "ratings",
            ".merchant__details__rating__content span.ypStars::attr(aria-label)",
        )
        return l.load_item()
