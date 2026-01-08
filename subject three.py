container_data={}# القاموس الذي سوف يتم تخزين البيانات فيه
container_data={1:["ammar",78],2:["ahmed",83],3:["ali",77],
                4:["rami",90],5:["hasan",84],6:["Hani",95.1],
                7:["wassim",80],8:["zaid",71],9:["Amir",60],
                10:["kamal",95],11:["hassan",81],12:["zoher",95.1]}# عينة عشوائية تم ادخالها لاختبار التوايع والعمل عليها
def check_id():
    id=input("ادخل الرقم الجامعي: ")
    while True:
        if id.isdigit():# التحقق من أن القيمة رقمية
            if int(id) > 0:# التحقق من أن القيمة موجبة
                if int(id) not in container_data.keys():# التحقق من أن القيمة غير مستخدمة سابقاً
                    return int(id)
                else:
                    # في حال عدم تحقق أي من الشروط السابقة يجب على المستخدم ادخال الرقم الجامعي مرة اخرى
                    print("الرقم المدخل مستخدم, يرجى استخدام رقم أخر")
        id = input("يجب أن يكون الرقم الجامعي عدد صحيح و موجب وغير مستخدم سابقاً,ادخل الرقم الجامعي بشكل صحيح: ")

def check_name():
    name = input("ادخل اسم الطالب الثلاثي: ")
    while True:
        if all(x.isalpha() or x.isspace() for x in name):#التحقق من أن اسم الطالب المدخل يحوي فقط أحرف وفراغات فقط
            if len(name) >=3:# التحقق من أن طول الاسم المدخل ليس أقل من 3 محارف
                return name.strip()# ازالة الفراغات من بداية ونهاية الاسم المدخل قبل الادخال
        name = input("لا يجب أن يحوي اسم الطالب سوى أحرف وفراغات وعلى الأقل 3 محارف , ادخل اسم الطالب بشكل صحيح: ")

def check_average():
    average=input("ادخل المعدل التراكمي: ")
    while True:
        if average.isdigit():# التحقق من ان القيمة المدخلة رقمية
            if int(average) >0 and int(average) <=100:# التحقق من ان القيمة المدخلة بين 0 و 100
                return int(average)
        average = input("يجب أن يكون المعدل بين 0و 100, ادخل المعدل التراكمي بشكل صحيح: ")

def add_Student():
    id=check_id() #استدعاء دالة التحقق من الرقم الجامعي
    name=check_name()# استدعاء دالة التحقق من الاسم
    average=check_average()# استدعاء دالة التحقق من المعدل
    container_data[id] = [name,average]# تخزين القيم في القاموس حيث يتم تخزين الرقم كمفتاح وتخزين الاسم والمعدل في قائمة كقيمة لهذا المفتاح

def adding_process():
    add_Student()# استدعاء دالة اضافة طالب
    desire=input("هل تريد أضافة طالب أخر؟ Y/N")# الاستعلام عن رغبة المستخدم باضافة طالب أخر
    while True:
        while desire not in ["Y","y","N","n"]:# لاجبار المستخدم على ادخال احدى القيم Y y N n
            desire = input("يرجى اختيار احدى الاجابتين؟ Y/N")
        if "Y" == desire or "y" == desire: # في حال كان خيار الطالب y يتم استدعاء دالة اضافة طالب
            add_Student()
            desire = input("هل تريد أضافة طالب أخر؟ Y/N")
        if "N" == desire or "n" == desire:# في حال كان ادخال مالستخدم n  يتم الخروج من التابع
            return

def get_name(dict,id):# يقوم هذا التابع باعادة اسم الطالب المرتبط بالرقم الجامعي المرسل
    if len(dict) == 0: return "القاموس المرسل فارغ"# التحقق من أن القاموس غير فارغ
    try:# تم استخدام أسلوب try لأن البحث عن مفتاح غير موجود في القاموس سوف يولد خطأ برمجياً
        return dict[id][0]#اعادة الاسم المرتبط بالرقك الجامعي المرسل
    except:# في حال حدوث خطأ أي أن الرقم الجامعي غير موجود يتم اعلام المستخدم بذلك
        return("الرقم الجامعي غير موجود")

def get_high_average(dict):# اعادة اسماء الطلاب أصحاب المعدل الأعلى أي في حال كان لدينا أكثر من طالب لديهم نفس المعدل
    #وكان معدلهم هو المعدل الأعلى بين الطلاب يتم اعادة اسماء هؤلاء الطلاب على شكل قائمة
    if len(dict)==0: return "القاموس المرسل فارغ"
    key_of_high_average=[]# سوف يتم تخزين أسماء الطلاب ذوي المعدل الأعلى في هذه القائمة
    high_average=0 #سوف يخزن المعدل الأعلى
    for key in dict.keys():#للمرور على قائمة المفاتيح في القاموس
        if dict[key][1]>high_average:# سوف يتم المقارنة بين المعدل المرتبط بالمفتاح والمعدل المخزن في المتغير
            high_average=dict[key][1]# في حال كان المعدل المرتبط بالمفتاح أكبر من المعدل المخزن في المتغير يتم اسناد قيمة المعدل الأعلى في المتغير
            key_of_high_average.clear()#يتم حذف جميع عناصر القائمة لأنها تحوي أرقام طلاب معدلهم أقل من المعدل الأعلى الذي وجد في اخر خطوة تكرارية
            key_of_high_average.append(key)#اضافة الرقم الجامعي للطالب صاحب المعدل الأعلى بشكل مؤقت
        elif dict[key][1]==high_average:# في حال عثر طالب له نفس المعدل الأعلى يتم اضافة رقمه الجامعي الى قائمة الأرقام الجامعية
            key_of_high_average.append(key)
    return  [dict[k][0] for k in key_of_high_average]# يتم اعادة اسماء الطلاب الذين أرقامهم الجامعية موجودة في قائمة المعدل الأعلى

def list_name_descending(dict): #تابع عرض اسماء الطلاب مرتبين بشكل تنازلي وفقاً للمعدل
    if len(dict) == 0: return "القاموس المرسل فارغ"# التحقق من ان القاموس المرسل غير فارغ
    sorted_list=sorted(dict.items(), key=lambda item: item[1][1],reverse=True)#استخراج لائحة تضم عناصر القاموس مرتبين وفق المعدل تنازلياً
    result=[]# هذه القائمة سوف تحوي اسماء الطلاب
    for item in sorted_list:
        result.append(item[1][0])#استخراج اسماء الطلاب من القائمة المرتبة السابقة واضافتها الى القائمة النهائية
    return result#اعادة قائمة اسماء الطلاب

def high_three_average(dict):
    if len(dict) == 0: return "القاموس المرسل فارغ"
    sorted_list = sorted(dict.items(), key=lambda item: item[1][1])#استخراج لائحة تضم عناصر القاموس مرتبين وفق المعدل تصاعدياً
    sorted_list=sorted_list[-3:]#يتم أخذ أخر 3 عناصر من قائمة الأسماء
    result = []
    for item in sorted_list:
        result.append(item[1][0])
    return result

def write_to_file(dict,file_name="new_file"):#تابع كتابة محتويات القاموس في ملف علماً أن تم تعيين اسم افتراضي للملف في حال يم يقم المستخدم بتعيين الاسم
    if len(dict) == 0: return "القاموس المرسل فارغ"# التحقق من أن القاموس غير فارغ
    file=open(file_name,"w")#فتح الملف المحدد بوضع w أي أنه سوف يتم مسح جميع محتويات الملف  قبل بدأ الادخال
    file.write("student id\tStudent Name\tcumulative average\n")# كتابة الترويسات في الملف
    for key in dict.keys():# قراءة محتويات القاموس
        file.write(f"{key}\t\t\t{dict[key][0]}\t\t\t{dict[key][1]}\n")# كتابة محتويات القاموس في الملف حيث سوف يتم كتابة كل عنصر في سطر
    print("تم حفظ المعلومات في الملف بنجاح")


#print(get_name(container_data,11))
#print(get_name(container_data,15))
adding_process()
#print(get_high_average(container_data))
#print(list_name_descending(container_data))
#print(high_three_average(container_data))
#write_to_file(container_data)
