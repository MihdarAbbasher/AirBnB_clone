#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_m_j = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_m_j.keys():
    print("\t{}: ({}) - {}".format(key, type(my_m_j[key]), my_m_j[key]))
