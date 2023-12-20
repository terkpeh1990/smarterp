from django import forms
from .models import *
from django.forms.widgets import NumberInput
from company.models import *

class CategoryForm(forms.ModelForm):
    name = forms.CharField(label=False)
    tenant_id = forms.ModelChoiceField(label=False, queryset=Tenants.objects.all(),required=False)
    class Meta:
        model = Categorys
        fields = ('name','tenant_id')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(CategoryForm,self).__init__(*args, **kwargs)
        if self.request.user.is_superuser:
            self.fields['tenant_id'].queryset = Tenants.objects.all()
        else:
            self.fields['tenant_id'].queryset = Tenants.objects.filter(name=self.request.user.devision.tenant_id.name)

class BrandForm(forms.ModelForm):
    name = forms.CharField(label=False)
    tenant_id = forms.ModelChoiceField(label=False, queryset=Tenants.objects.all(),required=False)
    class Meta:
        model = Brands
        fields = ('name','tenant_id')
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(BrandForm,self).__init__(*args, **kwargs)
        if self.request.user.is_superuser:
            self.fields['tenant_id'].queryset = Tenants.objects.filter()
        else:
            self.fields['tenant_id'].queryset = Tenants.objects.filter(name=self.request.user.devision.tenant_id.name)

class MeasurementForm(forms.ModelForm):
    name = forms.CharField(label=False)
    tenant_id = forms.ModelChoiceField(label=False, queryset=Tenants.objects.all(),required=False)
    class Meta:
        model = Unit_of_Measurement
        fields = ('name','tenant_id')
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(MeasurementForm,self).__init__(*args, **kwargs)
        if self.request.user.is_superuser:
            self.fields['tenant_id'].queryset = Tenants.objects.filter()
        else:
            self.fields['tenant_id'].queryset = Tenants.objects.filter(name=self.request.user.devision.tenant_id.name)


class ProductForm(forms.ModelForm):
    # brand_id =forms.ModelChoiceField(queryset=Brands.objects.all().order_by('name'),label=False,required=False)
    category_id =forms.ModelChoiceField(queryset=Categorys.objects.all().order_by('name'),label=False)
    name = forms.CharField(label=False)
    restock_level = forms.IntegerField(label=False)
    unit_of_measurement =forms.ModelChoiceField(queryset=Unit_of_Measurement.objects.order_by('name'),label=False)
    tenant_id = forms.ModelChoiceField(label=False, queryset=Tenants.objects.all(),required=False)

    class Meta:
        model = Products
        fields = ('category_id','name','restock_level','unit_of_measurement','type_of_product','tenant_id')
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(ProductForm,self).__init__(*args, **kwargs)
        if self.request.user.is_superuser:
            self.fields['tenant_id'].queryset = Tenants.objects.filter()
        else:
            self.fields['tenant_id'].queryset = Tenants.objects.filter(name=self.request.user.devision.tenant_id.name)
            self.fields['category_id'].queryset = Categorys.objects.filter(tenant_id=self.request.user.devision.tenant_id)
            self.fields['unit_of_measurement'].queryset = Unit_of_Measurement.objects.filter(tenant_id=self.request.user.devision.tenant_id)
            # self.fields['brand_id'].queryset = Brands.objects.filter(tenant_id=self.request.user.devision.tenant_id)


    def clean_name(self):
        return self.cleaned_data['name'].title()

    def clean_name_avialable(self, *args, **kwargs):
        name = self.cleaned_data['name'].title()
        name_exists = Products.objects.filter(name=name)
        if name:
            if name_exists.exists():
                raise forms.ValidationError(
                    {'name': ["A product with this name already exist"]})
        
        return super(ProductForm, self).clean(*args, **kwargs)

class SupplierForm(forms.ModelForm):
    name = forms.CharField(label=False)
    address = forms.CharField(label=False)
    city = forms.CharField(label=False)
    country = forms.CharField(label=False)
    tenant_id = forms.ModelChoiceField(label=False, queryset=Tenants.objects.all(),required=False)
    class Meta:
        model = Supplier
        fields = ('name','address','city','country','tenant_id')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(SupplierForm,self).__init__(*args, **kwargs)
        if self.request.user.is_superuser:
            self.fields['tenant_id'].queryset = Tenants.objects.all()
        else:
            self.fields['tenant_id'].queryset = Tenants.objects.filter(name=self.request.user.devision.tenant_id.name)



class RestockForm(forms.ModelForm):
   
    restock_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),label=False)
    supplier_id = forms.ModelChoiceField(label=False, queryset=Supplier.objects.all())
    driver_name = forms.CharField(label=False)
    driver_contact = forms.CharField(label=False)
    tenant_id = forms.ModelChoiceField(label=False, queryset=Tenants.objects.all(),required=False)
    class Meta:
        model = Restocks
        fields = ('restock_date','supplier_id','driver_name','driver_contact','tenant_id')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(RestockForm,self).__init__(*args, **kwargs)
        if self.request.user.is_superuser:
            self.fields['tenant_id'].queryset = Tenants.objects.all()
            self.fields['supplier_id'].queryset = Supplier.objects.all()
        else:
            self.fields['tenant_id'].queryset = Tenants.objects.filter(name=self.request.user.devision.tenant_id.name)
            self.fields['supplier_id'].queryset = Supplier.objects.filter(tenant_id=self.request.user.devision.tenant_id.id)
            

    def clean_driver_name(self):
        return self.cleaned_data['driver_name'].title()


class RestockDetailForm(forms.ModelForm):
   
    quantity = forms.IntegerField(label=False)
    expiring_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),label=False)

    class Meta:
        model = Restock_details
        fields = ('quantity','expiring_date',)


class JobForm(forms.ModelForm):
    certification_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),label=False)
    supplier_id = forms.ModelChoiceField(label=False, queryset=Supplier.objects.all())
    driver_name = forms.CharField(label=False)
    driver_contact = forms.CharField(label=False)
    tenant_id = forms.ModelChoiceField(label=False, queryset=Tenants.objects.all(),required=False)
    class Meta:
        model = Job_Certification
        fields = ('certification_date','supplier_id','driver_name','driver_contact','tenant_id')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(JobForm,self).__init__(*args, **kwargs)
        if self.request.user.is_superuser:
            self.fields['tenant_id'].queryset = Tenants.objects.all()
            self.fields['supplier_id'].queryset = Supplier.objects.all()
        else:
            self.fields['tenant_id'].queryset = Tenants.objects.filter(name=self.request.user.devision.tenant_id.name)
            self.fields['supplier_id'].queryset = Supplier.objects.filter(tenant_id=self.request.user.devision.tenant_id.id)
            

    def clean_driver_name(self):
        return self.cleaned_data['driver_name'].title()

class JobDetailForm(forms.ModelForm):
    status = (
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
       
    )  
    funding = (
        ('Gov. of Ghana', 'Gov. of Ghana'),
        ('Donor', 'Donor'),
       
    )
    brand_id = forms.ModelChoiceField(label=False, queryset=Brands.objects.all())
    serial_number = forms.CharField(label=False)
    description = forms.CharField(label=False)
    status= forms.ChoiceField(choices = status,label=False)
    funding = forms.ChoiceField(choices = funding,label=False)
    class Meta:
        model = Job_detail
        fields = ('serial_number','description','status','funding')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(JobDetailForm, self).__init__(*args, **kwargs)
        self.fields['serial_number'].widget.attrs.update({'autofocus': 'autofocus'})
        
        if self.request.user.is_superuser:
            self.fields['brand_id'].queryset = Brands.objects.all() 
        else:
            self.fields['brand_id'].queryset = Brands.objects.filter(tenant_id=self.request.user.devision.tenant_id) 
            
    def describtion(self):
        return self.cleaned_data['description'].title()


class RequisitionForm(forms.ModelForm):
    sts= (
        ('Capital','Capital'),
        ('Consumables','Consumables'),
         
    ) 
    requisition_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),label=False)
    classification = forms.ChoiceField(choices = sts,label=False)
    tenant_id = forms.ModelChoiceField(label=False, queryset=Tenants.objects.all(),required=False)
    class Meta:
        model = Requisition
        fields = ('requisition_date','classification','tenant_id')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(RequisitionForm,self).__init__(*args, **kwargs)
        if self.request.user.is_superuser:
            self.fields['tenant_id'].queryset = Tenants.objects.all()
            
        else:
            self.fields['tenant_id'].queryset = Tenants.objects.filter(name=self.request.user.devision.tenant_id.name)
           
            

    def clean_driver_name(self):
        return self.cleaned_data['driver_name'].title()

class RequisitionDetailForm(forms.ModelForm):
    quantity = models.IntegerField(default=1)
    class Meta:
        model = Requisition_Details
        fields = ('quantity',)

class QuantityForm(forms.ModelForm):
    quantity_approved = forms.IntegerField(label=False)
    def clean(self, *args, **kwargs):
        quantity_approved = self.cleaned_data.get('quantity_approved')
        if quantity_approved < 1:
            
            raise forms.ValidationError(
                    {'quantity_approved': ["Quantity Approved Cannot Be Less Than 1"]})
        return super(QuantityForm, self).clean(*args, **kwargs)
    class Meta:
        model = Requisition_Details
        fields = ('quantity_approved',)


class TypeForm(forms.Form):
    sts= (
        ('Staff','Staff'),
        ('Pool','Pool'),
    ) 
    type_of_issue = forms.ChoiceField(choices = sts,label=False)


class AllocationForm(forms.ModelForm):
    
    allocation_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),label=False)
    description = forms.CharField(label=False)
    
    class Meta:
        model = Allocation
        fields = ('allocation_date','description')

    def clean_describtion(self):
        return self.cleaned_data['description'].title()

class AllocationDestinantionForm(forms.ModelForm):
    sts= (
        ('Capital','Capital'),
        ('Consumables','Consumables'),
         
    ) 
    devision = forms.ModelChoiceField(label=False, queryset=Devision.objects.filter(status = True))
    classification = forms.ChoiceField(choices = sts,label=False)
    class Meta:
        model = Allocation_Destination
        fields = ('devision','classification')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(AllocationDestinantionForm,self).__init__(*args, **kwargs)
        self.fields['devision'].queryset = Devision.objects.filter(tenant_id=self.request.user.devision.tenant_id.id,status = True)

class EditAllocationDestinantionForm(forms.ModelForm):
    devision = forms.ModelChoiceField(label=False, queryset=Devision.objects.filter(status = True))
    sub_division = forms.ModelChoiceField(queryset=Sub_Devision.objects.all(),label=False)
    class Meta:
        model = Allocation_Destination
        fields = ('devision','sub_division')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(AllocationDestinantionForm,self).__init__(*args, **kwargs)
       
        self.fields['devision'].queryset = Devision.objects.filter(tenant_id=self.request.user.devision.tenant_id.id,status = True)
        if 'devision' in self.data:
            try:
                devision = int(self.data.get('devision'))
                self.fields['sub_division'].queryset = Sub_Devision.objects.filter(
                    devision=devision)
            except (ValueError, TypeError):
                pass