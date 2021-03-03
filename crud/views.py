from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect,redirect, resolve_url, reverse
from .models import itemsPost, saveOrder , requestS, set
from .forms import requestPostForm, order, order2
from django.forms.models import model_to_dict
import datetime
import re 


data = itemsPost.objects.all()
data2 =  saveOrder.objects.all()

##########################################################################################

###  NEW DEV

def update_view2(request, id):

    print("222 INSIDE UPDATE VIEW2")
    print("re //// {}".format(request.POST))
    ko = get_object_or_404(requestS, id=id)
    kN = ko.documentName 
    kD = ko.documentDate
    kQ = ko.quantity + 2
    kR = ko.remarks 
    kA = kQ * ko.rate
    txt = ' updated'
    print("ko ,,,, {}".format(ko))
    if request.method == "POST" :
        con = request.POST.get('qq', False)
        print("con -> {}".format(con))
        rem = request.POST.get('na', False)
        print("rem --> {}".format(rem))
        ko.quantity = con
        ko.amount = kA  
        ko.remarks = rem
        ko.save()
        f2 = order2(initial = { 'documentNo' : kN, 'documentDate' : kD } )
        dataS = requestS.objects.filter(documentName = kN, documentDate=kD)
        val =0
        for obj in dataS:
            val = val+obj.amount
    return render(request, "crud/post/fill2.html", {'f2':f2, 'dataS': dataS ,'val' : val} )
    


def open(request, id ):

    obj = get_object_or_404(set, id = id) 
    companyName = obj.companyName
    requestedBy = obj.requestedBy
    q1 = obj.q1
    dN = obj.dN
    dD =  obj.dD
    remarks = obj.remarks
    if request.method =="POST": 
        print("open request for id : {}".format(id))
    dataS = requestS.objects.filter(documentName = dN, documentDate=dD )
    val =0
    for obj in dataS:
        val = val+obj.amount
    f2 = order2(initial = { 'documentNo' : dN, 'documentDate' : dD } )
    return render(request, "crud/post/fill2.html", {'f2':f2, 'dataS': dataS ,'val' : val} ) 


def list_view(request):
    if request.method == "POST":
        if request.POST.get('form_type') == 'fThree':
            print("UNDER LIST VIEW POST")
    j = set.objects.all()
    return render(request ,'crud/post/list_view.html', { 'j' : j })


goL = []
dName = "" 
dDate = datetime.date.today()

def postData2(request):

    if request.method == "POST":
        global dName
        global dDate
        global goL
        if request.POST.get('form_type') == 'fOne':
            print("FORM 1")
            print("dName f1 >> {}".format(dName))
            print("dDate f1 >> {}".format(dDate))
            companyName = request.POST.get('companyName')
            requestedBy = request.POST.get('requestedBy')
            remarks = request.POST.get('remarks')
            g1 = goL
            dN = dName 
            dD = dDate
            z = set(
                companyName = companyName ,
                requestedBy = requestedBy ,
                q1 = goL ,
                dN = dN ,
                dD =  dD ,
                remarks = remarks
            )
            z.save()
            goL = []
        elif request.POST.get('form_type') == 'fTwo':
            print("FORM 2")
            f2 = order2(request.POST)
            print(f2)
            if f2.is_valid():
                cd = f2.cleaned_data
                print("cdf2 ---->{} ".format(cd)) 
                itemName= f2.cleaned_data['itemName']
                itr = itemsPost.objects.get(itemName = itemName)
                print(f2.cleaned_data['documentDate'])
                amount = itr.rate * f2.cleaned_data['quantity']
                sea = requestS(
                documentName = f2.cleaned_data['documentNo'],
                documentDate = f2.cleaned_data['documentDate'],
                itemName = itemName,
                make = itr.make,
                UOM = itr.UOM,
                quantity = f2.cleaned_data['quantity'],
                rate = itr.rate,
                amount = amount,
                requiredOn = f2.cleaned_data['requiredOn'],
                remarks = f2.cleaned_data['remarks'],
                )
                sea.save()
                p = requestS.objects.get(
                documentName = f2.cleaned_data['documentNo'],
                documentDate = f2.cleaned_data['documentDate'],
                itemName = itemName,
                make = itr.make,
                UOM = itr.UOM,
                quantity = f2.cleaned_data['quantity'],
                rate = itr.rate,
                amount = amount,
                requiredOn = f2.cleaned_data['requiredOn'],
                remarks = f2.cleaned_data['remarks'],
                )

                dName = f2.cleaned_data['documentNo']
                dDate = f2.cleaned_data['documentDate']
                z= int( p.id )
                goL.append( z )
                dataS = requestS.objects.filter(documentName = dName, documentDate=dDate)
                print('dataS-->{}'.format(dataS))
                val =0
                for obj in dataS:
                    val = val+obj.amount
                print("goL >> {}".format(goL))
                print("dName >> {}".format(dName))
                print("dDate >> {}".format(dDate))
                f2 = order2(initial = { 'documentNo' : dName, 'documentDate' : dDate } )
                return render(request, "crud/post/fill2.html", {'f2':f2, 'dataS': dataS ,'val' : val} )
            else:
                print("Not VALID F2")
        # dataS = requestS.objects.all()
        # print('dataS-->{}'.format(dataS))
        val =0
        # for obj in dataS:
        #     val = val+obj.amount
        print("goL >> {}".format(goL))
        print("dName >> {}".format(dName))
        print("dDate >> {}".format(dDate))
        f2 = order2()
        return render(request, "crud/post/fill2.html", {'f2':f2, 
        # 'dataS': dataS ,
        'val' : val} )
    else :
        f2 = order2()
        # dataS = requestS.objects.all()
        # print('dataS-->{}'.format(dataS))
        val =0
        # for obj in dataS:
        #     val = val+obj.amount
        return render(request, "crud/post/fill2.html", {'f2':f2 , 
        # 'dataS': dataS ,
        'val' : val })

def delete_view2(request, id): 
    print(request.POST)
    obj = get_object_or_404(requestS, id = id) 
    no = obj.id 
    deN = obj.documentName 
    deD = obj.documentDate
    so = set.objects.filter(dN = deN, dD = deD)
    print("so ==>>{}".format(so))
    if request.method =="POST": 
        li = so[0].q1
        li2 = [int(s) for s in re.findall(r'-?\d+\.?\d*', li )]
        print("li ******** {}".format(li2))
        li2.remove(no)
        print("li ******** {}".format(li2))
        so.update( q1 = li2 )
        obj.delete()
        f2 = order2(initial = { 'documentNo' : deN, 'documentDate' : deD } )
        dataS = requestS.objects.filter(documentName = deN, documentDate= deD )
        val =0
        for obj in dataS:
            val = val+obj.amount
        return render(request, "crud/post/fill2.html", {'f2':f2, 'dataS': dataS ,'val' : val} )
    else:
        val = 0
        f2 = order2()
        dataS = requestS.objects.all()
    return redirect('/crud/fill2/')  


##########################################################################################
def upDATA():
    print("=============upD here")

def update_view(request, id):
    # obj = get_object_or_404(saveOrder, id = id) 
    obj = saveOrder.objects.get(id = id)
    print('id ===> {}'.format(id ) )
    print("objU ---> {}".format(obj))
    if request.method =="POST": 
        print("model2 +++++{}".format( model_to_dict(obj) ))
        form2 = order(initial=model_to_dict(obj))
        form = requestPostForm()
        dataS = saveOrder.objects.all()
        print('dataS-->{}'.format(dataS))
        val =0
        for obj in dataS:
            val = val+obj.amount
        # return redirect('/crud/fill/')
        # return redirect('crud:postdata', {'form': form,'form2':form2,'dataS':dataS, 'val':val,})
        return render(request ,'crud/post/fill.html', {'form': form,'form2':form2,'dataS':dataS, 'val':val,})
    else :
        return HttpResponse('Invalid CREDENTIAL')

def delete_view(request, id): 
    context ={} 
    obj = get_object_or_404(saveOrder, id = id) 
    if request.method =="POST": 
        obj.delete() 
        form = requestPostForm()
        form2 = order()
        dataS = saveOrder.objects.all()
        val =0
        for obj in dataS:
            val = val+obj.amount
        # return redirect( 'Post_data', {'form': form, 'form2' : form2 , 
        #         'dataS':dataS, 'val':val})
        # return render(request, 'crud/post/fill.html', {'form': form, 'form2' : form2 , 
        #         'dataS':dataS, 'val':val})
        return redirect('/crud/fill/')
    else:
        val = 0
        form = requestPostForm()
        form2 = order()
        dataS = saveOrder.objects.all()
    return redirect('/crud/fill/')
    # return render(request, 'crud/post/fill.html', { 'data': data, 'data2' : data2 ,"dataS" : dataS,
    # 'form': form, 'form2' : form2, 'val' : val})

# Create your views here.
def Post_list(request):
    posts = itemsPost.objects.all()
    # print(posts)
    return render(request, 'crud/post/list.html', {'posts' : posts})

def Post_data(request):
    def any(iterable):
        for element in iterable:
            if element:
                return element
    d = any(data)
    d2 = any(data2)
    form = requestPostForm()
    form2 = order()
    if request.method == 'POST':

        if request.POST.get('form_type') == 'formOne':

            form = requestPostForm(request.POST)
            print(form)
            if form.is_valid:
                cd = form.cleaned_data 
                print(cd)
                return render(request, 'crud/post/show.html', { 'cd' : cd})
            else :
                return HttpResponse('Invalid CREDENTIAL')
        elif  request.POST.get('form_type') == 'formTwo' : 
            form2 = order(request.POST)
            print(form2)
            if form2.is_valid():
                cd = form2.cleaned_data
                print("cd ---->{} ".format(cd)) 
                costCenter = form2.cleaned_data['costCenter']
                # make = form2.cleaned_data['make']
                # unit = form2.cleaned_data['unit']
                # rate = form2.cleaned_data['rate']
                itemCode = form2.cleaned_data['itemCode']
                name = itemsPost.objects.get(itemCode = itemCode)
                quantity = form2.cleaned_data['quantity'] 
                # print(name.make, quantity)
                amount = name.rate * quantity
                sea = saveOrder(code=name.itemName,itemCode=itemCode,make =name.make, unit=name.UOM,
                quantity=quantity,amount = amount, rate=name.rate,center= costCenter)
                p = sea.save()
                count = saveOrder.objects.all().count()
                a_list = list(range(1, count+1))
                # print(a_list)
                k=[]
                v=[]
                for kl, vl in cd.items():
                    k.append(kl)
                    v.append(vl)
                v0=v[0]
                v1=v[1]
                v2=v[2]
                v3=int(v[3])
                v4=int(v[4])
                amount = v3*d.rate
                v5=v[5]
                print(data2)
                # print("count--->{}".format(count))
                # print(p)
                # k = cd.keys()
                # v= cd.values()
                # kli = []
                # for j in k :
                #     kli.append(j)
                # vli = []
                # for i in v :
                #     vli.append(i)
                # print('kli  {}'.format(kli))
                # print('vli  {}'.format(vli))
                # print(v)   
                # print(vli[0])
                # return render(request, 'crud/post/show.html', { 'cd' : cd , "k":kli , "v":vli })
                dataS = saveOrder.objects.all()
                print('dataS-->{}'.format(dataS))
                val =0
                for obj in dataS:
                    val = val+obj.amount
                form = requestPostForm()
                form2 = order()
                return render(request, 'crud/post/fill.html', { 'data': data, 'data2' : data2 ,'d2':d2,
                'form': form, 'form2' : form2 ,'count' : count,'itemsPost' :itemsPost,"d" : d, 'dataS':dataS,
                'a_list':a_list,'k' :k, 'v' : v,'v1' : v1, 'v2':v2,'v3':v3,"v4":v4,'v5':v5,'amount':amount,
                'saveOrder' :saveOrder,'val':val,"order":order, 
                # 'itemCode' :itemCode, 'itemName': itemName,'make':make,
                # 'unit':unit, 'rate':rate, 'costCenter': costCenter
                })
            else :
                return HttpResponse('Invalid CREDENTIAL') 
    else:
        form = requestPostForm()
        form2 = order()
        dataS = saveOrder.objects.all()
        val =0
        for obj in dataS:
            val = val+obj.amount
    return render(request, 'crud/post/fill.html', { 'data': data, 'data2' : data2 ,'dataS' :dataS ,
           'form': form, 'form2' : form2, "val" : val, "order":order,'val' :val })

