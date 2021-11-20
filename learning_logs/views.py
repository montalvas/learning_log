from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """Renderiza a página inicial"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Renderiza os assuntos"""
    topics = Topic.objects.order_by('data_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Renderiza um único assunto e todas as suas entradas"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,
               'entries': entries
               }
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Renderiza o cadastro de um novo assunto"""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = TopicForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
        
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Renderiza o cadastro de um novo registro"""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    
    context = {'topic': topic,
               'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """Renderiza a edição de um registro"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    topic_id = topic.id
    
    if request.method != 'POST':
        # Requisição inicial;
        # preenche previamente o formulário com a entrada atual
        form = EntryForm(instance=entry)
    else:
        # Dados de POST submetidos;
        # processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    
    return render(request, 'learning_logs/edit_entry.html', context)

    
