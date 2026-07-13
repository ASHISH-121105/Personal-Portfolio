from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency_percentage = models.IntegerField(help_text="Enter a number between 0 and 100")
    
    def __str__(self):
        return self.name

class Project(models.Model):
    CATEGORY_CHOICES = (
        ('DL', 'Deep Learning'),
        ('WEB', 'Full-Stack Web'),
        ('HACK', 'Hackathon'),
    )
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    # Allows you to upload project screenshots later
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True) 
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True, help_text="Link to the deployed live project")

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    title = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    date_range = models.CharField(max_length=50, help_text="e.g., Summer 2026 or June 2026 - Present")
    description = models.TextField()
    is_active = models.BooleanField(default=False, help_text="Check if this is your current role")

    def __str__(self):
        return f"{self.title} at {self.organization}"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"