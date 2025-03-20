from django.shortcuts import render
import os
import json
from django.conf import settings
from .models import UserPreference
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    currency_data=[]

    file_path= os.path.join(settings.BASE_DIR,'currencies.json')

    with open(file_path, 'r') as json_file:
        data=json.load(json_file)

        for k,v in data.items():
            currency_data.append({'name':k,'value':v})

    exists= UserPreference.objects.filter(user=request.user).exists()
    user_preferences= None
    if exists:
        user_preferences= UserPreference.objects.get(user=request.user)
    
    
    if request.method == 'GET':
        

        return render(request,"preferences/index.html",{"currencies":currency_data,'user_preferences':user_preferences})
    else:
        currency = request.POST['currency']
        if exists:

            user_preferences.currency= currency
            user_preferences.save()
        else:

            UserPreference.objects.create(user=request.user,currency=currency)
 
        messages.success(request,'Changes are saved')
        return render(request,"preferences/index.html",{"currencies":currency_data,'user_preferences':user_preferences})
    
def get_currency(user):
    UserPreference.objects.all()

    # user = User.objects.get(username=user.username)
    userpref= UserPreference.objects.filter(user=user).first()
    
    if(userpref):
        return userpref.currency
    else:
        return 'GBP'


#gpt code 
# from django.shortcuts import render
# import os
# import json
# from django.conf import settings
# from .models import UserPreference
# from django.contrib import messages
# from django.contrib.auth.models import User

# def index(request):
#     currency_data = []

#     # Corrected file path
#     file_path = os.path.join(settings.BASE_DIR, 'currencies.json')

#     # Debugging: Print the actual file path
#     print(f"Looking for currencies.json at: {file_path}")

#     # Ensure the file exists before reading
#     if not os.path.exists(file_path):
#         raise FileNotFoundError(f"File not found: {file_path}")

#     with open(file_path, 'r', encoding='utf-8') as json_file:
#         data = json.load(json_file)
#         for k, v in data.items():
#             currency_data.append({'name': k, 'value': v})

#     exists = UserPreference.objects.filter(user=request.user).exists()
#     user_preferences = None

#     if exists:
#         user_preferences = UserPreference.objects.get(user=request.user)

#     if request.method == 'GET':
#         return render(request, "preferences/index.html", {
#             "currencies": currency_data,
#             'user_preferences': user_preferences
#         })
#     else:
#         currency = request.POST.get('currency')

#         if exists:
#             user_preferences.currency = currency
#             user_preferences.save()
#         else:
#             UserPreference.objects.create(user=request.user, currency=currency)

#         messages.success(request, 'Changes are saved')
#         return render(request, "preferences/index.html", {
#             "currencies": currency_data,
#             'user_preferences': user_preferences
#         })

# def get_currency(user):
#     userpref = UserPreference.objects.filter(user=user).first()
#     return userpref.currency if userpref else 'GBP'
