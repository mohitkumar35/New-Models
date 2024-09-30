from django.shortcuts import render
from.models import student
# Create your views here.

def home(request):
    return render(request,"home.html")

def register(request):
    if request.method=='POST':
        # print(request.POST)
        name=request.POST.get('nm')
        email=request.POST.get('em')
        contact=request.POST.get('con')
        password=request.POST.get('pass')
        cpassword=request.POST.get('cpass')
        print(name,email,contact,password)
        user=student.objects.filter(stu_email=email)
        if user:
            msg="Email already exist"
            return render(request,"login.html",{'msg':msg})
        else:
            student.objects.create(
            stu_name=name,
            stu_email=email,
            stu_contact=contact,
            stu_password=password,
            )
            msg="Registration Successfully"
            return render(request,"login.html",{'msg':msg})
    else:
        msg="password & cpassword not matched"
        return render(request,"register.html",{'msg':msg})
        


        # user=student.objects.get(stu_email=email)
        # print(user)

        # Model_name.objects.create(
        #     col_name=value,
        #     col_name=value,
        #     col_name=value,
        
        # student.objects.create(
        #     stu_name=name,
        #     stu_email=email,
        #     stu_contact=contact,
        #     stu_password=password,
        #     )
        # msg="Registration successfull"
        # return render(request,"home.html",{'msg':msg})



    #  else:
    #    return render(request,"register.html")
    
def login(request):
    if request.method=='POST':
        email=request.POST.get('em')
        password=request.POST.get('pass')
        cpassword=request.POST.get('cpass')
        user=student.objects.filter(stu_email=email)
        if user:
            user_data=student.objects.get(stu_email=email)
            print(user_data)
            email1=user_data.stu_email
            name1=user_data.stu_name
            contact1=user_data.stu_contact
            password1=user_data.stu_password
            print(name1,email1,contact1,password1)
            if password==password1:
                data={
                    'name':name1,
                    'email':email1,
                    'contact':contact1,
                    'password':password1
                }
                return render(request,'dashboard.html',data)
            else:
                msg="Email & password not matched"
                return render(request,'login.html',{'msg':msg})

        else:
            msg="Email not register"
            return render(request,'register.html',{'msg':msg})
    else:
        return render(request,'login.html')
