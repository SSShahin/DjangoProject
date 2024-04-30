from django.contrib import admin
from .models import Emp
from .models import Testimonial
from .models import Feedback
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=('name','is_working','emp_id','department','phone')
    list_editable=('is_working','emp_id')
    search_fields=('name','phone',)
    list_filter=('is_working',)

admin.site .register(Emp,EmpAdmin)
admin.site.register(Testimonial)
admin.site.register(Feedback)