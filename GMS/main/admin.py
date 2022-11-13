# GYM MANAGEMENT SYSTEM BY PEACE OLORUNTOBA C.E.O. PEASCAINC
# You can contact me on gmail @ profprincepeace@gmail.com or peascainc@gmail.com
# You can also call me or whatsapp me on +2348166846226

from django.contrib import admin
from . import models

# Register your models here.

# Admin Banner
class BannerAdmin(admin.ModelAdmin):
	list_display=('alt_text','image_tag')
admin.site.register(models.Banners,BannerAdmin)

# Admin Service
class ServiceAdmin(admin.ModelAdmin):
	list_display=('title','image_tag')
admin.site.register(models.Service,ServiceAdmin)

# Admin Page
class PageAdmin(admin.ModelAdmin):
	list_display=('title',)
admin.site.register(models.Page,PageAdmin)

# Admin FAQ
class FaqAdmin(admin.ModelAdmin):
	list_display=('quest',)
admin.site.register(models.Faq,FaqAdmin)

# Admin Enquiry
class EnquiryAdmin(admin.ModelAdmin):
	list_display=('full_name','email','detail','send_time')
admin.site.register(models.Enquiry,EnquiryAdmin)

# Admin Gallery
class GalleryAdmin(admin.ModelAdmin):
	list_display=('title','image_tag')
admin.site.register(models.Gallery,GalleryAdmin)

# Admin Gallery Image
class GalleryImageAdmin(admin.ModelAdmin):
	list_display=('alt_text','image_tag')
admin.site.register(models.GalleryImage,GalleryImageAdmin)

# Admin Subscription Plan
class SubPlanAdmin(admin.ModelAdmin):
	list_editable=('highlight_status','max_member')
	list_display=('title','price','max_member','validity_days','highlight_status')
admin.site.register(models.SubPlan,SubPlanAdmin)

# Admin Subcription Plan Features
class SubPlanFeatureAdmin(admin.ModelAdmin):
	list_display=('title','subplans')
	def subplans(self,obj):
		return " | ".join([sub.title for sub in obj.subplan.all()])
admin.site.register(models.SubPlanFeature,SubPlanFeatureAdmin)

# Admin Plan Discount
class PlanDiscountAdmin(admin.ModelAdmin):
	list_display=('subplan','total_months','total_discount')
admin.site.register(models.PlanDiscount,PlanDiscountAdmin)

# Admin Subscriber
class SubscriberAdmin(admin.ModelAdmin):
	list_display=('user','image_tag','mobile')
admin.site.register(models.Subscriber,SubscriberAdmin)

# Admin Subscription
class SubscriptionAdmin(admin.ModelAdmin):
	list_display=('user','plan','reg_date','price')
admin.site.register(models.Subscription,SubscriptionAdmin)

# Admin Trainer
class TrainerAdmin(admin.ModelAdmin):
	list_editable=('is_active',)
	list_display=('full_name','mobile','salary','is_active','image_tag')
admin.site.register(models.Trainer,TrainerAdmin)

# Admin Notify
class NotifyAdmin(admin.ModelAdmin):
	list_display=('notify_detail','read_by_user','read_by_trainer')
admin.site.register(models.Notify,NotifyAdmin)

# Admin Notification User Status
class NotifUserStatusAdmin(admin.ModelAdmin):
	list_display=('notif','user','status')
admin.site.register(models.NotifUserStatus,NotifUserStatusAdmin)

# Admin Subscriber (Select)
class AssignSubscriberAdmin(admin.ModelAdmin):
	list_display=('trainer','user')
admin.site.register(models.AssignSubscriber,AssignSubscriberAdmin)

# Admin Trainer Achievement
class TrainerAchivementAdmin(admin.ModelAdmin):
	list_display=('title','image_tag')
admin.site.register(models.TrainerAchivement,TrainerAchivementAdmin)

# Admin Trainer Salary
class TrainerSalaryAdmin(admin.ModelAdmin):
	list_display=('trainer','amt','amt_date')
admin.site.register(models.TrainerSalary,TrainerSalaryAdmin)

# Admin Trainer Notification
class TrainerNotificationAdmin(admin.ModelAdmin):
	list_display=('notif_msg',)
admin.site.register(models.TrainerNotification,TrainerNotificationAdmin)

# Admin Trainer Notification Status
class TrainerNotificationStatusAdmin(admin.ModelAdmin):
	list_display=('notif',)
admin.site.register(models.NotifTrainerStatus,TrainerNotificationStatusAdmin)

# Admin Trainer Message
class TrainerMsgAdmin(admin.ModelAdmin):
	list_display=('user','trainer','message')
admin.site.register(models.TrainerMsg,TrainerMsgAdmin)

# Admin Report For user
class TrainerSubscriberReportAdmin(admin.ModelAdmin):
	list_display=('report_msg','report_for_trainer','report_for_user','report_from_trainer','report_from_user')
admin.site.register(models.TrainerSubscriberReport,TrainerSubscriberReportAdmin)

# Admin App Setting
class AppSettingAdmin(admin.ModelAdmin):
	list_display=('image_tag',)
admin.site.register(models.AppSetting,AppSettingAdmin)