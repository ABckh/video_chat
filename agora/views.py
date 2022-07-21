from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse



class AgoraVideoCall(View):
    app_id=''
    channel = ''
    permission_class = 'AllowAny'
    channel_end_url = '/success/'
    title = 'Agora Demo'

    def get_permission(self,request,permission_class):
        if permission_class == 'AllowAny':
            return True
        elif permission_class == 'IsAuthenticated':
            return bool(request.user and request.user.is_authenticated)
        elif permission_class == 'IsAdmin':
            return bool(request.user and request.user.is_staff)
        else:
            return False
    
    def checkAppID(self,appId):
        if appId == '':
            return False
        else:
            return True
    
    def checkChannel(self,channel):
        if channel == '':
            return False
        else:
            return True

    def checkAll(self,request):
        if self.get_permission(request,self.permission_class) == True and self.checkAppID(self.app_id) == True  and self.checkChannel(self.channel) == True:
            return True
        else:
            return False
           

    def get(self,request):
        stat = self.checkAll(request)
        print(self.app_id,self.channel)
        if stat:
            return render(request,'index.html',{
                    'agora_id':self.app_id,
                    'channel':self.channel,
                    'channel_end_url':self.channel_end_url,
                    'title':self.title
                    })
        else:
            if not self.checkAppID(self.app_id):
                return HttpResponse('Programming Error: No App ID')
            elif not self.get_permissions(request):
                return HttpResponse('User Permission Error: No Permission')
            elif not self.checkChannel(request,self.channel):
                return HttpResponse('Programming Error: No Channel Name')
            return HttpResponse('Unknown Error')
        

# allowed_permissions = ['AllowAny','IsAuthenticated','IsAdmin']

class Agora(AgoraVideoCall):
    app_id=''
    channel = ''
    permission_class = 'AllowAny'
    channel_end_url = '/success/'
    title = 'Agora Demo'


