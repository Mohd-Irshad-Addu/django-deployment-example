from django.shortcuts import render


# Create your views here.
def index(request):
    context_dict={'text':'Hello world','number':'100'}
    return render(request,'temp_url_app_files/index.html',context_dict)


def other(request):
    return render(request,'temp_url_app_files/other.html')

def relative(request):
    return render(request,'temp_url_app_files/relative_url.html')

def thank_you(request):
    return render(request,'temp_url_app_files/thank_you.html')
