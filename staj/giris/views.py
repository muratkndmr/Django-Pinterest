from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages





def indexPage(request):
    if request.method == "POST":
        if 'login1' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("anasayfa")
            else:
                messages.warning(request,"kullanici adi veya sifre yanlis")
                return redirect("index")

        elif 'register1' in request.POST or 'registerDwn' in request.POST:  # Burada düzeltilmiş bir kontrol
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password")
            if not User.objects.filter(username=username).exists() and not User.objects.filter(email=email).exists():
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                messages.success(request, 'Kaydınız başarıyla oluşturuldu ')
                messages.success(request, 'Lütfen giriş yapınız ')
                return redirect("index")
    context = {
        'user': request.user  # Kullanıcı nesnesini context'e ekleyin
    }
    return render(request, 'index.html', context)








def anasayfa(request):
    return render(request,'anasayfa.html')


def busines(request):
    return render(request,'busines.html')

def profile(request):
    return render(request,'profile.html')

def setting(request):
    return render(request,'settings.html')
def account(request):
    return render(request,'includes/_account.html')
def profiVisibility(request):
    return render(request,'includes/_profiVisibility.html')
def history(request):
    return render(request,'includes/_history.html')
def claim(request):
    return render(request,'includes/_claim.html')
def permissions(request):
    return render(request,'includes/_permissions.html')
def notifications(request):
    return render(request,'includes/_notifications.html')
def privacy(request):
    return render(request,'includes/_privacy.html')
def security(request):
    return render(request,'includes/_security.html')
def brand(request):
    return render(request,'includes/_brand.html')
def addAccount(request):
    return render(request,'add-account.html')
def inNavbar(request):
    return render(request,'includes/_inNavbar.html')
def comments(request):
    return render(request,'includes/_comments.html')




def logoutUser(request):
    logout(request)
    return redirect("index")
# def registerUser(request):
  
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password1 = request.POST.get("password1")
#         print(username)

#         if not User.objects.filter(username=username).exists():
#             if not User.objects.filter(email=email).exists():
#                 user = User.objects.create_user(username=username, password=password1, email=email)
#                 user.save()
#                 return redirect("account")
       
#             else:
#                 messages.warning(request, 'Bu mail zaten kullanılıyor!!')
#                 return redirect("registerUser")
#         else:
#             messages.warning(request, 'Bu kullanıcı adı daha önceden alınmış!!')
#             return redirect("registerUser")
      
#     context = {}
#     return render(request,'index.html',context)
