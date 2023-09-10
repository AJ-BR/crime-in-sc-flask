# crime-in-sc-flask
Flask application providing a REST API endpoint for city/town/county crime data in South Carolina

A working build can be found on `https://sc-crime-api.onrender.com/`

Prerequisites:
  * Python 3.10.*
  * Flask 2.2.3
  * Pip 22.3.*
  
1) Go to the `crime-sc-flask/` directory
2) To install the dependencies, type `pip install -e .`. This will install required dependencies
3) Run `flask run`
4) The server can be accessed at `127.0.0.1:5000`
5) Append `/fbi/?location={location}&year={year}&crime={crime}` to the end of the URL. 

For example, to see how many robberies occurred in Myrtle Beach in 2021, the url would be constructed as below:

`http://127.0.0.1:5000/fbi/?location=myrtle-beach&year=2021&crime=robbery`

Or 

`https://sc-crime-api.onrender.com/fbi/?location=myrtle-beach&year=2021&crime=robbery`

The total list of locations (including counties) are:
    "sullivans-island",
    "williamston",
    "ridgeville",
    "cottageville",
    "rock-hill",
    "west-union",
    "fort-mill",
    "cherokee",
    "johnsonville",
    "greenville",
    "charleston",
    "new-ellenton",
    "calhoun-falls",
    "fairfield",
    "nichols",
    "clarendon",
    "liberty",
    "summerton",
    "gifford",
    "st.-stephen",
    "chapin",
    "kingstree",
    "st.-george",
    "bamberg",
    "west-pelzer",
    "saluda",
    "bennettsville",
    "honea-path",
    "pickens",
    "lincolnville",
    "quinby",
    "union",
    "summerville",
    "port-royal",
    "gaffney",
    "due-west",
    "mccormick",
    "williston",
    "laurens",
    "bath",
    "timmonsville",
    "surfside-beach",
    "loris",
    "abbeville",
    "jonesville",
    "bluffton",
    "hardeeville",
    "dorchester",
    "darlington",
    "walterboro",
    "oconee",
    "holly-hill",
    "goose-creek",
    "dillon",
    "williamsburg",
    "denmark",
    "springfield",
    "inman",
    "bonneau",
    "pacolet",
    "manning",
    "mcbee",
    "lancaster",
    "latta",
    "tega-cay",
    "jasper",
    "travelers-rest",
    "tigerville",
    "greenwood",
    "westminster",
    "estill",
    "aiken",
    "ninety-six",
    "trenton",
    "richland",
    "society-hill",
    "jamestown",
    "aynor",
    "hemingway",
    "moncks-corner",
    "santee",
    "harleyville",
    "hanahan",
    "scranton",
    "bethune",
    "north-charleston",
    "edisto-beach",
    "bowman",
    "columbia",
    "beaufort",
    "clover",
    "belton",
    "seneca",
    "pageland",
    "woodruff",
    "hartsville",
    "pawleys-island",
    "varnville",
    "cheraw",
    "blacksburg",
    "north-myrtle-beach",
    "jackson",
    "sumter",
    "kershaw",
    "barnwell",
    "greeleyville",
    "olanta",
    "campobello",
    "camden",
    "salem",
    "lee",
    "fairfax",
    "yemassee",
    "horry",
    "olar",
    "ridge-spring",
    "pelion",
    "turbeville",
    "norway",
    "prosperity",
    "colleton",
    "branchville",
    "orangeburg",
    "gaston",
    "florence",
    "pamplico",
    "eutawville",
    "marion",
    "great-falls",
    "st.-matthews",
    "duncan",
    "allendale",
    "greer",
    "marlboro",
    "walhalla",
    "conway",
    "blythewood",
    "elloree",
    "easley",
    "irmo",
    "isle-of-palms",
    "lake-city",
    "clemson",
    "ware-shoals",
    "folly-beach",
    "johnston",
    "lake-view",
    "york",
    "coward",
    "wellford",
    "spartanburg",
    "anderson",
    "mccoll",
    "andrews",
    "winnsboro",
    "berkeley",
    "batesburg-leesville",
    "whitmire",
    "cayce",
    "blackville",
    "central",
    "springdale",
    "ridgeland",
    "clio",
    "west-columbia",
    "lexington",
    "landrum",
    "north-augusta",
    "mount-pleasant",
    "newberry",
    "clinton",
    "calhoun",
    "chesterfield",
    "perry",
    "fort-lawn",
    "cowpens",
    "chesnee",
    "hampton",
    "simpsonville",
    "lane",
    "edgefield",
    "bishopville",
    "cameron",
    "pendleton",
    "wagener",
    "chester",
    "fountain-inn",
    "ehrhardt",
    "north",
    "georgetown",
    "elgin",
    "myrtle-beach",
    "lamar",
    "mauldin",
    "mullins",
    "salley",
    "lyman",
    "swansea"
    
The years are:
    1990,
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
    "all", 
    "aggravated-assault", 
    "all-other-offenses-(except-traffic)", 
    "arson", 
    "burglary", 
    "curfew-and-loitering-law-violations", 
    "disorderly-conduct", 
    "driving-under-the-influence", 
    "drug-abuse-violations---grand-total", 
    "drunkenness", 
    "embezzlement", 
    "forgery-and-counterfeiting", 
    "fraud", 
    "gambling---total", 
    "human-trafficking---commercial-sex-acts", 
    "human-trafficking---involuntary-servitude", 
    "larceny---theft", 
    "liquor-laws", 
    "manslaughter-by-negligence", 
    "motor-vehicle-theft", 
    "murder-and-nonnegligent-manslaughter", 
    "offenses-against-the-family-and-children", 
    "prostitution-and-commercialized-vice", 
    "rape", 
    "robbery", 
    "sex-offenses-(except-rape--and-prostitution-and-commercialized-vice)", 
    "simple-assault", 
    "stolen-property:-buying--receiving--possessing",
    "suspicion", 
    "vagrancy", 
    "vandalism", 
    "weapons:-carrying--possessing--etc."
