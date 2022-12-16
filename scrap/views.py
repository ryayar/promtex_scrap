from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
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
def index(request):

    select_data = """   
            SELECT id, query_id, product_query_name, product_platform
            FROM scrap_scrapproduct
            GROUP BY query_id
            ORDER BY query_id DESC
            LIMIT 10"""

    scrap_product_group = ScrapProduct.objects.raw(select_data)
    # scrap_product = ScrapProduct.objects.all()
    return render(request, "scrap/index.html", {"group_positions": scrap_product_group})


def create(request):
    if request.method == "POST":
        product_name = request.POST.get("query")
        try:
            last_query_id = ScrapProduct.objects.last().query_id
        except:
            last_query_id = 0

        print(request.POST.get('ebay'))

        checked_status = []
        if request.POST.get('ebay') == 'checked':
            checked_status.append('Ebay')

        if request.POST.get('ali') == 'checked':
            checked_status.append('AliExpress')

        print(checked_status)

        if 'Ebay' in checked_status:
            query_ebay = parce.scrap_ebay(product_name)
            if query_ebay:
                for key, value in query_ebay.items():
                    product = ScrapProduct()

                    product.query_id = last_query_id + 1
                    product.product_query_name = product_name
                    product.product_scrap_name = value[0]
                    product.product_link = value[1]
                    product.product_link_img = value[2]
                    product.product_price = value[3]
                    product.product_country = value[4]
                    try:
                        product.product_quality = value[5]
                    except:
                        pass
                    product.user_name = 'Admin'
                    for i in checked_status:
                        product.product_platform += f'{i} '
                    product.save()

        if 'AliExpress' in checked_status:
            query_ali = parce.scrap_ali(product_name)
            if query_ali:
                for key, value in query_ali.items():
                    product = ScrapProduct()

                    product.query_id = last_query_id + 1
                    product.product_query_name = product_name
                    product.product_scrap_name = value[0]
                    product.product_link = value[1]
                    product.product_link_img = value[2]
                    product.product_price = value[3]
                    product.user_name = 'Admin'
                    for i in checked_status:
                        product.product_platform += f'{i} '
                    product.save()

    return HttpResponseRedirect("/")


# изменение данных в бд
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
            return render(request, "scrap/edit.html", {"person": person})
    except ScrapProduct.DoesNotExist:
        return HttpResponseNotFound(not_found)


def results(request):
    select_data = """   
            SELECT id, query_id, product_query_name, product_platform
            FROM scrap_scrapproduct
            GROUP BY query_id
            ORDER BY query_id DESC"""

    scrap_product_group = ScrapProduct.objects.raw(select_data)
    return render(request, "scrap/results.html", {"group_positions": scrap_product_group})


def result(request, query_id=0):
    if not query_id:
        return redirect(results)

    try:
        positions = ScrapProduct.objects.filter(query_id=query_id)
        query_name = ScrapProduct.objects.raw(f"SELECT id, product_query_name FROM scrap_scrapproduct WHERE query_id={query_id} GROUP BY query_id")
        name = query_name
        if positions:
            data = {
                "positions": positions,
                "query_name": name,
            }
            return render(request, "scrap/result.html", data)
        else:
            return HttpResponseNotFound(not_found)
    except ScrapProduct.DoesNotExist:
        return HttpResponseNotFound(not_found)

    # product_all = ScrapProduct.objects.all()
    # return render(request, "scrap/result.html", {"positions": product_all})


def generate_cp(request):
    try:
        if request.method == "POST":
            checkbox_new = request.POST.getlist('new')
            checkbox_bu = request.POST.getlist("bu")
            print(f'-------------------\n{checkbox_new}\n-------------------')
            print(f'-------------------\n{checkbox_bu}\n-------------------')
        else:
            print(f'-------------------\nНу чет такое себе\n-------------------')
        return HttpResponseRedirect("/")
    except Exception:
        return HttpResponseNotFound(not_found)


# удаление данных из бд
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
def dele(request, id):
    try:
        person = ScrapProduct.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except ScrapProduct.DoesNotExist:
        return HttpResponseNotFound(not_found)


def contact(request):
    return render(request, "scrap/contact.html")
