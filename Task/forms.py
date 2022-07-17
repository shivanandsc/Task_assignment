from django import forms  
from Task.models import UserTask  
  
class TaskForm(forms.ModelForm):  
    class Meta:  
        model = UserTask  
        fields = ['task_name', 'department', 'assign_to','task_description']

