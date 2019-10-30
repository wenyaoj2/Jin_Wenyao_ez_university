from django.db import models
from django.urls import reverse

class Period(models.Model):
    period_id = models.AutoField(primary_key=True)
    period_sequence = models.IntegerField(unique=True)
    period_name = models.CharField(max_length=45,unique=True)

    def __str__(self):
        return '%s' % self.period_name
    class Meta:
        ordering = ['period_sequence']

class Year(models.Model):
    year_id = models.AutoField(primary_key=True)
    year = models.IntegerField(unique=True)

    def __str__(self):
        return '%s' % self.year
    class Meta:
        ordering = ['year']

class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    year = models.ForeignKey(Year, related_name='semesters',on_delete=models.PROTECT)
    period = models.ForeignKey(Period, related_name='semesters',on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.year.year,self.period.period_name)
    def get_absolute_url(self):
        return reverse('courseinfo_semester_detail_urlpattern',kwargs={'pk':self.pk})
    def get_update_url(self):
        return reverse('courseinfo_semester_update_urlpattern',kwargs={'pk': self.pk})
    def get_delete_url(self):
        return reverse('courseinfo_semester_delete_urlpattern',kwargs={'pk': self.pk})
    class Meta:
        ordering = ['year__year','period__period_sequence']
        unique_together = ('year','period')

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    course_number = models.CharField(max_length=20)
    def __str__(self):
        return '%s - %s' % (self.course_number,self.course_name)
    def get_absolute_url(self):
        return reverse('courseinfo_course_detail_urlpattern',kwargs={'pk':self.pk})
    def get_update_url(self):
        return reverse('courseinfo_course_update_urlpattern',kwargs={'pk': self.pk})
    def get_delete_url(self):
        return reverse('courseinfo_course_delete_urlpattern',kwargs={'pk': self.pk})
    class Meta:
        ordering = ['course_number', 'course_name']
        unique_together = (('course_number', 'course_name'),)

class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
    def get_absolute_url(self):
        return reverse('courseinfo_instructor_detail_urlpattern',kwargs={'pk':self.pk})
    def get_update_url(self):
        return reverse('courseinfo_instructor_update_urlpattern',kwargs={'pk':self.pk})
    def get_delete_url(self):
        return reverse('courseinfo_instructor_delete_urlpattern',kwargs={'pk':self.pk})
    class Meta:
        ordering = ['last_name', 'first_name']
        unique_together = (('first_name', 'last_name'),)


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    nick_name = models.CharField(max_length=45, blank=True, default='')
    def __str__(self):
        result = ''
        if self.nick_name == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.nick_name)
        return result
    def get_absolute_url(self):
        return reverse('courseinfo_student_detail_urlpattern',kwargs={'pk':self.pk})
    def get_update_url(self):
        return reverse('courseinfo_student_update_urlpattern',kwargs={'pk': self.pk})
    def get_delete_url(self):
        return reverse('courseinfo_student_delete_urlpattern',kwargs={'pk': self.pk})
    class Meta:
        ordering = ['last_name', 'first_name', 'nick_name']
        unique_together = (('last_name', 'first_name', 'nick_name'),)


class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=10)
    semester = models.ForeignKey(Semester, related_name='sections', on_delete=models.PROTECT)
    course = models.ForeignKey(Course, related_name='sections', on_delete=models.PROTECT)
    instructor = models.ForeignKey(Instructor, related_name='sections', on_delete=models.PROTECT)
    def __str__(self):
        return '%s - %s (%s)' % (self.course.course_name, self.section_name, self.semester.__str__())
    def get_absolute_url(self):
        return reverse('courseinfo_section_detail_urlpattern',kwargs={'pk':self.pk})
    def get_update_url(self):
        return reverse('courseinfo_section_update_urlpattern',kwargs={'pk':self.pk})
    def get_delete_url(self):
        return reverse('courseinfo_section_delete_urlpattern',kwargs={'pk': self.pk})
    class Meta:
        ordering = ['course__course_name', 'section_name', 'semester__semester_name']
        unique_together = (('semester', 'course', 'section_name'),)

class Registration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, related_name='registrations', on_delete=models.PROTECT)
    section = models.ForeignKey(Section, related_name='registrations', on_delete=models.PROTECT)
    def __str__(self):
        return '%s / %s' % (self.section, self.student)
    def get_absolute_url(self):
        return reverse('courseinfo_registration_detail_urlpattern',kwargs={'pk':self.pk})
    def get_update_url(self):
        return reverse('courseinfo_registration_update_urlpattern',kwargs={'pk': self.pk})
    def get_delete_url(self):
        return reverse('courseinfo_registration_delete_urlpattern',kwargs={'pk': self.pk})
    class Meta:
        ordering = ['section', 'student']
        unique_together = (('section', 'student'),)