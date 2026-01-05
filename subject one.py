age, monthly_income, loan_value, monthly_payment, insurance, total_monthly_payment,ban_reason = 0, 0, 0, 0, 0, 0,[]
def reinsert(note):#تعمل هذه الدالة على تكرار عملية الادخال حتى يقوم المستخدم بادخال قيمة عددية موجبة
    value = input(note)
    while True:
        if value.isdigit():
            if int(value) > 1:
                return int(value)
        value = input(note)
def check_numeric_value(value,note):
    #تعمل هذه الدالة على التأكد من أن القيمة المدخلة رقمية وموجبة
    if value.isdigit() : #يتم التحقق من أن القيمة المدخلة رقمية
        if int(value) >1:# يتم التحقق من أن الرقم المدخل موجب في حال عدم تحقق أحد الشرطين يتم استدعاء الدالة Resinsert
            return int(value)
        else:reinsert(note)
    else:
        return reinsert(note)
# القائمة  ban_reason سوف تحوي الأسباب الأولية التي سوف تمنع المصرف من اعطاء القرض وهي العمر - الدخل الشهري - قيمة القرض
def getting_loan():
    age = input("يرجى ادخال العمر: ")
    age = check_numeric_value(age,"يرجى ادخال العمر بشكل صحيح: ")
    monthly_income = input("ادخل قيمة الدخل الشهري: ")
    monthly_income = check_numeric_value(monthly_income, "يرجى ادخال قيمة الدخل الشهري بشكل صحيح: ")
    loan_value = input("أدخل قيمة القرض المطلوب: ")
    loan_value = check_numeric_value(loan_value, "يرجى ادخال قيمة القرض المطلوب بشكل صحيح: ")
    if age <21 or age >=65:
        ban_reason.append("العمر غير مناسب")
    if monthly_income < 3000:
        ban_reason.append("الدخل الشهري غير كاف")
    if loan_value <= 5000:
        ban_reason.append("قيمة القرض أقل من المسموح")
    if len(ban_reason) == 0:# سوف يتم التحقق من طول القائمة  ban_reason لأنه اذا كان طول هذه القائمة لايساوي الصفر فهذا يعني وجود سبب أولي يمنع البنك من اعطاء القرض للعميل
        monthly_payment=loan_value * 0.1#حساب قيمة القسط الشهري للقرض
        if loan_value < 20000:# التحقق من قيمة القرض لمعرفة قيمة التأمين التي سوف يتم فرضها على الزبون
            insurance=loan_value * 0.015
        else:
            insurance=loan_value * 0.01
        total_monthly_payment=monthly_payment + insurance# حساب قيمة القسك الشهري الكامل التي يجب على الزبون دقعها كل شهر
        if total_monthly_payment > monthly_income * 0.3:#التحقق من أن قيمة القسط الشهري الشامل لا يتجاوز 30% من الدخل الشهري للزبون
            print("القسط الشهري يتجاوز 30% من الدخل الشهري")
        else:
            print("أنت مؤهل للحصول على قرض")
            print("قيمة القسط الشهري: ",int(monthly_payment))
            print("قيمة قسط التأمين: ", int(insurance))
            print("المجموع الكلي للقسط الشهري" , int(total_monthly_payment))
    else:
        [print(x) for x in ban_reason]
getting_loan()



