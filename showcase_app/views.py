from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from showcase_app.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

def index(request):
    return render(request, 'showcase_app/index.html', {})

def projects(request):
    return render(request, 'showcase_app/projects.html', {})

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            message = request.POST.get('message', '')

            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'message': message
            })

            content = template.render(context)

            email = EmailMessage(
                'New contact form submission',
                content,
                "Your website",
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return HttpResponse('Email Sent')
            #return render(request, 'showcase_app/projects.html', {})
            # should this be an HttpResponseRedirect?

        else:
            return HttpResponse('Error: form submission invalid.')
            #return render(request, 'showcase_app/projects.html', {})
    else:
        return render(request, 'showcase_app/contact.html', {'form': form_class})
