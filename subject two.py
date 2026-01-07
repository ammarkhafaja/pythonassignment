num_list,pair_list,target_number=[],[],0
def check_numeric_value(value,note):
    #تعمل هذه الدالة على التأكد من أن القيمة المدخلة رقمية وموجبة
    if value.isdigit():# التحقق من أن القيمة المدخلة رقمية
        if int(value) >=0:# التحقق من أن القيمة المدخلة موجبة
            return int(value)
    #في حال عدم ادخال قيمة عددية صحيحة وموجبة
    else:
        print("يجب ادخال عدد صحيح موجب")
        value = input(note)
        while True:
            if value.isdigit():
                if int(value) >=0:
                    return int(value)
            print("يجب ادخال عدد صحيح موجب")
            value = input(note)
def construct_pairs():
    for z in range(10):#ادخال الأرقام من قبل المستخدم
        value=input("أدخل الرقم "+str(z+1)+ ": ")
        global pair_list    # تم تحويل هذا المتحول الى global لتكون القيم التي سوف يأخذها داخل مجال حلقة for متاحة للتعامل معها خارج هذا المجال
        num_list.append(check_numeric_value(value,f"أدخل الرقم {z+1}: ")) # التحقق من أن الرقم المدخل رقم صحيح وموجب ثم اضافته الى قائمة الأرقام
    target_number=input("أدخل الرقم الهدف: ") # ادخال العدد الهدف
    target_number=check_numeric_value(target_number,"يرجى ادخال الرقم الهدف, يجب أن يكون عدداً صحيحاً وموجباً")
    # تعمل حلقات For التالية على البحث عن الأزواج في الأرقام المدخلة التي يمكن أن يكون مجموعها يساوي الرقم الهدف
    for x in range(len(num_list)-1):#تكرر هذه الحلقة 9 مرات لأنه سوف يتم فحص العدد قبل الأخير مع العدد الأخير في الحلقة التالية
        for y in range(len(num_list)):
            if num_list[x]+num_list[y] == target_number:#التحقق اذا كان مجموع العددين يساوي العدد الهدف
                pair_list.append(sorted([num_list[x],num_list[y]]))# في حال كان العددين يحققان الشرط يتم انشاء قائمة تحوي العددين بعد ترتيبهما ثم اضافة هذه القائمة الى قائمة pair list
    if len(pair_list) == 0:#
        print("لا يوجد أي زوج يحقق الهدف")
    else:
        pair_list=list(set(tuple(x) for x in pair_list))#الهدف من هذه السطر التخلص من الأزواج المكررة فالنوع set لا يقبل أن يحوي متغيرات مكررة لذلك في حال وجود tuples  تحوي نفس الأرقام   يتم حذفها
        print(pair_list)

construct_pairs()
