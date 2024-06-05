from django.db import models

# Create your models here.
from django.db import models

class Website(models.Model):
    name = models.CharField(max_length=200)
    zip_file = models.FileField(upload_to='zip_files/', blank=True, null=True)
    optimization_status = models.CharField(max_length=200, default='Not started')
    last_optimization_result = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    from django.db import models

class File(models.Model):
    file = models.FileField(upload_to='files/', blank=True, null=True)
    size = models.IntegerField(default=0)
    file_type = models.CharField(max_length=200)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.url

from django.db import models

class OptimizedFile(models.Model):
    original_file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='original_files')
    optimized_file = models.FileField(upload_to='optimized_files/')
    optimization_result = models.TextField(blank=True)

    def __str__(self):
        return self.original_file.name
    
    from django.db import models

class Log(models.Model):
    optimized_file = models.ForeignKey(OptimizedFile, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Log for {self.optimized_file.original_file.name} at {self.timestamp}'
    
    from django.db import models

class Feedback(models.Model):
    optimized_file = models.ForeignKey(OptimizedFile, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback for {self.optimized_file.original_file.name} at {self.timestamp}'
    
    from django.db import models

class Report(models.Model):
    optimized_file = models.ForeignKey(OptimizedFile, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Report for {self.optimized_file.original_file.name} at {self.timestamp}'

class Contact(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def str(self):
        return self.name
    
class DownloadFile(models.Model):
    file = models.FileField(upload_to='downloads/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name