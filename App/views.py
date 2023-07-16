from math import ceil
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from . models import Song,Playlist,Category,UserSong,Queue
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

def home(request):
    user = request.user
    categories = Category.objects.all().order_by('priority')
    data = []
    for cat in categories:
        if cat.public==False and cat.name!=user.username:
            continue
        playlists=Playlist.objects.filter(category=cat)
        n = len(playlists)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        data.append([playlists, range(1, nSlides), nSlides, cat.name])
    params = {'data':data,'signin':0}
    if request.user.is_authenticated:
        params['signin']=1
    return render(request,"home.html",params)

def playlist(request,id):
    p = Playlist.objects.filter(id=int(id))
    params={'playlist':p[0]}
    return render(request,'playlist.html',params)

def likedsongs(request):
    return HttpResponse("likedsongs")

def register(request):
    if request.user.is_authenticated:
        messages.info(request,'you are already registered')
        return redirect('/')
    params={'username':'','first_name':'','last_name':'','email':'','pss1':'','pss2':''}
    if(request.method=="GET"):
        return render(request,"register.html",params)
    params['username'] = request.POST['username']
    params['first_name'] = request.POST['first_name']
    params['last_name'] = request.POST['last_name']
    params['email'] = request.POST['email']
    params['pss1'] = request.POST['password1']
    params['pss2'] = request.POST['password2']
    if(User.objects.filter(username=params['username']).exists()):
        messages.info(request,'username already exists')
        return render(request,"register.html",params)
    if(User.objects.filter(email=params['email']).exists()):
        messages.info(request,'email already exists')
        return render(request,"register.html",params)
    if(params['pss1']!=params['pss2']):
        messages.info(request,'password is not same in both column')
        return render(request,"register.html",params)
    if(len(params['pss1'])<5):
        messages.info(request,'password should be of atleast 5 characters')
        return render(request,"register.html",params)
    user = User.objects.create_user(username=params['username'],password=params['pss1'],first_name=params['first_name'],last_name=params
    ['last_name'],email=params['email'])
    user.save()
    auth.login(request,user)
    messages.info(request,"you are successfully registered")
    return redirect('/')

def login(request):
    if request.user.is_authenticated:
        messages.info(request,'you are already logined')
        return redirect('/')
    params={'username':'','pss':''}
    if(request.method=="GET"):
        return render(request,"login.html",params)
    params['username'] = request.POST['username']
    params['pss'] = request.POST.get('password', False)
    user = auth.authenticate(username=params['username'],password=params['pss'])
    if user is None :
        messages.info(request,"credentials does not match")
        return render(request,"login.html",params)
    auth.login(request,user)
    messages.info(request,"you are successfully logined")
    return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')

def song(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)

def playsong(request):
    if not request.user.is_authenticated:
        messages.info(request,"please login first before playing a song")
        return redirect("/")
    # queue = Queue.objects.filter(user=request.user)[0]
    # queue.pointer+=1
    # queue.save()
    # print(queue.pointer)
    # print(Queue.objects.filter(user=request.user)[0].pointer)
    paginator= Paginator(Queue.objects.filter(user=request.user)[0].songs.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # for item in page_obj:
    #     print(item.image)
    context={"page_obj":page_obj}
    return render(request,"playsong.html",context)

def queue(request):
    if not request.user.is_authenticated:
        messages.info(request,"please login first to access queue")
        return redirect("/")
    queue = Queue.objects.filter(user=request.user)
    params = {"queue":queue[0]}
    return render(request,"queue.html",params)