from db import session
from model import User

### Querying all data
## query all users
users_all = session.query(User).all()

### Query data using filter method of query object
## query all users with age is greater than 25
# users_filtered = session.query(User).filter(User.age >= 25).all()

## query all users with age is greater than 25 and name is eqaul to Iron Man
# users_filtered = session.query(User).filter(User.age >= 25, User.name=="Iron Man").all()

### Query data using filter_by method of query object

users_filtered = session.query(User).filter_by(age=25, name="Iron Man").all()

# for user in users_filtered:


print(f"All Users: {len(users_all)}")
print(f"Filtered Users: {len(users_filtered)}")