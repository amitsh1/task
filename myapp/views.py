from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse,JsonResponse

from .models import Message
import json
@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're aat the polls index.")

@csrf_exempt
def get_all_messages(request):
    return JsonResponse(
        {
            "messages":[x.todict() for x in 
            get_messages()
            ]
            }
        )      



@csrf_exempt
def get_all_messages_for_receiver(request,receiver):
    return JsonResponse(
        {
            "messages":[x.todict() for x in 
            get_messages(receiver=receiver) 
            ]  
            }
        )      


@csrf_exempt
def get_unread_messages_for_receiver(request,receiver):
    return JsonResponse(
        {
            "messages":[x.todict() for x in 
            get_messages(receiver=receiver,filter_read=False)
            ] 
            }
        )      
 

@csrf_exempt
def read_message(request,message_id):
    message = Message.objects.filter(message_id=message_id)
    if list(message)!=[]:
        message=message[0]    
        message.is_read = True
        message.save()
        return JsonResponse(
            message.todict()
            ) 
    else:
        return JsonResponse(
                    {"message":f"no unread messages for message_id: {message_id}"}
                    )         

@csrf_exempt
def delete_message(request,message_id):
    message = Message.objects.filter(message_id=message_id)
    if list(message)!=[]:
        message=message[0]
        message.delete()
        return JsonResponse(
                    {"message":"deleted"}
                    )
    else:
        return JsonResponse(
                    {"message":f"no unread messages for message_id: {message_id}"}
                    )  
@csrf_exempt
def write_message(request,**kwargs):
    if request.method == 'POST': 
        kwargs = json.loads(request.body)
        message = Message(**kwargs)
        message.save()
        return HttpResponse("message written\n")    


def get_messages(receiver=None,filter_read=None):
    # t = str(len(Message.objects.get()))
    kwargs = {}
    if receiver:
        kwargs['receiver']=receiver
    if filter_read!=None:
        kwargs['is_read']=filter_read

    return Message.objects.filter(**kwargs)
    return 
        # return HttpResponse("Hello, world. You're at the polls index.")
    return JsonResponse(
        {
            "messages":[x.todict() for x in Message.objects.filter(**kwargs)]
            }
        )        