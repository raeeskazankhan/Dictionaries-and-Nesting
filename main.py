# INTRODUCTION TO DICTIONARIES & NESTING
# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected",
#                           "Function": "A piece of code that you can easily call over and over again", }
#
# print(programming_dictionary["Bug"])
# programming_dictionary["Loop"] = "The action of doing something over and over again"
#
# print(programming_dictionary)

# GRADING PROGRAM
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
# }
#
# student_grades = {}
# for student in student_scores:
#     student_grade_description = ""
#     if student_scores[student] < 70:
#         student_grade_description = "FAIL"
#     elif student_scores[student] < 80:
#         student_grade_description = "ACCEPTABLE"
#     elif student_scores[student] < 90:
#         student_grade_description = "EXCEEDS EXCEPTIONS"
#     else:
#         student_grade_description = "OUTSTANDING"
#     student_grades[student] = student_grade_description
#
# print(student_grades)

# NESTING LIST AND DICTIONARIES
#   NESTING DICTIONARY IN A DICTIONARY
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
# }
#
# #   NESTING DICTIONARY IN A LIST
# travel_log_list = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     },
# ]

# EXERCISE: DICTIONARY IN LIST
# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     }
# ]
#
#
# def add_new_country(country, visits, cities):
#     new_country = {
#         "country": country,
#         "visits": visits,
#         "cities": cities
#     }
#     travel_log.append(new_country)
#
#
# add_new_country(country="Russia", visits=2, cities=["Moscow", "Saint Petersburg", "Kazan"])
# print(travel_log)

# THE SECRET AUCTION PROGRAM
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
more_bidders = "YES"
auction_bidders = {}
amount_list = []

while more_bidders != "NO":
    auction_name = str(input("WHAT IS YOUR NAME? ")).upper()
    auction_amount = int(input("WHAT'S YOUR BID? R"))
    auction_bidders[auction_name] = auction_amount
    more_bidders = str(input("ARE THERE ANY OTHER BIDDERS? YES OR NO: ")).upper()
    print("")

amount_list = list(auction_bidders.values())
person_list = list(auction_bidders.keys())
max_amount = max(amount_list)
position = amount_list.index(max_amount)
max_person = person_list[position]

print(f"THE WINNER IS A {max_person} WITH BID OF R{max_amount}")
