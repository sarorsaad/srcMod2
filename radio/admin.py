from django.contrib import admin
from .models import Patient, TestRequest

class TestRequestInline(admin.TabularInline):
    model = TestRequest
    extra = 0
    fields = ('Unit_name', 'status', 'infectious_disease', 'way_of_transport', 'is_new_request', 'modalities', 'study_part')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('MRN', 'name', 'ID_number', 'age', 'gender', 'Nationality')
    search_fields = ('MRN', 'name', 'ID_number')
    list_filter = ('gender', 'Nationality')
    inlines = [TestRequestInline]

@admin.register(TestRequest)
class TestRequestAdmin(admin.ModelAdmin):
    list_display = ('patient', 'Unit_name', 'status', 'infectious_disease', 'way_of_transport', 'is_new_request', 'modalities', 'study_part')
    search_fields = ('patient', 'Unit_name', 'status', 'modalities', 'study_part')
    list_filter = ('status', 'modalities', 'study_part')


#################################################


# from django.contrib import admin
# from .models import Patient, TestRequest

# class TestRequestAdmin(admin.ModelAdmin):
#     list_display = ('patient', 'Unit_name', 'status', 'modalities', 'study_part')
#     search_fields = ('patient__name', 'Unit_name', 'status', 'modalities', 'study_part')
#     list_filter = ('Unit_name', 'status', 'modalities', 'study_part')

# admin.site.register(Patient)
# admin.site.register(TestRequest, TestRequestAdmin)


