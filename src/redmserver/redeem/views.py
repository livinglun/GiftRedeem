from django.http import HttpResponse
from redeem.models import RedeemRecord
import util

ERROR_CMDER = '<xml><error>command format error</error></xml>' # command error
ERROR_EMFMT = '<xml><error>email format error</error></xml>' # email format error
ERROR_EMUSE = '<xml><error>this email has been used</error></xml>' # email has been used
ERROR_USLMT = '<xml><error>a user\'s redeem limitation is 3</error></xml>' # user's redeem limitation
ERROR_NOREG = '<xml><error>no such redeem code</error></xml>' # no such email and redeem code registration
ERROR_RCUSE = '<xml><error>the redeem code has been used</error></xml>' # the redeem code has been used
ERROR_NOSRV = '<xml><error>there provide no such service</error></xml>' # there is no such service

# Create your views here.
def rules(request):
    return HttpResponse("Showing the rules")
    
def register(request, name, email):
    # 1. check email format
    if not util.checkEmail(email):
        return HttpResponse(ERROR_EMFMT)
        
    # 2. check email is registered before
    if RedeemRecord.objects.filter(email=email).count() > 0:
        return HttpResponse(ERROR_EMUSE)
        
    # 3. generate redeem code and check database
    code = util.genRedmCode(email)
    if RedeemRecord.objects.filter(redmcode=code).count() > 0:
        return HttpResponse(ERROR_EMUSE)
            
    # 4. save name, email and redeem code
    p = RedeemRecord(name=name, email=email, redmcode=code, redmbit='0', gift='None')
    p.save()
    
    # 5. return message
    rpstmt = '<xml><result>email registration succss</result>\
            <name>%s</name>\
            <redmcode>%s</redmcode></xml>'%(name, code)
    return HttpResponse(rpstmt)

    
def redeem(request, name, redmcode):
    # 1. check redeem code is in database
    if RedeemRecord.objects.filter(redmcode=redmcode).count() == 0:
        return HttpResponse(ERROR_NOREG)

    # 2. check redeem code is not in redeem record
    if RedeemRecord.objects.filter(redmcode=redmcode, redmbit='1').count() > 0:
        return HttpResponse(ERROR_RCUSE)

    # 3. check user's redeem times
    redmtime = RedeemRecord.objects.filter(name=name, redmbit='1').count()
    if redmtime >= 3:
        return HttpResponse(ERROR_USLMT)
   
    # 4. get gift and save redeem record into database
    p = RedeemRecord.objects.get(redmcode=redmcode)
    p.redmbit = '1'
    p.gift = util.getGift(redmcode)
    p.save()
    
    # 5. return message
    rpstmt = '<xml><result>gift redeem succss</result>\
            <name>%s</name>\
            <redmcode>%s</redmcode>\
            <gift>%s</gift></xml>'%(name, redmcode, p.gift)
    return HttpResponse(rpstmt)