from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst

def get_price(txt):
    return float(txt.replace('£', '' ))

def convert_to_dollar(pounds):
    return pounds * 0.89

def get_quantity(txt):
    return int(txt.replace('(', '').split()[0])

class EbookItem(Item):
    
    title = Field()
    price = Field(
        input_processor=MapCompose(get_price),
        output_processor=TakeFirst()
    )
    quantity = Field(
        input_processor=MapCompose(get_quantity),
        output_processor=TakeFirst()
    )
