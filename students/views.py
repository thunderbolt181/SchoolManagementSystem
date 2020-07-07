from django.shortcuts import render,redirect,reverse
from .models import student
from .forms import StudentCreateForm, submit_fees
from django.contrib import messages
from django.db.models import Q
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def search_fun(request):
    if request.method == "GET":
        if request.GET.get('q') != None and request.GET.get('q') != "":
            search = request.GET['q']
            lookup = Q(Admission_no__icontains = search,)
            result = student.objects.filter(lookup).distinct()
            if len(result) !=0:
                content = {
                    'results':result,
                    'search':search,
                    'title':"Home",
                }
                return render(request, 'students/search.html',content)
            else:
                content = {
                'no_result':"No Search Results Found",
                'title':"Home",
                }
            return render(request, 'students/search.html',content)
        else:
            return redirect('home')

@login_required
def home(request):
    s = student.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(s, 20)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    context = {
        'students':students,
        'user':request.user
    }
    return render(request,'students/Main.html',context)

@login_required
def create_entry(request):
    if request.method == 'POST':
        s_form = StudentCreateForm(request.POST)
        if s_form.is_valid():
            S = s_form.save(commit=False)
            S.created_by=request.user
            S.remaning_fees=20000
            S.save()
            return redirect("home")
    else:
        s_form = StudentCreateForm()
    return render(request, 'students/Create_post.html', {'s_form': s_form,'user':request.user})

@login_required
def studentID(request,student_id):
    user = request.user 
    student_obj = student.objects.get(id=int(student_id))
    return render(request,"students/student_id.html",{'student':student_obj,'user':user})

class Edit_Student_Detail(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = student
    fields = ['Admission_no','Name','DOB','Gender','Phone','Phone_Other','Email',
            'Class','Fathers_Name','Fathers_Occupation','Mothers_Name','Mothers_Occupation',
            'Relegion','caste','Category','Address','Nationality','Note_about_Student']
    
    def form_valid(self,form):
        form.instance.created_by=self.request.user
        messages.success(self.request, 'Updated Successfully')
        form.save()
        return self.render_to_response(self.get_context_data(form=form))

@login_required
def submit_student_fees(request,student_id):
    student_obj = student.objects.get(id=int(student_id))
    if request.method == "POST":
        form = submit_fees(request.POST)
        if form.is_valid():
            if form.cleaned_data["Amount_Paying"] > 0 and form.cleaned_data["Staff_username"] == request.user.username:
                student_obj.remaning_fees = student_obj.remaning_fees-form.cleaned_data["Amount_Paying"]
                student_obj.save()
                messages.success(request, 'Your Fees was Submitted successfully!')
                return redirect('student-ID',student_obj.id)
            else:
                messages.warning(request, 'Please Enter Correct Information')
    else:
        form = submit_fees()
    return render(request,'students/submit-fees.html',{"form":form,'user':request.user})