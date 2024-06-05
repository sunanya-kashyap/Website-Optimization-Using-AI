from django import forms
from .models import Website, File, OptimizedFile, Log, Feedback, Report, Contact

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['name', 'zip_file']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file', 'size', 'file_type', 'website']

class OptimizedFileForm(forms.ModelForm):
    class Meta:
        model = OptimizedFile
        fields = ['original_file', 'optimized_file']

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['optimized_file', 'message']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['optimized_file', 'message']

class ReportForm(forms.ModelForm):                                                                                       
    class Meta:
        model = Report
        fields = ['optimized_file', 'content']
        
class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']