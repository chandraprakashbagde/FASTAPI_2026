from models import create_table
from services import *
import asyncio


async def main():
    # Create table
    # await create_table()

    # await create_user(name="navin", email="navin@gmail.com")
    # await create_user_with_address()
    # await create_category("Electronics")
    # await create_product(
    #     category_id=1,
    #     name="AirPods",
    #     price="14999.00",
    #     stock=50
    # )
    # await create_multiple_products()

    # await create_user_with_add_rel()
    # await create_order_for_user()

    # await create_order_with_orde_items()
    # await create_payment_for_order()
    # await create_review_for_prod()
    # await get_user_by_id(4)

    # await get_user_by_email("navin@gmail.com")

    # await get_all_active_users()
    await get_product_under(under_num=1000)



asyncio.run(main())