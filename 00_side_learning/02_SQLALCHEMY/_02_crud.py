from db import session
from model import User

### Creating a record
## Add Single Record
# user = User(name="Chandraprakash", age="25")
# session.add(user)

## Add multiple Records
# session.add_all([
#     User(name="Akash", age="25"),
#     User(name="Pritish", age="25"),
#     User(name="Bhumesh", age="25"),
# ])
# session.commit()

### Fetching a record
# users = session.query(User).all()

# user = users[0]
# print(user.id)
# print(user.name)
# print(user.age)

# for user in users:
#     print(f"User id: {user.id}, User Name: {user.name}, User Age: {user.age}")


### Filter By
# users = session.query(User).filter_by(id=1).all()
# user = session.query(User).filter_by(id=1).one_or_none

# if user is None:
#     print("User not found with provided id!!")
# else:
#     print(user.name)

### Update user information
# user = session.query(User).filter_by(id=1).one_or_none()
# if user is not None:
#     user.name = "Prince"

### Delete 
user = session.query(User).filter_by(id=1).one_or_none()
if user is not None:
    session.delete(user)

session.commit()