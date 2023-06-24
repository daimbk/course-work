# Daim Bin Khalid
# 251686775
# Lab 1

class Assignment:
    def __init__(self, name, month, day, hour, minute):
        self.total_weight = None
        self.total_points = None
        self.score = None
        self.name = name
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        
    def set_score(self, score):
        self.score = score

    def set_total_points(self, total_points):
        self.total_points = total_points

    def set_total_weight(self, total_weight):
        self.total_weight = total_weight

    def get_name(self):
        return self.name

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def get_score(self):
        return self.score

    def get_total_points(self):
        return self.total_points

    def get_total_weight(self):
        return self.total_weight

    def to_string(self):
        return f'Name: {self.name}\nMonth: {self.month}\nDay: {self.day}\nMinute: {self.minute}\nScore: {self.score}\nTotal Points: {self.total_points}\nTotal Weight: {self.total_weight}%'


class Lab(Assignment):
    def __init__(self, name, month, day, hour, minute, specification):
        super().__init__(name, month, day, hour, minute)
        self.specification = specification

    def to_string(self):
        return super().to_string() + f'\nSpecification: {self.specification}'


class Project(Assignment):
    def __init__(self, name, month, day, hour, minute, specification, data_file):
        super().__init__(name, month, day, hour, minute)
        self.specification = specification
        self.data_file = data_file

    def to_string(self):
        return super().to_string() + f'Specification: {self.specification}\nData File: {self.data_file}'


class AssignmentList:
    def __init__(self):
        self.assignment_list = []

    def add_item(self, assignment):
        self.assignment_list.append(assignment)

    def compute_course_grade(self):
        if len(self.assignment_list) == 0:
            return 0
        else:
            final_score = 0
            for i in self.assignment_list:
                final_score += ((i.get_total_weight() * (i.get_score() / i.get_total_points())) / i.get_total_weight())

            return final_score


def main():
    lab_1 = Lab('DSA', 10, 4, 3, 29, 'Lab 1')
    lab_1.set_score(58)
    lab_1.set_total_points(60)
    lab_1.set_total_weight(30)

    project_1 = Project('DLD', 5, 16, 7, 35, 'Robot Making', 'robo.exe')
    project_1.set_score(70)
    project_1.set_total_points(100)
    project_1.set_total_weight(70)

    final_obj = AssignmentList()
    final_obj.add_item(lab_1)
    final_obj.add_item(project_1)

    print(lab_1.to_string())
    print()
    print(project_1.to_string())
    print()
    print(final_obj.compute_course_grade())


main()
