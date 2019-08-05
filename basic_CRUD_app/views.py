from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from basic_CRUD_main.settings import db
from bson import ObjectId
import time
from datetime import datetime







def login_page(request):
    return render(request, 'dashboard/login.html')


def admin_tasks_page(request, id):
    return render(request, 'dashboard/superadmin_tasks.html', context={"id": id})

def user_tasks_page(request, id):
    return render(request, 'dashboard/user_tasks.html', context={"id": id})



def admin_add_tasks_page(request, id):
    return render(request, 'dashboard/addTasks.html', context={"id": id})


def addTaskLogic(request, id):
    data = {
        "userId": ObjectId(id),
        "title": request.POST.get('title'),
        "description": request.POST.get('desc'),
        "timing": request.POST.get('startdate'),
        "statusCode": 0,
        "statusMsg": "pending",
        "createdAt": time.time(),
        "modifiedAt": "",
        "isDeleted": False
    }
    db.tasks.insert(data)
    detailsDB = db.superAdmin.find({"_id": ObjectId(id)}).count()
    if detailsDB > 0:
        return redirect('/superadmin/tasks/'+id)
    else:
        return redirect('/user/tasks/'+id)



class LoginAPI(APIView):
    def post(self, request):
        '''
                API to Login a User with respected credentials

        '''
        print(request.data)
        try:
            if int(request.data['identity']) == 0:
                detailsDB = db.superAdmin.find({'email': request.data['email'], 'password': request.data['password'], "statusCode": 1})
            else:
                detailsDB = db.users.find({'email': request.data['email'], 'password': request.data['password'], "statusCode": 1})

            if detailsDB.count() > 0:
                for item in detailsDB:
                    data = {
                        "message": "Authorized User..!!",
                        'id': str(item['_id']),
                        'identity': int(request.data['identity'])
                    }
                    print(data)
                    return JsonResponse(data, safe=False, status=200)
            else:
                data = {
                    "message": "Incorrect usernamne or password"
                }

                return JsonResponse(data, safe=False, status=404)
        except:
            data = {
                "message": "Internal Server Error"
            }
            return JsonResponse(data, safe=False, status=500)

class TasksAPI(APIView):
    def get(self, request):
        '''
                API to list out all the tasks

        '''
        # try:
        if 'HTTP_USERID' in request.META:
            tasksDB = db.tasks.find({"userId": ObjectId(request.META['HTTP_USERID']), "isDeleted": False})
        else:
            tasksDB = db.tasks.find({})
        if tasksDB.count() > 0:
            data = []
            for item in tasksDB:
                usersDB = db.users.find({"_id": item['userId']})
                if usersDB.count() > 0:
                    for user in usersDB:
                        data.append({
                            "id": str(item['_id']),
                            "userId": str(item['userId']),
                            "userName": str(user['email']),
                            "title": str(item['title']),
                            "description": str(item['description']),
                            "timing": str(item['timing']),
                            "statusMsg": str(item['statusMsg']),
                            "createdAt": datetime.utcfromtimestamp(item['createdAt']).strftime('%Y-%m-%d %H:%M:%S'),
                            "modifiedAt": datetime.utcfromtimestamp(item['modifiedAt']).strftime(
                                '%Y-%m-%d %H:%M:%S') if len(str(item['modifiedAt'])) > 0 else "",
                            "isDeleted": str(item['isDeleted']),
                        })
                else:
                    print("no user found..!!")
                    usersDB = db.superAdmin.find({"_id": item['userId']})
                    if usersDB.count() > 0:
                        for user in usersDB:
                            data.append({
                                "id": str(item['_id']),
                                "userId": str(item['userId']),
                                "userName": str(user['email']),
                                "title": str(item['title']),
                                "description": str(item['description']),
                                "timing": str(item['timing']),
                                "statusMsg": str(item['statusMsg']),
                                "createdAt": datetime.utcfromtimestamp(item['createdAt']).strftime('%Y-%m-%d %H:%M:%S'),
                                "modifiedAt": datetime.utcfromtimestamp(item['modifiedAt']).strftime(
                                    '%Y-%m-%d %H:%M:%S') if len(str(item['modifiedAt'])) > 0 else "",
                                "isDeleted": str(item['isDeleted']),
                            })
                    else:
                        print("no user or superadmin found..!!")

            response_message = {
                "message": "Authorized User..!!",
                'data': data,
            }
            return JsonResponse(response_message, safe=False, status=200)
        else:
            data = {
                "message": "No Data Found"
            }

            return JsonResponse(data, safe=False, status=404)
        # except:
        #     data = {
        #         "message": "Internal Server Error"
        #     }
        #     return JsonResponse(data, safe=False, status=500)


class TaskActionAPI(APIView):
    def delete(self, request, id):
        '''
                API to delete tasks

        '''
        detailsDB = db.tasks.find({'_id': ObjectId(id)})
        if detailsDB.count() > 0:
            db.tasks.update_one({
                '_id': ObjectId(id)
            }, {
                '$set': {
                    'isDeleted': True,
                }
            }, upsert=False)

            data = {
                "message": "task deleted..!!",
            }
            return JsonResponse(data, safe=False, status=200)
        else:
            data = {
                "message": "No data found"
            }
            return JsonResponse(data, safe=False, status=404)