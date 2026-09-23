from db import engine
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import (
        ForeignKey, 
        String, 
        Integer, 
        Boolean, 
        Enum as SQLEnum, 
        Numeric
    )
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from schemas import OrderStatus, PaymentStatus
from decimal import Decimal


class Base(AsyncAttrs, DeclarativeBase):
    pass



# User Table
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False) 
    name: Mapped[str] = mapped_column(String(100), nullable=False) 
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)  
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False) 

    ## One to One: users to address
    address: Mapped["Address"] = relationship("Address", back_populates="user", cascade="all, delete", uselist=False)

    ## One to Many: users to order
    orders: Mapped[list["Order"]] = relationship("Order", back_populates="user", cascade="all, delete")

    ## One to Many: User to Review
    reviews:Mapped[list["Review"]] = relationship("Review", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email}, is_active={self.is_active})>"

# Address Table
class Address(Base):
    __tablename__ = "address"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False) 
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True) 
    city: Mapped[str] = mapped_column(String(100), nullable=False) 
    country: Mapped[str] = mapped_column(String(100), nullable=False)

    ## Later I am going to add is_default
    ## One to One: Address to User
    user: Mapped["User"] = relationship("User", back_populates="address", uselist=False)

    def __repr__(self):
        return f"<Address(id={self.id}, user_id={self.user_id}, city={self.city}, country={self.country})>"

## Product Table
class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False) 
    category_id:Mapped[int] = mapped_column(Integer, ForeignKey("category.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True) 
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    stock:  Mapped[int] = mapped_column(Integer, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False) 

    ## Many To One: Product to Category
    category:Mapped["Category"] = relationship("Category", back_populates="products")

    ## One to Many: Product to Order Items
    order_items: Mapped[list["OrderItem"]] = relationship("OrderItem", back_populates="product")

    ## One to Many: Product to Review
    reviews: Mapped[list["Review"]] = relationship("Review", back_populates="product")



    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price}, stock={self.stock}, is_active={self.is_active})>"

## Category Table
class Category(Base):
    __tablename__ = "category"

    id:Mapped[int] = mapped_column(Integer,primary_key=True, nullable=False)
    name:Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    ## One To Many: Category to Product
    products: Mapped[list["Product"]] = relationship("Product", back_populates="category", cascade="all, delete")

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"

## Order Table
class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False) 
    status: Mapped[OrderStatus] =  mapped_column(SQLEnum(OrderStatus), nullable=False, default=OrderStatus.PENDING)
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    ## Many to One: Orders to User
    user: Mapped["User"] = relationship("User", back_populates="orders")

    ## One to Many: Order to Order Item
    order_items: Mapped[list["OrderItem"]] = relationship("OrderItem", back_populates="order", cascade="all, delete")

    ## One to One: Order To Payment
    payment: Mapped["Payment"] = relationship("Payment", back_populates="order", uselist=False)

    def __repr__(self):
        return f"<Order(id={self.id}, user_id={self.user_id}, status={self.status}, total_amount={self.total_amount})>" 

## OrderItem Table
class OrderItem(Base):
    __tablename__ = "orderitems"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False) 
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("order.id", ondelete="CASCADE"), nullable=False) 
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)  
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)  
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False) 

    ## Many to One: Order Items to Order
    order: Mapped["Order"] = relationship("Order", back_populates="order_items")

    ## Many to One: OrderItem to Product
    product: Mapped["Product"] = relationship("Product", back_populates="order_items")

    def __repr__(self):
        return f"<OrderItem(id={self.id}, order_id={self.order_id}, product_id={self.product_id}, quantity={self.quantity}, price={self.price})>";

## Payment Table
class Payment(Base):
    __tablename__ = "payment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)  
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("order.id", ondelete="CASCADE"), nullable=False,unique=True) 
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)  
    status: Mapped[PaymentStatus] = mapped_column(SQLEnum(PaymentStatus), nullable=False, default=PaymentStatus.PENDING) 

    ## One to One: Payment to Order
    order: Mapped["Order"] = relationship("Order", back_populates="payment", uselist=False)

    def __repr__(self):
        return f"<Payment(id={self.id}, order_id={self.order_id}, amount={self.amount}, status={self.status})"

## Review Table
class Review(Base):
    __tablename__ = "review"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)  
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False) 
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)  
    rating: Mapped[int] = mapped_column(Integer, nullable=False)  
    comment: Mapped[str] = mapped_column(String(100), nullable=False)  


    ## Many to One: Review to User
    user: Mapped["User"] = relationship("User", back_populates="reviews")


    ## Many to One: Review to Product
    product: Mapped["Product"] = relationship("Product", back_populates="reviews")

    def __repr__(self):
        return f"<Review(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, rating={self.rating}, comment={self.comment})>"


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)