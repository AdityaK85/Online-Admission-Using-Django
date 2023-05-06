from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib import messages

# Create your views here.

def test(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')


@csrf_exempt
def new_Register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')
        userphone = request.POST.get('userphone')
        password = request.POST.get('password')
        userConfpassword = request.POST.get('userConfpassword')

        student_Signup.objects.create(
            username=username,
            useremail=useremail,
            userphone = userphone,
            password=password,
            userConfpassword = userConfpassword
        )

        content = {
                'stu_user_name':username,
                'stu_user_password':password
            }
        
        html_file = render_to_string('mail_template.html', content)
        text_content = strip_tags(html_file)
        to = useremail

        email = EmailMultiAlternatives(
            'Mundle Dharampeth college',
            text_content,
            settings.EMAIL_HOST_USER,
            [useremail]
        )
        email.attach_alternative(html_file, 'text/html')
        email.send()

    return HttpResponse("success")




@csrf_exempt
def login_Request(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not student_Signup.objects.filter(username=username, password=password).exists():
            return HttpResponse("error")
        else:
            obj = student_Signup.objects.get(username=username,password=password)
       
            request.session['user_id'] = str(obj.id)
            request.session['username'] = str(obj.username)



            return HttpResponse('success')
        
@csrf_exempt
def signout(request):
    del request.session['user_id']
    return redirect('/')
    
@csrf_exempt
def already_fill_fomr(request):
    try:
        if request.session.get('user_id') or request.session.get('username'):
            request.session.set_expiry(1000)
            username = request.session['username']
            id = request.session['user_id']
            stuId =  student_Signup.objects.get(id = id)
            if stuId.application_status:
                return redirect("/preview")
            else :
                return redirect("/Personal-details")
    except:
        return redirect('/')


@csrf_exempt
def submit_personal_details(request):
    try:
        if request.session.get('user_id') or request.session.get('username'):
            request.session.set_expiry(1000)
            username = request.session['username']
            id = request.session['user_id']
            if request.method == "POST":
                stuId =  student_Signup.objects.get(id = id)
                stuId.title = request.POST['title']
                # stuId.useremail = request.POST['useremail']
                stuId.lname = request.POST['lname']
                stuId.fname = request.POST['fname']
                stuId.mname = request.POST['mname']
                stuId.mobile = request.POST['mobile']
                stuId.altphone = request.POST['altphone']
                stuId.marital_status = request.POST['marital_status']
                stuId.blood = request.POST['blood']
                stuId.gender = request.POST['gender']
                stuId.dob = request.POST['dob']
                stuId.mother_tougue = request.POST['mother_tougue']
                stuId.place_birth = request.POST['place_birth']
                stuId.birth_state = request.POST['birth_state']
                stuId.nationality = request.POST['nationality']
                stuId.caste_category = request.POST['caste_category']
                stuId.religion = request.POST['religion']
                stuId.schoolarship = request.POST['schoolarship']
                stuId.subcast = request.POST['subcast']
                stuId.bank_name = request.POST['bank_name']
                stuId.acno = request.POST['acno']
                stuId.father_name = request.POST['father_name']
                stuId.father_occupation = request.POST['father_occupation']
                stuId.mother_name = request.POST['mother_name']
                stuId.gardian_no = request.POST['gardian_no']
                stuId.father_first_name = request.POST['father_first_name']
                stuId.father_middle_name = request.POST['father_middle_name']
                stuId.father_last_name = request.POST['father_last_name']
                stuId.is_diff_abled = request.POST['is_diff_abled']
                stuId.adhaar = request.POST['adhaar']
                stuId.adhaar_link = request.POST['adhaar_link']
                stuId.id_proof = request.POST['id_proof']
                stuId.sport_person = request.POST['sport_person']
                stuId.ncc = request.POST['ncc']
                stuId.uni_reg_no = request.POST['uni_reg_no']
                stuId.medium_of_instru = request.POST['medium_of_instru']
                stuId.social_res = request.POST['social_res']
                stuId.full_nominee = request.POST['full_nominee']
                stuId.nominee_relation = request.POST['nominee_relation']
                stuId.nominee_dob = request.POST['nominee_dob']
                stuId.nominee_age = request.POST['nominee_age']
                stuId.nominee_mobile_no = request.POST['nominee_mobile_no']
                stuId.nominee_adhar_no = request.POST['nominee_adhar_no']
                stuId.save()

                return HttpResponse('success')
    except:
        return redirect('/')
                

@csrf_exempt
def submit_address(request):
    try:
        if request.session.get('user_id') or request.session.get('username'):
            request.session.set_expiry(1000)
            username = request.session['username']
            id = request.session['user_id']
            if request.method == "POST":
                stuId =  student_Signup.objects.get(id = id)
                stuId.h_no = request.POST['h_no']
                stuId.paddress = request.POST['paddress']
                stuId.country = request.POST['country']
                stuId.state = request.POST['state']
                stuId.district = request.POST['district']
                stuId.city = request.POST['city']
                stuId.tehsil = request.POST['tehsil']
                stuId.gram_p = request.POST['gram_p']
                stuId.pincode = request.POST['pincode']
                stuId.save()
                return HttpResponse("success")
    except:
        return redirect('/')
        
@csrf_exempt
def submit_education(request):
    try:
        if request.session.get('user_id') or request.session.get('username'):
            request.session.set_expiry(1000)
            username = request.session['username']
            id = request.session['user_id']
            if request.method == "POST":
                stuId =  student_Signup.objects.get(id = id)
                stuId.examlevel = request.POST['examlevel'] 
                stuId.exam_name = request.POST['exam_name'] 
                stuId.board = request.POST['board'] 
                stuId.dop = request.POST['dop'] 
                stuId.yop = request.POST['yop'] 
                stuId.op_mark = request.POST['op_mark'] 
                stuId.total_mark = request.POST['total_mark'] 
                stuId.perc = request.POST['perc'] 
                stuId.result = request.POST['result'] 
                stuId.save()
                return HttpResponse("success")
    except:
        return redirect('/')

@csrf_exempt
def submit_photo_signature(request):
    try:
        if request.session.get('user_id') or request.session.get('username'):
            request.session.set_expiry(1000)
            username = request.session['username']
            id = request.session['user_id']
            if request.method == "POST":
                stuId =  student_Signup.objects.get(id = id)
                stuId.stu_photo = request.FILES.get('stu_photo')
                stuId.stu_signature = request.FILES.get('stu_signature')
                stuId.save()
                return redirect("/course-select")
    except:
        return redirect('/')

@csrf_exempt
def select_course(request):
    try:
        if request.session.get('user_id') or request.session.get('username'):
            request.session.set_expiry(1000)
            username = request.session['username']
            id = request.session['user_id']
            if request.method == "POST":
                stuId =  student_Signup.objects.get(id = id)
                stuId.sel_course = request.POST['sel_course']
                stuId.save()
                return HttpResponse("success")
    except:
        return redirect('/')
        
@csrf_exempt
def confirm(request):
    try:
        if request.session.get('user_id') or request.session.get('username'):
            request.session.set_expiry(1000)
            username = request.session['username']
            id = request.session['user_id']
            status  = request.POST['application_status'].capitalize()
            if request.method == "POST":
                stuId =  student_Signup.objects.get(id = id)
                if status:
                    stuId.application_status = True
                else:
                    stuId.application_status = False
                stuId.save()

                useremail = stuId.useremail
                sel_course = stuId.sel_course

                content = {
                    'username':username,
                    'id':id,
                    'sel_course':sel_course,
                }
                return HttpResponse("success")
    except:
        return redirect('/')
        


@csrf_exempt
def page_1(request):
    try:
        if request.session.get('user_id') or request.session.get('username'):
            request.session.set_expiry(1000)
            id = request.session['user_id']

            obj = student_Signup.objects.get(id=id).application_status
            
            if obj:
                msg = True
                return render(request, "page_1.html", {'msg':msg})
            else:
                username = request.session['username']
                useremail = student_Signup.objects.get(id=id).useremail
                title = student_Signup.objects.get(id=id).title
                lname = student_Signup.objects.get(id=id).lname
                fname = student_Signup.objects.get(id=id).fname
                mname = student_Signup.objects.get(id=id).mname
                mobile = student_Signup.objects.get(id=id).mobile
                altphone = student_Signup.objects.get(id=id).altphone
                marital_status = student_Signup.objects.get(id=id).marital_status
                blood = student_Signup.objects.get(id=id).blood
                gender = student_Signup.objects.get(id=id).gender
                dob = student_Signup.objects.get(id=id).dob
                mother_tougue = student_Signup.objects.get(id=id).mother_tougue
                place_birth = student_Signup.objects.get(id=id).place_birth
                birth_state = student_Signup.objects.get(id=id).birth_state
                nationality = student_Signup.objects.get(id=id).nationality
                caste_category = student_Signup.objects.get(id=id).caste_category
                religion = student_Signup.objects.get(id=id).religion
                schoolarship = student_Signup.objects.get(id=id).schoolarship
                subcast = student_Signup.objects.get(id=id).subcast
                bank_name = student_Signup.objects.get(id=id).bank_name
                acno = student_Signup.objects.get(id=id).acno
                father_name = student_Signup.objects.get(id=id).father_name
                father_occupation = student_Signup.objects.get(id=id).father_occupation
                mother_name = student_Signup.objects.get(id=id).mother_name
                gardian_no = student_Signup.objects.get(id=id).gardian_no
                father_first_name = student_Signup.objects.get(id=id).father_first_name
                father_middle_name = student_Signup.objects.get(id=id).father_middle_name
                father_last_name = student_Signup.objects.get(id=id).father_last_name
                is_diff_abled = student_Signup.objects.get(id=id).is_diff_abled
                adhaar = student_Signup.objects.get(id=id).adhaar
                adhaar_link = student_Signup.objects.get(id=id).adhaar_link
                id_proof = student_Signup.objects.get(id=id).id_proof
                sport_person = student_Signup.objects.get(id=id).sport_person
                ncc = student_Signup.objects.get(id=id).ncc
                uni_reg_no = student_Signup.objects.get(id=id).uni_reg_no
                medium_of_instru = student_Signup.objects.get(id=id).medium_of_instru
                social_res = student_Signup.objects.get(id=id).social_res
                full_nominee = student_Signup.objects.get(id=id).full_nominee
                nominee_relation = student_Signup.objects.get(id=id).nominee_relation
                nominee_dob = student_Signup.objects.get(id=id).nominee_dob
                nominee_age = student_Signup.objects.get(id=id).nominee_age
                nominee_mobile_no = student_Signup.objects.get(id=id).nominee_mobile_no
                nominee_adhar_no = student_Signup.objects.get(id=id).nominee_adhar_no

                context = {
                    'username':username,
                    'useremail':useremail,
                    'title':title,
                    'lname':lname,
                    'fname':fname,
                    'mname':mname,
                    'mobile':mobile,
                    'altphone':altphone,
                    'marital_status':marital_status,
                    'blood':blood,
                    'gender':gender,
                    'dob':dob,
                    'mother_tougue':mother_tougue,
                    'place_birth':place_birth,
                    'birth_state':birth_state,
                    'nationality':nationality,
                    'caste_category':caste_category,
                    'religion':religion,
                    'schoolarship':schoolarship,
                    'subcast':subcast,
                    'bank_name':bank_name,
                    'acno':acno,
                    'father_name':father_name,
                    'father_occupation':father_occupation,
                    'mother_name':mother_name,
                    'gardian_no':gardian_no,
                    'father_first_name':father_first_name,
                    'father_middle_name':father_middle_name,
                    'father_last_name':father_last_name,
                    'is_diff_abled':is_diff_abled,
                    'adhaar':adhaar,
                    'adhaar_link':adhaar_link,
                    'id_proof':id_proof,
                    'sport_person':sport_person,
                    'ncc':ncc,
                    'uni_reg_no':uni_reg_no,
                    'medium_of_instru':medium_of_instru,
                    'social_res':social_res,
                    'full_nominee':full_nominee,
                    'nominee_relation':nominee_relation,
                    'nominee_dob':nominee_dob,
                    'nominee_age':nominee_age,
                    'nominee_mobile_no':nominee_mobile_no,
                    'nominee_adhar_no':nominee_adhar_no,
                }
                return render(request, "page_1.html", context)
    except:
        return redirect('/')
    

    
@csrf_exempt
def page_2(request):
    try:
        if request.session.get('user_id') or request.session.get('username'):
            request.session.set_expiry(1000)
            username = request.session['username']
            id = request.session['user_id']

            obj = student_Signup.objects.get(id=id).application_status

            if obj:
                msg = True
                return render(request, "page_2.html", {'msg':msg})
            else:
                h_no = student_Signup.objects.get(id=id).h_no
                paddress = student_Signup.objects.get(id=id).paddress
                country = student_Signup.objects.get(id=id).country
                state = student_Signup.objects.get(id=id).state
                district = student_Signup.objects.get(id=id).district
                city = student_Signup.objects.get(id=id).city
                tehsil = student_Signup.objects.get(id=id).tehsil
                gram_p = student_Signup.objects.get(id=id).gram_p
                pincode = student_Signup.objects.get(id=id).pincode
                context = {
                    'username':username,
                    'h_no' : h_no,
                    'paddress' : paddress,
                    'country' : country,
                    'state' : state,
                    'district' : district,
                    'city' : city,
                    'tehsil' : tehsil,
                    'gram_p' : gram_p,
                    'pincode' : pincode,
                }
            return render(request, "page_2.html", context)
    except :
        return redirect('/')

        
@csrf_exempt
def page_3(request):
        if request.session.get('user_id') or request.session.get('username'):
            request.session.set_expiry(1000)
            username = request.session['username']
            id = request.session['user_id']
            obj = student_Signup.objects.get(id=id).application_status
            
            if obj:
                msg = True
                return render(request, "page_3.html", {'msg':msg})
            else:

                examlevel = student_Signup.objects.get(id=id).examlevel
                exam_name = student_Signup.objects.get(id=id).exam_name
                board = student_Signup.objects.get(id=id).board
                dop = student_Signup.objects.get(id=id).dop
                yop = student_Signup.objects.get(id=id).yop
                op_mark = student_Signup.objects.get(id=id).op_mark
                total_mark = student_Signup.objects.get(id=id).total_mark
                perc = student_Signup.objects.get(id=id).perc
                result = student_Signup.objects.get(id=id).result
                context = {
                    'username':username,
                    'examlevel' : examlevel,
                    'exam_name' : exam_name,
                    'board' : board,
                    'dop' : dop,
                    'yop' : yop,
                    'op_mark' : op_mark,
                    'total_mark' : total_mark,
                    'perc' : perc,
                    'result' : result,
                }
                return render(request, "page_3.html", context)
    
@csrf_exempt
def page_4(request):
    try:
        if request.session.get('user_id') or request.session.get('username'):
            request.session.set_expiry(1000)
            username = request.session['username']
            id = request.session['user_id']
            obj = student_Signup.objects.get(id=id).application_status
            
            if obj:
                msg = True
                return render(request, "page_4.html", {'msg':msg})
            else:
                stu_photo = student_Signup.objects.get(id=id).stu_photo
                stu_signature = student_Signup.objects.get(id=id).stu_signature
                context = {
                    'username':username,
                    'stu_photo':stu_photo,
                    'stu_signature':stu_signature,
                }
                return render(request, "page_4.html", context)
    except:
        return redirect('/')
    
@csrf_exempt
def page_5(request):
    try:
        if request.session.get('user_id') or request.session.get('username'):
            request.session.set_expiry(1000)
            username = request.session['username']
            id = request.session['user_id']
            obj = student_Signup.objects.get(id=id).application_status
            
            if obj:
                msg = True
                return render(request, "page_5.html", {'msg':msg})
            else:
                sel_course = student_Signup.objects.get(id=id).sel_course
                application_status = student_Signup.objects.get(id=id).application_status

                context = {
                    'username':username,
                    'sel_course':sel_course,
                    'application_status':application_status,
                    'id':id
                }
                return render(request, "page_5.html", context)
    except:
        return redirect('/')


    
@csrf_exempt
def preview_html(request):
    try:
        if request.session.get('user_id') or request.session.get('username'):
            request.session.set_expiry(1000)
            username = request.session['username']
            id = request.session['user_id']
            useremail = student_Signup.objects.get(id=id).useremail
            title = student_Signup.objects.get(id=id).title
            lname = student_Signup.objects.get(id=id).lname
            fname = student_Signup.objects.get(id=id).fname
            mname = student_Signup.objects.get(id=id).mname
            mobile = student_Signup.objects.get(id=id).mobile
            altphone = student_Signup.objects.get(id=id).altphone
            marital_status = student_Signup.objects.get(id=id).marital_status
            blood = student_Signup.objects.get(id=id).blood
            gender = student_Signup.objects.get(id=id).gender
            dob = student_Signup.objects.get(id=id).dob
            mother_tougue = student_Signup.objects.get(id=id).mother_tougue
            place_birth = student_Signup.objects.get(id=id).place_birth
            birth_state = student_Signup.objects.get(id=id).birth_state
            nationality = student_Signup.objects.get(id=id).nationality
            caste_category = student_Signup.objects.get(id=id).caste_category
            religion = student_Signup.objects.get(id=id).religion
            schoolarship = student_Signup.objects.get(id=id).schoolarship
            subcast = student_Signup.objects.get(id=id).subcast
            bank_name = student_Signup.objects.get(id=id).bank_name
            acno = student_Signup.objects.get(id=id).acno
            father_name = student_Signup.objects.get(id=id).father_name
            father_occupation = student_Signup.objects.get(id=id).father_occupation
            mother_name = student_Signup.objects.get(id=id).mother_name
            gardian_no = student_Signup.objects.get(id=id).gardian_no
            father_first_name = student_Signup.objects.get(id=id).father_first_name
            father_middle_name = student_Signup.objects.get(id=id).father_middle_name
            father_last_name = student_Signup.objects.get(id=id).father_last_name
            is_diff_abled = student_Signup.objects.get(id=id).is_diff_abled
            adhaar = student_Signup.objects.get(id=id).adhaar
            adhaar_link = student_Signup.objects.get(id=id).adhaar_link
            id_proof = student_Signup.objects.get(id=id).id_proof
            sport_person = student_Signup.objects.get(id=id).sport_person
            ncc = student_Signup.objects.get(id=id).ncc
            uni_reg_no = student_Signup.objects.get(id=id).uni_reg_no
            medium_of_instru = student_Signup.objects.get(id=id).medium_of_instru
            social_res = student_Signup.objects.get(id=id).social_res
            full_nominee = student_Signup.objects.get(id=id).full_nominee
            nominee_relation = student_Signup.objects.get(id=id).nominee_relation
            nominee_dob = student_Signup.objects.get(id=id).nominee_dob
            nominee_age = student_Signup.objects.get(id=id).nominee_age
            nominee_mobile_no = student_Signup.objects.get(id=id).nominee_mobile_no
            nominee_adhar_no = student_Signup.objects.get(id=id).nominee_adhar_no
            # Address
            h_no = student_Signup.objects.get(id=id).h_no
            paddress = student_Signup.objects.get(id=id).paddress
            country = student_Signup.objects.get(id=id).country
            state = student_Signup.objects.get(id=id).state
            district = student_Signup.objects.get(id=id).district
            city = student_Signup.objects.get(id=id).city
            tehsil = student_Signup.objects.get(id=id).tehsil
            gram_p = student_Signup.objects.get(id=id).gram_p
            pincode = student_Signup.objects.get(id=id).pincode
            # education
            examlevel = student_Signup.objects.get(id=id).examlevel
            exam_name = student_Signup.objects.get(id=id).exam_name
            board = student_Signup.objects.get(id=id).board
            dop = student_Signup.objects.get(id=id).dop
            yop = student_Signup.objects.get(id=id).yop
            op_mark = student_Signup.objects.get(id=id).op_mark
            total_mark = student_Signup.objects.get(id=id).total_mark
            perc = student_Signup.objects.get(id=id).perc
            result = student_Signup.objects.get(id=id).result
            # photo and signature
            stu_photo = student_Signup.objects.get(id=id).stu_photo
            stu_signature = student_Signup.objects.get(id=id).stu_signature
            # select course
            sel_course = student_Signup.objects.get(id=id).sel_course

            context = {
                'username':username,
                'useremail':useremail,
                'title':title,
                'lname':lname,
                'fname':fname,
                'mname':mname,
                'mobile':mobile,
                'altphone':altphone,
                'marital_status':marital_status,
                'blood':blood,
                'gender':gender,
                'dob':dob,
                'mother_tougue':mother_tougue,
                'place_birth':place_birth,
                'birth_state':birth_state,
                'nationality':nationality,
                'caste_category':caste_category,
                'religion':religion,
                'schoolarship':schoolarship,
                'subcast':subcast,
                'bank_name':bank_name,
                'acno':acno,
                'father_name':father_name,
                'father_occupation':father_occupation,
                'mother_name':mother_name,
                'gardian_no':gardian_no,
                'father_first_name':father_first_name,
                'father_middle_name':father_middle_name,
                'father_last_name':father_last_name,
                'is_diff_abled':is_diff_abled,
                'adhaar':adhaar,
                'adhaar_link':adhaar_link,
                'id_proof':id_proof,
                'sport_person':sport_person,
                'ncc':ncc,
                'uni_reg_no':uni_reg_no,
                'medium_of_instru':medium_of_instru,
                'social_res':social_res,
                'full_nominee':full_nominee,
                'nominee_relation':nominee_relation,
                'nominee_dob':nominee_dob,
                'nominee_age':nominee_age,
                'nominee_mobile_no':nominee_mobile_no,
                'nominee_adhar_no':nominee_adhar_no,
                'h_no' : h_no,
                'paddress' : paddress,
                'country' : country,
                'state' : state,
                'district' : district,
                'city' : city,
                'tehsil' : tehsil,
                'gram_p' : gram_p,
                'pincode' : pincode,
                'username':username,
                'examlevel' : examlevel,
                'exam_name' : exam_name,
                'board' : board,
                'dop' : dop,
                'yop' : yop,
                'op_mark' : op_mark,
                'total_mark' : total_mark,
                'perc' : perc,
                'result' : result,
                'stu_photo':stu_photo,
                'stu_signature':stu_signature,
                'sel_course':sel_course,
                'id':id
            }
            return render(request, "preview.html", context)
    except :
        return redirect('/')
