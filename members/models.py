from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator
length= 255

class County(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True) 
  code = models.CharField(max_length=3, null=True) 
  def __str__(self):
        return str(self.name)
      

class SubCounty(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    county_id = models.ForeignKey('County', on_delete=models.CASCADE)
    name = models.CharField(max_length=length, blank=True, null=True,)
    lat = models.CharField(max_length=length, blank=True, null=True,)
    lng = models.CharField(max_length=length, blank=True, null=True,)
    category = models.CharField(max_length=length, blank=True, null=True,)
    code = models.CharField(max_length=length, blank=True, null=True,)
    loccode = models.CharField(max_length=length, blank=True, null=True,)

    def __str__(self):
        return '%s' % self.name


class Ward(models.Model):
    county_id = models.ForeignKey('County', on_delete=models.CASCADE)
    subcounty_id = models.ForeignKey('SubCounty', on_delete=models.CASCADE)
    name = models.CharField(max_length=length, blank=True, null=True,)
    lat = models.CharField(max_length=length, blank=True, null=True,)
    lng = models.CharField(max_length=length, blank=True, null=True,)
    category = models.CharField(max_length=length, blank=True, null=True,)
    code = models.CharField(max_length=length, blank=True, null=True,)
    loccode = models.CharField(max_length=length, blank=True, null=True,)

    def __str__(self):
        return '%s' % self.name


class Group(models.Model):
    name = models.CharField(max_length=length,null=True, blank=True, unique=True)
    special_code = models.CharField(max_length=4,null=True, blank=True)
    group_type = models.CharField(max_length=length,null=True, blank=True)
    ward_id = models.ForeignKey(Ward, on_delete=models.CASCADE,null=True, blank=True)
    business_activity = models.CharField(max_length=length,null=True, blank=True)
    bank_name = models.CharField(max_length=length,null=True, blank=True)
    bank_services = models.CharField(max_length=length,null=True, blank=True)
    mpesa_paybill = models.CharField(max_length=length,null=True, blank=True)
    mpesa_busines_number = models.CharField(max_length=length,null=True, blank=True)
    mpesa_account_number = models.CharField(max_length=length,null=True, blank=True)
    chairperson_name = models.CharField(max_length=length,null=True, blank=True)
    chairperson_phone_number = models.CharField(max_length=length,null=True, blank=True)
    secretary_name = models.CharField(max_length=length,null=True, blank=True)
    secretary_phone = models.CharField(max_length=length,null=True, blank=True)
    opportunity = models.CharField(max_length=length,null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s' % self.name


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=length,null=True, blank=True)
    last_name = models.CharField(max_length=length,null=True, blank=True)
    physical_address = models.TextField(max_length=length,null=True, blank=True)
    national_id = models.CharField(max_length=length,null=True, blank=True)
    primary_phone_number = models.CharField(max_length=length,null=True, blank=True)
    primary_phone_number_provider = models.CharField(max_length=length,null=True, blank=True)
    alternative_phone_number = models.CharField(max_length=length,null=True, blank=True)
    alternative_phone_number_provider = models.CharField(max_length=length,null=True, blank=True)
    year_of_birth = models.CharField(max_length=4,null=True, blank=True)
    gender = models.CharField(max_length=10,null=True, blank=True)
    ward_id = models.ForeignKey(Ward, on_delete=models.CASCADE,null=True, blank=True)
    default_group_id = models.ForeignKey(Group, on_delete=models.CASCADE,null=True, blank=True)
    profile_img = models.ImageField(upload_to='Profile', default='default.png',null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.user.username    #i use this function because i dont use null =True in user -everytime i need this
	

    class Meta:
        verbose_name_plural ='Member'
        db_table = 'tbl_members'
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        
    @receiver(post_save, sender = User)
    def update_profile(sender,instance,created,*args,**kwargs):
        if created:
            Member.objects.create(user=instance)
            instance.profile.save()
			




class Saving(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE,null=True, blank=True)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE,null=True, blank=True)
    amount = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(999999999.0)], default=0.0)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.create_at)


class SavingLog(models.Model):
    savings_id = models.ForeignKey(Saving, on_delete=models.CASCADE,null=True, blank=True)
    amount = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(999999999.0)], default=0.0)
    transaction_phone = models.CharField(max_length=length,null=True, blank=True)
    transaction_id = models.CharField(max_length=length,null=True, blank=True)
    log_type = models.CharField(max_length=length,null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s' % self.transaction_phone

class LoanProduct(models.Model):
    name = models.CharField(max_length=length,null=True, blank=True)
    description =  models.TextField(null=True, blank=True)
    loan_duration_days = models.IntegerField(null=True, blank=True)
    penalty_rate = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(99.9)], default=0.0)
    interest_rate = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(99.9)], default=0.0)
    product_type = models.CharField(max_length=length,null=True, blank=True)
    borrowing_percentage = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(99.9)], default=0.0)
    borrowing_times = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s' % self.name


class GroupLoanProduct(models.Model):
    #group_id = models.ForeignKey(Group, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=length,null=True, blank=True)
    group_loan_product_id = models.ForeignKey(LoanProduct, on_delete=models.CASCADE,null=True, blank=True)
    group_loan_product_name = models.CharField(max_length=length,null=True, blank=True)
    group_loan_product_description = models.TextField(null=True, blank=True)
    group_loan_product_duration_days = models.IntegerField(null=True, blank=True)
    group_loan_product_penalty_rate = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(99.9)], default=0.0)
    group_loan_product_interest_rate = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(99.9)], default=0.0)
    group_loan_product_type = models.CharField(max_length=length,null=True, blank=True)
    group_loan_product_borrowing_percentage = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(99.9)], default=0.0)
    group_loan_product_borrowing_times = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s' % self.loan_product_name


class Loan(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE,null=True, blank=True)
    group_member_id =models.ForeignKey(Member, on_delete=models.CASCADE,null=True, blank=True)
    loan_product_id = models.ForeignKey(LoanProduct, on_delete=models.CASCADE,null=True, blank=True)
    amount = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(999999999.9)], default=0.0)
    amount_due = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(999999999.9)], default=0.0)
    duration_days = models.IntegerField(null=True, blank=True)
    penalty_rate = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(99.9)], default=0.0)
    interest = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(99.9)], default=0.0)
    interest_rate = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(99.9)], default=0.0)
    loan_type = models.CharField(max_length=length,null=True, blank=True)
    borrowing_percentage = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(99.9)], default=0.0)
    borrowing_times = models.IntegerField(null=True, blank=True)
    approved_date = models.CharField(max_length=length,null=True, blank=True)
    due_date = models.CharField(max_length=length,null=True, blank=True)
    purpose = models.CharField(max_length=length,null=True, blank=True)
    status = models.CharField(max_length=length,null=True, blank=True, default="ACTIVE")
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s' % self.loan_type



class LoanRepayment(models.Model):
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE,null=True, blank=True)
    amount = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(999999999.9)], default=0.0)
    payment_type = models.CharField(max_length=length,null=True, blank=True)
    transaction_code = models.CharField(max_length=length,null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s' % self.loan_id


class Penalty(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE,null=True, blank=True)
    purpose = models.CharField(max_length=length,null=True, blank=True)
    amount = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(999999999.9)], default=0.0)
    status = models.CharField(max_length=length,null=True, blank=True, default="ACTIVE")
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s' % self.member_id


class GroupUser(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE,null=True, blank=True)
    first_name = models.CharField(max_length=length,null=True, blank=True)
    last_name = models.CharField(max_length=length,null=True, blank=True)
    email = models.CharField(max_length=length,null=True, blank=True)
    password = models.CharField(max_length=length,null=True, blank=True)
    phone = models.CharField(max_length=length,null=True, blank=True)
    api_key = models.CharField(max_length=length,null=True, blank=True)
    active = models.CharField(max_length=length,null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s' % self.email
    

class Admin(models.Model):
    first_name = models.CharField(max_length=length,null=True, blank=True)
    last_name = models.CharField(max_length=length,null=True, blank=True)
    email = models.CharField(max_length=length,null=True, blank=True)
    password = models.CharField(max_length=length,null=True, blank=True)
    phone = models.CharField(max_length=length,null=True, blank=True)
    api_key = models.CharField(max_length=length,null=True, blank=True)
    active = models.CharField(max_length=length,null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s' % self.email


class Email(models.Model):
    email_address =models.CharField(max_length=length,null=True, blank=True)
    subject = models.CharField(max_length=length,null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    sent = models.CharField(max_length=length,null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s' % self.email_address


class GroupAnnouncement(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE,null=True, blank=True)
    announce_at = models.DateField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    announced = models.CharField(max_length=length,null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s' % self.message


class LoanReminder(models.Model):
    group_id = models.ForeignKey(GroupAnnouncement, on_delete=models.CASCADE,null=True, blank=True)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE,null=True, blank=True)
    phone = models.CharField(max_length=length,null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    send_at = models.DateTimeField(null=True, blank=True)
    sent = models.CharField(max_length=10,null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s' % self.phone




class Vendor(models.Model):
    ward_id = models.ForeignKey(Ward, on_delete=models.CASCADE,null=True, blank=True)
    business_name = models.CharField(max_length=length,null=True, blank=True)
    shopping_centre_name = models.CharField(max_length=length,null=True, blank=True)
    contact_person_name = models.CharField(max_length=length,null=True, blank=True)
    contact_person_phone = models.CharField(max_length=length,null=True, blank=True)
    contact_person_password = models.CharField(max_length=length,null=True, blank=True)
    api_key = models.CharField(max_length=length,null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return '%s' % self.business_name


class Product(models.Model):
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=length,null=True, blank=True)
    category = models.CharField(max_length=length,null=True, blank=True)
    retail_price = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(99999999.9)], default=0.0)
    wholesale_price = models.FloatField( validators=[MinValueValidator(0.0), MaxValueValidator(999999999.9)], default=0.0)
    photo = models.ImageField(upload_to='Products', default='default.png',null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s' % self.name