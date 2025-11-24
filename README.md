A powerful Django application for creating, managing, and downloading data visualizations from manual input or CSV files.

Features
* Multiple Plot Types: Create line, scatter, and bar charts
* Flexible Data Input:
- Manual data entry with real-time validation
- CSV file uploads with header detection
- Sample data generators (linear, quadratic, sinusoidal, random)
* Data Management:
- Save plots to database with metadata
- View plot history with thumbnails
- Download plots as PNG files
- Export original CSV data
* User Experience:
- Responsive Bootstrap 5 interface
- Tab-based data entry workflow
- Real-time data validation
- Comprehensive error handling
* Admin Integration: Full admin interface for plot management
Installation & Setup
Prerequisites
* Python 3.8+
* pip package manager
* Virtual environment (recommended)
Setup Steps


1) Clone the repository:
git clone https://github.com/yourusername/django-plotter-pro.git
cd django-plotter-pro

2) Create and activate virtual environment:
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

3) Install dependencies:
pip install -r requirements.txt

4) Run migrations and create superuser:
python manage.py migrate
python manage.py createsuperuser

5) Create required directories:
mkdir static media staticfiles

6) Collect static files:
python manage.py collectstatic --noinput

7) Start the development server:
python manage.py runserver

8) Access the application:
Main application: http://127.0.0.1:8000
Admin interface: http://127.0.0.1:8000/admin

Usage Guide
Creating a Plot
1. Navigate to the homepage
2. Choose your data input method:
* Manual Entry: Enter X and Y values directly (comma or space separated)
* CSV Upload: Upload a CSV file with two columns of data
3. Configure plot settings:
* Set title and axis labels
* Select plot type (line, scatter, bar)
* Add optional notes
4. Click "Generate Plot" to create your visualization
Managing Plots
* Saved Plots: View all your plots in the gallery
* Plot Details: Click any plot to see details and download options
* Download: Get PNG versions of your plots
* Admin Panel: Manage all plots through the Django admin interface

Configuration
Create a .env file with these settings:

SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=.localhost,127.0.0.1,[::1]

Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a pull request

Guidelines
* Write clear commit messages
* Follow PEP 8 style guide
* Add tests for new features
* Update documentation for changes
License
Distributed under the MIT License. See LICENSE file for details.

Contact

~ Project Link: https://github.com/jaudat150/django-plotter-pro
~ Issues: https://github.com/jaudat150/django-plotter-pro/issues
~ Creator: Jawdat Al-Husien - jaudat02@gmail.com
