from django.shortcuts import render
from donation.forms import DonationForm
from donation.models import doner
from django.http import HttpResponse

from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from blogproject.settings import EMAIL_HOST_USER
from django.template import Context
from django.core.mail import send_mail

from django.views.decorators.csrf import csrf_exempt
from Paytm import Checksum
MERCHANT_KEY = 'wVc51j!OatzNdALC';
# Create your views here.

def donationhome(request):
    return render(request, 'donation/donation1.html')

def Donation(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        cno = request.POST.get('cno', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        pin = request.POST.get('pin', '')
        state = request.POST.get('state', '')
        amount = request.POST.get('amount')

        form = doner(name=name, email=email, cno=cno, address=address, city=city, pin=pin, State=state, Amount=amount)
        form.save()
        #email
        htmly = get_template('email1.html')
        d = {'username': name, 'amount': amount}
        subject, from_email, to = 'Thanks for Donation', 'your_email@gmail.com', email
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        messages.success(request, f'Thanks For Donation')

             # request paytm to transfer amount to your account
        param_dict = {
            'MID': 'iuiFUB86800105926685',
            'ORDER_ID': '03',
            'TXN_AMOUNT': amount,
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/donation/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'donation/paytm.html', {'param_dict': param_dict})
    return render(request, 'donation/donate.html')


@csrf_exempt
def hendlerequest(request):
    # payment will send you post
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('Donate Successfully ')
        else:
            print('Donation was not successful because' + response_dict['RESPMSG'])
    return render(request, 'donation/response.html', {'response': response_dict})
    return render(request, 'donation/response.html')
    pass
