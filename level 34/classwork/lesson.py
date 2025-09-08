'''
საკლასო დავალება:
შექმენით ფუნქცია რომელიც მიიღებს ორ პარამეტრს - main_list, indexes_list.
თქვენი დავალებაა, რომ indexes_list სიაში რა ინდექსებიც იქნება მოცემული,
მთავარ სიაში, მაგ ინდექსებზე წაშალოთ ელემენტები
'''
def remove_elements_by_indexes(main_list, indexes_list):
    indexes_list.sort(reverse=True)    
    for index in indexes_list:
        if 0 <= index < len(main_list):
            main_list.pop(index)
    
    return main_list





'''
შექმენით ფუნქცია სახელად remove_one_element, რომელსაც გადაეცემა სია და ინდექსი.
სიიდან მაგ ინდექსზე მყოფი ელემენტი ამოშალეთ და დაბეჭდეთ სია.
'''
def remove_one_element(main_list, index):
    if 0 <= index < len(main_list):
        main_list.pop(index)
    else:
        print("hello world")
    
    print(main_list)





'''

'''
