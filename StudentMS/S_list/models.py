from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Student(models.Model):
    PROGRAM_CHOICES = [
        ('BSCS', 'Bachelor of Science in Computer Science'),
        ('BSSE', 'Bachelor of Science in Software Engineering'),
        ('BSIT', 'Bachelor of Science in Information Technology'),
        ('BBA', 'Bachelor of Business Administration'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    
    full_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    program = models.CharField(max_length=10, choices=PROGRAM_CHOICES)
    gpa = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0.0), MaxValueValidator(4.0)]
    )
    admission_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    profile_pic = models.ImageField(
        upload_to='media/student_profile_pics/',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    
    def __str__(self):
        return f"{self.full_name} ({self.roll_number})"
    
    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.pk})
    
    def get_edit_url(self):
        return reverse('S_edit', kwargs={'pk': self.pk})
    
    def get_delete_url(self):
        return reverse('student_delete', kwargs={'pk': self.pk})
    
    @property
    def formatted_admission_date(self):
        return self.admission_date.strftime('%Y-%m-%d')
    
    @property
    def profile_pic_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return f"https://ui-avatars.com/api/?name={self.full_name.replace(' ', '+')}&background=4361ee&color=fff"