from db import engine, session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey, String, and_, or_, not_

class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(nullable=False)
    department: Mapped[str] = mapped_column(String(50))
    salary: Mapped[int] = mapped_column(nullable=False)
    experience: Mapped[int] = mapped_column(nullable=False)
    city: Mapped[str] = mapped_column(String(50))
    is_active: Mapped[bool] = mapped_column(default=True)

# Base.metadata.create_all(bind=engine)

# users = [
#     Employee(name="Rahul", age="25", department="IT", salary="45000", experience="2", city="Nagpur", is_active=True),
#     Employee(name="Priya", age="29", department="HR", salary="55000", experience="5", city="Pune", is_active=True),
#     Employee(name="Amit", age="32", department="IT", salary="75000", experience="8", city="Mumbai", is_active=True),
#     Employee(name="Sneha", age="24", department="Sales", salary="40000", experience="1", city="Nagpur", is_active=True),
#     Employee(name="Rohit", age="35", department="IT", salary="90000", experience="10", city="Pune", is_active=False),
#     Employee(name="Neha", age="28", department="HR", salary="60000", experience="4", city="Mumbai", is_active=True),
#     Employee(name="Karan", age="31", department="Sales", salary="65000", experience="7", city="Nagpur", is_active=True),
#     Employee(name="Pooja", age="26", department="IT", salary="50000", experience="3", city="Pune", is_active=True),
#     Employee(name="Vivek", age="38", department="Management", salary="120000", experience="14", city="Mumbai", is_active=True),
#     Employee(name="Anjali", age="30", department="HR", salary="70000", experience="6", city="Nagpur", is_active=False),
# ]

# session.add_all(users)
# session.commit()


### Part 1 — Basic WHERE
## Q1 - Get all employees whose age is greater than 30.
# emps = session.query(Employee).where(Employee.age > 30).all()

## 02 - Get all employees whose salary is greater than or equal to 60000.
# emps = session.query(Employee).where(Employee.salary >= 60000).all()

## 03 - Get all employees who have less than 5 years of experience.
# emps = session.query(Employee).where(Employee.experience < 5).all()

## 04 - Get all employees from Nagpur.
# emps = session.query(Employee).where(Employee.city == "Nagpur").all()

## 05 - Get all employees who are not active.
# emps = session.query(Employee).where(Employee.is_active == False).all()


### Part 2 — and_() 
## 06 - Find employees who work in IT AND have salary greater than 60000
# emps = session.query(Employee).where(Employee.department=="IT", Employee.salary > 60000).all()
# emps = session.query(Employee).where(and_(Employee.department=="IT", Employee.salary > 60000)).all()
# emps = session.query(Employee).where((Employee.department=="IT") & (Employee.salary > 60000)).all()

## 07 - Find employees who are older than 25 AND have more than 3 years of experience.
# emps = session.query(Employee).where(and_(Employee.age > 25, Employee.experience > 3)).all()

## 08 - Find employees who live in Nagpur AND are active
# emps = session.query(Employee).where(and_(Employee.city == "Nagpur", Employee.is_active==True))

## 09 - Find employees who work in HR AND have salary greater than 55000 AND are active.
# emps = session.query(Employee).where(and_(
#     Employee.department == "HR", 
#     Employee.salary > 55000, 
#     Employee.is_active == True
# )).all()

## 10 - Find employees who are between 25 and 35 years old AND have salary greater than 50000
# emps = session.query(Employee).where(and_(
#     Employee.age >= 25,
#     Employee.age <= 35,
#     Employee.salary > 50000
# )).order_by(Employee.age.asc()).all()


### Part 3 — or_()
## 11 - Find employees who work in either IT OR HR
# emps = session.query(Employee).where(or_(Employee.department=="IT", Employee.department=="HR")).order_by(Employee.department).all()

## 12 - Find employees who live in Napgur Or Pune
# emps = session.query(Employee).where(or_(Employee.city=="Nagpur",Employee.city=="Pune")).order_by(Employee.city).all()

## 13 - Find employees whose salary is: greater than 90000 OR less than 45000
# emps = session.query(Employee).where(or_(Employee.salary > 90000, Employee.salary < 45000)).all()

## 14 - Find employees who are: older than 35 OR have more than 10 years of experience.
# emps = session.query(Employee).where(or_(Employee.age > 35, Employee.experience > 10)).all()


### Part 4 not_
## Q15 - Find employees who are not from Nagpur.
# emps = session.query(Employee).where(not_(Employee.city == "Nagpur")).all()

## Q16 - Find employees who are not working in IT.
# emps = session.query(Employee).where(not_(Employee.department == "IT")).all()

## Q17 - Find employees whose salary is not greater than 60000.
# emps = session.query(Employee).where(not_(Employee.salary >= 60000)).all()

## Q18 - Find employees who are not inactive.
emps = session.query(Employee).where(not_(Employee.is_active == True)).all()


### Part 5 Mixed Conditions
## Q19 - Find employees who work in IT AND are active AND have salary greater than 50000.
# emps = session.query(Employee).where(and_(Employee.department=="IT", Employee.is_active==True, Employee.salary > 50000))

##Q20 - Find employees who: work in either IT or HR AND have salary greater than 55000.
# emps = session.query(Employee).where(or_(Employee.department=="IT", Employee.department=="HR"), Employee.salary > 55000)

## Q21 - Find employees who: live in Nagpur OR Pune AND are active. Be careful with your parentheses here.
# emps = session.query(Employee).where(or_(Employee.city=="Nagpur", Employee.city=="Pune"), Employee.is_active == True)

## Q22 - Find employees who: are older than 30 AND work in IT OR HR. Think carefully about how the conditions should be grouped.
# emps = session.query(Employee).where(Employee.age > 30, or_(Employee.department == "HR" , Employee.department=="IT")).all()

## Q23 - Find employees who: are NOT from Nagpur AND have salary greater than 60000.
# emps = session.query(Employee).where(and_(Employee.city != "Nagpur", Employee.salary > 60000)).all()

## Q24 — Challenge 🔥 Find employees who satisfy: (IT OR HR) AND salary >= 60000 AND active.
# emps = session.query(Employee).where(or_(Employee.department=="IT", Employee.department=="HR"), Employee.salary >=60000, Employee.is_active==True)

## Q25 — Final Challenge 🔥🔥 Find employees who satisfy: (Nagpur OR Pune) AND (salary > 50000) AND NOT (department == HR) AND active.
# emps = session.query(Employee).where(or_(Employee.city=="Nagpur", Employee.city=="Pune"), Employee.salary > 50000, not_(Employee.department=="HR"), Employee.is_active==True)