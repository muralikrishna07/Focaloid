from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import account
from bank.forms import accountcreateform,LoginForm,BalanceCheckForm,TransferAmountForm,DepositAmountForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')

def acc(request):
    form=accountcreateform()
    context = {}
    context["form"]=form
    if (request.method=='POST'):
        form=accountcreateform(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get("name")
            accno=form.cleaned_data.get("accno")
            mpin=form.cleaned_data.get("mpin")
            email=form.cleaned_data.get("email")
            phonenumber=form.cleaned_data.get("phonenumber")
            balance=form.cleaned_data.get("balance")
            
            print(name,",",accno,",",mpin,",",email,",",phonenumber,",",balance)
            accou=account(name=name,accno=accno,mpin=mpin,email=email,phonenumber=phonenumber,balance=balance)
            accou.save()

            return redirect("create")
    return  render(request,"createacc.html",context)

def login(request):
    form=LoginForm()
    context={}
    context["form"]=form
    form=LoginForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            phone=form.cleaned_data.get("phonenumber")
            mpin=form.cleaned_data.get("mpin")

            try:

                object=account.objects.get(phonenumber=phone)
              
                if((object.phonenumber==phone) & (object.mpin==mpin)):
                    print("user exist")
                    return redirect("user")

            except Exception as e:
                print("invalid user")
                context["form"]=form
                return render(request,"login.html",context)

    return render(request, "login.html",context)

def balanceEnq(request):
    form=BalanceCheckForm()
    context={}
    context["form"]=form
    if(request.method=="POST"):
        form=BalanceCheckForm(request.POST)
        if form.is_valid():
            mpin=form.cleaned_data.get("mpin")
            try:

                object=account.objects.get(mpin=mpin)
                context["balance"]=object.balance
                return render(request,"balance.html",context)
            except Exception as e:
                context["form"]=form
                return render(request,"balance.html",context)


    return render(request,"balance.html",context)

def usr(request):
    return render(request,'user.html')


def transfer(request):
    form=TransferAmountForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=TransferAmountForm(request.POST)
        if form.is_valid():
            mpin=form.cleaned_data.get("mpin")
            amount=form.cleaned_data.get("amount")
            accno = form.cleaned_data.get("accno")
            try:
                object=account.objects.get(mpin=mpin)
                object1=account.objects.get(accno=accno)
                bal=object.balance-amount
                bal1=object1.balance+amount
                object.balance=bal
                object1.balance=bal1
               
                object.save()
                object1.save()

            except Exception:
                context["form"] = form
                return render(request, "transfer.html", context)

            form.save()


            return redirect("balance")
        else:
            context["form"]=form
            return render(request, "transfer.html", context)

    return render(request,"transfer.html",context)

def deposit(request):
    form=DepositAmountForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=DepositAmountForm(request.POST)
        if form.is_valid():
            mpin=form.cleaned_data.get("mpin")
            amount=form.cleaned_data.get("amount")
            
            try:
                object=account.objects.get(mpin=mpin)
                
                bal=object.balance+amount
                
                object.balance=bal
            
                object.save()

            except Exception:
                context["form"] = form
                return render(request, "deposit.html", context)

            form.save()


            return redirect("balance")
        else:
            context["form"]=form
            return render(request, "deposit.html", context)

    return render(request,"deposit.html",context)


def withdraw(request):
    form=DepositAmountForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=DepositAmountForm(request.POST)
        if form.is_valid():
            mpin=form.cleaned_data.get("mpin")
            amount=form.cleaned_data.get("amount")
            
            try:
                object=account.objects.get(mpin=mpin)
                
                bal=object.balance-amount
                
                object.balance=bal
            
                object.save()

            except Exception:
                context["form"] = form
                return render(request, "withdraw.html", context)

            form.save()


            return redirect("balance")
        else:
            context["form"]=form
            return render(request, "withdraw.html", context)

    return render(request,"withdraw.html",context)

