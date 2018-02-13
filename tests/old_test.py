from context import nuqui

#nuqui.remove_user(1)
#nuqui.create_user(1, "Peter")
#nuqui.add_meal(1, "wasser,Apfel,salz", 100)
print(nuqui.get_predefined_question_dict_with_random_answers(1))


fruits= {
     "apple": {
         "amount": 2,
         "calories": 50
     },
     "tomato": {
         "amount": 1,
         "calories": 10
     }
  }

#nuqui.add_meal(1, fruits)

#print(nuqui.evaluate("a shiitake", 156375))
