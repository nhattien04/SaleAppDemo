from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from saleapp import db
from datetime import datetime
from enum import Enum as UserEnum
from flask_login import UserMixin

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class UserRole(UserEnum):
    ADMIN = 1
    USER = 2

class User(BaseModel, UserMixin):
    __tablename__ = 'user'
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(200))
    email = Column(String(50))
    active = Column(Boolean, default=True)
    joined_date = Column(DateTime, default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    products = relationship('Receipt', backref='user', lazy=True)

    def __str__(self):
        return self.name

class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=False)

    def __str__(self):
        return self.name

class Product(BaseModel):
    __tablename__ = 'product'

    name = Column(String(50), nullable=True)
    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    receipt_details = relationship('ReceiptDetail', backref='product', lazy=True)

    def __str__(self):
        return self.name

class Receipt(BaseModel):
    created_date = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    details = relationship('ReceiptDetail', backref='receipt', lazy=True)

class ReceiptDetail(db.Model):
    receipt_id = Column(Integer, ForeignKey('receipt.id'), nullable=False, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False, primary_key=True)
    quantity = Column(Integer, default=0)
    unit_price = Column(Float, default=0)

if __name__ == '__main__':
    db.create_all()
    """
    c1 = Category(name='Điện thoại')
    db.session.add(c1)

    c2 = Category(name='Máy tính bảng')
    db.session.add(c2)

    c3 = Category(name='Đồng hồ thông minh')
    db.session.add(c3)

    db.session.commit()
    """

"""
    products = [{
            "id": 1,
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image": "images/p1.jpg",
            "category_id": 1
            }, {
            "id": 2,
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "images/p2.jpg",
            "category_id": 2
            }, {
            "id": 3,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAM: 6GB",
            "price": 24000000,
            "image": "images/p3.jpg",
            "category_id": 1
            }]

    for p in products:
        pro = Product(name=p['name'], price=p['price'], image=p['image'],
                      description=p['description'], category_id=p['category_id'])
        db.session.add(pro)

    db.session.commit()
"""












