from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order,OrderUpdate
import json
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
MERCHANT_KEY='aBuXjd69676206712894###';
#WHATEVER CHANGES WWE HAVE DONE IN THE DATABASE, WE HAVE T SAVE THE CHANGES IN THE VIEWS.PY FILE TOO
from  math import ceil
# Create your views here.
def index(request):
    '''this statement will print all the objects available in the database in the form of a list and we are sending this list to the index.html file
    in the form of params dictionary'''
    # products=Product.objects.all()
    # print(products)
    # n=len(products)
    # nslides= (n//4+ceil(n/4-n//4))
    # allprods=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslides= (n//4+ceil(n/4-n//4))
        allprods.append([prod,range(1,nslides),nslides])
    params={'allprods':allprods}
    #print(catprods)
    #params={'no_of_slides':nslides,'product':products,'range':range(1,nslides) }
    return render(request,'shop/index.html',params)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    thank=False
    if(request.method=='POST'):
        print(request)
        name=request.POST.get('name','')
        print(name)
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        text=request.POST.get('text','')
        print(name,email,phone,text)
        contact=Contact(name=name,email=email,phone=phone,text=text)
        #we  have to save the changes which wr have done in the databse in the viewspy file
        contact.save()
        thank=True
    return render(request,'shop/contact.html',{'thank':thank})
def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            print(order)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                print(update)
                updates = []
                for item in update:
                    print(item)
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')


def productview(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    print(product)

    return render(request, 'shop/productview.html', {'product':product[0]})
def checkout(request):
    if(request.method=='POST'):
        items_json=request.POST.get('items_json','')
        amount=request.POST.get('amount','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        address=request.POST.get('address1','') + " "+request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        thank=True;
        order=Order(items_json=items_json,name=name,email=email,phone=phone,address=address, city=city, state=state,zip_code=zip_code,amount=amount )
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="The order has been placed")
        update.save()
        id=order.order_id
        param_dict = {

            'MID':'aBuXjd69676206712894',
            'ORDER_ID':str(order.order_id),
            'TXN_AMOUNT':str(amount),
            'CUST_ID':email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'shop/paytm.html', {'param_dict': param_dict})
        #return render(request,'shop/checkout.html',{'thank':thank,'id':id})
    return render(request,'shop/checkout.html')
@csrf_exempt
def handlerequest(request):
    return HttpResponse('done')
def search(request):
    return render(request,'shop/search.html')
