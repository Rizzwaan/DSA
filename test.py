from operator import itemgetter, attrgetter


# student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10),
# ]

# # s = sorted(student_tuples, key=itemgetter(1, 2))
# # print(s)


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


x = Student('john', 'A', 15)
y = Student('jane', 'B', 12)
z = Student('dave', 'B', 10)


s = [x, y, z]

# x = sorted(s, key=attrgetter('grade', 'age'))


x = sorted(s, key=attrgetter('age'))

y = sorted(x, key=attrgetter('grade'), reverse=True)
print(x)
print(y)
