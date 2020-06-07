from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Message(models.Model):
    '''
    1. sender (owner)
    2. receiver
    3. message
    4. subject
    5. creation date  
    '''
    message_id = models.AutoField(primary_key=True,default=None)
    when = models.DateTimeField("date created", auto_now_add=True)
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    subject = models.CharField(max_length=200) 
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return "asd"   
    def todict(self):
        return {key:getattr(self, key) for key in [
            'message_id',
            'sender',
            'receiver',
            'message',
            'subject',
            'when',
            'is_read'
        ] }  