from django.shortcuts import render, redirect
from.models import User,Member
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse

def index(req):
    return render(req, "index.html")
def create(req):
    member = Member(firstname=req.POST['firstname'], lastname=req.POST['lastname'])
    member.save()
    message = 'hello'
    email = 'nieldigitalco@gmail.com'
    send_mail('Contact form',
              message,
              'settings.EMAIL_HOST_USER',
              [email],
              fail_silently=False)
    return redirect('/')

# def read(req):
#     # conn = connections['default']
#     with connections['default'].cursor() as cursor:
#         cursor.execute('SELECT id, firstname, lastname FROM tbl_member')
#         result = cursor.fetchall()
#     return render(req, 'result.html', {'members': result})

def read(req):
    members = Member.objects.all()
    context= {
        "members": members,
    }
    
    return render(req, "result.html", context)

def edit(req, id):
    member = Member.objects.get(id=id)
    print(member.id)
    context = {
        "member":member,
    }
    return render(req, "edit.html", context)

def update(req, id):
    member = Member.objects.get(id=id)
    member.firstname = req.POST['firstname']
    member.lastname = req.POST['lastname']
    member.save()
    result = "success"
    data = {'status': 'success', 'message': 'Action was successful'}
    return HttpResponse(result)
    # return redirect('/')

def delete(req, id):
    member = Member.objects.get(id=id)
    member.delete()
    return HttpResponse("success")
# Create your views here.
# Create your views here.
