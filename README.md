# Django Portfolio Project

A modern, responsive portfolio website built with Django and Tailwind CSS. This project showcases your skills, projects, and professional experience with a clean, professional design.

## Features

- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Modern UI**: Clean, professional design with smooth animations
- **Project Showcase**: Display your projects with detailed information
- **Skills Management**: Organize skills by category with proficiency levels
- **Experience Timeline**: Showcase your work history and education
- **Contact Form**: Functional contact form with email notifications
- **Admin Interface**: Easy content management through Django admin
- **SEO Optimized**: Meta tags and structured data for better search visibility

## User Flow

### Primary User Journey
1. **Landing** → Home page with hero section and featured projects
2. **Discovery** → Browse about page for background and skills
3. **Evaluation** → View detailed project information
4. **Connection** → Contact form or social links

### Secondary User Journey
1. **Direct Navigation** → About page for background info
2. **Project Focus** → Projects page for detailed portfolio
3. **Contact** → Contact page for inquiries

## Quick Start

### Prerequisites
- Python 3.9+
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd idxDjangoProject
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\Activate.ps1
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Populate with sample data**
   ```bash
   python manage.py populate_data
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

8. **Visit your portfolio**
   - Portfolio: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Project Structure

```
idxDjangoProject/
├── idxDjangoProject/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/                 # Portfolio app
│   ├── models.py             # Profile, Skills, Experience
│   ├── views.py              # Home, About views
│   ├── admin.py              # Admin configuration
│   └── management/           # Custom management commands
├── projects/                 # Projects app
│   ├── models.py             # Project, ProjectImage, ProjectFeature
│   ├── views.py              # Project list and detail views
│   └── admin.py              # Admin configuration
├── contact/                  # Contact app
│   ├── models.py             # ContactMessage
│   ├── views.py              # Contact form view
│   ├── forms.py              # Contact form
│   └── admin.py              # Admin configuration
├── templates/                # HTML templates
│   ├── base.html             # Base template
│   ├── portfolio/            # Portfolio templates
│   ├── projects/             # Project templates
│   └── contact/              # Contact templates
├── static/                   # Static files (CSS, JS, images)
├── media/                    # User uploaded files
└── requirements.txt          # Python dependencies
```

## Customization

### 1. Update Your Information

1. Go to Django Admin: http://127.0.0.1:8000/admin/
2. Navigate to **Portfolio > Profiles**
3. Edit your profile information:
   - Personal details (name, title, bio)
   - Contact information (email, phone, location)
   - Social media links
   - Upload profile image and resume

### 2. Add Your Skills

1. Go to **Portfolio > Skills**
2. Add your technical skills:
   - Name (e.g., "JavaScript", "Python")
   - Category (Frontend, Backend, Database, etc.)
   - Proficiency level (0-100%)
   - Font Awesome icon class (optional)
   - Mark as featured to show on homepage

### 3. Add Your Experience

1. Go to **Portfolio > Experiences**
2. Add your work history and education:
   - Job title and company
   - Start and end dates
   - Description of your role
   - Type (Work, Education, Certification, Project)

### 4. Add Your Projects

1. Go to **Projects > Projects**
2. Add your portfolio projects:
   - Project title and description
   - Technologies used
   - Live demo and GitHub links
   - Upload featured image
   - Add project features and additional images

### 5. Customize Styling

The project uses Tailwind CSS via CDN. To customize:

1. **Colors**: Update the gradient classes in templates
2. **Fonts**: Add custom fonts in the base template
3. **Layout**: Modify the grid and spacing classes
4. **Components**: Update the component styles in templates

## Deployment

### Environment Variables

Create a `.env` file for production settings:

```env
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost:5432/portfolio_db
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

### Production Settings

Update `settings.py` for production:

```python
import os
from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
```

### Deployment Options

1. **Heroku**: Use Heroku Postgres and configure environment variables
2. **DigitalOcean**: Deploy on a VPS with Nginx and Gunicorn
3. **AWS**: Use Elastic Beanstalk or EC2 with RDS
4. **Vercel**: Deploy with Vercel and use external database

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you have any questions or need help with customization, please open an issue or contact me through the portfolio contact form.

---

**Happy coding!** 🚀
