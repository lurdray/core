from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import *
from transactions.models import *


class HomeView(View):
    template_name = "home.html"
    def get(self, request):        
        labels = []
        data = []        
        stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        querysale = SaleItem.objects.order_by('-quantity')
        querypurchase = PurchaseItem.objects.order_by('-quantity')
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)
        sales = SaleBill.objects.order_by('-time')[:3]
        
        purchases = PurchaseBill.objects.order_by('-time')[:3]

        added=0
        for instance in stockqueryset:
            added +=  instance.quantity

        sale = 0 
        for instance in querysale:
            sale += instance.quantity

        purchase = 0 
        for instance in querypurchase:
            purchase += instance.quantity
        context = {
            'labels'    : labels,
            'data'      : data,
            'sale'      : sale,
            'sales'     : sales,
            'purchase'  : purchase,
            'purchases' : purchases,
            'added'     : added,
        }
        return render(request, self.template_name, context)

class BinView(View):
    template_name = "bin.html"
    def get(self, request):        
        labels = []
        data = []        
        stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)
        sales = SaleBill.objects.order_by('-time')
        purchases = PurchaseBill.objects.order_by('-time')
        stock = Stock.objects.all()
        context = {
            'labels'    : labels,
            'data'      : data,
            'sales'     : sales,
            'items'         : SaleItem.objects.order_by('billno'),
            'itemss'         : PurchaseItem.objects.order_by('billno'),
            'purchases' : purchases,
            'stock'     : stock
        }
        return render(request, self.template_name, context)

class AboutView(TemplateView):
    template_name = "about.html"