from django import forms
from .models import qasession, question, answer, comment
from django.core.exceptions import ObjectDoesNotExist


class addsessForm(forms.Form):
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',

        }
    ))

    detail = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': '4',
            'cols': '100',

        }
    ))

    def save(self, uid):
        qasession.objects.create(name=self.cleaned_data['name'],
                                 teacher_id=uid,
                                 detail=self.cleaned_data['detail'],
                                 )

class addquesForm(forms.Form):
    content = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': '2',
            'cols': '50',
            'placeholder': 'Add a question'



        }
    ))

    def __init__(self, *args, **kwargs):
        super(addquesForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ""



    def save(self, uid, sid):
        qa = qasession.objects.get(id=sid)
        if qa.status == 0:
            question.objects.create(owner_id=uid,
                                    qa_id=sid,
                                    content=self.cleaned_data['content'])

class addAnswerForm(forms.Form):
    content = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': '1',
            'cols': '40',
            'placeholder': 'Write answer'



        }
    ))

    def __init__(self, *args, **kwargs):
        super(addAnswerForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ""



    def save(self, uid, qid):

            answer.objects.create(owner_id=uid,
                                  ques_id=qid,
                                  content=self.cleaned_data['content'])

class addCmForm(forms.Form):
    content = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': '1',
            'cols': '50',
            'placeholder': 'Add a comment'



        }
    ))

    def __init__(self, *args, **kwargs):
        super(addCmForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ""



    def save(self, uid, aid):
        comment.objects.create(owner_id=uid,
                               ans_id=aid,
                               content=self.cleaned_data['content'])
