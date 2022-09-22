# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class YellowpagesPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        websites = adapter.get("website")
        for each_website in websites:
            if "redirect" in each_website:
                break
        adapter["website"] = each_website
        return item
