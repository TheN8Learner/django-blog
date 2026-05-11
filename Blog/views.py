from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Commentaire, Category
from .forms import commentaryMessage, contactMessage
from django.contrib import messages

def blog(request):
    posts = Post.objects.filter(is_published=True).order_by("-created_at")
    return render(request, 'blog.html', {"posts": posts})

def article_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    commentaires = Commentaire.objects.filter(post=post).order_by('created_at')
    form = commentaryMessage()

    if request.method == 'POST':
        form = commentaryMessage(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)  # ne sauvegarde pas encore
            commentaire.post = post                 # lie le commentaire au post
            commentaire.save()                      # maintenant on sauvegarde
            return redirect('article_details', pk=pk)

    return render(request, "article_details.html", {
        "post": post,
        "commentaires": commentaires,
        "form": form,
    })

def about(request):
    return render(request, "about.html")

def contact(request):
    form = contactMessage()
    if request.method == 'POST':
        form = contactMessage(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message envoyé ! Je vous répondrai bientôt.')
            return redirect('Blog')
    else:
        form = contactMessage()
    return render(request, 'contact.html', {'form': form})


def posts_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category= category, is_published=True).order_by('-created_at')
    return render(request, 'blog.html', {'posts': posts, 'category': category})