import json
import os

class ItemManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}
        self.load()

    def load(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}

    def save(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def find_first_available_id(self):
        for i in range(1, len(self.data) + 2):
            if str(i) not in self.data:
                return str(i)
        return str(len(self.data) + 1)

    def add_item(self, name, amount, expiration_date, entry_date):
        item_id = self.find_first_available_id()
        self.data[item_id] = {
            "name": name,
            "amount": amount,
            "expiration_date": expiration_date,
            "entry_date": entry_date
        }
        self.save()

    def remove_item(self, name, amount, expiration_date):
        item_to_remove = None
        for item_id, item in self.data.items():
            if item["name"] == name and item["amount"] == amount and item["expiration_date"] == expiration_date:
                item_to_remove = item_id
                break
        if item_to_remove:
            del self.data[item_to_remove]
        self.save()

    def has_item(self, name):
        for item in self.data.values():
            if item["name"] == name:
                return True
        return False
    
    def get_item_amount(self, name):
        for item in self.data.values():
            if item["name"] == name:
                return item['amount']
        return None
    
    def update_item_amount(self, name, new_amount):
        for item in self.data.values():
            if item["name"] == name:
                item['amount'] = new_amount
                self.save()
                return True
        return False

    def remove_item_by_name(self, name):
        item_to_remove = None
        for item_id, item in self.data.items():
            if item["name"] == name:
                item_to_remove = item_id
                break
        if item_to_remove:
            del self.data[item_to_remove]
            self.save()
            return True
        return False
    
    def get_items(self):
        return self.data

    def reset(self):
        self.data = {}
        self.save()

class Expired(ItemManager):
    def __init__(self, file_path="expired.json"):
        super().__init__(file_path)

class ExpiringSoon(ItemManager):
    def __init__(self, file_path="expiring_soon.json"):
        super().__init__(file_path)

class InStock(ItemManager):
    def __init__(self, file_path="instock.json"):
        super().__init__(file_path)

class Shopping(ItemManager):
    def __init__(self, file_path="shopping.json"):
        super().__init__(file_path)
