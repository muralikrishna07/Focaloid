from django import forms
from django.forms import ModelForm

from bank.models import account,Transferdetails

class accountcreateform(forms.Form):
    name=forms.CharField(max_length=120)
    accno=forms.IntegerField()
    mpin=forms.CharField(max_length=6)
    email=forms.EmailField(max_length=20)
    phonenumber=forms.CharField(max_length=12)
    balance=forms.IntegerField()

class LoginForm(forms.Form):
    phonenumber = forms.CharField(max_length=12)
    mpin = forms.CharField(max_length=6)

class BalanceCheckForm(forms.Form):
    mpin = forms.CharField(max_length=6)
    def clean(self):
        clean_data=super().clean()
        mpin=clean_data.get("mpin")
        try:
            object=account.objects.get(mpin=mpin)

            if object:
                pass
        except:
            msg="you have provided invalid mpin"
            self.add_error("mpin",msg)


class TransferAmountForm(ModelForm):
    class Meta:
        model=Transferdetails
        fields="__all__"

    def clean(self):
        cleaned_data=super().clean()
        mpin=cleaned_data.get("mpin")
        accno=cleaned_data.get("accno")
        amount=cleaned_data.get("amount")
        print(mpin,",",accno,",",amount)
        try:
            object=account.objects.get(mpin=mpin)
            if(object):

        # for checking sufficent balance
                if(object.balance<amount ):
                    msg="insufficent amount"
                    self.add_error("amount",msg)
                pass
        except:
            msg="you have provided invalid mpin"
            self.add_error("mpin",msg)
        # for account validation
        try:
            object=account.objects.get(accno=accno)
            if(object):
                pass
        except:
            msg="you have provided invalid accno"
            self.add_error("accno",msg)

class DepositAmountForm(ModelForm):
    class Meta:
        model=Transferdetails
        fields=["amount","mpin"]

    def clean(self):
        cleaned_data=super().clean()
        mpin=cleaned_data.get("mpin")
        amount=cleaned_data.get("amount")
        print(mpin,",",amount)
        try:
            object=account.objects.get(mpin=mpin)
            if(object):

        # for checking sufficent balance
                if(object.balance<amount ):
                    msg="insufficent amount"
                    self.add_error("amount",msg)
                pass
        except:
            msg="you have provided invalid mpin"
            self.add_error("mpin",msg)
   
