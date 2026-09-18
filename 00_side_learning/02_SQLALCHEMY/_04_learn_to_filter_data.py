from model import User 
from db import session;
from sqlalchemy import or_, not_, and_

### Query with Single condition
# users = session.query(User).where(User.age <= 22).all()

### Query with or conditions

## or_ function
#users = session.query(User).where(or_(User.age == 22, User.name=="Iron Man")).all()

## "or" condition with bitwise operator
# users = session.query(User).where((User.age == 22) | (User.name=="Iron Man")).all()

## and condition by default and conditions works in the where condition
# and_ function
# We can achive the same output by "&" operator
# users = session.query(User).where(User.age <= 22, User.name != "Iron Man")

## not_ function 
# users = session.query(User).where(not_(User.name == "Iron Man")).all()

## Combine All
users = session.query(User).where(
    or_(
        not_(User.name == "Iron Man"),
        and_(
            (User.age > 25),
            (User.age < 60),
        )
    )
)

for user in users:
    print(f"User Name: {user.name}, User Age: {user.age}")