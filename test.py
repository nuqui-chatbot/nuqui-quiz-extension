from nuqui_quiz.nuqui import create_user, remove_user, get_predefined_question, add_meal, evaluate

remove_user(1)
create_user(1, "Peter")
#print(get_predefined_question(1))


# fruits= {
#     "apple": {
#         "amount": 2,
#         "calories": 50
#     },
#     "tomato": {
#         "amount": 1,
#         "calories": 10
#     }
#  }

#add_meal(1, fruits)

print(evaluate("a shiitake", 156375))