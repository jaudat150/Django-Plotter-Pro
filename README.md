# Django Plotter Pro

A powerful Django application for creating, managing, and downloading data visualizations from manual input or CSV files.

---

 ✨ Features

- Multiple Plot Types: Line, scatter, and bar charts  
- Flexible Data Input:
  - Manual data entry with real-time validation
  - CSV uploads with automatic header detection
  - Sample data generators (linear, quadratic, sinusoidal, random)
- Data Management:
  - Save plots to database with metadata
  - View plot history with thumbnails
  - Download plots as PNG
  - Export original CSV data
- User Experience:
  - Responsive Bootstrap 5 UI
  - Tab-based workflow
  - Real-time validation & comprehensive error handling
- Admin Integration: Full CRUD management via Django admin

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- `pip`
- Virtual environment (recommended)

### Steps

1. Clone the repository
   ```bash
   git clone https://github.com/jaudat150/django-plotter-pro.git
   cd django-plotter-pro
   ```

2. Create & activate virtual environment

   Windows (PowerShell):
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

   macOS / Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations & create superuser
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. Create required directories

   Windows (PowerShell):
   ```powershell
   mkdir static, media, staticfiles
   ```

   macOS / Linux:
   ```bash
   mkdir -p static media staticfiles
   ```

6. Collect static files
   ```bash
   python manage.py collectstatic --noinput
   ```

7. Start the development server
   ```bash
   python manage.py runserver
   ```

8. Access the application
   - Main app: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
   - Admin interface: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## ⚙️ Configuration

Create a `.env` file in the project root:

```env
SECRET_KEY=your_strong_secret_key_here
DEBUG=True
ALLOWED_HOSTS=.localhost,127.0.0.1,[::1]
```

> 🔐 Never commit `.env` — it should be excluded via `.gitignore`.

💡 To generate a strong `SECRET_KEY`:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

---

## 📊 Usage Guide

### Creating a Plot
1. Navigate to the homepage (`/`)
2. Choose input method:
   - Manual Entry: Enter X and Y values (comma- or space-separated)
   - CSV Upload: Upload a CSV file with two numeric columns
3. Configure:
   - Title & axis labels
   - Plot type (line / scatter / bar)
   - Optional notes
4. Click "Generate Plot"

### Managing Plots
- Gallery: View all saved plots with thumbnails and metadata  
- Plot Detail Page: Click any plot to:
  - View full-size visualization
  - Download as PNG
  - Export original data as CSV
- Admin Interface (`/admin`): Full management — edit, delete, search, export plots

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository  
2. Create your feature branch:  
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:  
   ```bash
   git commit -m 'Add AmazingFeature'
   ```
4. Push to the branch:  
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

### Guidelines
- Write clear, imperative commit messages  
- Follow [PEP 8](https://pep8.org/)  
- Add tests for new functionality  
- Update documentation (including this README) when needed

---

## 📜 License

Distributed under the MIT License.  
© 2025 [Jawdat Al-Husien](mailto:jaudat02@gmail.com)  
See [`LICENSE`](LICENSE) for full details.

---

## 📬 Contact

- 🐙 Project: [https://github.com/jaudat150/django-plotter-pro](https://github.com/jaudat150/django-plotter-pro)  
- 🐞 Issues & Requests: [https://github.com/jaudat150/django-plotter-pro/issues](https://github.com/jaudat150/django-plotter-pro/issues)  
- ✉️ Email: [jaudat02@gmail.com](mailto:jaudat02@gmail.com)
```
