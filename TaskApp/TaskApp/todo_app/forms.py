from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from TaskApp.todo_app.models import Book
from django.forms import modelform_factory, modelformset_factory
from django.contrib.auth.forms import UserCreationForm


class SomeForm(forms.Form):
    username = forms.CharField(max_length=10)
    email = forms.EmailField()
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        cleaned_password = cleaned_data.get('confirm_password')

        if password != cleaned_password:
            raise forms.ValidationError("There is a mismatch between the passwords")

        return cleaned_data


class NameForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    def clean(self):
        cleaned_data = super().clean()

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            raise forms.ValidationError('First name and last name should not be the same.')


class ContactForm(forms.Form):
    username = forms.CharField(max_length=10)
    email = forms.EmailField()


class NewsletterForm(forms.Form):
    email = forms.EmailField()


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get['price']

        if price and price < 0:
            raise forms.ValidationError("The price field cannot be negative")
        return price

        authors = []
        for author in authors:
            name = self.cleaned_data.get('')

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author[0].isupper:
            raise forms.ValidationError('Author should start with capitalized letter!')
        return author


class BaseBookFormSet(forms.BaseModelFormSet):
    def clean(self):
        authors = []
        for form in self.forms:
            author = form.cleaned_data.get('author')
            if author in authors:
                raise forms.ValidationError('Duplicate authors are not allowed')
            authors.append(author)


BookFormSet = modelformset_factory(Book, BaseBookFormSet, fields=('title', 'author',), extra=3)


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Oops, this email address is already taken.')

        return email
