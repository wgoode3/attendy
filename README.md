# Attendy

Attendance automation tool using Selenium

### To use

Be sure to modify ```settings.json``` before use.

```JSON
{
    "driver_type": "Firefox",
    "page_load_timeout": 30,
    "suppress_alerts": true,
    "type": "Any Programs",
    "location": "All Locations",
    "email": "example@codingdojo.com",
    "sheet_url": "https://docs.google.com/spreadsheets/d/..." 
}
```

Set ```email``` to the email used to login to Gmail and ```sheet_url``` to the url of the Google Docs Spreadsheet.

Before running the program ensure you have [Selenium](https://selenium-python.readthedocs.io/installation.html) and [Geckodriver](https://github.com/mozilla/geckodriver/releases) installed first. 

With virtual environment active...

```shell
python attendy.py
```

You will then be prompted to enter the password used for gmail and learn platform access.