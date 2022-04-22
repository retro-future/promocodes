from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import json
from os.path import exists


class PromoCode:
    def __init__(self, amount: int, group_name: str):
        self.amount = amount
        self._group_name = group_name
        self._code_list = []
        self.__generate_codes()

    def __generate_codes(self):
        for i in range(self.amount):
            self.codes.append(get_random_string(length=8))

    @property
    def group(self):
        return self._group_name

    @property
    def codes(self):
        return self._code_list


class PromoCodesContext:
    def __init__(self):
        try:
            with open("data_file.json") as fp:
                self.json_data = json.load(fp)
        except FileNotFoundError:
            self.json_data = {}

    def add(self, promo_code: PromoCode):
        group = promo_code.group
        codes = promo_code.codes
        self.json_data[group] = codes
        with open("data_file.json", "w") as fp:
            json.dump(self.json_data, fp)

    def delete(self, promo_code: PromoCode):
        group = promo_code.group
        if not self.json_data.get(group):
            return "that group not exists"
        del self.json_data[group]
        with open("data_file.json", "w") as fp:
            json.dump(self.json_data, fp)



mypromo = PromoCode(10, "test34")
mypromo1 = PromoCode(10, "test12")
mypromo2 = PromoCode(10, "test23")

mypromocodes = PromoCodesContext()
mypromocodes.add(mypromo)
mypromocodes.add(mypromo1)
mypromocodes.add(mypromo2)
mypromocodes.delete(mypromo2)
