age, monthly_income, loan_value, monthly_payment, insurance, total_monthly_payment = 0, 0, 0, 0, 0, 0

def check_numeric_value(value,note):
    #تعمل هذه الدالة على التأكد من أن القيمة المدخلة رقمية وموجبة
    if value.isdigit(): #يتم التحقق من أن القيمة المدخلة رقمية
        if int(value) >0:# يتم التحقق من أن الرقم المدخل موجب
            return int(value)
    else:

        value = input(note)
        while True:
            if value.isdigit():
                if int(value) > 0:
                    return int(value)
            value = input(note)

def getting_loan():
    age = input("يرجى ادخال العمر: ")
    age = check_numeric_value(age,"يرجى ادخال العمر بشكل صحيح")
    if age >=21 and age <65:
        # يتم التحقق من أن العمر المدخل  يحقق الشرط المطلوب قبل ادخال باقي معلومات المستخدم
        # لأنه لا حاجة لجعل المستخدم يدخل باقي المعلومات كون القرض سوف يرفض بسبب شرط العمر
        monthly_income=input("ادخل قيمة الدخل الشهري: ")
        monthly_income=check_numeric_value(monthly_income,"يرجى ادخال قيمة الدخل الشهري بشكل صحيح")
        if monthly_income < 3000:
            print("الدخل الشهري غير كاف")
        else:
            loan_value=input("أدخل قيمة القرض المطلوب: ")
            loan_value=check_numeric_value(loan_value,"يرجى ادخال قيمة القرض المطلوب بشكل صحيح")
            if loan_value <= 5000:
                print("ٌقيمة القرض أقل من المسموح")
            else:
                monthly_payment=loan_value * 0.1
                if loan_value < 20000:
                    insurance=loan_value * 0.015
                else:
                    insurance=loan_value * 0.01
                total_monthly_payment=monthly_payment + insurance
                if total_monthly_payment > monthly_income * 0.3:
                    print("القسط الشهري يتجاوز 30% من الدخل الشهري")
                else:
                    print("أنت مؤهل للحصول على قرض")
                    print("قيمة القسط الشهري: ",int(monthly_payment))
                    print("قيمة قسط التأمين: ", int(insurance))
                    print("المجموع الكلي للقسط الشهري" , int(total_monthly_payment))
    else:
        print("العمر غير مناسب")
getting_loan()



