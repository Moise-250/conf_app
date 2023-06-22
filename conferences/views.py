from django.shortcuts import render

def conference_list(request):
    return render(request, 'conferences/conference_list.html')

def conference_create(request):
    return render(request, 'conferences/conference_create.html')

def conference_detail(request, pk):
    return render(request, 'conferences/conference_detail.html')

def conference_update(request, pk):
    return render(request, 'conferences/conference_update.html')

def conference_delete(request, pk):
    return render(request, 'conferences/conference_delete.html')

]


# Create your views here.
