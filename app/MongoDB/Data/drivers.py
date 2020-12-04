from app.MySQL.data.db import session
from app.MySQL.data.model_imports import *
import app.MongoDB.Data.mongo_models as mm


def fix_car_models():

    car_models = session.query(CarModel).all()
    product_compatability = session.query(Compatibility).all()
    for car in car_models:
        car_dict = car.__dict__
        del car_dict['_sa_instance_state']
        car_dict['car_brand'] = str(car_dict['car_brand'])
        car_dict['model_name'] = str(car_dict['model_name'])
        car_dict['production_year'] = str(car_dict['production_year'])
        car_dict['colour'] = str(car_dict['colour'])
        car_dict['compatability'] = []
        for pa in product_compatability:
            if car_dict['id'] == pa.ModelId:
                car_dict['compatability'].append(pa.ProductId)
        mongo_car_model = mm.CarModel(car_dict)
        mongo_car_model.save()




def main():
    fix_car_models()


if __name__ == "__main__":
    main()
