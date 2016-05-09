from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from notes.models import Document
from .forms import DocumentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def documents_list(request):
    title = "需求連絡單列表"
    obj_list = Document.objects.all()

    paginator = Paginator(obj_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        obj = paginator.page(paginator.num_pages)

    return render(request, "documents_list.html", locals())

def documents_create(request):
    title = "填寫需求連絡單"
    form = DocumentForm( request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    return render(request, "documents_create.html", locals())

def documents_detail(request, id):
    print(id)
    title = "需求連絡單列表"
    obj = Document.objects.all()

    return render(request, "documents_list.html", locals())

def documents_update(request):
    title = "需求連絡單列表"
    obj = Document.objects.all()

    return render(request, "documents_list.html", locals())

def documents_delete(request):
    title = "需求連絡單列表"
    obj = Document.objects.all()

    return render(request, "documents_list.html", locals())







def hello(request):
    greeting = "Welcome Django Home Page"

    #return HttpResponse("Welcome Django Index Page")
    return render(request, "index.html", locals() )



def myDevies(request):
    values = request.META.items()
    #values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
