from django.shortcuts import render, get_object_or_404, redirect
from conversation.models import Conversation
from item.models import Item
from .forms import ConverstionMessageForm
from django.contrib.auth.decorators import login_required

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    # Prevent the item creator from starting a conversation with themselves
    if item.created_by == request.user:
        return redirect('dashboard:index')

    # Check if the user is already part of a conversation related to this item
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    
    if conversations.exists():
        
        # Redirect to an existing conversation if found
        return redirect('conversation:detail', pk=conversations.first().id)  # Redirect to the existing conversation
    
    if request.method == 'POST':
        form = ConverstionMessageForm(request.POST)
        
        if form.is_valid():
            # Create a new conversation
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            # Create and save the first message in the conversation
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            # Redirect to the item detail page after creating the conversation and message
            return redirect('item:detail', pk=item_pk)
    else:
        form = ConverstionMessageForm()

    # Render the form for a new conversation if not a POST request or if the form is invalid
    return render(request, 'conversation/new.html', {'form': form})


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    return render(request, 'conversation/inbox.html',{
        'conversations':conversations 
    })



@login_required
def detail(request,pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    
    if request.method =='POST':
        form = ConverstionMessageForm (request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            conversation.save()
            
            return redirect ('conversation:detail', pk=pk)
    else:
            form = ConverstionMessageForm()
             
    
    return render (request, 'conversation/detail.html',{
        'conversation':conversation,
        'form':form
    })
    