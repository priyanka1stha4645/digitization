from django.shortcuts import render, redirect
from crudeapp.forms import StudentForm
from crudeapp.models import Student


def take_attendance(request):
		student = Student.objects.all()
		return render(request, "take_attendance.html", {'student': student})



def update_attendance(request):
	# student = Student.objects.get(id=id)
	# print("a")
	if request.method == "POST":
		 print("a")
		# sid = request.POST.get('sid')
		sname = request.POST.get(sname)
		 print("a")
		for student in student:
			daily.save()
	return render(request, "edit.html")

