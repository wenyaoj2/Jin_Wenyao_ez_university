from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http.response import HttpResponse
from django.template import loader
from django.views import View

from courseinfo.forms import InstructorForm, SectionForm, StudentForm, SemesterForm, CourseForm, RegistrationForm
from courseinfo.utils import ObjectCreateMixin
from .models import(
    Instructor, Section, Student, Semester, Course, Registration
)


class InstructorList(View):
    def get(self, request):
        return render(
            request,
            'courseInfo/instructor_list.html',
            {'instructor_list': Instructor.objects.all()}
        )
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

class InstructorCreate(ObjectCreateMixin,View):
    form_class = InstructorForm
    template_name = 'courseInfo/instructor_form.html'

class InstructorUpdate(View):
    form_class = InstructorForm
    model = Instructor
    template_name = 'courseInfo/instructor_form_update.html'

    def get_object(self,pk):
        return get_object_or_404(
            self.model,
            pk=pk
        )

    def get(self,request,pk):
        instructor = self.get_object(pk)
        context = {
            'form':self.form_class(instance=instructor),
            'instructor': instructor,
        }
        return render(request,self.template_name,context)

    def post(self,request,pk):
        instructor = self.get_object(pk)
        bound_form = self.form_class(request.POST,instance=instructor)
        if bound_form.is_valid():
            new_instructor = bound_form.save()
            return redirect(new_instructor)
        else:
            context = {
                'form':bound_form,
                'instructor':instructor,
            }
            return render(
                request,
                self.template_name,
                context
            )

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

class SectionList(View):
    def get(self, request):
        return render(
            request,
            'courseInfo/section_list.html',
            {'section_list': Section.objects.all()}
        )

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
class SectionCreate(ObjectCreateMixin,View):
    form_class = SectionForm
    template_name = 'courseInfo/section_form.html'

class SectionUpdate(View):
    form_class = SectionForm
    model = Section
    template_name = 'courseInfo/section_form_update.html'

    def get_object(self,pk):
        return get_object_or_404(
            self.model,
            pk=pk
        )

    def get(self,request,pk):
        section = self.get_object(pk)
        context = {
            'form':self.form_class(instance=section),
            'section': section,
        }
        return render(request,self.template_name,context)

    def post(self,request,pk):
        section = self.get_object(pk)
        bound_form = self.form_class(request.POST,instance=section)
        if bound_form.is_valid():
            new_section = bound_form.save()
            return redirect(new_section)
        else:
            context = {
                'form':bound_form,
                'section':section,
            }
            return render(
                request,
                self.template_name,
                context
            )

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

class StudentList(View):
    def get(self, request):
        return render(
            request,
            'courseInfo/students_list.html',
            {'student_list': Student.objects.all()}
        )

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

class StudentCreate(ObjectCreateMixin,View):
    form_class = StudentForm
    template_name = 'courseInfo/student_form.html'

class StudentUpdate(View):
    form_class = StudentForm
    model = Student
    template_name = 'courseinfo/student_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, pk):
        student = self.get_object(pk)
        context = {
            'form': self.form_class(instance=student),
            'student': student
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):
        student = self.get_object(pk)
        bound_form = self.form_class(request.POST, instance=student)
        if bound_form.is_valid():
            new_student = bound_form.save()
            return redirect(new_student)
        else:
            context = {
                'form': bound_form,
                'student': student,
            }
            return render(request, self.template_name, context)

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

class SemesterList(View):
    def get(self, request):
        return render(
            request,
            'courseInfo/semester_list.html',
            {'semester_list': Semester.objects.all()}
        )

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

class SemesterCreate(ObjectCreateMixin,View):
    form_class = SemesterForm
    template_name = 'courseInfo/semester_form.html'

class SemesterUpdate(View):
    form_class = SemesterForm
    model = Semester
    template_name = 'courseinfo/semester_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, pk):
        semester = self.get_object(pk)
        context = {
            'form': self.form_class(instance=semester),
            'semester': semester
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):
        semester = self.get_object(pk)
        bound_form = self.form_class(request.POST, instance=semester)
        if bound_form.is_valid():
            new_semester = bound_form.save()
            return redirect(new_semester)
        else:
            context = {
                'form': bound_form,
                'semester': semester,
            }
            return render(request, self.template_name, context)

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

class CourseList(View):
    def get(self, request):
        return render(
            request,
            'courseInfo/course_list.html',
            {'course_list': Course.objects.all()}
        )

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

class CourseCreate(ObjectCreateMixin,View):
    form_class = CourseForm
    template_name = 'courseInfo/course_form.html'

class CourseUpdate(View):
    form_class = CourseForm
    model = Course
    template_name = 'courseinfo/course_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, pk):
        course = self.get_object(pk)
        context = {
            'form': self.form_class(instance=course),
            'course': course
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):
        course = self.get_object(pk)
        bound_form = self.form_class(request.POST, instance=course)
        if bound_form.is_valid():
            new_course = bound_form.save()
            return redirect(new_course)
        else:
            context = {
                'form': bound_form,
                'course': course,
            }
            return render(request, self.template_name, context)

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

class RegistrationList(View):
    def get(self, request):
        return render(
            request,
            'courseInfo/registration_list.html',
            {'registration_list': Registration.objects.all()}
        )

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

class RegistrationCreate(ObjectCreateMixin,View):
    form_class = RegistrationForm
    template_name = 'courseInfo/registration_form.html'

class RegistrationUpdate(View):
    form_class = RegistrationForm
    model = Registration
    template_name = 'courseinfo/registration_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, pk):
        registration = self.get_object(pk)
        context = {
            'form': self.form_class(instance=registration),
            'registration': registration
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):
        registration = self.get_object(pk)
        bound_form = self.form_class(request.POST, instance=registration)
        if bound_form.is_valid():
            new_registration = bound_form.save()
            return redirect(new_registration)
        else:
            context = {
                'form': bound_form,
                'registration': registration,
            }
            return render(request, self.template_name, context)

class RegistrationDelete(View):

    def get_object(self, pk):
        return get_object_or_404(Registration, pk=pk)

    def get(self, request, pk):
        registration = self.get_object(pk)
        return render(
            request,
            'courseinfo/registration_confirm_delete.html',
            {'registration': registration}
        )

    def post(self, request, pk):
        registration = self.get_object(pk)
        registration.delete()
        return redirect('courseinfo_registration_list_urlpattern')