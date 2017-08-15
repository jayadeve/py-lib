import time
from way2sms_lib import way2sms
from twilio.rest import Client


class sms(object):
    def __init__(self, sp):
        self.me = '8147568968'
        if sp == 'twilio':
            self.send_function = self.send_sms_twilio
        elif sp == 'way2sms':
            self.send_function = self.send_sms_way2sms

    def send_sms_twilio(self, dest, msg):
        accountSid = 'AC24047e5464b9f453a2e9ac01a23d9cee'
        authToken = '7aff7c0498763305ed5d9ba4b6e9a9c2'
        twilioClient = Client(accountSid, authToken)
        myTwilioNumber = '+16283000312'
        destCellPhone = '+91{}'.format(dest)
        myMessage = twilioClient.api.account.messages.create(to=destCellPhone, from_=myTwilioNumber, body = msg)

    def send_sms_way2sms(self, dest, msg):    
        q = way2sms.sms(self.me, 'sms2yaw')
        q.send(dest, msg)
        #q.msgSentToday()
        q.logout()
        
    def send_sms(self, dest, msg):
        self.send_function(dest, msg) 
        

if __name__ == '__main__':
    msg = 'Test message from'
    
    sms_twilio = sms('twilio') 
    sms_twilio.send_sms('8147568968', msg + ' twilioi')

    sms_twilio = sms('way2sms') 
    sms_twilio.send_sms('8147568968', msg + ' way2sms')
