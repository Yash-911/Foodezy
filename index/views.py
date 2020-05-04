import random

from django.shortcuts import render
from add_recipe.models import Recipes
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html');
def newfunc(request):
    all_items = Recipes.objects.values('id').all()
    print(all_items)
    itemlist=[]
    new_list=[]
    for i in all_items:
        itemlist.append(i['id'])
    for i in range(0,6):
        random_num=random.choice(itemlist)
        if random_num not in new_list:
            new_list.append(random_num)
    print(new_list)
    skill_grp = Recipes.objects.filter(id__in=new_list)
    print(skill_grp)
    return render(request,'new_index.html',{'skills': skill_grp})