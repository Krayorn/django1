from django.http import HttpResponse, HttpResponseRedirect
from django.forms import ModelForm
from django.shortcuts import render
from pasteAsMarkdown.models import Markdown
from django.views.generic.edit import FormView

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
            t = Markdown(markdownText=request.POST['markdownText'], url=request.POST['url'])
            t.save()
            return HttpResponseRedirect(f"{t.url}")

def show(request, markdownUrl):
    m = Markdown.objects.get(url=markdownUrl)
    return render(request, 'pasteAsMarkdown/show.html', {
        'text': m.markdownText
    })
