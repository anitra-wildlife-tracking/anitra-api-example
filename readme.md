
<a href="https://anitracking.com"><img src="https://anitracking.com/wp-content/uploads/2018/05/Anitrabiglogo-8-323x180.png" title="Anitra logo" alt="Anitra logo"></a>

# Anitra API sample code

This code provides a sample Anitra API-based application, a command line interface to export device list and device data. This code is only sample code to indicate how to work with the API, and any real application would need more user inputs checks and to ensure that ie the user is not inputting anything in the wrong format or proper exception handling.

## Commands

### Export device data
Exports all data you can access from the given device. This code uses the Anitra data scroll API to ensure data scroll consistency in case any new data is received.

Sample usage:
```python3 anitra-cli.py --clientid=YOUR_CLIENTID --clientkey=YOUR_CLIENT_KEY device-data 9999 --format csv --output 9999.csv```

### Export device list
Exports the list of devices you can access.

Sample usage:
```python3 anitra-cli.py --clientid=YOUR_CLIENTID --clientkey=YOUR_CLIENT_KEY device-data 9999 --format csv --output 9999.csv```

# Other API routes
Tracking data and tracking list can be implementedin the exact same fashion as their device counterparts, only the URL needs to be changed.