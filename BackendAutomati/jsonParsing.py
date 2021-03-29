import json


courses = '{"name":"lavanya", "languages":["java", "python"]}'

#Loads method parse json string and it returns dictionary

dict_courses = json.loads(courses)
print(type(dict_courses))

print(dict_courses['name'])

#list_languages = dict_courses['languages']
#print(type(list_languages))
#print(list_languages[0])
#print(list_languages[1])

print(dict_courses['languages'][0])

#json file externally with the system
#********Pares content present in Json Fil*********

with open('C:\\Users\\Lavanya Mantha\\Desktop\\course.json') as f:
    data = json.load(f)
   # print(type(data))
    print(data['courses'][1]['title'])
    print(type(data['dashboard']))
    print(data['dashboard']['website'])

#price of course 'RPA

    print(data['courses'])
    for course in data['courses']:
        if course['title'] == 'RPA':
            print(course['price'])
            assert course['price'] == 45


#******how to compare two json files

with open('C:\\Users\\Lavanya Mantha\\Desktop\\course2.json') as fi:
    data2 = json.load(fi)
    print(data == data2)

    assert data == data2