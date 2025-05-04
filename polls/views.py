from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # context = ", ".join([q.question_text for q in latest_question_list])
    context = {'latest_question_list': latest_question_list} # Making this a dictionary, wasted so much time fixing issue related to this
    return render(request, 'polls/index.html', context)

# for the dj4e mooc assignment
def owner(request: HttpRequest) -> HttpResponse:
        response = HttpResponse()
        response.write("Hello, world. 141590c8 is the polls index.")
        return response

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, "polls/detail.html", {"question": question})

    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)