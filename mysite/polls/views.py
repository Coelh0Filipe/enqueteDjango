from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.urls import reverse

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order.by(' -pub_date)')[:5]
    context = {'latest_question_list':latest_question_list}
    return HttpResponse("Olá, esse é o meu primeiro site!")

def results(request, question_id):
    question = Question(pk=question_id)
    return HttpResponse ('Essa é a pergunta de número %s %question_id')

def vote (request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return render(request, 'polls/vote.html', {
            'question': question,
            'error_message': "Você não selecionou uma alternativa.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))