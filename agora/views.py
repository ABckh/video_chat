from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse

import time
import secrets

from connection.agora_key.RtcTokenBuilder import RtcTokenBuilder, Role_Attendee


class AgoraVideoCall(View):
    app_id='a92dcfe3b54442f29716549a58080bf9'
    appCertificate = '43e2c04734274caf9b9461570643e9f7'
    channel = ''
    permission_class = 'AllowAny'
    uid = '' # User ID
    expire_time = 3600
    currentTimestamp = int(time.time())
    privilegeExpiredTs = currentTimestamp + expire_time


    channel_end_url = '/'

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
        if self.get_permission(request,self.permission_class) == True and self.checkChannel(self.channel) == True:
            return True
        else:
            return False
           

    def get(self,request):
        stat = self.checkAll(request)
        print(self.app_id,self.channel)
        if stat:
            token = RtcTokenBuilder.buildTokenWithUid(self.app_id,self.appCertificate, self.channel, self.uid, Role_Attendee, self.privilegeExpiredTs)
            print(token)

            return render(request,'index.html',{
                    'agora_id':self.app_id,
                    'channel':self.channel,
                    'channel_end_url':self.channel_end_url,
                    'token': token,
                    'user_id': self.uid,
                    })
        else:

            if not self.get_permissions(request):
                return HttpResponse('User Permission Error: No Permission')
            elif not self.checkChannel(request,self.channel):
                return HttpResponse('Programming Error: No Channel Name')
            return HttpResponse('Unknown Error')
        


class Agora(AgoraVideoCall):
    app_id='a92dcfe3b54442f29716549a58080bf9'
    channel = ''
    permission_class = 'AllowAny'
    uid = '' # User ID
    expire_time = 3600
    currentTimestamp = int(time.time())
    privilegeExpiredTs = currentTimestamp + expire_time
    channel_end_url = '/'

