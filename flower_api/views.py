# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from flower.models import Items, ItemDetails

# # Create your views here.

# @api_view(['GET'])
# def getAllItems(request):
#     flower=Items.objects.all() #Get All Items
#     flowerlist = list(flower.values())
#     flowerlist=flower.serializer
#     return JsonResponse({
#         'flower':flowerlist
#     }) 

# def get_item_details(request):
#     flower=ItemDetails.objects.select_related('itemsid').all() #Get All Items
#     list1=[]
#     for item in flower:
#         getitems=({
#             'id':item.id,
#             'nmae':item.itemsid.name,
#             'colcor':item.color,
#             'price':item.price,
#             'qty':item.qty,
#             'tax':item.tax,
#             'image':item.image,
#             'total':item.total,
#         })
#     list1=[]
#     flowerlist = list(flower.values())
#     return JsonResponse({
#         'flower':flowerlist
#     })


# def get_item_details_byid(request):
#     flower=ItemDetails.objects.select_related('itemsid').all() #Get All Items
#     list1=[]
#     for item in flower:
#         getitems=({
#             'id':item.id,
#             'nmae':item.itemsid.name,
#             'colcor':item.color,
#             'price':item.price,
#             'qty':item.qty,
#             'tax':item.tax,
#             'image':item.image,
#             'total':item.total,
#         })
#     list1=[]
#     flowerlist = list(flower.values())
#     return JsonResponse({
#         'flower':flowerlist
#     })