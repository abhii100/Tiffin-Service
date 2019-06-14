import json
from django.http import *
from django.shortcuts import *
from django.core.serializers.json import DjangoJSONEncoder
from django import *
from partner import *
from admin import *
from category import *
from customer import *
from offer import *
from fooditem import *
from addtocart import *
from datetime import *
import http.client
from django.views.decorators.csrf import csrf_exempt

COUNT = 0
CARTDCT = dict()
CARTDATE = ""


# public site
def indexpage(request):
    return render(request, "index.html")


def signuppartner(request):
    return render(request, "signuppartner.html")


def signuppartneraction(request):
    dct = request.GET['dct']
    print(dct)
    k = json.loads(dct)

    # m = {"id": 2, "name": "hussain"}
    # print(m)
    # n = json.dumps(m)
    # o = json.loads(n)
    # print(o['id'], o['name'])
    print(k['location'], ' -----------------------')
    res = partner.signuppartner("", k['companyname'], k['ownername'], k['mobileno'], k['address'], k['email'],
                                k['password'], k['location'])
    return HttpResponse(res)


def loginpartnerpage(request):
    return render(request, "loginpartner.html")


def loginpartneraction(request):
    dct = request.GET['dct']
    print(dct)
    k = json.loads(dct)

    # m = {"id": 2, "name": "hussain"}
    # print(m)
    # n = json.dumps(m)
    # o = json.loads(n)
    # print(o['id'], o['name'])

    lst = partner.loginpartner("", k['email'], k['password'])
    mydct = dict()
    for i in range(0, len(lst)):
        request.session['PEMAIL'] = lst[i][5]
        request.session['PID'] = lst[i][0]
        myinnerdct = dict()
        myinnerdct['id'] = lst[i][0]
        myinnerdct['companyname'] = lst[i][1]
        myinnerdct['ownername'] = lst[i][2]
        myinnerdct['mobileno'] = lst[i][3]
        myinnerdct['address'] = lst[i][4]
        myinnerdct['email'] = lst[i][5]
        myinnerdct['status'] = lst[i][7]
        mydct['dict' + str(i)] = myinnerdct
    return HttpResponse(json.dumps(mydct))


def loginadminpage(request):
    return render(request, "loginadmin.html")


def loginadminaction(request):
    dct = request.GET['dct']
    print(dct)
    k = json.loads(dct)

    # m = {"id": 2, "name": "hussain"}
    # print(m)
    # n = json.dumps(m)
    # o = json.loads(n)
    # print(o['id'], o['name'])

    lst = admin.loginadmin("", k['email'], k['password'])
    mydct = dict()
    for i in range(0, len(lst)):
        request.session['ADMINEMAIL'] = lst[i][2]
        myinnerdct = dict()
        myinnerdct['id'] = lst[i][0]
        myinnerdct['name'] = lst[i][1]
        myinnerdct['email'] = lst[i][2]
        myinnerdct['status'] = lst[i][3]
        mydct['dict' + str(i)] = myinnerdct
    return HttpResponse(json.dumps(mydct))


def signupcustomer(request):
    return render(request, "signupcustomer.html")


def signupcustomeraction(request):
    name = request.POST['name']
    mobileno = request.POST['mobileno']
    address = request.POST['address']
    city = request.POST['city']
    email = request.POST['email']
    password = request.POST['password']
    photo = request.FILES['photo']
    # print(name)
    # print(photo)
    res = customer.signupcustomer("", name, mobileno, address, photo, str(photo), city, email, password)
    return HttpResponse(res)


def logincustomerpage(request):
    return render(request, 'logincustomer.html')


def logincustomeraction(request):
    dct = request.GET['dct']
    print(dct)
    k = json.loads(dct)

    # m = {"id": 2, "name": "hussain"}
    # print(m)
    # n = json.dumps(m)
    # o = json.loads(n)
    # print(o['id'], o['name'])

    lst = customer.logincustomer("", k['email'], k['password'])
    mydct = dict()
    for i in range(0, len(lst)):
        request.session['CUSTEMAIL'] = lst[i][6]
        request.session['CUSTID'] = lst[i][0]
        myinnerdct = dict()
        myinnerdct['id'] = lst[i][0]
        myinnerdct['name'] = lst[i][1]
        myinnerdct['email'] = lst[i][6]
        myinnerdct['status'] = lst[i][8]
        mydct['dict' + str(i)] = myinnerdct
    return HttpResponse(json.dumps(mydct))


def showitemspage(request):
    return render(request, 'showitems.html')


def addtocartpage(request):
    global COUNT, CARTDCT
    id = request.GET['id']
    qty = request.GET['qty']
    # partnerid = request.GET['partnerid']

    flag = False

    # if len(CARTDCT)==0:
    #     CARTDCT['dct0'] = addtocart.additemtocart("", id, qty)

    if request.session.has_key('MYCART'):
        CARTDCT = request.session['MYCART']
        for i in range(0, len(CARTDCT)):
            ar = CARTDCT

            if id == str(ar['dct' + str(i)]['itemid']):
                ar_qty = int(str(ar['dct' + str(i)]['qty']))
                ar_price = float(str(ar['dct' + str(i)]['price']))
                ar_qty += int(qty)
                ar['dct' + str(i)]['qty'] = str(ar_qty)
                ar['dct' + str(i)]['total'] = ar_price * ar_qty
                flag = True
                break

    if flag == False:
        COUNT = len(CARTDCT)
        print(COUNT, ' -----')
        CARTDCT['dct' + str(COUNT)] = addtocart.additemtocart("", id, qty)
        # COUNT += 1

    request.session['MYCART'] = CARTDCT
    k = getcartitemsintable(request)
    return HttpResponse(k)

def getcartcount(request):
    s = 0
    if request.session.has_key('MYCART'):
        s = len(request.session['MYCART'])
    else:
        s = 0
        # print(s,'^^^^^^^^^^^^^^^^^^^^^^^^^')
    return HttpResponse(str(s))


def deletefromcart(request):
    global COUNT, CARTDCT
    tempcart = dict()
    num = 0
    id = request.GET['id']

    for i in CARTDCT.keys():
        if id != i:
            # print("I am not equal ")
            tempcart['dct' + str(num)] = CARTDCT[i]
            num += 1

    request.session['MYCART'] = tempcart
    CARTDCT.clear()
    CARTDCT = tempcart
    # print(CARTDCT)
    k = getcartitemsintable(request)
    return HttpResponse(k)


def getcartitemsintable(request):
    s = ''
    netamount = 0.0
    # print(len(request.session['MYCART'])," ++++++++++")
    if request.session.has_key('MYCART'):
        s = "<table class='table table-bordered'>"
        s += "<th>Srno</th>"
        s += "<th>Item Name</th>"
        s += "<th>Price (Rs.)</th>"
        s += "<th>Qty</th>"
        s += "<th>Amount (Rs.)</th>"
        s += "<th>Action</th>"
        for i in range(0, len(request.session['MYCART'])):
            ar = request.session['MYCART']
            print(ar)
            netamount += float(ar['dct' + str(i)]['total'])
            s += "<tr>"
            s += "<td>" + str(i + 1) + "</td>"
            s += "<td>" + ar['dct' + str(i)]['itemname'] + "</td>"
            s += "<td>" + str(ar['dct' + str(i)]['price']) + "</td>"
            s += "<td>" + str(ar['dct' + str(i)]['qty']) + "</td>"
            s += "<td>" + str(ar['dct' + str(i)]['total']) + "</td>"
            s += "<td><button class='btn btn-danger' type='submit' onclick=deletefromcart('" + 'dct' + str(
                i) + "')>Delete</button></td>"
            s += "</tr>"
        s += "<tr>"
        s += "<td colspan='4' class='text-right'>Net Amount (Rs.)</td>"
        s += "<th colspan=2>" + str(netamount) + "</th>"
        s += "</tr>"
        s += "<tr>"
        s += "<td class='text-right' colspan='3'><a href='/allpartnerpage' class='btn btn-warning text-light'>Continue Shopping</a></td>"
        s += "<td class='text-left' colspan='3'><a href='/proceedtopay' class='btn btn-success'>Proceed to Pay</a></td>"
        s += "</tr>"
        s += "</table>"
    return HttpResponse(s)


def allpartnerpage(request):
    return render(request, 'allpartnerpage.html')


def allpartnerforcustomer(request):
    name = request.GET['name']
    lst = partner.allpartnerforcustomer("", name, "")
    mydct = generate_partner_dict(lst)
    return HttpResponse(json.dumps(mydct))


def partnerforcustomerbyid(request):
    id = request.GET['id']
    lst = partner.allpartnerforcustomer("", "", id)
    mydct = generate_partner_dict(lst)
    return HttpResponse(json.dumps(mydct))


def showpartnermenu(request):
    id = request.GET['id']
    return render(request, 'showpartnermenu.html', {"id": id})

def showpartnergallery(request):
    id = request.GET['id']
    return render(request,'showpartnergallery.html',{"id":id})


def getmenubypartner(request):
    global CARTDATE,CARTDCT
    partnerid = request.GET['partnerid']
    dt = request.GET['myday']

    if not request.session.has_key("MYCART"):
        CARTDATE=dt

    if CARTDATE!=dt:
        del request.session['MYCART']
        CARTDCT.clear()

        print("cghcjg")

    # print(CARTDATE,' ++++++++++++')
    # print(dt,' +++++++++++++++')
    dayname = datetime.strptime(dt, '%m/%d/%Y').strftime('%A')

    lst1 = fooditem.getcategory_item("", partnerid)
    # print(lst1)
    s = "<div class='row'>"
    for i in lst1:
        s += "<div class='col-md-6' style='padding:10px;'>"
        s += "<div class='mycategory'>"
        s += "<h5 class='text-uppercase'>" + i[1] + "</h5>"
        s += "<div class='table-responsive mytable1'>"
        s += "<table class='table table-bordered'>"
        s += "<tr class='bg-secondary text-white'>"
        s += "<th>ITEM</th>"
        s += "<th>PRICE</th>"
        s += "<th width='120'>ORDER</th>"
        s += "</tr>"
        lst2 = fooditem.getcategory_item("", partnerid, i[0])

        for j in lst2:
            daylist = list(j[7].split(","))
            for k in daylist:
                # print(k)
                if k == dayname:
                    s += "<tr>"
                    s += "<td>" + j[1] + "</td>"
                    s += "<td>" + str(j[2]) + "</td>"
                    s += "<td><button type='button' class='btn btn-success' onclick=addtocart(" + str(j[0]) + ",'1')>Add To Cart</button></td>"
                    s += "</tr>"
        s += "</table>"
        s += "</div>"
        s += "</div>"
        s += "</div>"

    s += "</div>"
    # print(s)
    # lst = fooditem.viewfooditem("", "", partnerid)
    # mydct = generate_food_dct(lst)
    # print(mydct)
    # return HttpResponse(json.dumps(mydct))
    return HttpResponse(s)


def mycart(request):
    return render(request, 'mycart.html')


def proceedtopay(request):
    request.session['FROMCART'] = 'yes'
    netamount = 0.0
    for i in range(0, len(request.session['MYCART'])):
        ar = request.session['MYCART']
        netamount += float(ar['dct' + str(i)]['total'])
    if request.session.has_key("CUSTID"):
        return render(request, 'customer/billinginfo.html',{'netamount':netamount})
    else:
        return render(request, 'logincustomer.html')

def billinginfo(request):
    email = request.POST['email']
    name = request.POST['name']
    mobileno = request.POST['mobileno']
    address = request.POST['address']
    city = request.POST['city']
    paymentmode = request.POST['paymentmode']
    netamount = 0.0
    partnerid = "0"
    for i in range(0, len(request.session['MYCART'])):
        ar = request.session['MYCART']
        print(ar)
        netamount += float(ar['dct' + str(i)]['total'])
        partnerid = str(ar['dct' + str(i)]['partnerid'])

    res = customer.addorder('',request.session['CUSTID'],request.session['CUSTEMAIL'],name,mobileno,city,address,str(netamount),str(partnerid),paymentmode)

    for i in range(0, len(request.session['MYCART'])):
        ar = request.session['MYCART']
        res1 = customer.addorderdetail('',res,ar['dct' + str(i)]['itemid'],ar['dct' + str(i)]['itemname'],ar['dct' + str(i)]['price'],ar['dct' + str(i)]['qty'],ar['dct' + str(i)]['total'])
    msg = "Your Order has been placed for Rs." + str(netamount) + " .Your order will be delivered after order approval. Thank You"
    msg = msg.replace(" ","%20")
    conn1 = http.client.HTTPConnection("server1.vmm.education")
    conn1.request('GET',
                  "/VMMCloudMessaging/AWS_SMS_Sender?username=ExamSystem&password=S4J5LT3C&message=" + msg + "&phone_numbers=" + mobileno)
    response = conn1.getresponse()
    print(response.read())
    return HttpResponse(res1)

def thankspage(request):

    del request.session['MYCART']
    return render(request,'customer/thankspage.html')

def showsales(request):
    customerid = request.GET['customerid']
    res = customer.showsales('',customerid)
    return JsonResponse(res,safe=False)

def myorderspage(request):
    return render(request,'customer/myorderspage.html')

def myorders(request):
    customerid = request.GET['customerid']
    res = customer.myorders('',customerid)
    return JsonResponse(res,safe=False)


# public site


# admin site
def adminchecksession(request):
    if not request.session.has_key('ADMINEMAIL'):
        return True


def adminindex(request):
    return render(request, "admin/indexadmin.html")


def cp_admin(request):
    return render(request, "admin/changepasswordadmin.html")


def cp_adminaction(request):
    dct = request.GET['dct']
    print(dct)
    k = json.loads(dct)
    res = admin.changepassword("", k['email'], k['oldpassword'], k['newpassword'])
    return HttpResponse(res)


def adminlogout(request):
    del request.session['ADMINEMAIL']
    return HttpResponseRedirect('/loginadminpage')


def generate_partner_dict(lst):
    mydct = dict()
    for i in range(0, len(lst)):
        myinnerdct = dict()
        myinnerdct['id'] = lst[i][0]
        myinnerdct['companyname'] = lst[i][1]
        myinnerdct['ownername'] = lst[i][2]
        myinnerdct['mobileno'] = lst[i][3]
        myinnerdct['address'] = lst[i][4]
        myinnerdct['location'] = lst[i][8]
        myinnerdct['email'] = lst[i][5]
        myinnerdct['status'] = lst[i][7]
        mydct['dict' + str(i)] = myinnerdct
    return mydct


def pendingpartnerlist(request):
    lst = partner.viewpendingpartner("", "")
    mydct = generate_partner_dict(lst)
    return HttpResponse(json.dumps(mydct))


def pendingpartnerpage(request):
    return render(request, "admin/pendingpartnerpage.html")


def partnerlistbyname(request):
    name = request.GET['name']
    lst = partner.viewpendingpartner("", name)
    mydct = generate_partner_dict(lst)
    return HttpResponse(json.dumps(mydct))


def approverejectpartner(request):
    id = request.GET['id']
    status = request.GET['status']
    res = partner.approverejectpartner("", id, status)
    return HttpResponseRedirect('/pendingpartnerpage')


def pendingcustomerpage(request):
    return render(request, "admin/pendingcustomerpage.html")


def generate_customer_dict(lst):
    mydct = dict()
    for i in range(0, len(lst)):
        myinnerdct = dict()
        myinnerdct['id'] = lst[i][0]
        myinnerdct['name'] = lst[i][1]
        myinnerdct['mobileno'] = lst[i][2]
        myinnerdct['address'] = lst[i][3]
        myinnerdct['photo'] = lst[i][4]
        myinnerdct['city'] = lst[i][5]
        myinnerdct['email'] = lst[i][6]
        myinnerdct['status'] = lst[i][8]
        mydct['dict' + str(i)] = myinnerdct
    return mydct


def pendingcustomerlist(request):
    lst = customer.viewpendingcustomer("", "")
    mydct = generate_customer_dict(lst)
    return HttpResponse(json.dumps(mydct))


def approverejectcustomer(request):
    id = request.GET['id']
    status = request.GET['status']
    res = customer.approverejectcustomer("", id, status)
    return HttpResponseRedirect('/pendingcustomerpage')


def customerlistbyname(request):
    name = request.GET['name']
    lst = customer.viewpendingcustomer("", name)
    mydct = generate_customer_dict(lst)
    return HttpResponse(json.dumps(mydct))


def addcategory(request):
    return render(request, 'admin/addcategory.html')


def addcategoryaction(request):
    dct = request.GET['dct']
    print(dct)
    k = json.loads(dct)

    res = category.addcategory("", k['cname'], k['description'])
    return HttpResponse(res)


def viewcategorypage(request):
    return render(request, 'admin/viewcategory.html')


def viewcategorylist(request):
    lst = category.viewcategory("")
    mydct = dict()
    for i in range(0, len(lst)):
        myinnerdct = dict()
        myinnerdct['id'] = lst[i][0]
        myinnerdct['cname'] = lst[i][1]
        myinnerdct['description'] = lst[i][2]
        mydct['dict' + str(i)] = myinnerdct
    print(mydct)
    return HttpResponse(json.dumps(mydct))


def editcategorypage(request):
    id = request.GET['id']
    return render(request, "admin/editcategory.html", {"id": id})


def viewcategorybyid(request):
    id = request.GET['id']
    lst = category.viewcategorybyid("", id)
    mydct = dict()
    for i in range(0, len(lst)):
        myinnerdct = dict()
        myinnerdct['id'] = lst[i][0]
        myinnerdct['cname'] = lst[i][1]
        myinnerdct['description'] = lst[i][2]
        mydct['dict' + str(i)] = myinnerdct
    # return mydct
    aa = mydct
    return HttpResponse(json.dumps(aa))  # here it returns only data not the whole page where htmlcode is written


def editcategoryaction(request):
    dct = request.GET['dct']
    print(dct)
    k = json.loads(dct)
    res = category.editcategoryaction("", k['cname'], k['description'], k['id'])
    # print(res)
    return HttpResponse(res)


def deletecategory(request):
    id = request.GET['id']
    res = category.deletecategory("", id)
    dct = {"ans": res, "id": id}
    return HttpResponseRedirect('/viewcategorypage')


def addoffer(request):
    return render(request, 'admin/addoffer.html')


def addofferaction(request):
    dct = request.GET['dct']
    print(dct)
    k = json.loads(dct)

    res = offer.addoffer("", k['offername'], k['rate'], k['fromdate'], k['todate'], k['description'])
    return HttpResponse(res)


def generate_offer_dict(lst):
    mydct = dict()
    for i in range(0, len(lst)):
        myinnerdct = dict()
        print(lst[i][3])
        myinnerdct['id'] = lst[i][0]
        myinnerdct['offername'] = lst[i][1]
        myinnerdct['rate'] = lst[i][2]
        myinnerdct['fromdate'] = lst[i][3]
        myinnerdct['todate'] = lst[i][4]
        myinnerdct['description'] = lst[i][5]
        myinnerdct['status'] = lst[i][6]
        mydct['dict' + str(i)] = myinnerdct
    return mydct


def viewofferpage(request):
    return render(request, 'admin/viewofferpage.html')


def viewofferlist(request):
    lst = offer.viewoffer("", "", "")
    mydct = generate_offer_dict(lst)
    return HttpResponse(json.dumps(mydct, cls=DjangoJSONEncoder))


def offerlistbydate(request):
    fromdate = request.GET['fromdate']
    todate = request.GET['todate']
    lst = offer.viewoffer("", fromdate, todate)
    mydct = generate_offer_dict(lst)
    return HttpResponse(json.dumps(mydct, cls=DjangoJSONEncoder))


def editofferpage(request):
    id = request.GET['id']
    return render(request, "admin/editoffer.html", {"id": id})


def viewofferbyid(request):
    id = request.GET['id']
    lst = offer.viewofferbyid("", id)
    mydct = generate_offer_dict(lst)
    return HttpResponse(json.dumps(mydct,
                                   cls=DjangoJSONEncoder))  # here it returns only data not the whole page where htmlcode is written


def editofferaction(request):
    dct = request.GET['dct']
    print(dct)
    k = json.loads(dct)
    res = offer.editofferaction("", k['offername'], k['rate'], k['fromdate'], k['todate'], k['description'], k['id'])
    # print(res)
    return HttpResponse(res)


def deleteoffer(request):
    id = request.GET['id']
    res = offer.deleteoffer("", id)
    dct = {"ans": res, "id": id}
    return HttpResponseRedirect('/viewofferpage')


# admin site


# partner site

def partnerindex(request):
    return render(request, "partner/indexpartner.html")

def addgallerypage(request):
    return render(request,"partner/addgallerypage.html")


@csrf_exempt
def addgalleryaction(request):
    partnerid = request.POST['partnerid']
    photo = request.FILES['photo']
    res = partner.addgallery('',str(partnerid),photo,str(photo))
    return JsonResponse(res,safe=False)

def viewgallerypage(request):
    return render(request,'partner/viewgallerypage.html')


def cp_partner(request):
    return render(request, "partner/changepasswordpartner.html")


def cp_partneraction(request):
    dct = request.GET['dct']
    print(dct)
    k = json.loads(dct)
    res = partner.changepassword("", k['email'], k['oldpassword'], k['newpassword'])
    return HttpResponse(res)


def addfooditempage(request):
    return render(request, 'partner/addfooditem.html')


def addfooditemaction(request):
    dct = request.GET['dct']
    print(dct)
    k = json.loads(dct)

    res = fooditem.addfooditem("", k['itemname'], k['price'], k['description'], k['categoryid'], request.session['PID'],
                               k['availabledays'])
    return HttpResponse(res)


def viewfooditempage(request):
    return render(request, 'partner/viewfooditem.html')


def viewfooditemlist(request):
    # print(request.session['PID'])
    pid = ""
    if request.session.has_key('PID'):
        pid = request.session['PID']
    lst = fooditem.viewfooditem("", "", pid)
    mydct = dict()
    for i in range(0, len(lst)):
        myinnerdct = dict()
        myinnerdct['id'] = lst[i][0]
        myinnerdct['itemname'] = lst[i][1]
        myinnerdct['price'] = lst[i][2]
        myinnerdct['description'] = lst[i][3]
        myinnerdct['categoryid'] = lst[i][4]
        myinnerdct['cname'] = lst[i][5]
        myinnerdct['availabledays'] = lst[i][6]
        mydct['dict' + str(i)] = myinnerdct
    # print(mydct)
    return HttpResponse(json.dumps(mydct))


def deletefooditem(request):
    id = request.GET['id']
    res = fooditem.deletefooditem("", id)
    dct = {"ans": res, "id": id}
    return HttpResponseRedirect('/viewfooditempage')


def editfooditempage(request):
    id = request.GET['id']
    return render(request, 'partner/editfooditem.html', {"id": id})


def generate_food_dct(lst):
    mydct = dict()
    for i in range(0, len(lst)):
        myinnerdct = dict()
        myinnerdct['id'] = lst[i][0]
        myinnerdct['itemname'] = lst[i][1]
        myinnerdct['price'] = lst[i][2]
        myinnerdct['description'] = lst[i][3]
        myinnerdct['categoryid'] = lst[i][4]
        mydct['dict' + str(i)] = myinnerdct
    return mydct


def viewfooditembyid(request):
    id = request.GET['id']
    partnerid = ""
    if request.session.has_key("PID"):
        partnerid = str(request.session['PID'])
    lst = fooditem.viewfooditem("", id, partnerid)
    mydct = generate_food_dct(lst)

    # return mydct
    aa = mydct
    print(aa)
    return HttpResponse(json.dumps(aa))  # here it returns only data not the whole page where htmlcode is written


def partnerlogout(request):
    del request.session['PEMAIL']
    del request.session['PID']
    return HttpResponseRedirect('/loginpartnerpage')

def restorderspage(request):
    status = request.GET['status']
    return render(request,'partner/restorderspage.html',{'status':status})

def restorders(request):
    partnerid = request.GET['partnerid']
    status = request.GET['status']
    res = partner.restorders('',partnerid,status)
    return JsonResponse(res,safe=False)

def restorderdetailpage(request):
    orderid = request.GET['orderid']
    mobileno = request.GET['mobileno']
    return render(request,'partner/restorderdetailpage.html',{'orderid':orderid,'mobileno':mobileno})

def restorderdetail(request):
    orderid = request.GET['orderid']
    res = partner.restorderdetail('',orderid)
    return JsonResponse(res,safe=False)

def accept_reject_order(request):
    orderid = request.GET['orderid']
    status = request.GET['status']
    mobileno = request.GET['mobileno']
    res = partner.accept_reject_order('',orderid,status)
    msg = "Your Order has been "+status + " by ITiffinService. You will get your food at the specified date."
    msg = msg.replace(" ", "%20")
    conn1 = http.client.HTTPConnection("server1.vmm.education")
    conn1.request('GET',
                  "/VMMCloudMessaging/AWS_SMS_Sender?username=ExamSystem&password=S4J5LT3C&message=" + msg + "&phone_numbers=7508397712," + mobileno)
    response = conn1.getresponse()
    print(response.read())
    return render(request, 'partner/restorderspage.html', {'status': status})

def todaysales(request):
    partnerid = request.GET['partnerid']
    res = partner.todaysales('',partnerid)
    return JsonResponse(res,safe=False)

def monthlysales(request):
    partnerid = request.GET['partnerid']
    res = partner.monthlysales('',partnerid)
    print(res,'--------------')
    return JsonResponse(res,safe=False)



# partner site

# customer site

def customerindex(request):
    return render(request, 'customer/indexcustomer.html')


def cp_customer(request):
    return render(request, "customer/changepasswordcustomer.html")


def cp_customeraction(request):
    dct = request.GET['dct']
    print(dct)
    k = json.loads(dct)
    res = customer.changepassword("", k['email'], k['oldpassword'], k['newpassword'])
    return HttpResponse(res)


def customerlogout(request):
    del request.session['CUSTEMAIL']
    del request.session['CUSTID']
    return HttpResponseRedirect('/logincustomerpage')

# customer site
