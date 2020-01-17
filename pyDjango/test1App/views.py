from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .models import Question

def index(request):
    '''

    :param request:
    :return:
    late_question_list : 该变量应与index.html中 if xxx 、 for xxx 对应
    '''
    # return HttpResponse('Hello!')

    # latest_question_list = Question.objects.order_by('-pub_time')[:5]
    # output = ', '.join([q.question_text for q in last_question_list])
    # return HttpResponse(output)

    # template = loader.get_template('test1App/index.html')
    # return HttpResponse(template.render(contexts,request))
    late_question_list = Question.objects.order_by('-pub_time')[:5]
    context = {'late_question_list': late_question_list}
    return render(request, 'test1App/index.html', context)

def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'test1App/detail.html', {'question': question})

def results(request, question_id):
    # return HttpResponse("You're looking at the results of question %s." % question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'test1App/results.html',{'question': question})

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except Exception:
        return render(request,'test1App/detail.html', {'question': question, 'error_message': 'No Choice'})
        # pass
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('test1App:results', args=(question_id,)))