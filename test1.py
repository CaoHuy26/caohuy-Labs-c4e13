# # p  = ['Tuấn Anh', 22, 3, "Mộc Châu", 2]
# # print (p)
#
# # person = {}
# # print (person)
#
# # person = {
# #     'name': 'Tuấn Anh'
# #
# # }
# #
# # print (person)
#
# person = {
#     'name': 'Tuấn Anh',
#     'age': 22,
#     'home': 'Mộc Châu',
#     'exes': 3
# }
# # print (person['home'])
#
# person['home'] = "Hà Nội"
# print (person)
#
# person ['project_count'] = 2
# print (person)


teen_dict = {
    'gato': 'Ý nói sự ganh tỵ, khó chịu với người nào đó vì hơn mình',
    "ah": 'À',
    "r": 'Rồi',
    "ik": 'Đi',
    "hc": 'Học',
}

while True:
    print (*teen_dict)
    code = input ("Your code? ")

    if code in teen_dict:
        print (teen_dict[code])
    else:
        print ("Not found")
        choice = input ("Do you want to contribute? (Y/N)").upper()
        if choice == 'Y':
            translation = input ("Your translation? ")
            teen_dict[code] = translation
            print ("Updated")
        else:
            pass
