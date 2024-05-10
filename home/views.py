from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from . import models
from home.Serializer import StudentSerializer,StudentCountSerializer
from rest_framework import status
# Create your views here.


@api_view(['GET','POST'])
def home(req):
    student  = {
            "name" : "biplab ganguly",
            "roll" : 12
    }
    if req.method == "GET":
        return Response(student)
    elif req.method == "POST":
        return Response(req.data['name'])
    

class studentDetails(APIView):
    def get(self,req):
        data = models.StudentModel.objects.all()
        student_serializer = StudentSerializer(data,many = True)
        return Response(student_serializer.data)
    
    def post(self,req):
        student_serializer = StudentSerializer(data = req.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({"message":"success"})
        else:
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class total_student(APIView):
    def get(self,req):
        count_student = models.StudentModel.objects.all().count()
        total_student_data = StudentCountSerializer({'total_student': count_student})
        return Response(total_student_data.data)
