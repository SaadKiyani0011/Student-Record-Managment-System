from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        program = self.request.GET.get('program')
        search = self.request.GET.get('search')
        
        if program:
            queryset = queryset.filter(program=program)
        if search:
            queryset = queryset.filter(full_name__icontains=search)
            
        return queryset.order_by('-created_at')

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'
    success_url = reverse_lazy('S_list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'edit_student.html'
    success_url = reverse_lazy('S_list')

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('S_list')
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

def student_list(request):
    students = Student.objects.all()
    program_filter = request.GET.get('program', '')
    search_query = request.GET.get('search', '')
    
    if program_filter:
        students = students.filter(program=program_filter)
    if search_query:
        students = students.filter(full_name__icontains=search_query)
    
    context = {
        'students': students,
        'program_filter': program_filter,
        'search_query': search_query,
    }
    return render(request, 'student_list.html', context)