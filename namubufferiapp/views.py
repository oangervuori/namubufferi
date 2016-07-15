from django.shortcuts import render, get_object_or_404, redirect
from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from models import UserProfile, Product, Category, Transaction
from forms import MoneyForm


# TODO: Create custom context processor to reduce context copy pasting

@login_required
def cover(request):
    context = dict(money_form=MoneyForm(),
                   products=Product.objects.all(),
                   categories=Category.objects.all(),
                   transactions=Transaction.objects.all(),
                   message="",
                   )

    return render(request, 'namubufferiapp/base_home.html', context)


@login_required
def buy_view(request):
    context = dict(money_form=MoneyForm(),
                   products=Product.objects.all(),
                   categories=Category.objects.all(),
                   transactions=Transaction.objects.all(),
                   message="",
                   )

    product = get_object_or_404(Product, pk=request.POST['product_key'])
    price = product.price
    request.user.userprofile.make_payment(price)

    new_transaction = Transaction()
    new_transaction.customer = request.user.userprofile
    new_transaction.amount = price
    new_transaction.product = product
    new_transaction.transaction_type = 'P'

    new_transaction.save()

    context['message'] = 'Ostit ' + str(price)

    return render(request, 'namubufferiapp/base_home.html', context)


@login_required
def deposit_view(request):
    context = dict(money_form=MoneyForm(),
                   products=Product.objects.all(),
                   categories=Category.objects.all(),
                   transactions=Transaction.objects.all(),
                   message="",
                   )

    if request.method == 'POST':
        money_form = MoneyForm(request.POST)
        context['money_form'] = money_form
    if money_form.is_valid():
        amount = request.POST['amount']
        request.user.userprofile.make_deposit(amount)

        new_transaction = Transaction()
        new_transaction.customer = request.user.userprofile
        new_transaction.amount = amount
        new_transaction.transaction_type = 'D'
        new_transaction.save()

        context['message'] = 'Lisasit ' + str(amount)

    return render(request, 'namubufferiapp/base_home.html', context)


def register(request):
    """
    Check:
    http://www.djangobook.com/en/2.0/chapter14.html
    http://ipasic.com/article/user-registration-and-email-confirmation-django/
    https://docs.djangoproject.com/en/1.7/topics/email/

    """
    context = dict(signin_form=AuthenticationForm(),
                   register_form=UserCreationForm(),
                   message="",
                   )

    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        context['register_form'] = register_form
        if register_form.is_valid():
            new_user = register_form.save()

            new_profile = UserProfile()
            new_profile.user = new_user
            new_profile.save()
            context['message'] = 'Rekisteroityminen onnistui. Voit kirjautua sisaan.'

    return render(request, 'namubufferiapp/base_login.html', context)
