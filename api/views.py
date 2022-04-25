from asyncio.windows_events import NULL
from datetime import date, datetime,timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Washer.models import WashingMachine,Student
from .serializers import Serializer_Student, Serializer_Washing_Machine
from django.utils.timezone import make_naive

@api_view(['GET'])
def printer(request):
    deleter(request)
    WM = WashingMachine.objects.all()
    STU =Student.objects.all()
    WMS = Serializer_Washing_Machine(WM , many=True)
    STUS = Serializer_Student(STU , many=True)
    washing_machines = WMS.data
    students = STUS.data
    return Response({"Washin-machines":washing_machines , "Students":students})

@api_view(['PUT'])
def addStu(request):
    #print("hello")
    deleter(request)
    #print("Hi")
    serializer = Serializer_Student(data = request.data)
    if serializer.is_valid():
        serializer.save()
    WM = WashingMachine.objects.all()
    #WMS = Serializer_Washing_Machine(WM , many=True)
    washing_machines = WM
    S = serializer.data
    student = Student.objects.get(id = S.get('id'))
    found = 0
    for wms in washing_machines:
        if wms.floor==student.floor and wms.wing==student.wing and found==0:
            wms_occupation = wms.occupy
            if wms.occupation_status==False:
                found = 1
                machine = WashingMachine.objects.get(id= wms.id)
                machine.occupy = wms_occupation + student.I + '-'
                machine.occupation_status = True
                student.m_floor = wms.floor
                student.m_wing = wms.wing
                student.time_alloted = datetime.now()
                machine.occupied_at = datetime.now()
                print(type(datetime.now()))
                print(type(timedelta(minutes=5)))
                machine.occupied_till = (datetime.now() + timedelta(minutes=5))
                machine.save(update_fields=['occupy','occupation_status','occupied_at','occupied_till'])
                student.save(update_fields=['m_floor','m_wing','time_alloted'])
                
                break
        if wms.floor==student.floor and wms.wing!=student.wing and found==0:
            wms_occupation = wms.occupy
            if wms.occupation_status==False:
                found = 1
                machine = WashingMachine.objects.get(id= wms.id)
                machine.occupy = wms_occupation + student.I + '-'
                machine.occupation_status = True
                student.m_floor = wms.floor
                student.m_wing = wms.wing
                student.time_alloted = datetime.now()
                machine.occupied_at = datetime.now()
                machine.occupied_till = (datetime.now() + timedelta(minutes=5))
                machine.save(update_fields=['occupy','occupation_status','occupied_at','occupied_till'])
                student.save(update_fields=['m_floor','m_wing','time_alloted'])
                break
        if wms.floor!=student.floor and found==0:
            wms_occupation = wms.occupy
            if wms.occupation_status==False:
                found = 1
                machine = WashingMachine.objects.get(id= wms.id)
                machine.occupy = wms_occupation + student.I + '-'
                machine.occupation_status = True
                student.m_floor = wms.floor
                student.m_wing = wms.wing
                student.time_alloted = datetime.now()
                machine.occupied_at = datetime.now()
                machine.occupied_till = (datetime.now() + timedelta(minutes=5))
                machine.save(update_fields=['occupy','occupation_status','occupied_at','occupied_till'])
                student.save(update_fields=['m_floor','m_wing','time_alloted'])
                break
    if found==0:
            machine = WashingMachine.objects.get(floor = student.floor, wing = student.wing)
            machine.occupy = machine.occupy + student.I + '-'
            student.m_floor = machine.floor
            student.m_wing = machine.wing
            student.time_alloted = machine.occupied_till
            machine.occupied_till = make_naive(student.time_alloted) + (timedelta(minutes=5))
            machine.save(update_fields=['occupy','occupied_till'])
            student.save(update_fields=['m_floor','m_wing','time_alloted'])
            
    S1=Serializer_Student(student)
    return Response(S1.data)

def deleter(request):
    
    STU=Student.objects.all()
    WM=WashingMachine.objects.all()
    for stu in STU:
       
        if stu.time_alloted!=None and (datetime.now()-timedelta(minutes=5)).strftime('%H:%M:%S')>(stu.time_alloted).strftime('%H:%M:%S'):
            stu.delete()
    for wm in WM:
        
        if datetime.now().strftime('%H:%M:%S')>wm.occupied_till.strftime('%H:%M:%S'):
            print(wm.occupied_till.strftime('%H:%M:%S'))
            wm.occupation_status=False
            wm.occupied_at = datetime.min
            wm.occupied_till = datetime.min
            wm.occupy = '-'
            wm.save(update_fields=['occupy','occupation_status','occupied_at','occupied_till'])
