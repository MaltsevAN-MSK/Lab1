def print_students(students, sred):
    print ()
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(35), u"Оценки".ljust(20), "\n")
    for student in students:
        if ((student["marks"][0] + student["marks"][1] + student["marks"][2])/3 > sred):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(35), str(student["marks"]).ljust(20))

groupmates = [
    {
        "name": "Бонифаций",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [2, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [2, 4, 5]
    },
    {
        "name": "Александр",
        "surname": "Мальцев",
        "exams": ["Вышмат", "ИС", "Физкультура"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Клавдия",
        "surname": "Смирнова",
        "exams": ["Философия", "Вышмат", "Физика"],
        "marks": [4, 5, 4]
    }
]
x = int(input("\nВведите средний балл: "))
print_students(groupmates, x)
