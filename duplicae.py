student={
    "student1":{
        "name":"Aahaan",
        "grade":6,
        "subject":["math","English"]
        },
    "student2":{
        "name":"Rahul",
        "grade":7,
        "subject":["SST","Hindi"]
        },
    "student3":{
        "name":"Aahaan",
        "grade":6,
        "subject":["math","English"]
        }
}

name={}

for key,value in student.items():
    if value not in name.values():
        name[key]=value

print(name)