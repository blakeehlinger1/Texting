from twilio.rest import Client

accountSID = 'AC5cc40e15690b8315dfd06072069f8269'

authToken = 'f1035dbbff19081db65e6bb8821890ca'

client = Client(accountSID,authToken)

TwilioNumber = "+19125206973"

mycellphone = "+18326923524"

textmessage = client.messages.create(to=mycellphone,
                                    from_= TwilioNumber,
                                    body = "Hello World!")

print(textmessage.status)

call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
                            to=mycellphone,
                            from_=TwilioNumber)