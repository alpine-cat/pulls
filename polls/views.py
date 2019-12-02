from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse

from django.views.decorators.http import require_GET
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from polls.models import Question, Choise
from .forms import QuestionForm, ChoiseModelForm
# Create your views here.


class IndexView(ListView):
    template_name = 'polls/index.html'
    model = Question
    context_object_name = 'latest_question_list'
    queryset = Question.objects.order_by('-question_text')


class DetailsView(DetailView):
    template_name = 'polls/details.html'
    model = Question
    context_object_name='question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = QuestionForm()
        context['model_form'] = ChoiseModelForm()
        return context

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})


def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    #form = QuestionForm(request.POST)
    choise = Choise.objects.get(id=1)
    form= ChoiseModelForm(request.POST, instance=choise)

    if  form.is_valid():
        form.save()
        data = form.cleaned_data['question_id']
        try:
            selected_choice = question.choise_set.get(id=request.POST['choise'])
        except (KeyError, Choise.DoesNotExist):
            return render(request, 'polls/details.html', {
                'question':question,
                'error_message':"You didn't select a choice",
            })
        else:
            selected_choice.votes+=1
            selected_choice.save()
            return HttpResponse(reverse('results', args=(question_id,)))
    return render(request, 'polls/detail.html', context={'form':form, 'question':question})

class ChoiseForm(FormView):
    template_name = 'polls/detail.html'
    form_class = ChoiseModelForm
    success_url = '/polls'


class ChoiseCreate(CreateView):
    model = Choise
    fields = ['question', 'choise_text']

    template_name = 'polls/details.html'
    success_url = 'polls/'