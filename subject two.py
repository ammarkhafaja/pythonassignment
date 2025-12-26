num_list,pair_list,target_number=[],[],0
def check_numeric_value(value,note):
    #تعمل هذه الدالة على التأكد من أن القيمة المدخلة رقمية وموجبة
    if value.isdigit():
        if int(value) >0:
            return int(value)
    else:
        value = input(note)
        while True:
            if value.isdigit():
                if int(value) > 0:
                    return int(value)
            value = input(note)

def construct_pairs():
    for z in range(10):
        value=input("أدخل الرقم "+str(z+1)+ ": ")
        global pair_list
        num_list.append(check_numeric_value(value,"يجب ادخال عدد صحيح موجب"))
    target_number=input("أدخل الرقم الهدف")
    target_number=check_numeric_value(target_number,"يرجى ادخال الرقم الهدف, يجب أن يكون عدداً صحيحاً وموجباً")
    for x in range(len(num_list)-1):
        for y in range(len(num_list)):
            if num_list[x]+num_list[y] == target_number:
                pair_list.append(sorted([num_list[x],num_list[y]]))
    if len(pair_list) == 0:
        print("لا يوجد أي زوج يحقق الهدف")
    else:
        pair_list=list(set(tuple(x) for x in pair_list))
        print(pair_list)

construct_pairs()
