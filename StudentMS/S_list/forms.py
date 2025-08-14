from django import forms
from .models import Student
from django.core.validators import MinValueValidator, MaxValueValidator

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'admission_date': forms.DateInput(attrs={'type': 'date'}),
            'gpa': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '4'}),
        }
        labels = {
            'full_name': 'Full Name',
            'roll_number': 'Roll Number',
        }
    
    def clean_roll_number(self):
        roll_number = self.cleaned_data['roll_number']
        if not any(program in roll_number for program in dict(Student.PROGRAM_CHOICES).keys()):
            raise forms.ValidationError("Roll number should contain program code (e.g., BSCS-001)")
        return roll_number