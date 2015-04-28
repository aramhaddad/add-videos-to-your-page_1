from twilio import rest

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd4d9fd2e65865f2aa60f4c5004908226"
auth_token = "1d747b35231340c928a399584556ce15"
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="I Love You",
    to="+14074134411", # Replace with your phone number
    from_="+13214300273") # Replace with your Twilio number
print message.sid
