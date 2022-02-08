from django.shortcuts import render, redirect, get_object_or_404

from polls.models import *
from polls.forms import *

# Create your views here.


def isMajor(age: int) -> str:
    return 'Majeur' if self.age > 18 else 'Mineur'


def index(request, *args, **kwargs):
    template_name = 'index.html'
    age = 18
    name = 'Ali'
    sex = 'Masculin'
    country = 'Senegal'

    persons = Person.objects.all()
    magasins = Magasin.objects.all()
    profile_magasins = ProfileMagasin.objects.all()
    # produits = Produit.objects.all()
    persons_name = Person.objects.filter(name__contains='O')
    persons_major = Person.objects.filter(age__gt=18)

    context = {
        'age': age,
        'name': name,
        'sex': sex,
        'country': country,
        'persons': persons,
        'persons_major': persons_major,
        'persons_name': persons_name,
        'magasins': magasins,
        'profile_magasins': profile_magasins,
        # 'produits': produits,
    }

    return render(
        request=request,
        template_name=template_name,
        context=context
    )


def update_person(request, *args, **kwargs):
    template_name = 'update-person.html'
    obj = get_object_or_404(
        Person,
        pk=kwargs.get('pk')
    )
    if request.method == 'GET':
        form = PersonForm(
            initial={
                'name': obj.name,
                'age': obj.age,
            }
        )
        context = {
            'form': form
        }

        return render(
            request=request,
            template_name=template_name,
            context=context
        )

    if request.method == 'POST':
        form = PersonForm(
            request.POST,
            request.FILES,
            initial={
                'name': obj.name,
                'age': obj.age,
            }
        )
        context = {
            'form': form
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.sex = form.cleaned_data.get('sex')
            obj.age = form.cleaned_data.get('age')
            obj.country = form.cleaned_data.get('country')
            obj.save()
            return redirect('home')

        return render(
            request=request,
            template_name=template_name,
            context=context
        )


def add(request):

    template_name = 'add.html'
    context = {}

    form1 = PersonForm(request.POST or None)
    form2 = MagasinForm(request.POST or None)
    form3 = ProfileMagasinForm(request.POST or None)
    form4 = ProduitForm(request.POST or None)

    if form1.is_valid():
        form1.save()
        context['form'] = form1
        return redirect('home')

    elif form2.is_valid():
        form2.save()
        context['form'] = form2
        return redirect('home')

    elif form3.is_valid():
        form3.save()
        context['form'] = form3
        return redirect('home')

    elif form4.is_valid():
        form4.save()
        context['form'] = form4
        return redirect('home')

    context['form1'] = form1
    context['form2'] = form2
    context['form3'] = form3
    context['form4'] = form4
    return render(request=request, template_name=template_name, context=context)
