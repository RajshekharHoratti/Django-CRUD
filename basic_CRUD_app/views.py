from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from basic_CRUD_main.settings import db





def login_page(request):
    return render(request, 'dashboard/login.html')


def admin_dashboard_page(request, id):
    return render(request, 'dashboard/adminDashboard.html', context={"id": id})



def admin_tasks_page(request, id):
    return render(request, 'dashboard/adminDashboard.html', context={"id": id})


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
