import json
import keyword


class JsonObject:
    def __init__(self, mapping: dict):
        for atr in mapping:
            atr_name = atr
            if keyword.iskeyword(atr):
                atr_name = atr + '_'
            if isinstance(mapping[atr], dict):
                self.__dict__[atr_name] = JsonObject(mapping[atr])
            else:
                self.__dict__[atr_name] = mapping[atr]

    def __setattr__(self, key, value):
        self.__dict__[key] = value


class ColorizeMixin:
    repr_color_code = 0

    def color_string(self, out_str: str):
        return f'\033[{self.repr_color_code}m{out_str}\033[0m'



class Advert(ColorizeMixin, JsonObject):
    def __init__(self, mapping: dict):
        super().__init__(mapping)
        if not hasattr(self, 'title'):
            raise ValueError('No title!')
        if not hasattr(self, 'price'):
            self.price = 0
        elif self.price < 0:
            raise ValueError('must be >= 0')

    def __setattr__(self, key, value):
        if key == 'price' and value < 0:
            raise ValueError('must be >= 0')
        else:
            super().__setattr__(key, value)

    def __repr__(self):
        return super().color_string(f'{self.title} | {self.price} ₽')


def py3():
    lesson_str_python = """{
        "title": "python", 
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""
    lesson_str_iphone = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""
    lesson_str_corgi = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""
    lesson = json.loads(lesson_str_python)
    python_ad = Advert(lesson)
    print(python_ad.location.address)
    # python_ad.price = -10
    print(python_ad.location.metro_stations[0])
    # a.price = -10
    lesson = json.loads(lesson_str_iphone)
    iphone_ad = Advert(lesson)
    print(iphone_ad.price)
    print(iphone_ad.location.address)
    lesson = json.loads(lesson_str_corgi)
    corgi_ad = Advert(lesson)
    print(corgi_ad.class_)
    ColorizeMixin.repr_color_code = 33
    print(corgi_ad)
    print(iphone_ad)
    corgi_ad.repr_color_code = 31
    print(corgi_ad)
    print(iphone_ad)


if __name__ == '__main__':
    py3()
