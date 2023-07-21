from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import *



class MemberAdmin(ImportExportModelAdmin):
    list_display = ("id", "first_name","last_name", "ward_id", "default_group_id")
    pass
admin.site.register(Member, MemberAdmin)


class GroupAdmin(ImportExportModelAdmin):
    list_display = ("id", "name","special_code", "ward_id")
    pass
admin.site.register(Group, GroupAdmin)

class CountyAdmin(ImportExportModelAdmin):
    list_display = ("id", "name","code")
    pass
admin.site.register(County, CountyAdmin)

class SubCountyAdmin(ImportExportModelAdmin):
    list_display = ("id", "name","code")
    pass
admin.site.register(SubCounty, SubCountyAdmin)

class WardAdmin(ImportExportModelAdmin):
    list_display = ("id", "name","code")
    pass
admin.site.register(Ward, WardAdmin)



class SavingAdmin(ImportExportModelAdmin):
    list_display = ("id", "member_id","group_id", "amount")
    pass
admin.site.register(Saving, SavingAdmin)


class SavingLogAdmin(ImportExportModelAdmin):
    list_display = ("id", "savings_id","transaction_phone")
    pass
admin.site.register(SavingLog, SavingLogAdmin)

class LoanProductAdmin(ImportExportModelAdmin):
    list_display = ("id", "name","description")
    pass
admin.site.register(LoanProduct, LoanProductAdmin)

class GroupLoanProductAdmin(ImportExportModelAdmin):
    list_display = ("id", "name","group_loan_product_description")
    pass
admin.site.register(GroupLoanProduct, GroupLoanProductAdmin)

class LoanAdmin(ImportExportModelAdmin):
    list_display = ("id", "group_id","group_member_id", "amount", "status")
    pass
admin.site.register(Loan, LoanAdmin)

class LoanRepaymentAdmin(ImportExportModelAdmin):
    list_display = ("id", "loan_id","amount", "payment_type")
    pass
admin.site.register(LoanRepayment, LoanRepaymentAdmin)

class PenaltyAdmin(ImportExportModelAdmin):
    list_display = ("id", "member_id","purpose", "amount")
    pass
admin.site.register(Penalty, PenaltyAdmin)

class GroupAnnouncementAdmin(ImportExportModelAdmin):
    list_display = ("id", "group_id", "announce_at","message")
    pass
admin.site.register(GroupAnnouncement, GroupAnnouncementAdmin)



class LoanReminderAdmin(ImportExportModelAdmin):
    list_display = ("id", "group_id","phone", "message")
    pass
admin.site.register(LoanReminder, LoanReminderAdmin)


class VendorAdmin(ImportExportModelAdmin):
    list_display = ("id", "business_name","ward_id")
    pass
admin.site.register(Vendor, VendorAdmin)


class ProductAdmin(ImportExportModelAdmin):
    list_display = ("id", "vendor_id","name", "category", "retail_price", "wholesale_price")
    pass
admin.site.register(Product, ProductAdmin)


class GroupUserAdmin(ImportExportModelAdmin):
    list_display = ("id", "group_id", "first_name","email")
    pass
admin.site.register(GroupUser, GroupUserAdmin)





class AdminAdmin(ImportExportModelAdmin):
    list_display = ("id", "first_name","email")
    pass
admin.site.register(Admin, AdminAdmin)


class EmailAdmin(ImportExportModelAdmin):
    list_display = ("id", "email_address","subject")
    pass
admin.site.register(Email, EmailAdmin)

