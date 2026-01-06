container_data={}
def check_id():
    id=input("ادخل الرقم الجامعي: ")
    while True:
        if id.isdigit():
            if int(id) > 0:
                if int(id) in container_data.keys():
                    print("الرقم المدخل مستخدم, يرجى استخدام رقم أخر")
                else:
                    return int(id)
        id = input("يجب أن يكون الرقم الجامعي عدد صحيح و موجب وغير مستخدم سابقاً,ادخل الرقم الجامعي بشكل صحيح: ")

def check_name():
    name = input("ادخل اسم الطالب الثلاثي: ")
    while True:
        if all(x.isalpha() or x.isspace() for x in name):
            if len(name) >=3:
                return name
        name = input("لا يجب أن يحوي اسم الطالب سوى أحرف وفراغات وعلى الأقل 3 محارف , ادخل اسم الطالب بشكل صحيح: ")

def check_average():
    average=input("ادخل المعدل التراكمي: ")
    while True:
        if average.isdigit():
            if int(average) >0 and int(average) <100:
                return int(average)
        average = input("يجب أن يكون المعدل بين 0و 100, ادخل المعدل التراكمي بشكل صحيح: ")

def add_Student():
    id=check_id()
    name=check_name()
    average=check_average()
    container_data[id] = [name,average]

def adding_process():
    add_Student()
    desire=input("هل تريد أضافة طالب أخر؟ Y/N")
    while True:
        while desire not in ["Y","y","N","n"]:
            desire = input("يرجى اختيار احدى الاجابتين؟ Y/N")
        if "Y" in desire or "y" in desire:
            add_Student()
            desire = input("هل تريد أضافة طالب أخر؟ Y/N")
        if "N" in desire or "n" in desire:
            return




def get_name(dict,id):
    if len(dict) == 0: return "القاموس المرسل فارغ"
    try:
        return dict[id][0]
    except:
        return("الرقم الجامعي غير موجود")

def get_high_average(dict):
    if len(dict)==0: return "القاموس المرسل فارغ"
    key_of_high_average,high_average=[],0
    for key in dict.keys():
        if dict[key][1]>high_average:
            high_average=dict[key][1]
            key_of_high_average.clear()
            key_of_high_average.append(key)
        elif dict[key][1]==high_average:
            key_of_high_average.append(key)
    return  [dict[k][0] for k in key_of_high_average]

def list_name_descending(dict):
    if len(dict) == 0: return "القاموس المرسل فارغ"
    sorted_list=sorted(dict.items(), key=lambda item: item[1][1],reverse=True)
    result=[]
    for item in sorted_list:
        result.append(item[1][0])
    return result

def high_three_average(dict):
    if len(dict) == 0: return "القاموس المرسل فارغ"
    sorted_list = sorted(dict.items(), key=lambda item: item[1][1])[-3:]
    result = []
    for item in sorted_list:
        result.append(item[1][0])
    return result

def write_to_file(dict,file_name="new_file"):
    if len(dict) == 0: return "القاموس المرسل فارغ"
    file=open(file_name,"w")
    file.write("student id\tStudent Name\tcumulative average\n")
    for key in container_data.keys():
        file.write(f"{key}\t\t\t{container_data[key][0]}\t\t\t{container_data[key][1]}\n")
    print("تم حفظ المعلومات في الملف بنجاح")




container_data={1:["ammar",78],2:["ahmed",83],3:["ali",77],
                4:["rami",90],5:["hasan",84],6:["Hani",95.1],
                7:["wassim",80],8:["zaid",71],9:["Amir",60],
                10:["kamal",95],11:["hassan",81],12:["zoher",95.1]}
#print(get_name(container_data,11))
#print(get_name(container_data,15))
#adding_process()
#print(get_high_average(container_data))
print(list_name_descending(container_data))
print(high_three_average(container_data))
write_to_file(container_data)
