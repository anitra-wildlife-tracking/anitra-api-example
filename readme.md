<h1 align="center">
<a href="https://anitracking.com"><img src="https://anitracking.com/wp-content/uploads/2018/05/Anitrabiglogo-8-323x180.png" title="Anitra logo" alt="Anitra logo"></a>
</h1>

<p align="center">
  <a href="https://anitracking.com">
    Anitra
  </a>
  •
  <a href="https://anitracking.com/api/">
    Anitra API documentation
  </a>
  •
  <a href="https://support.anitracking.com/index.php?title=Main_Page#MAIN_CONCEPTS">
    Anitra data model
  </a>
  •
  <a href="https://github.com/anitra-wildlife-tracking/animal-tracking-data">
   Python library
  </a>
</p>

---
> Sample implementation of the Anitra data API in Python.

# Introduction

This code provides a reference implementation of an Anitra API-based application, a command line interface to export device list and device data. This code is only sample code to indicate how to work with the API, the code purposefully does not handle exceptions, does not check for inputs and contains some code duplication. If possible, it is preferrable to use the official API client library available on <a href="[https://github.com/anitra-wildlife-tracking/animal-tracking-data](https://pypi.org/project/animaltrackingdata/)">PyPi</a> using ```pip install animaltrackingdata```.

## Usage

This project was developed and tested in Python 3.11.

Install the required libraries using requirements.txt.

```pip install -r requirements.txt```

To utilize the API, you will need to generate an API key in the Anitra platform. Further instructions are available on <a href="https://support.anitracking.com/index.php?title=DATA_FLOWS#.28OUT.29_Anitra_API_data_.26_metadata_access">the user guide website</a>.

### Commands

#### Export device data
Exports all data you can access from the given device. This code uses the Anitra data scroll API endpoint to ensure data scroll consistency in case any new data is received.

Sample usage:
```python3 anitra-cli.py --clientid=YOUR_CLIENTID --clientkey=YOUR_CLIENT_KEY device-data 9999 --format csv --output 9999.csv```

#### Export device list
Exports the list of devices your user account can access.

Sample usage:
```python3 anitra-cli.py --clientid=YOUR_CLIENTID --clientkey=YOUR_CLIENT_KEY device-data 9999 --format csv --output 9999.csv```
