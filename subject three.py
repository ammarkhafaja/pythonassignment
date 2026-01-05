container_data,id,name,average={},0,"",0
def check_id():
    id=input("ادخل الرقم الجامعي: ")
    while True:
        if id.isdigit():
            if int(id) > 0:
                return int(id)
        name = input("يجب أن يكون الرقم الجامعي عدد صحيح و موجب ,ادخل الرقم الجامعي بشكل صحيح: ")

def check_name():
    name = input("ادخل اسم الطالب الثلاثي: ")
    while True:
        if all(x.isalpha() or x.isspace() for x in name):
            if len(name) >3:
                return name
        name = input("لا يجب أن يحوي اسم الطالب سوى أحرف وفراغات , ادخل اسم الطالب بشكل صحيح: ")

def check_average():
    average=input("ادخل المعدل التراكمي: ")
    while True:
        if average.isdigit():
            if int(average) >0 and int(average) <100:
                return int(id)
        name = input("يجب أن يكون المعدل بين 0و 100, ادخل المعدل التراكمي بشكل صحيح: ")

def add_Student():
    id=check_id()
    name=check_name()
    average=check_average()
    container_data[id] = [name,average]

def adding_process():
    add_Student()
    while(True):
        desire=input("هل تريد أضافة طالب أخر؟ Y/N")
        while desire not in ["Y","y","N","n"]:
            desire = input("يرجى اختيار احدى الاجابتين؟ Y/N")
            if "Y" in desire or "y" in desire:
                add_Student()
            if "N" in desire or "n" in desire:
                break
def get_name(dict,id):
    try:
        return dict[id][0]
    except:
        print("الرقم الجامعي غير موجود")



