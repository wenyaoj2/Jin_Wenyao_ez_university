from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http.response import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from courseinfo.forms import InstructorForm, SectionForm, StudentForm, SemesterForm, CourseForm, RegistrationForm
from courseinfo.utils import PageLinksMixin
from .models import(
    Instructor, Section, Student, Semester, Course, Registration
)

class InstructorList(PageLinksMixin,ListView):
    paginate_by = 25
    model = Instructor

class InstructorDetail(View):
    def get(self, request,pk):
        instructor = get_object_or_404(
            Instructor,
            pk = pk
        )
        section_list = instructor.sections.all()
        return render(
            request,
            'courseInfo/instructor_detail.html',
            {'instructor':instructor, 'section_list':section_list}
        )

class InstructorCreate(CreateView):
    form_class = InstructorForm
    model = Instructor

class InstructorUpdate(UpdateView):
    form_class = InstructorForm
    model = Instructor
    template_name = 'courseInfo/instructor_form_update.html'



class InstructorDelete(View):

    def get_object(self, pk):
        return get_object_or_404(Instructor, pk=pk)

    def get(self, request, pk):
        instructor = self.get_object(pk)
        sections = instructor.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/instructor_refuse_delete.html',
                {'instructor': instructor,
                 'sections': sections}
            )
        else:
            return render(
                request,
                'courseinfo/instructor_confirm_delete.html',
                {'instructor': instructor}
            )

    def post(self, request, pk):
        instructor = self.get_object(pk)
        instructor.delete()
        return redirect('courseinfo_instructor_list_urlpattern')

class SectionList(ListView):
    model = Section

class SectionDetail(View):
    def get(self, request,pk):
        section = get_object_or_404(
            Section,
            pk = pk
        )
        semester = section.semester
        course = section.course
        instructor = section.instructor
        registration_list = section.registrations.all()
        return render(
            request,
            'courseInfo/section_detail.html',
            {'section':section,
             "semester":semester,
             "course":course,
             'instructor':instructor,
             'registration_list':registration_list}
        )
class SectionCreate(CreateView):
    form_class = SectionForm
    model = Section

class SectionUpdate(UpdateView):
    form_class = SectionForm
    model = Section
    template_name = 'courseInfo/section_form_update.html'



class SectionDelete(View):

    def get_object(self, pk):
        return get_object_or_404(Section, pk=pk)

    def get(self, request, pk):
        section = self.get_object(pk)
        registrations = section.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/section_refuse_delete.html',
                {'section': section,
                 'registrations': registrations}
            )
        else:
            return render(
                request,
                'courseinfo/section_confirm_delete.html',
                {'section': section}
            )

    def post(self, request, pk):
        section = self.get_object(pk)
        section.delete()
        return redirect('courseinfo_section_list_urlpattern')

class StudentList(PageLinksMixin, ListView):
        paginate_by = 25
        model = Student


class StudentDetail(View):
    def get(self, request, pk):
        student = get_object_or_404(
            Student,
            pk = pk
        )
        registration_list = student.registrations.all()
        return render(
            request,
            'courseInfo/student_detail.html',
            {'student':student,
             'registration_list':registration_list}
        )

class StudentCreate(CreateView):
    form_class = StudentForm
    model = Student

class StudentUpdate(UpdateView):
    form_class = StudentForm
    model = Student
    template_name = 'courseinfo/student_form_update.html'

class StudentDelete(View):

    def get_object(self, pk):
        return get_object_or_404(Student, pk=pk)

    def get(self, request, pk):
        student = self.get_object(pk)
        registrations = student.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/student_refuse_delete.html',
                {'student': student,
                 'registrations': registrations}
            )
        else:
            return render(
                request,
                'courseinfo/student_confirm_delete.html',
                {'student': student}
            )

    def post(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return redirect('courseinfo_student_list_urlpattern')

class SemesterList(ListView):
    model = Semester

class SemesterDetail(View):
    def get(self, request,pk):
        semester = get_object_or_404(
            Semester,
            pk = pk
        )
        section_list = semester.sections.all()
        return render(
            request,
            'courseInfo/semester_detail.html',
            {'semester':semester, 'section_list':section_list}
        )

class SemesterCreate(CreateView):
    form_class = SemesterForm
    model = Semester

class SemesterUpdate(UpdateView):
    form_class = SemesterForm
    model = Semester
    template_name = 'courseinfo/semester_form_update.html'

class SemesterDelete(View):

    def get_object(self, pk):
        return get_object_or_404(Semester, pk=pk)

    def get(self, request, pk):
        semester = self.get_object(pk)
        sections = semester.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/semester_refuse_delete.html',
                {'semester': semester,
                 'sections': sections}
            )
        else:
            return render(
                request,
                'courseinfo/semester_confirm_delete.html',
                {'semester': semester}
            )

    def post(self, request, pk):
        semester = self.get_object(pk)
        semester.delete()
        return redirect('courseinfo_semester_list_urlpattern')

class CourseList(ListView):
    model = Course

class CourseDetail(View):
    def get(self,request, pk):
        course = get_object_or_404(
            Course,
            pk = pk
        )
        section_list = course.sections.all()
        return render(
            request,
            'courseInfo/course_detail.html',
            {'course':course,
             'section_list':section_list}
        )

class CourseCreate(CreateView):
    form_class = CourseForm
    model = Course

class CourseUpdate(UpdateView):
    form_class = CourseForm
    model = Course
    template_name = 'courseinfo/course_form_update.html'

class CourseDelete(View):

    def get_object(self, pk):
        return get_object_or_404(Course, pk=pk)

    def get(self, request, pk):
        course = self.get_object(pk)
        sections = course.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/course_refuse_delete.html',
                {'course': course,
                 'sections': sections}
            )
        else:
            return render(
                request,
                'courseinfo/course_confirm_delete.html',
                {'course': course}
            )

    def post(self, request, pk):
        course = self.get_object(pk)
        course.delete()
        return redirect('courseinfo_course_list_urlpattern')

class RegistrationList(ListView):
    model = Registration

class RegistrationDetail(View):
    def get(self, request, pk):
        registration = get_object_or_404(
            Registration,
            pk = pk
        )
        student = registration.student
        section = registration.section
        return render(
            request,
            'courseInfo/registration_detail.html',
            {'registration':registration,
             'student':student,
             'section':section
             }
        )

class RegistrationCreate(CreateView):
    form_class = RegistrationForm
    model = Registration

class RegistrationUpdate(UpdateView):
    form_class = RegistrationForm
    model = Registration
    template_name = 'courseinfo/registration_form_update.html'


class RegistrationDelete(DeleteView):
    model = Registration
    success_url = reverse_lazy('courseinfo_registration_list_urlpattern')