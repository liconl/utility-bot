![bot](https://user-images.githubusercontent.com/60866363/159187012-5eec3fd1-3515-44b2-9cb1-b7344f5a34a6.png)
 
# Utility-bot 

### Send a custom text message using twilio to your friends!
![discord](https://user-images.githubusercontent.com/60866363/159186963-9a39713b-4ff0-4d8c-8ee0-6b9ce980ef57.png)

### Store customn images to a mongo database 
![discord5](https://user-images.githubusercontent.com/60866363/159187002-e01245f8-2b93-473b-a817-7ee95724cf05.png)

## Contributors:
 
## Set up and Installation

1. Update Python to `v3.9.6`
2. Clone repository.

```
$ git clone https://github.com/liconl/utility-bot
```

3. Set up virtual environment.

```
$ cd Utility-bot
$ py -m venv <name-of-venv>
```

4. Activate the virtual environment.

- For Windows:

```
$ <name-of-venv>\Scripts\activate.bat
```

- For Mac OS X:

```
$ source bot-env/bin/activate
```

5. Install `requirements.txt`.

```
$ py -m pip install -r requirements.txt
```

6. Make a `.env` file and copy and paste these variables:

```
CLIENT_ID={client id from discord}
TOKEN={token from discord}
TWILIO_ACCOUNT_SID={Twilio account SID}
TWILIO_AUTH_TOKEN={Twilio auth token}
TWILIO_PHONE_NUMBER={Twilio sender phone number}
```

## Development

- Run your virtual environment before making any changes.
- Branch off of main (create a new feature branch) before making any changes.
- Make a pull request once you are done (assign a reviewer).
- Deactivate your virtual environment.

```
$ bot-env\Scripts\deactivate.bat
```

## Notes

- The main contributor to discord.py, has sadly stopped his involement to the project. Some features may not be working or have been updated by the community. Check the discord.py docs here: `https://discordpy.readthedocs.io/en/stable/`
- The sms service `twilio` might not be the best for everyone. Checkout of twilio docs here: `https://www.twilio.com/docs/api` 

