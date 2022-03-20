# Utility-bot :smiling_imp:

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
