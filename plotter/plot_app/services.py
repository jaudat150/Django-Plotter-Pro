import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import pandas as pd
from django.core.files.base import ContentFile

def generate_plot(plot_instance):
    """Generate plot image and save to model instance"""
    plt.figure(figsize=(10, 6))
    
    x = plot_instance.x_values
    y = plot_instance.y_values
    
    if plot_instance.plot_type == 'line':
        plt.plot(x, y, marker='o', linestyle='-', color='#1f77b4', linewidth=2, markersize=8)
    elif plot_instance.plot_type == 'scatter':
        plt.scatter(x, y, color='#ff7f0e', s=100, alpha=0.7, edgecolors='w', linewidth=1)
    elif plot_instance.plot_type == 'bar':
        plt.bar(x, y, color='#2ca02c', edgecolor='white', linewidth=1.5, alpha=0.8)
    
    plt.title(plot_instance.title, fontsize=16, pad=20)
    plt.xlabel(plot_instance.x_label, fontsize=12, labelpad=10)
    plt.ylabel(plot_instance.y_label, fontsize=12, labelpad=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    
    # Improve layout
    plt.tight_layout()
    
    # Save to buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    plt.close()
    
    # Save to model
    filename = f"plot_{plot_instance.id}_{plot_instance.created_at.strftime('%Y%m%d_%H%M%S')}.png"
    plot_instance.image.save(filename, ContentFile(buffer.getvalue()))
    buffer.close()
    
    return plot_instance

def parse_csv(file, has_header=True):
    """Parse CSV file and return x and y values"""
    try:
        df = pd.read_csv(file, header=0 if has_header else None)
        if df.shape[1] < 2:
            raise ValueError("CSV must have at least two columns")
        
        # Use first two columns
        x_col = df.columns[0]
        y_col = df.columns[1]
        
        x_values = df[x_col].tolist()
        y_values = df[y_col].tolist()
        
        # Validate data
        if len(x_values) != len(y_values):
            raise ValueError("X and Y columns must have the same number of values")
        
        # Convert to strings for storage
        x_str = ','.join(str(val) for val in x_values)
        y_str = ','.join(str(val) for val in y_values)
        
        return x_str, y_str
    except Exception as e:
        raise ValueError(f"Error parsing CSV: {str(e)}")