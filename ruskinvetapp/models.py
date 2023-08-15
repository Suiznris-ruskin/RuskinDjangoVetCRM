from django.db import models

# Create your models here.
class Communications(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()

class Pet_Parent(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth=models.DateField()
    email = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("NONBINARY", "Non Binary"),
    ]
    gender = models.CharField(
        max_length=15,
        choices = GENDER_CHOICES,
        )
    phone = models.CharField(max_length=15)
    address= models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    zipcode = models.CharField(max_length=10)
    CONTACT_METHOD_CHOICES = [
        ("PHONE", "Phone"),
        ("EMAIL", "Email"),
    ]
    contact_method=models.CharField(
        max_length=15,
        choices = CONTACT_METHOD_CHOICES,
        )
    CONTACT_TYPE_CHOICES = [
        ("CUSTOMER", "Customer"),
        ("VET", "Veterinarian"),
        ("STAFF", "Staff Member"),
        ("SUPPLIER", "Supplier Contact"),
        ("SYNDICATE", "Syndicate Contact"),
        ("PHARMACY", "Pharmacy"),
    ]
    contact_type=models.CharField(
        max_length=25,
        choices = CONTACT_TYPE_CHOICES,
        )
    

    def __str__(self):
        return(f"{self.first_name}{self.last_name}")
    



class Pet(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    species = models.CharField(max_length=25)
    BREEDS_CHOICES = [
        ("CANINE", "Dog"),
        ("FELINE", "Cat"),
    ]
    breed = models.CharField(
        max_length=50,
        choices = BREEDS_CHOICES,
        )
    COLOR_CHOICES = [
        ("ALBINO", "Albino"),
        ("AMBER", "Amber"),
        ("APRICOT", "Apricot"),
        ("BEIGE", "Beige"),
        ("BLACK", "Black"),
        ("BLONDE", "Blonde"),
        ("BROWN", "Brown"),
        ("PEACH", "Peach"),
        ("YELLOW", "Yellow"),
        ("WHITE", "White"),
    ]
    color = models.CharField(
        max_length=15,
        choices = COLOR_CHOICES,
        )
    notes = models.TextField()
    date_of_birth=models.DateField()
    weight=models.FloatField()
    pet_parent_id=models.ForeignKey(Pet_Parent, default=1, on_delete=models.SET_DEFAULT)


class Visit(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=250)
    meds_suppl = models.TextField(default=None, null=True)
    history = models.TextField(default=None, null=True)
    temperature = models.FloatField(default=None, null=True)
    pulse = models.IntegerField(default=None, null=True)
    RESPIRATORY_RATE_CHOICES = [
        ("LOW","<15"),
        ("NORMAL","15-30"),
        ("HIGH",">30"),
    ]
    respiratory_rate = models.CharField(
        max_length=15,
        choices = RESPIRATORY_RATE_CHOICES,
        default="15-30",
        null=True,
        )
    check_me_out = models.BooleanField(default=False)
    second_tag = models.BooleanField(default=False)
    weight=models.FloatField(default=None,blank=True,null=True)
    WEIGHT_UNIT_CHOICES = [
        ("KG","kg"),
        ("LBS","lbs")
    ]
    weight_unit = models.CharField(
        max_length=15,
        choices = WEIGHT_UNIT_CHOICES,
        default="kg",
        null=True,
        )
    date_of_visit = models.DateTimeField(auto_now_add=True)
    EXAM_ROOM_CHOICES = [
        ("ROOM1", "Exam Room 1"),
        ("ROOM2", "Exam Room 2"),
        ("ROOM3", "Exam Room 3"),
        ("ROOM4", "Exam Room 4"),
        ("ROOM5", "Exam Room 5"),
        ("ROOM6", "Exam Room 6"),
        ("ROOM7", "Exam Room 7"),
        ("ROOM8", "Exam Room 8"),
    ] 
    exam_room = models.CharField(
        max_length=15,
        choices = EXAM_ROOM_CHOICES,
        default="Exam Room 1",
        null=True,
        )
    notes = models.TextField(null=True)
    mucus_membrane = models.CharField(max_length=250,null=True)
    mucus_mentation = models.CharField(max_length=250,null=True)
    problem_list = models.CharField(max_length=250,null=True)
    diagnosis = models.CharField(max_length=250,null=True)
    assessment = models.CharField(max_length=250,null=True)
    prognosis = models.CharField(max_length=250,null=True)
    problem_list_ai = models.CharField(max_length=250,null=True)
    diagnosis_ai = models.CharField(max_length=250,null=True)
    assessment_ai = models.CharField(max_length=250,null=True)
    prognosis_ai = models.CharField(max_length=250,null=True)
    pet_parent_id=models.ForeignKey(Pet_Parent, default=1, on_delete=models.SET_DEFAULT)
    pet_id=models.ForeignKey(Pet, default=1, on_delete=models.SET_DEFAULT)

