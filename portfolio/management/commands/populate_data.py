from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from portfolio.models import Profile, Skill, Experience
from projects.models import Project, ProjectFeature
from contact.models import ContactMessage


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create or get user
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'first_name': 'John',
                'last_name': 'Doe',
                'is_staff': True,
                'is_superuser': True
            }
        )

        # Create profile
        profile, created = Profile.objects.get_or_create(
            user=user,
            defaults={
                'first_name': 'John',
                'last_name': 'Doe',
                'title': 'Full Stack Developer',
                'bio': 'Passionate full-stack developer with 5+ years of experience building web applications. I love creating innovative solutions and beautiful user experiences. When I\'m not coding, you can find me exploring new technologies or contributing to open source projects.',
                'email': 'john.doe@example.com',
                'phone': '+1 (555) 123-4567',
                'location': 'San Francisco, CA',
                'github_url': 'https://github.com/johndoe',
                'linkedin_url': 'https://linkedin.com/in/johndoe',
                'twitter_url': 'https://twitter.com/johndoe',
                'website_url': 'https://johndoe.dev'
            }
        )

        # Create skills
        skills_data = [
            # Frontend
            {'name': 'JavaScript', 'category': 'frontend', 'proficiency': 90, 'icon': 'fab fa-js-square', 'is_featured': True, 'order': 1},
            {'name': 'React', 'category': 'frontend', 'proficiency': 85, 'icon': 'fab fa-react', 'is_featured': True, 'order': 2},
            {'name': 'Vue.js', 'category': 'frontend', 'proficiency': 80, 'icon': 'fab fa-vuejs', 'is_featured': True, 'order': 3},
            {'name': 'HTML5', 'category': 'frontend', 'proficiency': 95, 'icon': 'fab fa-html5', 'is_featured': True, 'order': 4},
            {'name': 'CSS3', 'category': 'frontend', 'proficiency': 90, 'icon': 'fab fa-css3-alt', 'is_featured': True, 'order': 5},
            {'name': 'Tailwind CSS', 'category': 'frontend', 'proficiency': 85, 'icon': 'fas fa-palette', 'is_featured': True, 'order': 6},
            
            # Backend
            {'name': 'Python', 'category': 'backend', 'proficiency': 90, 'icon': 'fab fa-python', 'is_featured': False, 'order': 7},
            {'name': 'Django', 'category': 'backend', 'proficiency': 85, 'icon': 'fab fa-python', 'is_featured': False, 'order': 8},
            {'name': 'Node.js', 'category': 'backend', 'proficiency': 80, 'icon': 'fab fa-node-js', 'is_featured': False, 'order': 9},
            {'name': 'Express.js', 'category': 'backend', 'proficiency': 75, 'icon': 'fab fa-node-js', 'is_featured': False, 'order': 10},
            
            # Database
            {'name': 'PostgreSQL', 'category': 'database', 'proficiency': 85, 'icon': 'fas fa-database', 'is_featured': False, 'order': 11},
            {'name': 'MongoDB', 'category': 'database', 'proficiency': 80, 'icon': 'fas fa-database', 'is_featured': False, 'order': 12},
            {'name': 'Redis', 'category': 'database', 'proficiency': 70, 'icon': 'fas fa-database', 'is_featured': False, 'order': 13},
            
            # DevOps
            {'name': 'Docker', 'category': 'devops', 'proficiency': 80, 'icon': 'fab fa-docker', 'is_featured': False, 'order': 14},
            {'name': 'AWS', 'category': 'devops', 'proficiency': 75, 'icon': 'fab fa-aws', 'is_featured': False, 'order': 15},
            {'name': 'Git', 'category': 'devops', 'proficiency': 90, 'icon': 'fab fa-git-alt', 'is_featured': False, 'order': 16},
        ]

        for skill_data in skills_data:
            Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )

        # Create experience
        experiences_data = [
            {
                'title': 'Senior Full Stack Developer',
                'company': 'TechCorp Inc.',
                'location': 'San Francisco, CA',
                'start_date': '2022-01-01',
                'end_date': None,
                'is_current': True,
                'description': 'Leading development of scalable web applications using React, Django, and AWS. Mentoring junior developers and implementing best practices for code quality and deployment.',
                'type': 'work',
                'order': 1
            },
            {
                'title': 'Full Stack Developer',
                'company': 'StartupXYZ',
                'location': 'Remote',
                'start_date': '2020-06-01',
                'end_date': '2021-12-31',
                'is_current': False,
                'description': 'Developed and maintained multiple web applications using modern JavaScript frameworks and Python. Collaborated with cross-functional teams to deliver high-quality software solutions.',
                'type': 'work',
                'order': 2
            },
            {
                'title': 'Bachelor of Science in Computer Science',
                'company': 'University of California',
                'location': 'Berkeley, CA',
                'start_date': '2016-09-01',
                'end_date': '2020-05-31',
                'is_current': False,
                'description': 'Graduated with honors. Focused on software engineering, algorithms, and web development. Completed multiple projects including a capstone project on machine learning applications.',
                'type': 'education',
                'order': 3
            },
            {
                'title': 'AWS Certified Solutions Architect',
                'company': 'Amazon Web Services',
                'location': 'Online',
                'start_date': '2021-03-01',
                'end_date': '2021-03-01',
                'is_current': False,
                'description': 'Certified in designing distributed systems on AWS. Demonstrated expertise in cloud architecture, security, and cost optimization.',
                'type': 'certification',
                'order': 4
            }
        ]

        for exp_data in experiences_data:
            Experience.objects.get_or_create(
                title=exp_data['title'],
                company=exp_data['company'],
                defaults=exp_data
            )

        # Create projects
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'slug': 'ecommerce-platform',
                'description': 'A full-featured e-commerce platform with user authentication, payment processing, and inventory management.',
                'long_description': 'This comprehensive e-commerce platform was built using React for the frontend and Django REST Framework for the backend. It includes features like user authentication, product catalog, shopping cart, payment processing with Stripe, order management, and admin dashboard. The application is deployed on AWS with Docker containers and uses PostgreSQL for data storage.',
                'project_type': 'web',
                'technologies': 'React, Django, PostgreSQL, Stripe, AWS, Docker',
                'github_url': 'https://github.com/johndoe/ecommerce-platform',
                'live_url': 'https://ecommerce-demo.johndoe.dev',
                'is_featured': True,
                'is_published': True,
                'order': 1
            },
            {
                'title': 'Task Management App',
                'slug': 'task-management-app',
                'description': 'A collaborative task management application with real-time updates and team collaboration features.',
                'long_description': 'Built with Vue.js and Node.js, this task management application allows teams to collaborate on projects with real-time updates. Features include drag-and-drop task organization, team member assignment, deadline tracking, and progress visualization. The app uses WebSockets for real-time communication and MongoDB for data storage.',
                'project_type': 'web',
                'technologies': 'Vue.js, Node.js, MongoDB, Socket.io, Express.js',
                'github_url': 'https://github.com/johndoe/task-manager',
                'live_url': 'https://tasks.johndoe.dev',
                'is_featured': True,
                'is_published': True,
                'order': 2
            },
            {
                'title': 'Weather Dashboard',
                'slug': 'weather-dashboard',
                'description': 'A responsive weather dashboard with location-based forecasts and interactive charts.',
                'long_description': 'A beautiful weather dashboard that provides current weather conditions and forecasts for any location. Built with vanilla JavaScript and CSS, it features interactive charts, location search, and responsive design. The app integrates with multiple weather APIs and includes features like weather alerts and historical data visualization.',
                'project_type': 'web',
                'technologies': 'JavaScript, HTML5, CSS3, Chart.js, Weather API',
                'github_url': 'https://github.com/johndoe/weather-dashboard',
                'live_url': 'https://weather.johndoe.dev',
                'is_featured': True,
                'is_published': True,
                'order': 3
            },
            {
                'title': 'Blog API',
                'slug': 'blog-api',
                'description': 'A RESTful API for a blogging platform with authentication and content management.',
                'long_description': 'A comprehensive REST API built with Django REST Framework that powers a blogging platform. Features include user authentication, post creation and management, comment system, image uploads, and admin interface. The API includes rate limiting, caching, and comprehensive documentation.',
                'project_type': 'api',
                'technologies': 'Django, Django REST Framework, PostgreSQL, Redis, Celery',
                'github_url': 'https://github.com/johndoe/blog-api',
                'live_url': 'https://api-blog.johndoe.dev',
                'is_featured': False,
                'is_published': True,
                'order': 4
            },
            {
                'title': 'Mobile Expense Tracker',
                'slug': 'mobile-expense-tracker',
                'description': 'A React Native mobile app for tracking personal expenses with budget management.',
                'long_description': 'A cross-platform mobile application built with React Native for tracking personal expenses and managing budgets. Features include expense categorization, budget setting, spending analytics, and data export. The app includes offline functionality and syncs data across devices.',
                'project_type': 'mobile',
                'technologies': 'React Native, Redux, SQLite, Chart.js, AsyncStorage',
                'github_url': 'https://github.com/johndoe/expense-tracker',
                'is_featured': False,
                'is_published': True,
                'order': 5
            }
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                slug=project_data['slug'],
                defaults=project_data
            )

            # Add features for featured projects
            if project.is_featured:
                if project.slug == 'ecommerce-platform':
                    features = [
                        {'title': 'User Authentication', 'description': 'Secure user registration and login with JWT tokens'},
                        {'title': 'Payment Processing', 'description': 'Integrated Stripe payment gateway for secure transactions'},
                        {'title': 'Admin Dashboard', 'description': 'Comprehensive admin interface for managing products and orders'},
                        {'title': 'Inventory Management', 'description': 'Real-time inventory tracking and low-stock alerts'}
                    ]
                elif project.slug == 'task-management-app':
                    features = [
                        {'title': 'Real-time Updates', 'description': 'Live collaboration with WebSocket integration'},
                        {'title': 'Drag & Drop', 'description': 'Intuitive task organization with drag-and-drop functionality'},
                        {'title': 'Team Collaboration', 'description': 'Multi-user support with role-based permissions'},
                        {'title': 'Progress Tracking', 'description': 'Visual progress indicators and completion statistics'}
                    ]
                elif project.slug == 'weather-dashboard':
                    features = [
                        {'title': 'Location Search', 'description': 'Search weather for any location worldwide'},
                        {'title': 'Interactive Charts', 'description': 'Beautiful data visualization with Chart.js'},
                        {'title': 'Weather Alerts', 'description': 'Real-time weather warnings and notifications'},
                        {'title': 'Responsive Design', 'description': 'Optimized for all device sizes and screen resolutions'}
                    ]

                for feature_data in features:
                    ProjectFeature.objects.get_or_create(
                        project=project,
                        title=feature_data['title'],
                        defaults={'description': feature_data['description'], 'order': len(ProjectFeature.objects.filter(project=project)) + 1}
                    )

        # Create sample contact messages
        contact_messages = [
            {
                'name': 'Sarah Johnson',
                'email': 'sarah.johnson@example.com',
                'subject': 'Web Development Project Inquiry',
                'message': 'Hi John, I came across your portfolio and I\'m impressed with your work. I have a web development project that I think would be a great fit for your skills. Would you be available for a consultation?',
                'status': 'new'
            },
            {
                'name': 'Mike Chen',
                'email': 'mike.chen@techstartup.com',
                'subject': 'Full Stack Developer Position',
                'message': 'Hello John, we\'re looking for a full stack developer to join our team. Your experience with React and Django aligns perfectly with our tech stack. Are you open to discussing potential opportunities?',
                'status': 'read'
            }
        ]

        for msg_data in contact_messages:
            ContactMessage.objects.get_or_create(
                email=msg_data['email'],
                subject=msg_data['subject'],
                defaults=msg_data
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )
        self.stdout.write('You can now:')
        self.stdout.write('1. Run "python manage.py runserver" to start the development server')
        self.stdout.write('2. Visit http://127.0.0.1:8000/ to see your portfolio')
        self.stdout.write('3. Visit http://127.0.0.1:8000/admin/ to manage content')
