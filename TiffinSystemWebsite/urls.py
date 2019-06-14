"""TiffinSystemWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import myfunctions

urlpatterns = [
    path('admin/', admin.site.urls),

    # public site
    path('', myfunctions.indexpage, name='indexpage'),
    path('signuppartner', myfunctions.signuppartner, name='signuppartner'),
    path('signuppartneraction', myfunctions.signuppartneraction, name='signuppartneraction'),
    path('loginpartnerpage', myfunctions.loginpartnerpage, name='loginpartnerpage'),
    path('loginpartneraction', myfunctions.loginpartneraction, name='loginpartneraction'),
    path('signupcustomer', myfunctions.signupcustomer, name='signupcustomer'),
    path('signupcustomeraction', myfunctions.signupcustomeraction, name='signupcustomeraction'),
    path('logincustomerpage', myfunctions.logincustomerpage, name='logincustomerpage'),
    path('logincustomeraction', myfunctions.logincustomeraction, name='logincustomeraction'),
    path('showitemspage',myfunctions.showitemspage,name='showitemspage'),
    # path('addtocartpage',myfunctions.addtocartpage,name='addtocartpage'),
    path('addtocartpage1',myfunctions.addtocartpage,name='addtocartpage1'),
    path('getcartitemsintable',myfunctions.getcartitemsintable,name='getcartitemsintable'),
    path('deletefromcart',myfunctions.deletefromcart,name='deletefromcart'),
    path('getcartcount',myfunctions.getcartcount,name='getcartcount'),

    path('allpartnerpage',myfunctions.allpartnerpage,name='allpartnerpage'),
    path('allpartnerforcustomer',myfunctions.allpartnerforcustomer,name='allpartnerforcustomer'),
    path('partnerforcustomerbyid',myfunctions.partnerforcustomerbyid,name='partnerforcustomerbyid'),
    path('showpartnermenu',myfunctions.showpartnermenu,name='showpartnermenu'),
    path('showpartnergallery',myfunctions.showpartnergallery,name='showpartnergallery'),
    path('getmenubypartner',myfunctions.getmenubypartner,name='getmenubypartner'),
    path('mycart',myfunctions.mycart,name='mycart'),
    path('proceedtopay',myfunctions.proceedtopay,name='proceedtopay'),
    path('billinginfo',myfunctions.billinginfo,name='billinginfo'),
    path('thankspage',myfunctions.thankspage,name='thankspage'),
    path('showsales',myfunctions.showsales,name='showsales'),
    path('myorderspage',myfunctions.myorderspage,name='myorderspage'),
    path('myorders',myfunctions.myorders,name='myorders'),

    # public site
    # admin site
    path('adminindex', myfunctions.adminindex, name='adminindex'),
    path('loginadminpage', myfunctions.loginadminpage, name='loginadminpage'),
    path('loginadminaction', myfunctions.loginadminaction, name='loginadminaction'),
    path('cp_admin', myfunctions.cp_admin, name='cp_admin'),
    path('cp_adminaction', myfunctions.cp_adminaction, name='cp_adminaction'),
    path('adminlogout', myfunctions.adminlogout, name='adminlogout'),
    path('pendingpartnerpage', myfunctions.pendingpartnerpage, name='pendingpartnerpage'),
    path('pendingpartnerlist', myfunctions.pendingpartnerlist, name='pendingpartnerlist'),
    path('approverejectpartner', myfunctions.approverejectpartner, name='approverejectpartner'),
    path('partnerlistbyname', myfunctions.partnerlistbyname, name='partnerlistbyname'),
    path('pendingcustomerpage', myfunctions.pendingcustomerpage, name='pendingcustomerpage'),
    path('pendingcustomerlist', myfunctions.pendingcustomerlist, name='pendingcustomerlist'),
    path('approverejectcustomer', myfunctions.approverejectcustomer, name='approverejectcustomer'),
    path('customerlistbyname', myfunctions.customerlistbyname, name='customerlistbyname'),
    path('addcategory', myfunctions.addcategory, name='addcategory'),
    path('addcategoryaction', myfunctions.addcategoryaction, name='addcategoryaction'),
    path('viewcategorypage', myfunctions.viewcategorypage, name='viewcategorypage'),
    path('viewcategorylist', myfunctions.viewcategorylist, name='viewcategorylist'),
    path('editcategorypage', myfunctions.editcategorypage, name='editcategorypage'),
    path('viewcategorybyid', myfunctions.viewcategorybyid, name='viewcategorybyid'),
    path('editcategoryaction', myfunctions.editcategoryaction, name='editcategoryaction'),
    path('deletecategory', myfunctions.deletecategory, name='deletecategory'),
    path('addoffer', myfunctions.addoffer, name='addoffer'),
    path('addofferaction', myfunctions.addofferaction, name='addofferaction'),
    path('viewofferpage', myfunctions.viewofferpage, name='viewofferpage'),
    path('viewofferlist', myfunctions.viewofferlist, name='viewofferlist'),
    path('offerlistbydate', myfunctions.offerlistbydate, name='offerlistbydate'),
    path('editofferpage', myfunctions.editofferpage, name='editofferpage'),
    path('viewofferbyid',myfunctions.viewofferbyid,name='viewofferbyid'),
    path('editofferaction', myfunctions.editofferaction, name='editofferaction'),
    path('deleteoffer', myfunctions.deleteoffer, name='deleteoffer'),
    # admin site

    # partner site
    path('partnerindex', myfunctions.partnerindex, name='partnerindex'),
    path('addgallerypage', myfunctions.addgallerypage, name='addgallerypage'),
    path('addgalleryaction', myfunctions.addgalleryaction, name='addgalleryaction'),
    path('viewgallerypage', myfunctions.viewgallerypage, name='viewgallerypage'),
    path('cp_partner', myfunctions.cp_partner, name='cp_partner'),
    path('cp_partneraction', myfunctions.cp_partneraction, name='cp_partneraction'),
    path('partnerlogout', myfunctions.partnerlogout, name='partnerlogout'),
    path('addfooditem',myfunctions.addfooditempage,name='addfooditem'),
    path('addfooditemaction',myfunctions.addfooditemaction,name='addfooditemaction'),
    path('viewfooditempage', myfunctions.viewfooditempage, name='viewfooditempage'),
    path('viewfooditemlist',myfunctions.viewfooditemlist,name='viewfooditemlist'),
    path('editfooditempage',myfunctions.editfooditempage,name='editfooditempage'),
    path('viewfooditembyid',myfunctions.viewfooditembyid,name='viewfooditembyid'),

    path('deletefooditem',myfunctions.deletefooditem,name='deletefooditem'),
    path('restorderspage',myfunctions.restorderspage,name='restorderspage'),
    path('restorders',myfunctions.restorders,name='restorders'),
    path('restorderdetailpage',myfunctions.restorderdetailpage,name='restorderdetailpage'),
    path('restorderdetail',myfunctions.restorderdetail,name='restorderdetail'),
    path('accept_reject_order',myfunctions.accept_reject_order,name='accept_reject_order'),
    path('todaysales',myfunctions.todaysales,name='todaysales'),
    path('monthlysales',myfunctions.monthlysales,name='monthlysales'),

    # partner site

    # customer site

    path('customerindex', myfunctions.customerindex, name='customerindex'),
    path('cp_customer', myfunctions.cp_customer, name='cp_customer'),
    path('cp_customeraction', myfunctions.cp_customeraction, name='cp_customeraction'),
    path('customerlogout',myfunctions.customerlogout,name='customerlogout'),

    # customer site

]
