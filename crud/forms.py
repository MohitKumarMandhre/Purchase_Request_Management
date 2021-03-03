from django import forms
from django.forms import ModelForm
from .models import itemsPost
import datetime

INDENT_CHOICES= [
    ('Capital', 'Capital'),
    ('Revenue', 'Revenue')
    ]

CHARGE_CHOICES= [
    ('Chargeable', 'Chargeable'),
    ('NonChargeable', 'NonChargeable')
    ]
RESERVED_CHOICES = (
    ("Reserved", "Reserved"),
    ("Unreserved", "Unreserved")
)

CENTER_CHOICES = (
    ("center1", "center1"),
    ("center2", "center2"),
    ("center3", "center3"),
)
COMP_CHOICES = (
    ("ABC Company", "ABC Company"),
    ("DEF Company", "DEF Company"),
    ("XYZ Company", "XYZ Company"),
)
MAKE_CHOICES = (
    ("Metal", "metal"),
    ("Plastic", "plastic"),
    ("Metal & Plastic", "metal & plastic"),
)
UOM_CHOICES = (
    ("Count", "count"),
    ("Number", "number"),
)
# def unique(list1): 
#     li = []
#     list_set = set(list1) 
#     unique_list = (list(list_set)) 
#     for x in unique_list: 
#         li.append(x)
#     return li

qsL = []
qs = itemsPost.objects.values_list('itemCode').values()[0]['itemCode']
for q in itemsPost.objects.values('itemCode') :
    v = q['itemCode']
    # print("v --> {}".format(v))
    qsT = ( str(v) , v)
    qsL.append(qsT)
# print(qsL)
CODE_CHOICES = ( qsL )

nL = []
ns = itemsPost.objects.values_list('itemCode').values()[0]['itemCode']
for q in itemsPost.objects.values('itemName'):
    n = q['itemName']
    nsT = ( n , n )
    nL.append( nsT )
# print( nL  )
NAME_CHOICES = ( nL )

# mL = []
# ms = itemsPost.objects.values_list().values()[0]['make']
# for q in itemsPost.objects.values('make'):
#     n = q['make']
#     msT = ( n , n )
#     mL.append( msT )
# print(mL)
# Make_CHOICES = ( mL )

# uoL = []
# uos = itemsPost.objects.values_list().values()[0]['UOM']
# for q in itemsPost.objects.values('UOM'):
#     n = q['UOM']
#     uosT = ( n , n )
#     uoL.append( uosT )
# print( uoL )
# UOM_CHOICES = ( uoL )

class requestPostForm(forms.Form):
    
    documentNo = forms.CharField(label="Document Number",max_length=100 ,required=True)
    documentDate = forms.DateField(label="Document Date",required=True)
    # li = forms.ChoiceField(required=False,choices=COMP_CHOICES, )
    # companyName = forms.ChoiceField(label="Company Name",required=True,
    #             choices=COMP_CHOICES, )
    indentType = forms.MultipleChoiceField(label="Indent Type", 
                initial = 'Capital',choices=INDENT_CHOICES,required=True)
    isReserved = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxInput,
        choices=RESERVED_CHOICES,
    )
    # isReserved = forms.ChoiceField(label="Is Reserved",widget = forms.CheckboxInput,required= False,)
    # isReserved = forms.ChoiceField(label="Is Reserved",widget=forms.RadioSelect , choices=RESERVED_CHOICES)
    department = forms.CharField(label="Department",max_length=250,required=True)
    chargeType = forms.MultipleChoiceField(label="Charge Type", 
                initial = 'Chargeable',choices=CHARGE_CHOICES,required=True,
                )
    requestedBy = forms.CharField(label="Requested By",required=True)
    indentTag = forms.CharField(label="Indent Tag",required=True)
    remarks = forms.Textarea()

class order(forms.Form):

    # itemName = forms.ModelChoiceField(queryset=itemsPost.objects.values_list('itemName'))
    # itemCode = forms.IntegerField(label="Item Code",required=True)
    # itemCode = forms.ModelChoiceField(queryset=itemsPost.objects.values('itemCode') )
    itemCode = forms.ChoiceField(choices=CODE_CHOICES, required = True, initial = None)
    # itemName= forms.ChoiceField(choices=NAME_CHOICES, required = True, initial = None)
    make = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Please enter the make'}))
    techSpecs = forms.Textarea(attrs=None)
    unit = forms.CharField(required=True)
    quantity = forms.IntegerField(max_value=1000, required=True)
    rate = forms.IntegerField( required=True)
    costCenter = forms.MultipleChoiceField(label="Center Type", 
                initial = 'center1',choices=CENTER_CHOICES,required=True,
                )


class order2(forms.Form):

    documentNo = forms.CharField(label="Document Number",max_length=100 ,required=True)
    documentDate = forms.DateField(label="Document Date",required=True, initial=datetime.date.today() )
    itemName= forms.ChoiceField(choices=NAME_CHOICES, required = True, initial = None, label="Item Name")
    make = forms.CharField(label='Make', widget=forms.Select(choices=MAKE_CHOICES))
    UOM = forms.CharField(label='UOM', widget=forms.Select(choices=UOM_CHOICES))
    quantity = forms.IntegerField(required = True)
    # rate = forms.IntegerField(required = True)
    requiredOn = forms.DateField( label="Required On",widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'} ))
    # costCenter = forms.MultipleChoiceField(label="Center Type", 
    #             initial = 'center1',choices=CENTER_CHOICES,required=True,
    #             )
    # techSpecs = forms.Textarea(attrs=None)
    remarks = forms.CharField(label="Tech Specs",widget = forms.Textarea())