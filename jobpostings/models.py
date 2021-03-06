from django.db     import models

from oneted.common import TimeStampModel

class Country(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "countries"

class Region(models.Model):
    country   = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="region")
    name      = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table = "regions"

class Company(models.Model):
    region         = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="company")
    name           = models.CharField(max_length=45)
    description    = models.TextField()
    employee_count = models.IntegerField()
    coordinate     = models.JSONField()
    image_url      = models.URLField(max_length=3000, null=True)

    class Meta:
        db_table = "companies"

class TagCategory(models.Model):
    name               = models.CharField(max_length=45, unique=True)
    is_multiple_choice = models.BooleanField(default=False)

    class Meta:
        db_table = "tag_categories"

class Tag(models.Model):
    tag_category = models.ForeignKey(TagCategory, on_delete=models.CASCADE, related_name="tag")
    name         = models.CharField(max_length=45)

    class Meta:
        db_table = "tags"

class JobGroup(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "job_groups"

class Job(models.Model):
    job_group = models.ForeignKey(JobGroup, on_delete=models.CASCADE, related_name="job")
    name      = models.CharField(max_length=45)

    class Meta:
        db_table = "jobs"

class Experience(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "experiences"

class JobPosting(TimeStampModel):
    job         = models.ForeignKey(Job, on_delete=models.PROTECT, related_name="job_posting")
    company     = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="job_posting")
    experience  = models.ForeignKey(Experience, on_delete=models.PROTECT, related_name="job_posting")
    tags        = models.ManyToManyField(Tag, through="TagJobPosting", related_name="job_posting")
    title       = models.CharField(max_length=300)
    salary      = models.IntegerField()
    description = models.TextField(null=True)
    main_task   = models.TextField(null=True)
    requirement = models.TextField(null=True)
    preference  = models.TextField(null=True)
    benefit     = models.TextField(null=True)
    due_date    = models.DateTimeField(null=True)
    image_url   = models.URLField(max_length=3000, null=True)

    class Meta:
        db_table = "job_postings"

class TagJobPosting(models.Model):
    tag         = models.ForeignKey(Tag, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)

    class Meta:
        db_table        = "tags_job_postings"
        unique_together = ["tag", "job_posting"]