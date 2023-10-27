items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


def find_item_index(list_products, desiared_product):

    if desiared_product in list_products:
        return list_products.index(desiared_product)
    else:
        return None


for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
