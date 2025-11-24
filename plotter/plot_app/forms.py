from django import forms
from .models import Plot

class PlotForm(forms.ModelForm):
    csv_file = forms.FileField(
        required=False,
        help_text="Upload a CSV file (two columns: X and Y values)",
        widget=forms.ClearableFileInput(attrs={'accept': '.csv'})
    )
    has_header = forms.BooleanField(
        required=False,
        initial=True,
        label="CSV has header row"
    )
    
    class Meta:
        model = Plot
        fields = ['title', 'x_label', 'y_label', 'plot_type', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional notes about this plot...'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Enter plot title'})
        self.fields['x_label'].widget.attrs.update({'placeholder': 'X-axis label'})
        self.fields['y_label'].widget.attrs.update({'placeholder': 'Y-axis label'})