from db import AsyncSessionLocal
from models import *
from sqlalchemy import select, desc

### LEVEL 1 — INSERT OPERATIONS

## E1
async def create_user(name: str, email: str):
    user = User(name=name, email=email)
    print(user)

    async with AsyncSessionLocal() as session:
        session.add(user)
        await session.commit()
        await session.refresh(user)

    print(user)

## E2
async def create_category(name: str):
    cat = Category(name=name)

    async with AsyncSessionLocal() as session:
        session.add(cat)
        await session.commit()
        await session.refresh(cat)

    return cat

## E3
async def create_product(category_id: int, name:str, price:Decimal, stock: int):
    product = Product(
        category_id=category_id,
        name=name,
        price=price,
        stock=stock
    )

    async with AsyncSessionLocal() as session:
        session.add(product)
        await session.commit()
        await session.refresh(product)

    return product
async def create_multiple_products():
    async with AsyncSessionLocal() as session:
        products = [
            Product(category_id=1, name="Wireless Headphones", price="5999.00", stock=35),
            Product(category_id=1, name="Bluetooth Speaker", price="3499.00", stock=40),
            Product(category_id=1, name="Mechanical Keyboard", price="4499.00", stock=25),
            Product(category_id=1, name="Wireless Mouse", price="1299.00", stock=80),
            Product(category_id=1, name="Gaming Mouse", price="2499.00", stock=45),
            Product(category_id=1, name="Gaming Keyboard", price="6999.00", stock=20),
            Product(category_id=1, name="USB-C Hub", price="1999.00", stock=60),
            Product(category_id=1, name="Power Bank", price="2499.00", stock=75),
            Product(category_id=1, name="Fast Charger", price="1799.00", stock=90),

            Product(category_id=1, name="Smartwatch", price="7999.00", stock=30),
            Product(category_id=1, name="Fitness Band", price="2999.00", stock=55),
            Product(category_id=1, name="Webcam", price="3999.00", stock=28),
            Product(category_id=1, name="External SSD", price="6499.00", stock=35),
            Product(category_id=1, name="USB Flash Drive", price="899.00", stock=120),
            Product(category_id=1, name="Wi-Fi Router", price="2999.00", stock=42),
            Product(category_id=1, name="Computer Monitor", price="12999.00", stock=18),
            Product(category_id=1, name="Soundbar", price="8999.00", stock=22),
            Product(category_id=1, name="Tablet", price="18999.00", stock=15),
            Product(category_id=1, name="Smartphone", price="24999.00", stock=25),

            Product(category_id=1, name="iPhone 17 Pro", price="129999.00", stock=12),
            Product(category_id=1, name="Samsung Galaxy S26 Ultra", price="139999.00", stock=10),
            Product(category_id=1, name="Google Pixel 10 Pro", price="99999.00", stock=14),
            Product(category_id=1, name="MacBook Air M4", price="114999.00", stock=8),
            Product(category_id=1, name="MacBook Pro M4 Pro", price="199999.00", stock=5),
            Product(category_id=1, name="Dell XPS 16", price="179999.00", stock=6),
            Product(category_id=1, name="Lenovo ThinkPad X1 Carbon", price="149999.00", stock=7),
            Product(category_id=1, name="ASUS ROG Gaming Laptop", price="189999.00", stock=5),
            Product(category_id=1, name="Sony Bravia 65-inch OLED TV", price="179999.00", stock=6),
            Product(category_id=1, name="Samsung 75-inch Neo QLED TV", price="229999.00", stock=4),

            Product(category_id=1, name="LG 65-inch OLED TV", price="159999.00", stock=7),
            Product(category_id=1, name="Sony WH-1000XM6 Headphones", price="39999.00", stock=18),
            Product(category_id=1, name="Bose QuietComfort Ultra", price="42999.00", stock=15),
            Product(category_id=1, name="Apple Studio Display", price="159999.00", stock=5),
            Product(category_id=1, name="Samsung Odyssey Gaming Monitor", price="89999.00", stock=9),
            Product(category_id=1, name="LG UltraGear OLED Monitor", price="99999.00", stock=8),
            Product(category_id=1, name="Sony Home Theatre System", price="89999.00", stock=10),
            Product(category_id=1, name="Bose Smart Ultra Soundbar", price="79999.00", stock=12),
            Product(category_id=1, name="Apple Vision Pro", price="299999.00", stock=3),
            Product(category_id=1, name="DJI Professional Drone", price="149999.00", stock=6),
        ]

        session.add_all(products)
        await session.commit()

## E4 
## Using ForeignKey
async def create_user_with_address():
    async with AsyncSessionLocal() as session:
        user = User(name="Amit", email="amit@gmail.com")

        session.add(user)

        await session.flush()

        address = Address(
            user_id=user.id,
            city="Gondia",
            country="India"
        )

        session.add(address)

        await session.commit()

## E5
## Create user + address using relationship
async def create_user_with_add_rel():
    async with AsyncSessionLocal() as session:
        user = User(
            name="Lokesh",
            email="lokesh@gmail.com"
        )

        user.addresses = Address(
            city="Jangantola",
            country="India"
        )

        session.add(user)
        await session.commit()

## E6
async def create_order_for_user():
    async with AsyncSessionLocal() as session:
        order = Order(
            user_id=1,
            status=OrderStatus.PENDING,
            total_amount="159998.00"
        )

        session.add(order)
        await session.commit()
        await session.refresh(order)
        print(order)

## E7
async def create_order_with_orde_items():
    async with AsyncSessionLocal() as session:

        order = Order(
            user_id="1",
            status=OrderStatus.PENDING,
            total_amount="209996.00",
        )

        order.order_items = [
            OrderItem(
                product_id="1",
                quantity="2",
                price="89999.00"
            ),
            OrderItem(
                product_id="2",
                quantity="2",
                price="14999.00"
            ),
        ]

        session.add(order)
        await session.commit()

## E8
async def create_payment_for_order():
    async with AsyncSessionLocal() as session:
        payment = Payment(
            order_id="2",
            amount="209996.00",
            status=PaymentStatus.PENDING,
        )

        session.add(payment)
        await session.commit()

## E9 
async def create_review_for_prod():
    async with AsyncSessionLocal() as session:
        review = Review(
            user_id=1,
            product_id=1,
            rating=5,
            comment="Super performace mobile.."
        )

        session.add(review)
        await session.commit()


### LEVEL 2 — SELECT OPERATIONS

## E10
async def get_user_by_id(id: int):
    async with AsyncSessionLocal() as session:
        stmt = select(User).where( User.id == id )
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()

        if user:
            print(f"User with id {id} is:")
            print(user)
        else:
            print("user found with provided ID")

## E11 
async def get_user_by_email(email:int):
    async with AsyncSessionLocal() as session:
        stmt = select(User).where(User.email == email)
        result = await session.execute(stmt)

        user = result.scalar_one_or_none()
        print(user)

## E12, E13
async def get_all_active_users():
    async with AsyncSessionLocal() as session:
        # stmt = select(User).where( User.is_active == True )
        # stmt = select(User).where(User.is_active.is_(True))
        stmt = select(User).where(User.is_active.is_(False))
        result = await session.execute(stmt)

        active_users = result.scalars().all()
        # active_users = result.fetchall()

        print(active_users)

## E14
async def get_product_under(under_num:int = 50000):
    async with AsyncSessionLocal() as session:
        stmt = select(Product.name, Product.price).where( Product.price < Decimal(under_num)).order_by(desc(Product.price))
        result = await session.execute(stmt)

        print(result.all())