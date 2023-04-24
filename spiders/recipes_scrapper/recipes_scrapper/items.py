from scrapy import Item, Field
from itemloaders.processors import TakeFirst, MapCompose, Compose


def normalize_ingredients(values):
    grouped_values = []
    arr_length = len(values)
    normalized = [item.strip() for item in values]

    index = 0
    while index < arr_length:
        value = {}
        if index+1 < arr_length and normalized[index+1] == '-':
            value = {'name': normalized[index], 'amount': normalized[index + 2]}
            index += 3
        else:
            value = {'name': normalized[index]}
            index += 1
        grouped_values.append(value)
    return grouped_values


class RecipeItem(Item):
    title = Field(output_processor=TakeFirst())
    ingredients = Field(input_processor=Compose(normalize_ingredients))
    url = Field(output_processor=TakeFirst())
