from django.db import models
from django.utils import timezone

class Plot(models.Model):
    PLOT_TYPES = [
        ('line', 'Line Plot'),
        ('scatter', 'Scatter Plot'),
        ('bar', 'Bar Chart'),
    ]
    
    title = models.CharField(max_length=255, default='Untitled Plot')
    x_label = models.CharField(max_length=100, default='X Values')
    y_label = models.CharField(max_length=100, default='Y Values')
    plot_type = models.CharField(max_length=10, choices=PLOT_TYPES, default='line')
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='plots/')
    csv_file = models.FileField(upload_to='csv_files/', null=True, blank=True)
    x_data = models.TextField(help_text='Comma-separated X values')
    y_data = models.TextField(help_text='Comma-separated Y values')
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} ({self.get_plot_type_display()})"
    
    @property
    def x_values(self):
        return [float(x.strip()) for x in self.x_data.split(',') if x.strip()]
    
    @property
    def y_values(self):
        return [float(y.strip()) for y in self.y_data.split(',') if y.strip()]