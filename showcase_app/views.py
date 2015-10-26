from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, FormView, UpdateView
from showcase_app.models import UserProfile
from showcase_app.forms import ContactForm, UserProfileForm
from django.core.urlresolvers import reverse

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
                ['chrissiegman@yahoo.com'],
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

class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user

class UserProfileEditView(UpdateView):
    model = UserProfile
    fields = ['bio']
























