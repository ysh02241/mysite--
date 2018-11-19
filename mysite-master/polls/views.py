from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question

def vote(request,question_id):
    select = request.POST['select']

    q=Question.objects.get(id=question_id)
    c=q.choice_set.get(id=select)
    c.votes += 1
    c.save()

    print(select)

    return render(request,'polls/result.html',{'q':q})




def datail(request,question_id):
    q = Question.objects.get(id=question_id)
    c = q.choice_set.all()
    #choice = ''
    #for a in c:
    #    choice += a.choice_text

   # 렌더사용법(외우기) request 템플릿  컨텍스트(데이터/모델)
    return render(request,'polls/detail.html',
                  {
                      'question':q.question_text,
                      'choice':c
                  })

    #Question이 가진 변수명을 get()에 넣는것이 보통.
    #조건에 맞는 데이터 1개


    #return HttpResponse(q.question_text + '<br>' + choice)
    #return HttpResponse('id는 %s' % question_id)

def datail2(request,num1,num2):
    return HttpResponse(num1+num2)


def datail3(request,num1):
    return HttpResponse('메롱 %s' % num1)


def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html',{'question': questions})


    # 1번 create를 이용하여 데이터 입력
    # Question.objects.create()

    # 2번 save를 이용하여 데이터 입력
    # Question(question_text='aaaa', pub_date=timezone.now()).save()

'''
    q = Question.objects.all()[0]
    choices = q.choice_set.all()

    print(q.question_text)
    print(choices[0].choice_text)
    print(choices[1].choice_text)
    print(choices[2].choice_text)
'''

