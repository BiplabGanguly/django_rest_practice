from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from . import models
from home.Serializer import StudentSerializer,StudentCountSerializer
from rest_framework import status
from django.http import Http404
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

    def get_student_data(self, pk):
        try:
            return models.StudentModel.objects.get(id = pk)
        except models.StudentModel.DoesNotExist:
            raise Http404


    def get(self, request, pk=None):
        if pk is not None:
            data = models.StudentModel.objects.get(id = pk)
            student_serializer = StudentSerializer(data)
        else:
            data = models.StudentModel.objects.all()
            student_serializer = StudentSerializer(data, many=True)
        return Response(student_serializer.data)
    
    def post(self, request):
        student_serializer = StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({"message": "success"})
        else:
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, format=None): 
        student = self.get_student_data(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def patch(self,req,pk):
        student_data = self.get_student_data(pk)
        serializer = StudentSerializer(student_data, data=req.data, partial = True)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
    
    
class total_student(APIView):
    def get(self,req):
        count_student = models.StudentModel.objects.all().count()
        total_student_data = StudentCountSerializer({'total_student': count_student})
        return Response(total_student_data.data)
