
from django.db import models

# Create your models here.
class Patient(models.Model):
    MRN = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    ID_number = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=[('male', 'male'), ('female', 'female')])
    Nationality = models.CharField(max_length=10, choices=[('Saudi', 'Saudi'), ('non-Saudi', 'non-Saudi')])
    def __str__(self):
        return self.name



class TestRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='test_requests')
    Unit_name = models.CharField(max_length=255, choices=[
        ('ER', 'ER'), ('pedia_ward', 'pedia_ward'), ('male_ward', 'male_ward'), ('female_ward', 'female_ward'), ('OB_ward', 'OB_ward'), ('L&D_ward', 'L&D_ward'), ('covid_ward', 'covid_ward'), ('OPD', 'OPD'), ('refferal', 'referral')
    ])
    status = models.CharField(max_length=255, choices=[
        ('emergency/immediatly', 'emergency/immediatly'), ('urgent/24hrs', 'urgent/24hrs'), ('routine/ 48 hours', 'routine/ 48 hours')
    ])
    infectious_disease = models.CharField(max_length=3, choices=[('yes', 'yes'), ('no', 'no')])
    way_of_transport = models.CharField(max_length=255, choices=[('walking', 'walking'),
                                                                 ('wheelchair', 'wheelchair'),
                                                                 ('trolley', 'trolley')])
    is_new_request = models.CharField(max_length=255, choices=[("new", "New Request"), ("followup", "Follow Up")],default='new')
    modalities = models.CharField(max_length=255, choices=[
        ('CT', 'CT'), ('US', 'US'), ('X_ray', 'X_ray'), ('MRI', 'MRI'),
        ('Mammography', 'Mammography'), ('Angiogram.', 'Angiogram.'), 
        ('Interventional radiological procedures', 'Interventional radiological procedures'), 
        ('Fluoroscopy', 'Fluoroscopy'), ('Nuclear medicine imaging', 'Nuclear medicine imaging'),
        ('Molecular Imaging /Positron Emission Tomography /PET scanning', 
         'Molecular Imaging /Positron Emission Tomography /PET scanning'),
        ('Bedside /critical care radiography', 'Bedside /critical care radiography'), 
        ('Portable radiological machines', 'Portable radiological machines')
    ])
    study_part = models.CharField(max_length=255, choices=[
        ('Abdomen', 'Abdomen'), ('KUB', 'KUB'), ('OB less than 14 Weeks', 'OB less than 14 Weeks '),
        ('OB more than 14 Weeks', 'OB more than 14 Weeks '), ('Brain', 'Brain'), ('Neck', 'Neck'),
        ('Chest', 'Chest'), ('pelvis', 'pelvis'), ('pan-CT', 'pan-CT'), ('thyroid', 'thyroid'), 
        ('breast', 'breast'), ('scrotal', 'scrotal'), ('cervical spine', 'cervical spine'), 
        ('L/S spine', 'L/S spine'), ('D/L spine', 'D/L spine'), ('doppler-venous-lower', 'doppler-venous-lower'), 
        ('doppler-arterial-lower', 'doppler-arterial-lower'), ('doppler-venous-upper', 'doppler-venous-upper'), 
        ('doppler-arterial-upper', 'doppler-arterial-upper'), ('all spine', 'all spine'), ('Shoulder', 'Shoulder'),
        ('elbow', 'elbow'), ('wrist', 'wrist'), ('hand', 'hand'), ('hip', 'hip'), ('knee', 'knee'), 
        ('ankle', 'ankle'), ('foot', 'foot'), ('other-study', 'other-study')
])

    side_label = models.CharField(max_length=255, choices=[('right', 'right'), ('left', 'left'), ('none', 'none')])
    other_test = models.CharField(max_length=255, blank=True, null=True)
    need_contrast = models.CharField(max_length=3, choices=[('yes', 'yes'), ('no', 'no')])
    contrast_specification = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        choices=[("oral", "Oral"), ("iv", "IV Contrast"), ("oral_iv", "Oral and IV Contrast")]
    )

    allergies = models.CharField(max_length=255, choices=[('yes', 'yes'), ('no', 'no')])
    allergy_specification = models.CharField(max_length=255, blank=True, null=True)
    physician = models.CharField(max_length=255)
    technician = models.CharField(max_length=255)
    radiologist = models.CharField(max_length=255)
    def __str__(self):
            return self.name
