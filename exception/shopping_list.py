class ShoppingList:
    # 初始化购物清单，shopping_list 是字典类型，包含商品名和对应价格
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list
    # 返回购物清单上物品的数量
    def get_items_count(self):
        return len(self.shopping_list)
    # 返回购物清单上所有物品的总价格、
    def get_total_price(self):
        total_price = 0
        for price in self.shopping_list.values():
            total_price += price
        return total_price