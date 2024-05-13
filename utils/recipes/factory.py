from random import randint
from faker import Faker


class Factory:

    def __init__(self):
        self.fake = Faker('pt-BR')

    def rand_ratio(self) -> int:
        return randint(840, 900)
        
    def make_recipe(self):
        return {
            'title': self.fake.sentence(nb_words=6),
            'description': self.fake.sentence(nb_words=12),
            'preparation_time': self.fake.random_number(digits=2, fix_len=True),
            'preparation_time_unit': 'Minutos',
            'servings': self.fake.random_number(digits=2, fix_len=True),
            'servings_unit': 'Porção',
            'preparation_steps': self.fake.text(3000),
            'created_at': self.fake.date_time(),
            'author': {
                'first_name': self.fake.first_name(),
                'last_name': self.fake.last_name(),
            },
            'category': {
                'name': self.fake.word()
            },
            'cover': {
                'url': f'https://loremflickr.com/{self.rand_ratio()}/{self.rand_ratio()}/food,cook',
            }
        }
    

if __name__ == "__main__":
    from pprint import pprint

    fac = Factory()
    a = fac.make_recipe()
    pprint(a)
