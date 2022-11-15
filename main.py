my_student = {
  "Name" : "Rolf Smith",
  "Grades" : [70,88,90,99]
}

def average_grades(student):
  return sum(student["Grades"])/ len(student["Grades"])


print(average_grades(my_student))



class Student :
  def __init__(self, new_name, new_grades):
    self.name = new_name
    self.grades = new_grades

  def average (self):
    return sum(self.grades) / len(self.grades)


student_one = Student("Rolf Smith", [70, 88, 90, 99])
student_two = Student("Gibson Maina", [50, 60, 99, 100])

print(student_one.name)
print(student_two.name)
print(student_one.average())


class Movie :
  def __init__(self, movie_name, movie_director) :
    self.name = movie_name
    self.director = movie_director

movie_one = Movie("The Matrix", "Wachowski")

print(movie_one.name)


class Garage :
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def __getitem__(self, i):
    return self.cars[i]

  def __repr__(self):
    return f'<Garage {self.cars}>'

  def __str__(self):
    return f'Garage with {len(self)} cars.'



ford = Garage()
ford.cars.append("Fiesta")
ford.cars.append("Focus")

for car in ford:
  print(car)

print(ford)



class Club :
  def __init__(self, name):
    self.name = name
    self.players = []


  def __len__(self):
    return len(self.players)

  def __getitem__(self, i):
    return self.players[i]


  def __repr__(self):
    return f"Club {self.name}: {self.players}"

  def __str__(self):
    return f"Club {self.name} with {len(self)} players."



some_club = Club('Arsenal')
    


class SchoolStudent:
  def __init__(self, name, school):
    self.name = name
    self.school = school
    self.marks =[]
    
    
  @property
  def average (self):
    return sum(self.marks) / len(self.marks)



class WorkingStudent (SchoolStudent):
  def __init__(self, name, school, salary):
    super().__init__(name, school)
    self.salary = salary


  @property
  def weekly_salary(self):
    return self.salary * 37.5


rolf = WorkingStudent ("Rolf", "Mit", 15.50)
print(rolf.salary)
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.average)
print(rolf.weekly_salary)


class FixedFloat :
  def __init__(self, amount):
    self.amount = amount


  def __repr__(self):
    return f'<FixedFloat {self.amount:.2f}>'

  @staticmethod
  def from_sum(value1, value2):
    return FixedFloat(value1 + value2)


  @classmethod
  def to_sum(cls, value1, value2) :
    return cls(value1 + value2)
  


number = FixedFloat(18.5746)
new_number = FixedFloat.from_sum(19.575, 0.789)
print(new_number)
print(number)


class Euro(FixedFloat) :
  def __init__(self, amount):
    super().__init__(amount)
    self.symbol = "€"
  
  
  def __repr__(self):
    return f'<Euro {self.symbol} {self.amount :.2f}>'



money = Euro(18.786)
print(money)

money_2 = Euro.to_sum(16.537, 15.349)
print(money_2)

money_3= Euro.from_sum(16.537, 15.349)
print(money_3)



