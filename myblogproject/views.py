from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.views.generic.edit import CreateView, View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from posts.models import Post
from django.db.models import Q
from myblogproject.forms import ContactForm
from django.core.mail import EmailMessage
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        qs = None
        if query:
            qs = Post.objects.filter(
                    Q(title__icontains=query)
                )
        context = {"posts": qs}
        return render(request, "search.html", context)

def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['tanveerobjects@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'contactus.html', {
        'form': form_class,
    })