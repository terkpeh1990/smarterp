# from msilib.schema import Error
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from authentication.forms import UploadFileForm
from django.contrib.auth.decorators import login_required, permission_required
from .upload_thread import *
import pandas as pd
from tablib import Dataset
from django.core.files.storage import FileSystemStorage
from appsystem.models import *
import os





@login_required(login_url='authentication:login')
@permission_required('inventory.custom_view_supplier',raise_exception = True)
def supplier(request):
    if request.user.is_superuser:
        app_model = Companymodule.objects.all()
        supplier_list = Supplier.objects.all()
    else:
        app_model = Companymodule.objects.filter(tenant_id = request.user.devision.tenant_id.id)
        supplier_list = Supplier.objects.filter(tenant_id=request.user.devision.tenant_id.id)
    template = 'inventory/supplier/supplier.html'
    context = {
        'supplier_list': supplier_list,
        'heading': 'List of Suppliers',
        'pageview': 'Suppliers',
        'app_model':app_model
    }
    return render(request,template,context)


    name = models.CharField(max_length=250,null=True,blank=True)
    address = models.CharField(max_length=250,null=True,blank=True)
    city = models.CharField(max_length=250,null=True,blank=True)
    country = models.CharField(max_length=250,null=True,blank=True)

@login_required(login_url='authentication:login')
@permission_required('inventory.custom_create_supplier',raise_exception = True)
def add_supplier(request):
    if request.user.is_superuser:
        app_model = Companymodule.objects.all()
    else:
        app_model = Companymodule.objects.filter(tenant_id = request.user.devision.tenant_id.id)
    if request.method == 'POST':
        form = SupplierForm(request.POST,request=request)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']
            if request.user.is_superuser:
                tenant_id = form.cleaned_data['tenant_id']
            else:
                tenant_id = request.user.devision.tenant_id
            supplier = Supplier.objects.get_or_create(name=name.title(),address= address.title(),city=city.title(),country=country.title(),tenant_id=tenant_id)
            messages.info(request,'Supplier Saved')
            return redirect('inventory:supplier-list')
    else:
        form = SupplierForm(request=request)

    template = 'inventory/supplier/create-supplier.html'
    context = {
        'form':form,
        'heading': 'New Supplier',
        'pageview': 'List of Suppliers',
        'app_model':app_model
    }
    return render(request,template,context)

@login_required(login_url='authentication:login')
@permission_required('inventory.custom_update_supplier',raise_exception = True)
def edit_supplier(request,supplier_id):
    if request.user.is_superuser:
        app_model = Companymodule.objects.all()
    else:
        app_model = Companymodule.objects.filter(tenant_id = request.user.devision.tenant_id.id)
    supplier=Supplier.objects.get(id=brand_id)
    if request.method == 'POST':
        form = SupplierForm(request.POST,instance=supplier,request=request)
        if form.is_valid():
            suppliers = form.save(commit=False)
            if request.user.is_superuser:
                tenant_id = form.cleaned_data['tenant_id']
            else:
                tenant_id = request.user.devision.tenant_id
            suppliers.tenant_id = tenant_id
            suppliers.save()
            messages.info(request,'Supplier Updated')
            return redirect('inventory:supplier-list')
    else:
        form = SupplierForm(instance=supplier,request=request)

    template = 'inventory/supplier/create-supplier.html'
    context = {
        'form':form,
        'heading': 'Update',
        'pageview': 'List of Suppliers',
        'app_model':app_model,
       
    }
    return render(request,template,context)

@login_required(login_url='authentication:login')
@permission_required('inventory.custom_delete_supplier',raise_exception = True)
def delete_supplier(request,supplier_id):
    supplier=Supplier.objects.get(id=supplier_id)
    supplier.delete()
    messages.error(request,'Supplier Deleted')
    return redirect('inventory:supplier-list')
   
@login_required(login_url='authentication:login')
def supplier_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data['file']
            fs = FileSystemStorage()
            filename = fs.save(excel_file.name, excel_file)
            uploaded_file_url = fs.url(filename)
            # Get the complete path to the uploaded file
            file_path = os.path.join(fs.location, filename)
            if os.path.exists(file_path):  # Check if the file exists
                empexceldata = pd.read_excel(file_path)
                dbframe = empexceldata
                SupplierThread(dbframe).start()
                messages.success(request,'Supplier Data Uploaded Successfully')
            
            else:
                messages.error(request, 'File not found.')
            return redirect('inventory:supplier-list')
    else:
        form = UploadFileForm()

    template = 'authentication/upload.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
   
