from django.shortcuts import render,redirect
from  googletrans import Translator
from WebApp.models import Feedback
from django.contrib import messages





def translator(request):

    return render(request,'index.html')


def translated(request):
    text= request.POST.get('text')
    lang = request.POST.get('lang')
    trans=Translator()
    dt=trans.detect(text)
    dt2=dt.lang
    translated=trans.translate(text,lang)
    tr=translated.text
    if lang=='hi':
        return render(request, 'translated.html', {"translated": tr, "e_language": dt2, "t_lang": "Hindi"})
    elif lang=='en':
        return render(request, 'translated.html', {"translated": tr, "e_language": dt2, "t_lang": "English"})
    elif lang == 'gu':
        return render(request, 'translated.html', {"translated": tr, "e_language": dt2, "t_lang": "Gujurati"})
    elif lang == 'bn':
        return render(request, 'translated.html', {"translated": tr, "e_language": dt2, "t_lang": "Bangala"})
    elif lang == 'or':
        return render(request, 'translated.html', {"translated": tr, "e_language": dt2, "t_lang": "Odia"})
    else:
        return render(request, 'translated.html', {"translated": tr, "e_language": dt2, "t_lang": lang})


def feedback(request):
    return render(request,'feedback.html')


def save(request):
    fn=request.POST.get("firstname")
    ln=request.POST.get("lastname")
    mail=request.POST.get("mailid")
    country=request.POST.get("country")
    feedback=request.POST.get("subject")
    data=Feedback(first_name=fn,last_name=ln,mail_id=mail,country=country,feedback=feedback).save()
    messages.success(request,'Saved Successfully')
    return render(request,"feedback.html")
