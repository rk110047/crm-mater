from django.db import models
from datetime import datetime, timedelta
# from model_utils import Choices
# from services.models import Service
# from multiselectfield import MultiSelectField
from django.db.models.signals import pre_save
from django.contrib.auth.models import (AbstractUser,BaseUserManager)
#from ServiceLevelAgreement.models import SLA
from utils.models import BaseAbstractModel
from django.conf import settings
import jwt



govId_choices = (
    ('driving license', 'DRIVING LICENSE'),
    ('passport', 'PASSPORT'),
    ('aadhar', 'AADHAR CARD'),
    ('other', 'OTHER')
)

position = (
    ('SUPER USER', 'super user'),
    ('MANAGER', 'manager'),
    ('HR', 'hr'),
    ('STAFF', 'staff')
)

############################################# for generating unique cust_id,vend_id,emp_id

##############for user reg/login##################
class EmailField(models.EmailField):
    def get_prep_value(self, value):
        value = super(EmailField, self).get_prep_value(value)
        if value is not None:
            value = value.lower()
        return value


class UserManager(BaseUserManager):

    def create_user(
            self,
            email=None,
            password=None,
            role='VI'
    ):

        # if not first_name:
        #     raise TypeError('Users must have a first name.')

        # if not last_name:
        #     raise TypeError('Users must have a last name.')

        if not email:
            raise TypeError('Users must have an email address.')

        if not password:
            raise TypeError('Users must have a password.')

        user = self.model(
            # first_name=first_name,
            # last_name=last_name,
            email=self.normalize_email(email),
            username=self.normalize_email(email))
        user.set_password(password),
        user.role = role,
        user.save()
        return user

    def create_superuser(
            self, email=None, password=None, username=None
    ):
        # if not first_name:
        #     raise TypeError('Superusers must have a first name.')

        # if not last_name:
        #     raise TypeError('Superusers must have a last name.')

        if not email:
            raise TypeError('Superusers must have an email address.')

        if not password:
            raise TypeError('Superusers must have a password.')

        user = self.model(
            # first_name=first_name, last_name=last_name,
            email=self.normalize_email(email), username=self.normalize_email(email), role='admin')
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_verified = True
        user.set_password(password)
        user.save()
#

class User(AbstractUser, BaseAbstractModel):
    """ Here we will define the user modal """

    USER_ROLES = (
        ('AD', 'admin'),
        ('CA', 'client_admin'),
        ('VI', 'viewer'),
    )

    # username = models.CharField(
    #     null=True, blank=True, max_length=100, unique=True)
    email = EmailField(unique=True)
    role = models.CharField(
        verbose_name='user role', max_length=20, choices=USER_ROLES,
        default='VI'
    )
    # acct_expiry_date=models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    # USERNAME_FIELD = 'email'

    # REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()

    def __str__(self):
        return f'{self.email}'

    @property
    def get_email(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        expiration_time = datetime.now() + timedelta(hours=24)

        token = jwt.encode({
            'id': self.pk,
            'email': self.get_email,
            # 'exp': int(expiration_time.strftime('%s'))
            },
        settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


def counter(start,interval):
    count = start

    if count == 999999:
        count = 1

    while True:
        yield count
        count+= interval


count = counter(start=1,interval=1)

def autoinc():
    return str(next(count)).zfill(6)

############################################## ALL PROFILES



# employeeaccount
#
# class User(AbstractUser):
#     # role = models.CharField(verbose_name='user role', choices=position, max_length=20, default='unknown',null = True)
#
#     class Meta:
#         verbose_name_plural = 'user'

class EmployeeProfile(models.Model):

    
    first_name        = models.CharField(max_length=150, blank=False, null=True)
    last_name         = models.CharField(max_length=150, blank=False, null=True)
    username          = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    # username        = models.CharField(max_length=20, primary_key=True)
    email_id          = models.EmailField(max_length=150, blank=False, null=True)
    # password        = models.CharField(max_length=100)
    dob               = models.DateField()
    contact           = models.CharField(verbose_name='PhoneNo.',max_length=20,blank=False, null=True)
    address_1         = models.CharField(max_length=150, blank=False, null=True)
    address_2         = models.CharField(max_length=150, blank=False, null=True)
    city              = models.CharField(max_length=150, blank=False, null=True)
    state             = models.CharField(max_length=150, blank=False, null=True)
    country           = models.CharField(max_length=150, blank=False, null=True)
    zip_code          = models.CharField(max_length=150, blank=False, null=True)
    govt_id           = models.CharField(max_length=150, blank=False, null=True,choices=govId_choices)
    id_no             = models.CharField(verbose_name='',max_length=150, unique=True,blank=False, null=True)
    employee_id       = models.CharField(max_length=50, blank=True, null=True, unique=True)
    p_id1             = models.CharField(verbose_name='PersonalID',max_length=150, blank=False, null=True)  #type of pid
    p_id2             = models.CharField(verbose_name='',max_length=500, blank=False, null=True, unique=True)                      #link of pid
    upload_documents  = models.FileField(null=True,blank=True)
    company_code      = models.CharField(max_length=150, blank=False, null=True)
    position          = models.CharField(max_length=150, blank=False, null=True)
    staff             = models.BooleanField(default=False)  # staff user
    admin             = models.BooleanField(default=False)  # super user
    hr                = models.BooleanField(default=False)
    manager           = models.BooleanField(default=False)
    active            = models.BooleanField(default=False)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.employee_id

    @property
    def is_superUser(self):
        return self.admin

    @property
    def is_hr(self):
        return self.hr

    @property
    def is_active(self):
        return self.active

    @property
    def is_manager(self):
        return self.manager
    
    class Meta:
        verbose_name_plural = 'employee'
    

def pre_save_emp_id(instance,sender,*args,**kwargs):
    # print(instance.company_code)
    def Letters(*args, **kwargs):
        string = instance.company_code[0:2]
        for i in range(len(instance.company_code)):
            if instance.company_code[i] == ' ':
                if len(string) == 4:
                    break
                else:
                    string += instance.company_code[i+1:i+3]
        # print(self.string)
        return str(string)   

    

    instance.employee_id = Letters() + autoinc()

    
pre_save.connect(pre_save_emp_id,sender=EmployeeProfile)




# customeraccount
class Customer(models.Model):

    
    first_name        = models.CharField(max_length=150, blank=False, null=True)
    last_name         = models.CharField(max_length=150, blank=False, null=True)
    email_id          = models.CharField(max_length=150, blank=False, null=True)
    govt_id           = models.CharField(max_length=150, blank=False, null=True, choices=govId_choices)
    id_no             = models.CharField(verbose_name='',max_length=150, unique = True,blank=False, null=True)
    p_id1             = models.CharField(verbose_name='PersonalID',max_length=150, blank=False, null=True) # type of id
    p_id_link         = models.CharField(verbose_name='',max_length=500, blank=False, null=True, unique=True)                      #link of pid
    contact           = models.CharField(verbose_name='PhoneNo.'
                                                      '',max_length=20,blank=False, null=True)
    address_1         = models.CharField(max_length=150, blank=False, null=True)
    address_2         = models.CharField(max_length=150, blank=False, null=True)
    city              = models.CharField(max_length=150, blank=False, null=True)
    state             = models.CharField(max_length=150, blank=False, null=True)
    country           = models.CharField(max_length=150, blank=False, null=True)
    zip_code          = models.CharField(max_length=150, blank=False, null=True) 
    createdBy         = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, default='',editable=False,null=True)
    company_code      = models.CharField(max_length=150, blank=False, null=True)
    customer_id       = models.CharField(max_length=150, blank=True, null=True)
    # ticket_no         = models.IntegerField(blank=True,null=True)
    # issue             = models.CharField(max_length=150,blank=True,null=True)
    # services          = MultiSelectField(choices=MY_CHOICES,null=True)
    # serviceTAG        = models.ManyToManyField(Service)


    # creationDate    = models.DateTimeField(auto_now_add=True)
    # updatedAt       = models.DateTimeField(auto_now=True)
    # board             = ArrayField(
    #                        ArrayField(
    #                             models.CharField(max_length=10, blank=True),
    #                             size=8,
    #                       ),
    #                       size=8,null=True
    # )
    

    def __str__(self):
        return (self.first_name)


    class Meta:
        verbose_name_plural = 'Customer'

  

def pre_save_cust_id(instance,sender,*args,**kwargs):
    # print(instance.company_code)
    def Letters(*args, **kwargs):
        string = instance.company_code[0:2]
        for i in range(len(instance.company_code)):
            if instance.company_code[i] == ' ':
                if len(string) == 4:
                    break
                else:
                    string += instance.company_code[i+1:i+3]
        # print(self.string)
        return str(string)   

    

    instance.customer_id = Letters() + autoinc()

    
pre_save.connect(pre_save_cust_id,sender=Customer)


class Vendor(models.Model):

    

    first_name         = models.CharField(max_length=150, blank=False, null=True)
    last_name          = models.CharField(max_length=150, blank=False, null=True)
    email_id           = models.CharField(max_length=150, blank=False, null=True)
    govt_id            = models.CharField(max_length=150, blank=False, choices=govId_choices,null=True)
    id_no              = models.CharField(verbose_name='',max_length=150, blank=False, unique = True, null=True)
    p_id1              = models.CharField(verbose_name='PersonalID',max_length=150, blank=False, null=True) # type of id
    p_id_link          = models.CharField(verbose_name='',max_length=500, blank=False, null=True, unique=True)                      #link of pid
    contact            = models.CharField(verbose_name='PhoneNo.',max_length=20,blank=False, null=True)
    address_1          = models.CharField(max_length=150, blank=False, null=True)
    address_2          = models.CharField(max_length=150, blank=False, null=True)
    city               = models.CharField(max_length=150, blank=False, null=True)
    state              = models.CharField(max_length=150, blank=False, null=True)
    country            = models.CharField(max_length=150, blank=False, null=True)
    zip_code           = models.CharField(max_length=150, blank=False, null=True) 
    company_Name       = models.CharField(max_length=150, blank=False, null=True) 
    company_Address1   = models.CharField(max_length=150, blank=False, null=True) 
    company_Address2   = models.CharField(max_length=150, blank=False, null=True) 
    company_Phone      = models.CharField(max_length=150, blank=False, null=True) 
    company_EmailId    = models.CharField(max_length=150, blank=False, null=True) 

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'vendor'



class Company(models.Model):

    company_Name       = models.CharField(max_length=150, blank=False, null=True) 
    company_Address1   = models.CharField(max_length=150, blank=False, null=True) 
    company_Address2   = models.CharField(max_length=150, blank=False, null=True) 
    city               = models.CharField(max_length=150, blank=False, null=True) 
    zip_code           = models.CharField(max_length=150, blank=False, null=True) 
    country            = models.CharField(max_length=150, blank=False, null=True) 
    company_Phone      = models.CharField(max_length=150, blank=False, null=True) 
    company_EmailId    = models.CharField(max_length=150, blank=False, null=True) 

    def __str__(self):
        return self.company_Name

    class Meta:
        verbose_name_plural = 'company'
    





