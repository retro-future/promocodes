from django.utils.crypto import get_random_string
import json


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
        print("successfully added")

    def delete(self, promo_code: PromoCode):
        group = promo_code.group
        if not self.json_data.get(group):
            return "that group not exists"
        del self.json_data[group]
        with open("data_file.json", "w") as fp:
            json.dump(self.json_data, fp)
        print("OK")

    def check(self, code: str):
        if not self.json_data:
            print("файл пуст")
            return
        code_list = []
        for code_array in self.json_data.values():
            code_list.extend(code_array)
        if code not in code_list:
            print("код не существует")
            return
        else:
            for group, values in self.json_data.items():
                for value in values:
                    if code == value:
                        print(f"код существует группа = {group}")
                        return group
