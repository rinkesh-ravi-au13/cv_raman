#question:-Model a real life School in python code which can contain
#  students batches subjects.


class School:
  def __init__(self, No_of_students, batch, subjects):
    self.name = self
    self.No_of_students = No_of_students
    self.batch = batch
    self.subject = subjects

s1= School ("st. joseph's school", 30, "A1", "Science")

print(s1.name)
print(s1.No_of_students)
print (s1.batch)
print(s1.subjects)