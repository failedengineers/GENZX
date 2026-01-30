from django.db import models

# Create your models here.
# models.py



from django.db import models

# Create your models here.
# models.py


from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    total_semesters = models.IntegerField()

    def __str__(self):
        return self.name


class Semester(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.course.name} - Sem {self.number}"


class Subject(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Resource(models.Model):
    RESOURCE_TYPES = [
        ('syllabus', 'Syllabus'),
        ('notes', 'Notes'),
        ('assignment', 'Assignment'),
        ('lab', 'Lab File'),
        ('pyq', 'PYQ'),
        ('video', 'Video'),
        ('other', 'Other'),
    ]

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="resources"
    )
    type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    unit_number = models.PositiveIntegerField(blank=True, null=True)
    content = models.TextField(blank=True)
    link = models.URLField(blank=True, null=True)
    link_text = models.CharField(max_length=100, blank=True)
    title = models.CharField(
        max_length=255,blank=True,null=True
    )


    class Meta:
        ordering = ['unit_number', 'type']
        

    def __str__(self):
        return self.title or f"{self.subject.name} - {self.type}"

class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    message = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
