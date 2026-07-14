from django.db import models

# Create your models here.
from django.db import models

class Career(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    skills = models.TextField()
    salary = models.CharField(max_length=100)
    opportunities=models.TextField()
    roadmap = models.TextField()
    resources = models.TextField()
    roadmap_link=models.URLField(blank=True)
    resources_link=models.URLField(blank=True)
    quiz_link=models.URLField(blank=True)



    def __str__(self):
        return self.title
   

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class RoadmapStep(models.Model):
    career = models.ForeignKey(
        Career,
        on_delete=models.CASCADE,
        related_name="roadmap_steps"
    )
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ["step_number"]

    def __str__(self):
        return f"{self.career.title} - Step {self.step_number}"