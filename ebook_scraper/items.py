from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst

def get_price(txt):
    return float(txt.replace('£', '' ))

def convert_to_dollar(pounds):
    return pounds * 0.89

class EbookItem(Item):
    
    title = Field()
    price = Field(
        input_processor=MapCompose(get_price, convert_to_dollar),
        output_processor=TakeFirst()
    )
