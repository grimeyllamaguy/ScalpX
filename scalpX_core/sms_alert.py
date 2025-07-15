from twilio.rest import Client

def send_sms_alert(symbol, price, signal):
    # Set your Twilio account SID and Auth Token
    account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
    auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
    client = Client(account_sid, auth_token)

    message = f"Trade Signal Alert!\nSymbol: {symbol}\nPrice: ${price}\nSignal: {signal}"

    # Replace with the phone number you want to send the message to
    to_phone_number = 'RECIPIENT_PHONE_NUMBER'
    from_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'

    message = client.messages.create(
        body=message,
        from_=from_phone_number,
        to=to_phone_number
    )

    print(f"SMS alert sent to {to_phone_number}")
