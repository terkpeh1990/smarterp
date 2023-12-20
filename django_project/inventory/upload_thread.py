import threading
from django.http import request
from .models import *
from django.contrib import messages
from django.shortcuts import redirect,render
from django.utils.datastructures import MultiValueDictKeyError
from authentication.models import User
from company.models import Tenants
from erpproject.settings import  endPoint,key,Sender_Id, EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
import requests

class  CategoryThread(threading.Thread):
    def __init__(self, dbframe):
        self.data = dbframe 
       
        threading.Thread.__init__(self)

    def run(self):
        print('started')
        try:
            for i in self.data.itertuples():
                try:
                    tenant= Tenants.objects.get(name=i.Institutuion.title().strip())
                except Tenants.DoesNotExist:
                    tenant= Tenants.objects.create(name=i.Institutuion.title().strip())
                Categorys.objects.get_or_create(name=i.Category.title().strip(),tenant_id=tenant)
        except IOError:
            print('fail')
            pass

class  BrandThread(threading.Thread):
    def __init__(self, dbframe):
        self.data = dbframe 
       
        threading.Thread.__init__(self)

    def run(self):
        print('started')
        try:
            for i in self.data.itertuples():
                try:
                    tenant= Tenants.objects.get(name=i.Institutuion.title().strip())
                except Tenants.DoesNotExist:
                    tenant= Tenants.objects.create(name=i.Institutuion.title().strip())
                Brands.objects.get_or_create(name=i.Brand.title().strip(),tenant_id=tenant)
        except IOError:
            print('fail')
            pass

class  MeasureThread(threading.Thread):
    def __init__(self, dbframe):
        self.data = dbframe 
       
        threading.Thread.__init__(self)

    def run(self):
        print('started')
        try:
            for i in self.data.itertuples():
                try:
                    tenant= Tenants.objects.get(name=i.Institutuion.title().strip())
                except Tenants.DoesNotExist:
                    tenant= Tenants.objects.create(name=i.Institutuion.title().strip())
                Unit_of_Measurement.objects.get_or_create(name=i.Unit.title().strip(),tenant_id=tenant)
        except IOError:
            print('fail')
            pass


class  ProductThread(threading.Thread):
    def __init__(self, dbframe):
        self.data = dbframe 
       
        threading.Thread.__init__(self)

    def run(self):
        print('started')
        try:
            for i in self.data.itertuples():
               
                try:
                    tenant= Tenants.objects.get(name=i.Institutuion.title().strip())
                except Tenants.DoesNotExist:
                    tenant= Tenants.objects.create(name=i.Institutuion.title().strip())
                
                try:
                    category = Categorys.objects.get(name=i.Category.title().strip(),tenant_id =tenant)
                except Categorys.DoesNotExist:
                    category = Categorys.objects.create(name=i.Category.title().strip(),tenant_id =tenant)
                try:
                    unit = Unit_of_Measurement.objects.get(name=i.Unit.title().strip(),tenant_id =tenant)
                except Unit_of_Measurement.DoesNotExist:
                    unit = Unit_of_Measurement.objects.create(name=i.Unit.title().strip(),tenant_id =tenant)
                try:
                    product = Products.objects.get(name=i.Product.title().strip(),tenant_id =tenant)
                except Products.DoesNotExist:
                    product = Products.objects.create(category_id=category,name=i.Product.title().strip(),restock_level = i.ReorderLevel,unit_of_measurement=unit,type_of_product=i.Type.title().strip(),tenant_id=tenant)
                try:
                    inventory = Inventory.objects.get(product_id=product.id)
                    inventory.avialable_quantity += i.Quantity.strip()
                except Inventory.DoesNotExist:
                    inventory = Inventory.objects.create(product_id=product,avialable_quantity = i.Quantity,tenant_id = tenant)
                inventory_detail = Inventory_Details.objects.get_or_create(inventory_id = inventory,quantity_intake=i.Quantity,expiring_date=i.ExpiringDate)
        except IOError:
            print('fail')
            pass


class  SupplierThread(threading.Thread):
    def __init__(self, dbframe):
        self.data = dbframe 
       
        threading.Thread.__init__(self)

    def run(self):
        print('started')
        try:
            for i in self.data.itertuples():
                try:
                    tenant= Tenants.objects.get(name=i.Institutuion.title().strip())
                except Tenants.DoesNotExist:
                    tenant= Tenants.objects.create(name=i.Institutuion.title().strip())
                Supplier.objects.get_or_create(name=i.Supplier.title().strip(),address=i.Address.title().strip(),city=i.City.title().strip(),country=i.Country.title().strip(),tenant_id=tenant)
        except IOError:
            print('fail')
            pass


class  PendingThread(threading.Thread):
    def __init__(self,requisition):
        self.requisition = requisition
        self.hod = User.objects.filter(sub_division=self.requisition.staff.sub_division)
        threading.Thread.__init__(self)

    def run(self):
        print('started')
        url =endPoint + '&api_key=' + key 
        senders = Sender_Id

        usermessage =  'Dear ' + self.requisition.staff.last_name +' ' +self.requisition.staff.first_name  +','+'\nYour requisition with batch number' + ' '+ str(self.requisition.id) + ' '+ 'has been sent for approval. You will be notified when it is ready.'
        phone = '233'+self.requisition.staff.phone_number
        # hphone = '233'+self.hod_profile.telephone

        # try:
            
        #     subject = "Requisition"
        #     message = usermessage
        #     sender = EMAIL_HOST_USER
        #     to = [self.requisition.staff.email]
        #     send_mail(subject, message, sender, to, fail_silently=False)
        #     print('mail one success')
        # except Exception as e:
        #     print(e)
        #     pass
        # try:
        #     subject = "Requisition"
        #     message2 = hodmessage
        #     sender = EMAIL_HOST_USER
        #     to2 = [self.hod_profile.email]
        #     send_mail(subject, message2, sender, to2, fail_silently=False) 
        #     print('mail two success') 
        # except Exception as e:
        #     print(e)
        #     pass


        try:
            response = requests.get(url+'&to='+phone+'&from='+senders+'&sms='+usermessage)
            print(response.json())
        except IOError as e:
            print(e)
            pass
        for i in self.hod:
            if i.has_perm('inventory.custom_approve_requisition'):
                message = 'Dear ' + i.first_name + ' '+ i.last_name +',' + '\nRequisition with batch number' + ' '+ str(self.requisition.id) + ' '+ 'has been brougth to you attention for approval.'
                try:
                    response = requests.get(url+'&to='+i.phone_number+'&from='+senders+'&sms='+message)
                    print(response.json())
                except IOError as e:
                    print(e)
                    pass


class  AwaitingThread(threading.Thread):
    def __init__(self,requisition):
        self.requisition = requisition
        self.hod = User.objects.filter(tenant_id=self.requisition.staff.tenant_id)
        threading.Thread.__init__(self)

    def run(self):
        print('started')
        url =endPoint + '&api_key=' + key 
        senders = Sender_Id

        usermessage =  'Dear ' + self.requisition.staff.last_name +' ' +self.requisition.staff.first_name  +','+'\nYour requisition with batch number' + ' '+ str(self.requisition.id) + ' '+ 'has been sent been sent to Administration for approval. You will be notified when it is ready.'
        phone = '233'+self.requisition.staff.phone_number
        # hphone = '233'+self.hod_profile.telephone

        # try:
            
        #     subject = "Requisition"
        #     message = usermessage
        #     sender = EMAIL_HOST_USER
        #     to = [self.requisition.staff.email]
        #     send_mail(subject, message, sender, to, fail_silently=False)
        #     print('mail one success')
        # except Exception as e:
        #     print(e)
        #     pass
        # try:
        #     subject = "Requisition"
        #     message2 = hodmessage
        #     sender = EMAIL_HOST_USER
        #     to2 = [self.hod_profile.email]
        #     send_mail(subject, message2, sender, to2, fail_silently=False) 
        #     print('mail two success') 
        # except Exception as e:
        #     print(e)
        #     pass


        try:
            response = requests.get(url+'&to='+phone+'&from='+senders+'&sms='+usermessage)
            print(response.json())
        except IOError as e:
            print(e)
            pass
        for i in self.hod:
            if self.requisition.classification == "Consumables":
                
                if i.has_perm('inventory.custom_approve_consumable_requisition'):
                    message = 'Dear ' + i.first_name + ' '+ i.last_name +',' + '\nRequisition with batch number' + ' '+ str(self.requisition.id) + ' '+ 'has been brougth to you attention for approval.'
                    try:
                        response = requests.get(url+'&to='+i.phone_number+'&from='+senders+'&sms='+message)
                        print(response.json())
                    except IOError as e:
                        print(e)
                        pass
            else:
                if i.has_perm('inventory.custom_approve_capital_requisition'):
                    message = 'Dear ' + i.first_name + ' '+ i.last_name +',' + '\nRequisition with batch number' + ' '+ str(self.requisition.id) + ' '+ 'has been brougth to you attention for approval.'
                    try:
                        response = requests.get(url+'&to='+i.phone_number+'&from='+senders+'&sms='+message)
                        print(response.json())
                    except IOError as e:
                        print(e)
                        pass


class  ApprovedThread(threading.Thread):
    def __init__(self,requisition):
        self.requisition = requisition
        self.hod = User.objects.filter(tenant_id=self.requisition.staff.tenant_id)
        threading.Thread.__init__(self)

    def run(self):
        print('started')
        url =endPoint + '&api_key=' + key 
        senders = Sender_Id

        usermessage =  'Dear ' + self.requisition.staff.last_name +' ' +self.requisition.staff.first_name  +','+'\nYour requisition with batch number' + ' '+ str(self.requisition.id) + ' '+ 'has been approved. Please pass by the stores unit at the Head office to pickup your item(s). You will be required to provide the unique batch number before pickup'
        phone = '233'+self.requisition.staff.phone_number
        # hphone = '233'+self.hod_profile.telephone

        # try:
            
        #     subject = "Requisition"
        #     message = usermessage
        #     sender = EMAIL_HOST_USER
        #     to = [self.requisition.staff.email]
        #     send_mail(subject, message, sender, to, fail_silently=False)
        #     print('mail one success')
        # except Exception as e:
        #     print(e)
        #     pass
        # try:
        #     subject = "Requisition"
        #     message2 = hodmessage
        #     sender = EMAIL_HOST_USER
        #     to2 = [self.hod_profile.email]
        #     send_mail(subject, message2, sender, to2, fail_silently=False) 
        #     print('mail two success') 
        # except Exception as e:
        #     print(e)
        #     pass


        try:
            response = requests.get(url+'&to='+phone+'&from='+senders+'&sms='+usermessage)
            print(response.json())
        except IOError as e:
            print(e)
            pass
        for i in self.hod:
            if i.has_perm('inventory.custom_issue_requisition'):
                message = 'Dear ' + i.first_name + ' '+ i.last_name +',' + '\nRequisition with batch number' + ' '+ str(self.requisition.id) + ' '+ 'has been brougth to you attention for issuing.'
                try:
                    response = requests.get(url+'&to='+i.phone_number+'&from='+senders+'&sms='+message)
                    print(response.json())
                except IOError as e:
                    print(e)
                    pass


class  StoresThread(threading.Thread):
    def __init__(self,requisition):
        self.requisition = requisition
        threading.Thread.__init__(self)

    def run(self):
        print('started')
        url =endPoint + '&api_key=' + key 
        senders = Sender_Id

        usermessage =  'Dear ' + self.requisition.staff.last_name +' ' +self.requisition.staff.first_name  +','+'\nYour requisition with batch number' + ' '+ str(self.requisition.id) + ' '+ 'has been issued succesfully'
        phone = '233'+self.requisition.staff.phone_number
        # hphone = '233'+self.hod_profile.telephone

        # try:
            
        #     subject = "Requisition"
        #     message = usermessage
        #     sender = EMAIL_HOST_USER
        #     to = [self.requisition.staff.email]
        #     send_mail(subject, message, sender, to, fail_silently=False)
        #     print('mail one success')
        # except Exception as e:
        #     print(e)
        #     pass
        # try:
        #     subject = "Requisition"
        #     message2 = hodmessage
        #     sender = EMAIL_HOST_USER
        #     to2 = [self.hod_profile.email]
        #     send_mail(subject, message2, sender, to2, fail_silently=False) 
        #     print('mail two success') 
        # except Exception as e:
        #     print(e)
        #     pass


       