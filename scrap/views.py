from itertools import islice
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import ScrapProduct, Item
from .script import parce
import json

not_found = "<h2 style='" \
            "position: absolute; " \
            "top: 30%; " \
            "left: 50%; " \
            "transform: translate(-50%, -50%) " \
            "matrix(4, 0, 0, 4, 0, 0);'>" \
            "Page not found</h2>"


@csrf_exempt
def api_index(request):
    unique_data = get_query_from_db('home')
    return JsonResponse(unique_data, safe=False)


@csrf_exempt
def api_results(request):
    unique_data = get_query_from_db('results')
    return JsonResponse(unique_data, safe=False)


@csrf_exempt
def api_create(request):
    data = json.loads(request.body)
    if data.get('user'):
        user = data.get('user')
    else:
        user = 'Почему-то None'

    product_name = data.get('query')

    try:
        last_query_id = ScrapProduct.objects.last().query_id
    except:
        last_query_id = 0

    try:
        if data.get('ebay'):
            query_ebay = parce.scrap_ebay(product_name)
            if query_ebay:
                write_db(product_name, last_query_id, query_ebay, user)
    except AttributeError:
        pass

    try:
        if data.get('ali'):
            query_ali = parce.scrap_ali(product_name)
            if query_ali:
                write_db(product_name, last_query_id, query_ali, user)
    except AttributeError:
        pass

    try:
        if data.get('avito'):
            query_avito = parce.scrap_avito(product_name)
            if query_avito:
                write_db(product_name, last_query_id, query_avito, user)
    except AttributeError:
        pass

    return JsonResponse({'success': True})


@csrf_exempt
def api_result(request, query_id=0):
    try:
        positions = ScrapProduct.objects.filter(query_id=query_id).distinct().values()
        if positions:
            data = list(positions)
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'success': False})
    except ScrapProduct.DoesNotExist:
        return JsonResponse({'success': False})


@csrf_exempt
def api_settings(request):
    items = list(Item.objects.all().values())
    return JsonResponse(items, safe=False)


@csrf_exempt
def api_delete_item(request, query_id):
    item = Item.objects.get(id=query_id)
    item.delete()
    return JsonResponse({'success': True})


@csrf_exempt
def api_save_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        country = data['country']
        delivery_time_days = data['delivery_time_days']
        delivery_time_text = data['delivery_time_text']
        data_id = data.get('id')

        if data_id:
            # update
            item = Item.objects.get(id=data_id)
            item.country = country
            item.delivery_time_days = delivery_time_days
            item.delivery_time_text = delivery_time_text
            item.save()
            return JsonResponse({'updateSuccess': True})

        else:
            # create
            Item.objects.create(
                country=country,
                delivery_time_days=delivery_time_days,
                delivery_time_text=delivery_time_text
            )
            return JsonResponse({'createSuccess': True})
    else:
        return JsonResponse({'updateSuccess': False, 'createSuccess': False})


@csrf_exempt
def api_generate_cp(request):
    checkbox = json.loads(request.body)
    checkbox_new = checkbox['new']
    checkbox_bu = checkbox['bu']
    if checkbox_new or checkbox_bu:
        new = list(ScrapProduct.objects.filter(id__in=checkbox_new).values())
        bu = list(ScrapProduct.objects.filter(id__in=checkbox_bu).values())
        print('*' * 50)
        print(new)
        print(bu)
        print('*' * 50)
        return JsonResponse({'new': new, 'bu': bu}, safe=False)
    else:
        return JsonResponse({'success': False})


def get_query_from_db(page):
    data = ScrapProduct.objects.filter().values('query_id', 'product_query_name', 'product_platform',
                                                'query_date').order_by('-query_id')
    unique_data = {}
    for item in data:
        if item['query_id'] not in unique_data:
            unique_data[item['query_id']] = item
        else:
            if item['product_platform'] not in unique_data[item['query_id']]['product_platform']:
                unique_data[item['query_id']]['product_platform'] += ', ' + item['product_platform']
    if page == 'home':
        unique_data = list(dict(islice(unique_data.items(), 10)).values())
    elif page == 'results':
        unique_data = list(unique_data.values())
    return unique_data


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


#
# @login_required
# def index(request):
#     if request.POST.get('user'):
#         user = request.POST.get('user')
#     else:
#         user = 'Почему-то None'
#     # username = request.user
#     select_data = f"""SELECT id, query_id, product_query_name, product_platform
#                       FROM scrap_scrapproduct
#                       WHERE user_name = '{user}'
#                       GROUP BY query_id
#                       ORDER BY query_id DESC"""
#     #
#     scrap_product_group = ScrapProduct.objects.raw(select_data)
#     # scrap_product_group = ScrapProduct.objects.filter(user_name=user).order_by('-query_id').distinct()
#     # print(scrap_product_group)
#     # return scrap_product_group
#     return render(request, 'scrap/index.html',
#                   {'group_positions': scrap_product_group, 'page': 'home', 'user': request.user})
#
#
# @login_required
# def create(request):
#     print('Пришел запрос!')
#     if request.method == 'POST':
#         if request.POST.get('user'):
#             user = request.POST.get('user')
#         else:
#             user = 'Почему-то None'
#         product_name = request.POST.get('query')
#
#         try:
#             last_query_id = ScrapProduct.objects.last().query_id
#         except:
#             last_query_id = 0
#
#         try:
#             if request.POST.get('ebay') == 'checked':
#                 query_ebay = parce.scrap_ebay(product_name)
#                 if query_ebay:
#                     write_db(product_name, last_query_id, query_ebay, user)
#         except AttributeError:
#             pass
#
#         try:
#             if request.POST.get('ali') == 'checked':
#                 query_ali = parce.scrap_ali(product_name)
#                 if query_ali:
#                     write_db(product_name, last_query_id, query_ali, user)
#         except AttributeError:
#             pass
#
#         try:
#             if request.POST.get('avito') == 'checked':
#                 query_avito = parce.scrap_avito(product_name)
#                 if query_avito:
#                     write_db(product_name, last_query_id, query_avito, user)
#         except AttributeError:
#             pass
#
#     print('Отправлен ответ!')
#     return HttpResponseRedirect("/")
#
#
# @login_required
# def settings(request):
#     items = Item.objects.all()
#     return render(request, 'scrap/settings.html', {'items': items, 'page': 'settings', 'user': request.user})
# @login_required
# def edit(request, id):
#     try:
#         person = ScrapProduct.objects.get(id=id)
#
#         if request.method == 'POST':
#             person.product_scrap_name = request.POST.get("product_scrap_name")
#             person.product_price = request.POST.get("product_price")
#             person.save()
#             return HttpResponseRedirect("/")
#         else:
#             print(f'-------------------\n{id}\n-------------------')
#             return render(request, 'scrap/edit.html', {'person': person, 'page': 'edit', 'user': request.user})
#     except ScrapProduct.DoesNotExist:
#         return HttpResponseNotFound(not_found)
#
#
# @login_required
# def results(request):
#     username = request.user
#     if username != 'Admin' and username != 'admin':
#         select_data = f"""SELECT id, query_id, product_query_name, product_platform
#                       FROM scrap_scrapproduct
#                       WHERE user_name = '{username}'
#                       GROUP BY query_id
#                       ORDER BY query_id DESC"""
#     else:
#         select_data = f"""SELECT product_query_name
#                               FROM scrap_scrapproduct
#                               GROUP BY query_id
#                               ORDER BY query_id DESC"""
#     select_data = ScrapProduct.objects.raw(select_data)
#     return render(request, 'scrap/results.html',
#                   {'group_positions': select_data, 'page': 'result', 'user': username})
#
#
# @login_required
# def result(request, query_id=0):
#     if not query_id:
#         return redirect(results)
#
#     try:
#         positions = ScrapProduct.objects.filter(query_id=query_id).distinct()
#
#         if positions:
#             data = {
#                 'positions': positions,
#                 'page': 'result',
#                 'user': request.user,
#             }
#             return render(request, 'scrap/result.html', data)
#         else:
#             return HttpResponseNotFound(not_found)
#     except ScrapProduct.DoesNotExist:
#         return HttpResponseNotFound(not_found)
#
#
# @login_required
# def generate_cp(request):
#     try:
#         if request.method == 'POST':
#             checkbox_new = request.POST.getlist('new')
#             checkbox_bu = request.POST.getlist('bu')
#             if checkbox_new or checkbox_bu:
#                 # print(f'-------------------\n{checkbox_new}\n-------------------')
#                 # print(f'-------------------\n{checkbox_bu}\n-------------------')
#
#                 new = ScrapProduct.objects.filter(id__in=checkbox_new)
#                 bu = ScrapProduct.objects.filter(id__in=checkbox_bu)
#                 return render(request, 'scrap/generate_cp.html', {'new': new, 'bu': bu, 'user': request.user})
#             else:
#                 return redirect(request.META.get('HTTP_REFERER'))
#         return HttpResponseRedirect('/')
#     except Exception:
#         return HttpResponseNotFound(not_found)
#
#
# @login_required
# def delete(request):
#     ScrapProduct.objects.all().delete()
#     return HttpResponseRedirect('/')
#
#
# @login_required
# def dele(request, id):
#     try:
#         # product = ScrapProduct.objects.get(id=id)
#         products = ScrapProduct.objects.filter(query_id=id)
#         print(products)
#         products.delete()
#         return HttpResponseRedirect('/')
#     except ScrapProduct.DoesNotExist:
#         return HttpResponseNotFound(not_found)
#
#
# @login_required
# def contact(request):
#     return render(request, 'scrap/contact.html')
