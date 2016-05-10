from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, Question
from .forms import NameForm
from .forms import NameAndFile

from collections import OrderedDict
from wsgiref.util import FileWrapper

import StringIO


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def get_name(request):
    # if  this is a POST qeuset we need to process the form data.
    if request.method == 'POST':
        # create a form instance and populate it with data from the request.
        form = NameForm(request.POST)
        if form.is_valid():
            return render(request, 'polls/thanks.html', form.cleaned_data)
    # If a GET or any other method) we'll create a blank form.
    else:
        form = NameForm()

    return render(request, 'polls/name.html', {'form': form})

def handle_data(product_data, ticket_data):

    products = [product.decode('utf-8').strip() for product in product_data]
    tickets = [ticket.decode('utf-8').strip() for ticket in ticket_data]

    return products, tickets

def test(request):

    DELIMITER = ','

    data_dict = request.session['data_dict']
    products = data_dict['products']
    tickets = data_dict['tickets']

    if request.method == 'POST':
        checked = reversed(request.POST.getlist('checkbox'))
        result = OrderedDict()
        for data in checked:
            index_camera, index_ticket = [int(token) for token in
                    data.split(DELIMITER)]
            current_camera = products[index_camera]
            camera_list = result.get(current_camera)
            if not camera_list:
                result[current_camera] = camera_list = []
            camera_list.append(tickets[index_ticket])

        myfile = StringIO.StringIO()
        line_buffer = []
        for product, ticket_list in result.items():
            line_buffer.append(product)
            line_buffer.append('='*len(product))
            for ticket in reversed(ticket_list):
                line_buffer.append(ticket)
            line_buffer.append('\n')
        myfile.write('\n'.join(line_buffer).strip())

        response = HttpResponse(content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=file.pre'
        response.write(myfile.getvalue())
        return response
    else:
        table = []

        table = [['']+products] # inital product header.
        for row_index, ticket_text in enumerate(tickets):
            row = [ticket_text]
            for col_index, _ in enumerate(products):
                row.append("{}{}{}".format(col_index, DELIMITER, row_index))
            table.append(row)

        return render(request, 'polls/display_info.html', {'table': table})

def get_name_and_file(request):
    if request.method == 'POST':
        print('post')
        form = NameAndFile(request.POST, request.FILES)
        if form.is_valid():

            raw_products = form.cleaned_data['products_file'].readlines()

            raw_tickets = form.cleaned_data['tickets_file'].readlines()
            products, tickets = handle_data(raw_products, raw_tickets)

            data_dict = {
                         'products': products,
                         'tickets': tickets,
                        }

            request.session['data_dict'] = data_dict
            return HttpResponseRedirect('test')
    else:
        form = NameAndFile()

    return render(request, 'polls/name_and_file.html', {'form': form})
