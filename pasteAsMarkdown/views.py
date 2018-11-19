from django.http import HttpResponse, HttpResponseRedirect
from django.forms import ModelForm
from django.shortcuts import render
from django.core.exceptions import ValidationError
from pasteAsMarkdown.models import Markdown
from django.views.generic.edit import FormView
import random, string


# Create your views here.

class MarkdownForm(ModelForm):
    class Meta:
        model = Markdown
        fields = ["markdownText", "url"]

class PasteAsMarkdownIndex(FormView):
    template_name = 'pasteAsMarkdown/form.html'
    form_class = MarkdownForm

    def post(self, request, *args, **kwargs):
        if request.POST['markdownText']:
            if request.POST['url']:
                if Markdown.objects.filter(url=request.POST['url']).exists():
                    return render(request, 'pasteAsMarkdown/form.html', { 'error': 'Url already used', 'form': MarkdownForm })
                t = Markdown(markdownText=request.POST['markdownText'], url=request.POST['url'])
            else:
                generatedUri = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
                while Markdown.objects.filter(url=generatedUri).exists():
                    generatedUri = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
                    pass
                t = Markdown(markdownText=request.POST['markdownText'], url=generatedUri)

            t.save()
            return HttpResponseRedirect(f"{t.url}")

def show(request, markdownUrl):
    m = Markdown.objects.get(url=markdownUrl)
    return render(request, 'pasteAsMarkdown/show.html', {
        'text': m.markdownText
    })
