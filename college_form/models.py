from django.db import models

# Create your models here.

# User : form
# Pass : 123

class student_Signup(models.Model):
    # login
    username = models.CharField(("User Name"),max_length=50,null=True, blank=True)
    useremail = models.CharField(("User Email"), max_length=50)
    userphone = models.CharField(("User Phone"), max_length=50)
    password = models.CharField(("User Password"),max_length=50,null=True, blank=True)
    userConfpassword = models.CharField(("Confirm Password"), max_length=50)
    # In Details
    title = models.CharField(("Title"), max_length=50, null=True, blank=True)
    lname = models.CharField(("Last Name/ Surname"), max_length=50, null=True, blank=True)
    fname = models.CharField(("First Name"), max_length=50, null=True, blank=True)
    mname = models.CharField(("Middle Name"), max_length=50, null=True, blank=True)
    mobile = models.CharField(("Mobile"), max_length=50, null=True, blank=True)
    altphone = models.CharField(("Alternate Phone"), max_length=50, null=True, blank=True)
    marital_status = models.CharField(("Marital Status"), max_length=50, null=True, blank=True)
    blood = models.CharField(("Blood Group"), max_length=50, null=True, blank=True)
    gender = models.CharField(("Gender"), max_length=50, null=True, blank=True)
    dob = models.CharField(("dob"), max_length=50, null=True, blank=True)
    mother_tougue = models.CharField(("Mother tougue"), max_length=50, null=True, blank=True)
    place_birth = models.CharField(("Place Birth"), max_length=50, null=True, blank=True)
    birth_state = models.CharField(("Birth State"), max_length=50, null=True, blank=True)
    nationality = models.CharField(("Nationality"), max_length=50, null=True, blank=True)
    caste_category = models.CharField(("Caste Category"), max_length=50, null=True, blank=True)
    religion  = models.CharField(("Religion"), max_length=50, null=True, blank=True)
    schoolarship  = models.CharField(("Schoolarship"), max_length=50, null=True, blank=True)
    subcast  = models.CharField(("Sub Cast"), max_length=50, null=True, blank=True)
    bank_name  = models.CharField(("Bank Name"), max_length=50, null=True, blank=True)
    acno = models.CharField(("Ac no."), max_length=50, null=True, blank=True)
    father_name = models.CharField(("Father Name"), max_length=50, null=True, blank=True)
    father_occupation = models.CharField(("Father Occupation"), max_length=50, null=True, blank=True)
    mother_name = models.CharField(("Mother Name"), max_length=50, null=True, blank=True)
    gardian_no = models.CharField(("Gardian No."), max_length=50, null=True, blank=True)
    father_first_name = models.CharField(("Father First Name"), max_length=50, null=True, blank=True)
    father_middle_name = models.CharField(("Father middle Name"), max_length=50, null=True, blank=True)
    father_last_name = models.CharField(("Father Last Name"), max_length=50, null=True, blank=True)
    is_diff_abled = models.CharField(("Is Different Abled"), max_length=50, null=True, blank=True)
    adhaar = models.CharField(("Adhaar No."), max_length=50, null=True, blank=True)
    adhaar_link = models.CharField(("Adhaar Link"), max_length=50, null=True, blank=True)
    id_proof = models.CharField(("Id Proof"), max_length=50, null=True, blank=True)
    sport_person = models.CharField(("Sports Person"), max_length=50, null=True, blank=True)
    ncc = models.CharField(("NCC"), max_length=50, null=True, blank=True)
    uni_reg_no = models.CharField(("University Reg No."), max_length=50, null=True, blank=True)
    medium_of_instru = models.CharField(("Medium Of Instruction"), max_length=50, null=True, blank=True)
    social_res = models.CharField(("Social Reservation"), max_length=50, null=True, blank=True)
    full_nominee = models.CharField(("Full Nominee Name"), max_length=50, null=True, blank=True)
    nominee_relation = models.CharField(("Nominee Relation With Student"), max_length=50, null=True, blank=True)
    nominee_dob = models.CharField(("Nominee DOB"), max_length=50, null=True, blank=True)
    nominee_age = models.CharField(("Nominee AGE"), max_length=50, null=True, blank=True)
    nominee_mobile_no = models.CharField(("Nominee Mobile No"), max_length=50, null=True, blank=True)
    nominee_adhar_no = models.CharField(("Nominee Aadhaar No"), max_length=50, null=True, blank=True)
    # Address Details
    h_no = models.CharField(("House No"), max_length=50, null=True, blank=True)
    paddress = models.CharField(("Permanent Address"), max_length=50, null=True, blank=True)
    country = models.CharField(("Country"), max_length=50, null=True, blank=True)
    state = models.CharField(("State"), max_length=50, null=True, blank=True)
    district = models.CharField(("District"), max_length=50, null=True, blank=True)
    city = models.CharField(("city"), max_length=50, null=True, blank=True)
    tehsil = models.CharField(("Tehsil"), max_length=50, null=True, blank=True)
    gram_p = models.CharField(("Gram Panchayat"), max_length=50, null=True, blank=True)
    pincode = models.CharField(("Pin Code"), max_length=50, null=True, blank=True)
    #    education details
    examlevel = models.CharField(("Exam Level"), max_length=50, null=True, blank=True)
    exam_name = models.CharField(("Exam Name"), max_length=50, null=True, blank=True)
    board = models.CharField(("Board/University"), max_length=50, null=True, blank=True)
    dop = models.CharField(("Date Of Passing"), max_length=50, null=True, blank=True)
    yop = models.CharField(("Year Of Passing"), max_length=50, null=True, blank=True)
    op_mark = models.CharField(("Optained Marks"), max_length=50, null=True, blank=True)
    total_mark = models.CharField(("Total Marks"), max_length=50, null=True, blank=True)
    perc = models.CharField(("Percentage"), max_length=50, null=True, blank=True)
    result = models.CharField(("Result"), max_length=50, null=True, blank=True)
    # Student Photo and signature
    stu_photo = models.FileField(("Student Photo"), upload_to="student_photo", null=True, blank=True)
    stu_signature = models.FileField(("Student Signature"), upload_to="student_signature", null=True, blank=True)
    # select course
    sel_course = models.CharField(("Select Course"), max_length=50, null=True, blank=True)
    # application Status
    application_status = models.BooleanField(default=False)
    status = bool
    
    def __str__(self) -> str:
        return (f'id : {str(self.id)} Username : {self.username} Course : {self.sel_course}')
    
