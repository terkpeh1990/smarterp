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
from django.views.generic.list import ListView
import os



@login_required(login_url='authentication:login')
@permission_required('inventory.custom_view_job_certification',raise_exception = True)
def job_cert(request):
    if request.user.is_superuser:
        job_list = Job_Certification.objects.all()
        app_model = Companymodule.objects.all()
    else:
       
        app_model = Companymodule.objects.filter(tenant_id = request.user.devision.tenant_id.id)
        job_list = Job_Certification.objects.filter(tenant_id = request.user.devision.tenant_id.id)
    template = 'inventory/job/job.html'
    context = {
        'job_list': job_list,
        'heading': 'List of Certifications',
        'pageview': 'Certification',
        'app_model':app_model
    }
    return render(request,template,context)


@login_required(login_url='authentication:login')
@permission_required('inventory.custom_create_job_certification',raise_exception = True)
def add_job(request):
    if request.user.is_superuser:
        app_model = Companymodule.objects.all()
    else:
        app_model = Companymodule.objects.filter(tenant_id = request.user.devision.tenant_id.id)
    if request.method == 'POST':
        form = JobForm(request.POST,request=request)
        if form.is_valid():
            job = form.save(commit=False)
            if request.user.is_superuser:
                tenant_id = form.cleaned_data['tenant_id']
            else:
                tenant_id = request.user.devision.tenant_id
            job.tenant_id = tenant_id
            job.save()
            messages.info(request,'Certification Initiated, Please add or upload Products')
            return redirect('inventory:add-job-details' , job.id)
    else:
        form = JobForm(request=request)

    template = 'inventory/job/create-job.html'
    context = {
        'form':form,
        'heading': 'New Certification',
        'pageview': 'List of Certification',
        'app_model':app_model
    }
    return render(request,template,context)


def add_job_detail(request,job_id):
    job = Job_Certification.objects.get(id=job_id)
    detail = Job_detail.objects.filter(job_id=job.id)
    total = detail.count()
    total_accepted = detail.filter(status="Accepted").count()
    total_rejected = detail.filter(status="Rejected").count()
    if request.user.is_superuser:
        app_model = Companymodule.objects.all()
        product = Products.objects.filter(type_of_product="Capital")
    else:
        app_model = Companymodule.objects.filter(tenant_id = request.user.devision.tenant_id.id)
        product = Products.objects.filter(tenant_id = request.user.devision.tenant_id.id,type_of_product="Capital")
    if request.method == 'POST':
        form = JobDetailForm(request.POST,request=request)
        prod = request.POST.get("product")
        print(prod)
        if form.is_valid():
            tenant =request.user.devision.tenant_id.id
            inven = Inventory.objects.get(product_id__name = prod,tenant_id=tenant)
            serial_number  = form.cleaned_data['serial_number']
            describtion = form.cleaned_data['description']
            status = form.cleaned_data['status']
            funding = form.cleaned_data['funding']
            brand_id = form.cleaned_data['brand_id']
            Job_detail.objects.get_or_create(job_id=job,product_id=inven.product_id,brand_id=brand_id,serial_number=serial_number,description=describtion,status=status,funding=funding)
            messages.info(request,'Item added')
            return redirect('inventory:add-job-details' , job.id)
    else:
        form = JobDetailForm(request=request)

    template = 'inventory/job/create-job-detail.html'
    context = {
        'form':form,
        'heading': 'New Restock',
        'pageview': 'List of Restock',
        'app_model':app_model,
        'detail':detail,
        'job':job,
        'product':product,
        'total':total,
        'total_accepted':total_accepted,
        'total_rejected':total_rejected
    }
    return render(request,template,context)


def edit_job_detail(request,job_id):
    jobs = Job_detail.objects.get(id=job_id)
    job = Job_Certification.objects.get(id=jobs.job_id.id)
    detail = Job_detail.objects.filter(job_id=job.id)
    if request.user.is_superuser:
        app_model = Companymodule.objects.all()
        product = Products.objects.filter(type_of_product="Capital")
    else:
        app_model = Companymodule.objects.filter(tenant_id = request.user.devision.tenant_id.id)
        product = Products.objects.filter(tenant_id = request.user.devision.tenant_id.id,type_of_product="Capital")
    if request.method == 'POST':
        form = JobDetailForm(request.POST,instance=jobs,request=request)
        prod = request.POST.get("product")
        if form.is_valid():
            tenant =request.user.devision.tenant_id.id
            inven = Inventory.objects.get(product_id__name = prod,tenant_id=tenant)
            product_id = product_id=inven.product_id
            serial_number  = form.cleaned_data['serial_number']
            describtion = form.cleaned_data['description']
            status = form.cleaned_data['status']
            funding = form.cleaned_data['funding'] 
            brand_id= form.cleaned_data['brand_id'] 
            jobs.product_id = product_id
            jobs.serial_number = serial_number
            jobs.describtion  = describtion 
            jobs.status  = status
            jobs.funding  = funding 
            jobs.brand_id = brand_id
            jobs.job_id =job 
            jobs.save()
            messages.info(request,'Item Updated')
            return redirect('inventory:add-job-details' , job.id)
    else:
        form = JobDetailForm(instance=jobs,request=request)

    template = 'inventory/job/update-job-detail.html'
    context = {
        'form':form,
        'heading': 'Update Certification',
        'pageview': 'List of Certification',
        'app_model':app_model,
        'detail':detail,
        'product':product,
        'job ':job,
        'item':jobs
    }
    return render(request,template,context)

@login_required(login_url='authentication:login')
# @permission_required('inventory.custom_delete_product')
def delete_job_item(request,job_id):
    job= Job_detail.objects.get(id=job_id)
    job.delete()
    messages.error(request,'Item Deleted')
    return redirect('inventory:add-job-details', job.job_id.id )


@login_required(login_url='authentication:login')
@permission_required('inventory.custom_update_job_certification',raise_exception = True)
def edit_job(request,job_id):
    job = Job_Certification.objects.get(id=job_id)
    if request.user.is_superuser:
        app_model = Companymodule.objects.all()
    else:
        app_model = Companymodule.objects.filter(tenant_id = request.user.devision.tenant_id.id)
    if request.method == 'POST':
        form = JobForm(request.POST,instance=job ,request=request)
        if form.is_valid():
            restock=form.save(commit=False)
            if request.user.is_superuser:
                tenant_id = form.cleaned_data['tenant_id']
            else:
                tenant_id = request.user.devision.tenant_id
            restock.tenant_id = tenant_id
            restock.save()
            messages.info(request,'Restock Updated')
            return redirect('inventory:add-job-details',job.id)
    else:
        form = JobForm(instance=job ,request=request)

    template = 'inventory/restock/create-restock.html'
    context = {
        'form':form,
        'heading': 'Update',
        'pageview': 'List of Restocks',
        'app_model':app_model
    }
    return render(request,template,context)


def delete_job(request,job_id):
    job = Job_Certification.objects.get(id=job_id)
    job.delete()
    messages.error(request,'Certification Deleted')
    return redirect('inventory:job-list')



@login_required(login_url='authentication:login')
def job_detail_upload(request,job_id):
    job = Job_Certification.objects.get(id=job_id)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data['file']
            fs = FileSystemStorage()
            filename = fs.save(excel_file.name, excel_file)
            uploaded_file_url = fs.url(filename)  
            file_path = os.path.join(fs.location, filename) 
            if os.path.exists(file_path):           
                empexceldata = pd.read_excel(file_path)      
                dbframe = empexceldata
                try:
                    for i in dbframe.itertuples():
                        tenant =request.user.devision.tenant_id.id
                        try:
                            brand = Brands.objects.get(name=i.Brand.title().strip(),tenant_id=tenant)
                        except Brands.DoesNotExist:
                            brand = Brands.objects.create(name=i.Brand.title().strip(),tenant_id=tenant)
                        try:
                            inven = Inventory.objects.get(product_id__name = i.Products.title().strip(),tenant_id=tenant)
                            product_id=inven.product_id
                            
                            Job_detail.objects.get_or_create(job_id=job,product_id=product_id,brand_id=brand,serial_number=i.Serialnumber,description=i.Describtione,status=i.Status,funding=i.Funding)
                        except Inventory.DoesNotExist:
                            pass
                    messages.info(request,'Restock Data Uploaded')
                    return redirect('inventory:add-job-details',job.id)  
                except IOError:
                    messages.error(request,'Restock Data Upload Error')
                    return redirect('inventory:add-job-details',job.id)  
            else:
                messages.error(request, 'File not found.')
            return redirect('inventory:add-job-details',job.id) 
    else:
        form = UploadFileForm()

    template = 'authentication/upload.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def cancel_job(request,job_id):
    job = Job_Certification.objects.get(id=job_id)
    job.status="Cancelled"
    job.save()
    messages.error(request,'Certification Cancelled')
    return redirect('inventory:add-job-details',job.id)

def reverse_job(request,job_id):
    job = Job_Certification.objects.get(id=job_id)
    job.status="Pending"
    job.save()
    messages.info(request,'Certification Transaction Reversed')
    return redirect('inventory:add-job-details',job.id)

def approve_job(request,job_id):
    job = Job_Certification.objects.get(id=job_id)
    detail = Job_detail.objects.filter(job_id=job.id,status="Accepted")
    for i in detail:
        try:
            inventory = Inventory.objects.get(product_id = i.product_id.id,tenant_id=job.tenant_id)
            try:
                a = Assets.objects.get(product_id=i.product_id,serial_number=i.serial_number,description=i.description,brand_id=i.brand_id,tenant_id=job.tenant_id)
            except Assets.DoesNotExist:
                a = Assets.objects.create(product_id=i.product_id,serial_number=i.serial_number,description=i.description,brand_id=i.brand_id,tenant_id=job.tenant_id)
                inventory.avialable_quantity += 1
                inventory.save()
        except Inventory.DoesNotExist:
            pass
    job.status="Approved"
    job.save()
    messages.info(request,'Certification Approved ')
    return redirect('inventory:add-job-details',job.id)

