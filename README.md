# crime-in-sc-flask
Flask application providing a REST API endpoint for county crime data in South Carolina

### A working build of this project is hosted on AWS Lightsail
https://crime-api.5njplgatf1uts.us-east-1.cs.amazonlightsail.com/sled/?county={county}&year={year}&crime={crime}
Refer to step 5) to see how to correctly form the URL. For example if you wanted to get the number of larceny crimes that occured in Aiken county in 2021, the URL would be https://crime-api.5njplgatf1uts.us-east-1.cs.amazonlightsail.com/sled/?county=aiken&year=2021&crime=larceny


## Build Instructions:

NOTE: This project depends on a database that already contains the crime data. Without that database, this project will not build.

Prerequisites:
  * Python 3.10.*
  * Flask 2.2.3
  * Pip 22.2.*
  * Pipenv 2023.2.*
  
1) In the `crime-sc-flask/` directory, run `pipenv shell`
2) Go to the `main/`directory
3) Run `flask run`
4) The server can be accessed at `localhost:5000`
5) Append `/sled/?county={county}&year={year}&crime={crime}` to the end of the URL. 

The counties are:
    abbeville,
    aiken,
    allendale,
    anderson,
    bamberg,
    barnwell,
    beaufort,
    berkeley,
    calhoun,
    charleston,
    cherokee,
    chester,
    chesterfield,
    clarendon,
    colleton,
    darlington,
    dillon,
    dorchester,
    edgefield,
    fairfield,
    florence,
    georgetown,
    greenville,
    greenwood,
    hampton,
    horry,
    jasper,
    kershaw,
    lancaster,
    laurens,
    lee,
    lexington,
    marion,
    marlboro,
    mcCormick,
    newberry,
    oconee,
    orangeburg,
    pickens,
    richland,
    saluda,
    spartanburg,
    sumter,
    union,
    williamsburg,
    york
    
The years are:
  1991,
    1992,
    1993,
    1994,
    1995,
    1996,
    1997,
    1998,
    1999,
    2000,
    2002,
    2003,
    2004,
    2005,
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
    2020,
    2021
    
The crimes are:
   "kidnapping"
    "shoplifting"
    "vandalism"
    "theft-from-vehicle"
    "gta"
    "theft-from-building"
    "sexual-exposure"
    "statutory-rape"
    "murder"
    "larceny"
    "animal-cruelty"
    "simple-assault"
    "rape"
    "forgery"
    "weapons-violations"
    "stolen-property"
    "pick-pocketing"
    "burglary"
    "arson"
    "prostitution"
    "forcible-sodomy"
    "aggravated-assault"
    "robbery"
    "drug-violations"
   
