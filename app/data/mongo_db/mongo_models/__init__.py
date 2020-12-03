from app.data.mongo_db import Document, db


class Associate(Document):
    collection = db.associates


class Car(Document):
    collection = db.cars


class Compatibility(Document):
    collection = db.compatibilities


class ContactPerson(Document):
    collection = db.contact_persons


class Customer(Document):
    collection = db.customers


class CustomerCar(Document):
    collection = db.customer_cars


class Employee(Document):
    collection = db.employees


class InternalOrder(Document):
    collection = db.internal_orders


class OrderProduct(Document):
    collection = db.order_has_products


class Order(Document):
    collection = db.orders


class Product(Document):
    collection = db.products


class ProductAssociate(Document):
    collection = db.products_has_associates


class ProductInternalOrder(Document):
    collection = db.products_has_internal_orders


class Shop(Document):
    collection = db.shops


class Storage(Document):
    collection = db.storages


class ShopStorage(Document):
    collection = db.shops_storages


class CarModel(Document):
    collection = db.car_models
