from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from matplotlib.style import use
from rest_framework import viewsets
from rest_framework.serializers import Serializer
from .serializers import PostSerializer, ImageSerializer, RaspberrySerializer, PhotoSerializer
from .models import User, UserImage, Rasdata, Photo
from django.views.decorators.csrf import csrf_exempt
import time
from plantsClassification import Predict
from datetime import datetime
from .models import Plantmanage
from .serializers import WaterDataSerializer
import os
# from rest_framework.decorators import action


class ImageViewset(viewsets.ModelViewSet):
    
    queryset = UserImage.objects.all()
    serializer_class = ImageSerializer    
    userid = ''
    def create(self, request, *args, **kwargs):      

        data1 = ''
        global userid
        userid = request.POST.get('user')

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

        global userid

        data = UserImage.objects.values().filter(user = userid)
        
        data1 = data[0]
        filename = data1['userimage']
    

        label = Predict(userid, filename)
        print(label)
        serializer.save(plantname = label)

class WaterViewset(viewsets.ModelViewSet): # 바뀐점!!!!
    queryset = Plantmanage.objects.all()
    serializer_class = WaterDataSerializer

class PhotoViewset(viewsets.ModelViewSet): # 바뀐점!!!!
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def create(self, request, *args, **kwargs):
        os.system(
            'python3 /home/ubuntu/yolov5/detect.py --weights /home/ubuntu/ai/best.pt --img 640 --conf 0.1 --source /home/ubuntu/img/picam/woo.jpg --project=/home/ubuntu/img/health --name=img')

        return super().create(request, *args, **kwargs)



# @csrf_exempt
# def post(request):
#     if request.method == "POST":
#         a = request.POST.get('user')
#         b = request.POST.get('userimage')
#         print(a)
#         print(b)
#         return JsonResponse({'code': '0000', 'msg': '로그인성공입니다.'}, status=200)

    # def post(self, request, *args, **kwargs):
    #     parser_classes = (ImageViewset,)
    #         file_serializer = ImageSerializer(data=request.data)
    #         if file_serializer.is_valid():
    #             file_serializer.save()
            
            #     return JsonResponse({'code': '0000', 'msg': '로그인성공입니다.'}, status=200)
            # else:
            #     return JsonResponse({'code': '1001', 'msg': '로그인실패입니다.'}, status=400)


class PostViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PostSerializer
        


# class CheckAccountViewset(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = PostSerializer

#     def create(self, request):
    
#         checkID = request.data['id']
#         checkPW = request.data['pw']

#         if User.objects.filter(id=checkID).exists():
#             if User.objects.filter(pw=checkPW).exists():
#                 return Response(status=200)

#         return Response(status = 400)
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(status=200)

        



@csrf_exempt
def Login(request):
    if request.method == "POST":
        checkid = request.POST.get('id')     
        checkpw = request.POST.get('pw')  

        result = authenticate(checkid,checkpw)

        if result:
            print("로그인 성공!")
            return JsonResponse({'code': '0000', 'msg': '로그인성공입니다.'}, status=200)
        else:
            print("실패")
            return JsonResponse({'code': '1001', 'msg': '로그인실패입니다.'}, status=400) 


def authenticate(checkid,checkpw):
    if User.objects.filter(userid=checkid).exists():
        obj = User.objects.get(userid=checkid)
        print(obj.userpassword)
        if  obj.userpassword == checkpw:
            return True

    return False

# class CheckAccountViewset(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = PostSerializer

#     def create(self, request):
#         checkid = request.POST.get('id',"")
#         checkpw = request.POST.get('pw',"")

#         if User.objects.filter(id=checkid).exists():
#             if User.objects.filter(pw=checkpw).exists():
#                 return Response(status=200)

#         return Response(status=400)

@csrf_exempt
def CheckId(request):
    if request.method == "POST":
        idcheck = request.POST.get('idcheck')
    
        if User.objects.filter(userid=idcheck).exists():
            return JsonResponse({'code': '1001', 'msg': '아디중복.'}, status=400)
        else:
            return JsonResponse({'code': '0000', 'msg': '중복확인.'}, status=200)

@csrf_exempt
def UserProfileImage(request):
    import base64
    if request.method == "POST":
        userid = request.POST.get("userid")

        requestuser = UserImage.objects.get(user = userid)

        image = [requestuser.userimage]
        print(type(image))
        print(image)
        
        # return JsonResponse({'code': '0000', 'msg': "asd" }, status=200)
        return image

class PostViewset_raspberry(viewsets.ModelViewSet):
    queryset = Rasdata.objects.all()
    serializer_class = RaspberrySerializer



# 온도html
def temp(request):
    context = {'date': sel_item()["date"],
               'temp': sel_item()['temp']
               }
    return render(request, 'temp.html',context)

# 습도html
def humid(request):
    context = {'date': sel_item()["date"],
               'humid': sel_item()['soil_hum']
               }
    return render(request, 'humid.html',context)

# 광도html
def light(request):
    context = {'date': sel_item()["date"],
               'light': sel_item()['light']
               }
    return render(request, 'light.html',context)

# 문 준 날짜 html
def water(request):
    context = {#'waterDate': water_date().loc[0,'max(waterdate).to_pydatetime().strftime('%Y-%m-%d %H:%M:%S')'], # 서버에 원래 위치 (마지막엔 이걸로 연결해야해요!)
               'waterDate': water_date().loc[0, 'max(date)'].to_pydatetime().strftime('%Y-%m-%d %H:%M:%S'), # 서버 rasdate로 예시 위치
               'calDate': cal_date()}
    return render(request, 'water.html',context)


# 서버

import pymysql
import pandas as pd

host_name = 'team7mysql.clhnj2zwdisk.eu-west-2.rds.amazonaws.com'
host_port = 3306
username = 'team7'
password = 'multiteam07'
database_name = 'user'

def db_conn() :
    # db 연결 함수
    db = pymysql.connect(
        host=host_name,     # MySQL Server Address
        port=host_port,     # MySQL Server Port
        user=username,      # MySQL username
        passwd=password,    # password for MySQL username
        db=database_name,   # Database name
        charset='utf8'
    )
    return db

## 데이터 추출
def sel_item() : # db에서 data 추출 함수
    db = db_conn()
    sql = "select * from rasData WHERE date BETWEEN DATE_ADD(NOW(),INTERVAL -7 DAY ) AND NOW()" #1일 동안의 데이터 불러오기 (서버에 적용시 -1로 변경)
    df = pd.read_sql(sql,db)
    return df

def water_date() : # db에서 data 추출 함수
    db = db_conn()
    # sql = "select max(waterdate) from weather.plantmanage"  # 물 준 마지막 날짜 기록 가져오기 로컬
    sql = "select max(date) from user.rasData"  # 물 준 마지막 날짜 기록 가져오기 서버 예제
    # sql = "select max(waterdate) from user.plantmanage" # 물 준 마지막 날짜 기록 가져오기 서버(마지막엔 이걸로 연결해야해요!)
    df = pd.read_sql(sql,db)
    return df

def cal_date() :
    now = datetime.now()
    # datecompare = datetime.strptime(water_date().loc[0, 'max(waterdate)'], '%Y-%m-%d %H:%M') 로컬 테스트
    datecompare = water_date().loc[0, 'max(date)'].to_pydatetime() # 서버 rasData로 테스트
    # datecompare = water_date().loc[0, 'max(waterDate)'].to_pydatetime() # 서버 원래 위치 연결 (마지막엔 이걸로 연결해야해요!)
    date_diff = now - datecompare
    cd = date_diff.days
    return cd

def snapshot(request):
    time.sleep(1)
    image = open("/home/ubuntu/img/picam/woo.jpg","rb")
    return HttpResponse(image, content_type="image/jpg")