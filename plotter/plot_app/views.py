from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse, FileResponse
from django.contrib import messages
from .models import Plot
from .forms import PlotForm
from .services import generate_plot, parse_csv
import os,re

class PlotCreateView(View):
    template_name = 'plot_app/index.html'
    
    def get(self, request):
        form = PlotForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = PlotForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                plot = form.save(commit=False)
                plot.notes = form.cleaned_data.get('notes', '')
                
                # Handle CSV upload
                csv_file = request.FILES.get('csv_file')
                if csv_file:
                    has_header = request.POST.get('has_header') == 'on'
                    x_data, y_data = parse_csv(csv_file, has_header)
                    plot.x_data = x_data
                    plot.y_data = y_data
                    plot.csv_file = csv_file
                else:
                    # Enhanced manual data processing
                    x_data = request.POST.get('x_data', '').strip()
                    y_data = request.POST.get('y_data', '').strip()
                    
                    if not x_data or not y_data:
                        messages.error(request, "❌ Please provide X and Y values or upload a CSV file")
                        return render(request, self.template_name, {'form': form})
                    
                    # Clean and validate the data
                    try:
                        # Replace spaces with commas and clean up
                        x_clean = ','.join([val.strip() for val in re.split(r'[\s,]+', x_data) if val.strip()])
                        y_clean = ','.join([val.strip() for val in re.split(r'[\s,]+', y_data) if val.strip()])
                        
                        # Convert to numbers to validate
                        x_values = [float(val) for val in x_clean.split(',') if val.strip()]
                        y_values = [float(val) for val in y_clean.split(',') if val.strip()]
                        
                        if len(x_values) != len(y_values):
                            messages.error(request, f"❌ Data length mismatch! X has {len(x_values)} values, Y has {len(y_values)} values")
                            return render(request, self.template_name, {'form': form})
                        
                        plot.x_data = x_clean
                        plot.y_data = y_clean
                    except ValueError as e:
                        messages.error(request, f"❌ Invalid data format: {str(e)}")
                        return render(request, self.template_name, {'form': form})
                
                plot.save()
                generate_plot(plot)
                
                messages.success(request, f"✅ Plot created successfully! ID: #{plot.id}")
                return redirect('plot_detail', pk=plot.id)
                
            except Exception as e:
                messages.error(request, f"❌ Error creating plot: {str(e)}")
                return render(request, self.template_name, {'form': form})
        
        messages.error(request, "❌ Please correct the form errors below")
        return render(request, self.template_name, {'form': form})
class PlotDetailView(View):
    template_name = 'plot_app/plot_detail.html'
    
    def get(self, request, pk):
        plot = get_object_or_404(Plot, pk=pk)
        return render(request, self.template_name, {'plot': plot})

class PlotDownloadView(View):
    def get(self, request, pk):
        plot = get_object_or_404(Plot, pk=pk)
        file_path = plot.image.path
        
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="image/png")
                response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
                return response
        return HttpResponse("File not found", status=404)

class SavedPlotsView(View):
    template_name = 'plot_app/saved_plots.html'
    
    def get(self, request):
        plots = Plot.objects.all()
        return render(request, self.template_name, {'plots': plots})