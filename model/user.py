from datetime import datetime
import json


class User:

    def __init__(self, name, surname, birth_date, hobbies):
        self.name: str = name
        self.surname: str = surname
        self.birth_date: datetime = birth_date
        self.create_date: datetime = datetime.now()
        self.hobbies: [] = hobbies

    def to_json(self):
        return json.dumps(self.__dict__, default=str,
                          sort_keys=True, indent=4)
