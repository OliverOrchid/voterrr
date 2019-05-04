from django.shortcuts import render,get_object_or_404


from django.http import HttpResponse,Http404,HttpResponseRedirect


from django.urls import reverse
from django.views import generic

from .models import Question,Choice

from django.utils import timezone
#####################################################

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




###################################################

# from django.template import loader
# Create your views here.


######Just For Test!!!###
# def home(request):
#     return HttpResponse("Home.")

# def shit(request):
#     return HttpResponse("Hello,world.You are at the polls\
#         index.")
#######################################################
# def index(request):
# def IndexView(generic.ListView):
#     latest_question_list = Question.objects.order_by(
#         '-pub_date')[:5]
#     # output = ','.join([q.question_text for q in 
#     #     latest_question_list])
#     # return HttpResponse("#############喜迎宾客###########")
#     # return HttpResponse(output)
#     # template = loader.get_template('nsp_polls/home.html')
    
#     context ={'latest_question_list': latest_question_list,}
#     return render(request,'polls/index.html', context)

# def detail(request,question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#         context = {'question':question}
#     except Question.DoesNotExist:
#         raise Http404("嗷~~该投票主题不存在哦~~")
#     return render(request, 'polls/detail.html',context )

#     # return HttpResponse("You are looking at question %s." %
#     #     question_id)


# def results(request,question_id):
#     # response = "You are looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         'question':question
#     }
#     return render(request, 'polls/results.html', context)



# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



    # # return HttpResponse("You are voting on question %s."
    # #     %question_id)
    # question = get_object_or_404(Question, pk=question_id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

######################################################
# 以上代码中有些内容还未在本教程中提到过：

# request.POST 是一个类字典对象，让你可以通过关键字的名字获取提交的数据。 这个例子中， request.POST['choice'] 以字符串形式返回选择的 Choice 的 ID。 request.POST 的值永远是字符串。

# 注意，Django 还以同样的方式提供 request.GET 用于访问 GET 数据 —— 但我们在代码中显式地使用 request.POST ，以保证数据只能通过 POST 调用改动。

# 如果在 request.POST['choice'] 数据中没有提供 choice ， POST 将引发一个 KeyError 。上面的代码检查 KeyError ，如果没有给出 choice 将重新显示 Question 表单和一个错误信息。

# 在增加 Choice 的得票数之后，代码返回一个 HttpResponseRedirect 而不是常用的 HttpResponse 、 HttpResponseRedirect 只接收一个参数：用户将要被重定向的 URL（请继续看下去，我们将会解释如何构造这个例子中的 URL）。

# As the Python comment above points out, you should always return an HttpResponseRedirect after successfully dealing with POST data. This tip isn't specific to Django; it's just good Web development practice.

# 在这个例子中，我们在 HttpResponseRedirect 的构造函数中使用 reverse() 函数。这个函数避免了我们在视图函数中硬编码 URL。它需要我们给出我们想要跳转的视图的名字和该视图所对应的 URL 模式中需要给该视图提供的参数。 在本例中，使用在 教程第 3 部分 中设定的 URLconf， reverse() 调用将返回一个这样的字符串：

# '/polls/3/results/'
# 其中 3 是 question.id 的值。重定向的 URL 将调用 'results' 视图来显示最终的页面。

#########################################################
