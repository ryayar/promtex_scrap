from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import ScrapProduct
from .script import parce
import time

not_found = "<h2 style='" \
            "position: absolute; " \
            "top: 30%; " \
            "left: 50%; " \
            "transform: translate(-50%, -50%) " \
            "matrix(4, 0, 0, 4, 0, 0);'>" \
            "Page not found</h2>"


# получение данных из бд
@login_required
def index(request):
    select_data = f"""
            SELECT id
            FROM scrap_scrapproduct
            WHERE user_name='{request.user}'
            GROUP BY query_id
            ORDER BY query_id DESC
            LIMIT 10"""

    scrap_product_group = ScrapProduct.objects.raw(select_data)

    # for i in scrap_product_group:
    #     print(i)
    # print(scrap_product_group)
    # scrap_product_group = ScrapProduct.objects.all()
    temp = ''
    # scrap_product_1 = ScrapProduct.objects.values_list('query_id')
    # scrap_product_2 = ScrapProduct.objects.values_list('product_platform')
    # # scrap_product_group = temp.union(scrap_product_1, scrap_product_2).order_by('query_id')
    # print(scrap_product_1)
    # print('*'*50)
    # print(scrap_product_2)
    return render(request, "scrap/index.html",
                  {"group_positions": scrap_product_group, 'page': 'home', 'user': request.user})


@login_required
def create(request):
    if request.method == "POST":
        user = request.user
        product_name = request.POST.get("query")

        try:
            last_query_id = ScrapProduct.objects.last().query_id
        except:
            last_query_id = 0

        if request.POST.get('ebay') == 'checked':
            query_ebay = parce.scrap_ebay(product_name)
            if query_ebay:
                write_db(product_name, last_query_id, query_ebay, user)

        if request.POST.get('ali') == 'checked':
            query_ali = parce.scrap_ali(product_name)
            if query_ali:
                write_db(product_name, last_query_id, query_ali, user)

        if request.POST.get('avito') == 'checked':
            query_avito = parce.scrap_avito(product_name)
            if query_avito:
                write_db(product_name, last_query_id, query_avito, user)

    return HttpResponseRedirect("/")


def write_db(product_name, last_query_id, query, user):
    for key, value in query.items():
        product = ScrapProduct()
        product.query_id = last_query_id + 1
        product.product_query_name = product_name
        product.product_platform = value[0]
        product.product_scrap_name = value[1]
        product.product_link = value[2]
        if value[3] is None:
            product.product_link_img = 'https://ae01.alicdn.com/kf/Sf5580f12cd9c4f63b75d8811390c36d5S/800x800.png'
        else:
            product.product_link_img = value[3]
        product.product_price = value[4]
        product.product_country = value[5]
        try:
            product.product_quality = value[6]
        except:
            pass
        product.user_name = user

        product.save()


# изменение данных в бд
@login_required
def edit(request, id):
    try:
        person = ScrapProduct.objects.get(id=id)

        if request.method == "POST":
            person.product_scrap_name = request.POST.get("product_scrap_name")
            person.product_price = request.POST.get("product_price")
            person.save()
            return HttpResponseRedirect("/")
        else:
            print(f'-------------------\n{id}\n-------------------')
            return render(request, "scrap/edit.html", {"person": person, 'page': 'edit', 'user': request.user})
    except ScrapProduct.DoesNotExist:
        return HttpResponseNotFound(not_found)


@login_required
def results(request):
    if request.user != 'Admin':
        select_data = f"""SELECT id, query_id, product_query_name, product_platform
                      FROM scrap_scrapproduct
                      WHERE user_name = '{request.user}'
                      GROUP BY query_id
                      ORDER BY query_id DESC"""
    else:
        select_data = f"""SELECT id, query_id, product_query_name, product_platform
                              FROM scrap_scrapproduct
                              GROUP BY query_id
                              ORDER BY query_id DESC"""

    scrap_product_group = ScrapProduct.objects.raw(select_data)
    return render(request, "scrap/results.html",
                  {"group_positions": scrap_product_group, 'page': 'result', 'user': request.user})


@login_required
def result(request, query_id=0):
    if not query_id:
        return redirect(results)

    try:
        positions = ScrapProduct.objects.filter(query_id=query_id)
        query_name = ScrapProduct.objects.raw("""SELECT id, product_query_name
                                              FROM scrap_scrapproduct
                                              WHERE query_id={query_id}
                                              GROUP BY query_id""")
        if positions:
            data = {
                "positions": positions,
                "query_name": query_name,
                'page': 'result',
                'user': request.user,
            }
            return render(request, "scrap/result.html", data)
        else:
            return HttpResponseNotFound(not_found)
    except ScrapProduct.DoesNotExist:
        return HttpResponseNotFound(not_found)

    # product_all = ScrapProduct.objects.all()
    # return render(request, "scrap/result.html", {"positions": product_all})


@login_required
def generate_cp(request):
    try:
        if request.method == "POST":
            checkbox_new = request.POST.getlist('new')
            checkbox_bu = request.POST.getlist("bu")
            if checkbox_new or checkbox_bu:
                # print(f'-------------------\n{checkbox_new}\n-------------------')
                # print(f'-------------------\n{checkbox_bu}\n-------------------')

                new = ScrapProduct.objects.filter(id__in=checkbox_new)
                bu = ScrapProduct.objects.filter(id__in=checkbox_bu)
                return render(request, "scrap/generate_cp.html", {"new": new, "bu": bu, 'user': request.user})
            else:
                return redirect(request.META.get('HTTP_REFERER'))
        # else:
        #     print(f'-------------------\nНу чет такое себе\n-------------------')
        return HttpResponseRedirect("/")
    except Exception:
        return HttpResponseNotFound(not_found)


# удаление данных из бд
@login_required
def delete(request):
    ScrapProduct.objects.all().delete()
    # last_id = ebay.objects.last().id
    # first_id = ebay.objects.first().id
    # # print(f'last {last_id}')
    # # print(f'first {first_id}')
    # parce.delete_all(first_id, last_id)
    return HttpResponseRedirect("/")
    # try:
    #     person = ebay.objects.get(id=id)
    #     person.delete()
    #     return HttpResponseRedirect("/")
    # except ebay.DoesNotExist:
    #     return HttpResponseNotFound(not_found)


# удаление данных из бд
@login_required
def dele(request, id):
    try:
        product = ScrapProduct.objects.get(id=id)
        product.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    except ScrapProduct.DoesNotExist:
        return HttpResponseNotFound(not_found)


@login_required
def contact(request):
    return render(request, "scrap/contact.html")
