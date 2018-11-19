from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.core.exceptions import ValidationError
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
import numpy as np


def Wolf(x):
    buffer = []
    rule = int(x)
    rules = list(f"{rule:08b}")
    rules = [ int(x) for x in rules ]
    A = np.zeros((40, 79), dtype = int)

    A[0, 39] = 1

    def executeRules(a, b, c):
        if a == 1 and b == 1 and c == 1:
            return rules[0]
        if a == 1 and b == 1 and c == 0:
            return rules[1]
        if a == 1 and b == 0 and c == 1:
            return rules[2]
        if a == 1 and b == 0 and c == 0:
            return rules[3]
        if a == 0 and b == 1 and c == 1:
            return rules[4]
        if a == 0 and b == 1 and c == 0:
            return rules[5]
        if a == 0 and b == 0 and c == 1:
            return rules[6]
        if a == 0 and b == 0 and c == 0:
            return rules[7]
        return 0

    for i, row in enumerate(A):
        if(i != 0):
            for j in range(len(A[i])):
                if j is 0:
                    a = 0
                else:
                    a = A[i-1, j-1]

                b = A[i-1, j]

                if j is len(row) - 1:
                    c = 0
                else:
                    c = A[i-1, j+1]
                A[i, j] = executeRules(a, b, c)
        line = ""
        for _, letter in enumerate(A[i]):
            if int(letter) is 0:
                line = line + "."
            else:
                line = line + "#"
        buffer.append(line)
    return '\n'.join(buffer)

class RuleForm(forms.Form):
    rule_number = forms.IntegerField(min_value=0, max_value=256)

class ElementaryCellularAutomata(FormView):
    template_name = 'elementaryCellularAutomata/form.html'
    form_class = RuleForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        rule_number = int(request.POST['rule_number'])
        if not 0 <= rule_number <= 256:
            rule_number = 90

        value = Wolf(rule_number)
        return render(request, 'elementaryCellularAutomata/form.html', {
            'string': value,
            'rule_number': rule_number,
            'form': self.form_class,
        })

