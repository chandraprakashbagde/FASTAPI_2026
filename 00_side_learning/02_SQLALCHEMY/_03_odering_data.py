import random
from model import User
from db import session

## Data inserting script
# names = ["Andrew pip", "Iron Man", "John Doe", "Jane Doe"]
# ages = [20,21,22,23,24,25,26,27,30, 35, 60]

# for r in range(20):
#     user = User(name=random.choice(names), age=random.choice(ages))

#     session.add(user)

# session.commit()
users = session.query(User).order_by(User.age.desc()).all()

for user in users:
    print(f"User age: {user.age}, User name: {user.name}")