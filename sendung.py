from mailjet_rest import Client
import os
api_key = '58271d695ba38436aaea0a5fa6b2ba1b'
api_secret = 'f84f3646abdaf5b3866abb5f396cd10f'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "fayiko4911@runfons.com",
        "Name": "Marco"
      },
      "To": [
        {
          "Email": "fayiko4911@runfons.com",
          "Name": "Marco"
        }
      ],
      "Subject": "Greetings from Mailjet.",
      "TextPart": "My first Mailjet email",
      "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
