from configparser import ConfigParser


def db_config(filename="properties.ini", section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]

    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db


# def get_api_key(filename="../resources/properties.ini", section="fbi-api"):
#     # create a parser
#     parser = ConfigParser()
#     # read config file
#     parser.read(filename)
#     apiKey = None
#     if parser.has_section(section):
#         params = parser.items(section)
#         for param in params:
#             if param[0] == "apikey":
#                 apiKey = param[1]
#     else:
#         raise Exception('Section {0} is not found in the {1} file.'.format(section, filename))
#     if apiKey is None:
#         raise Exception("apiKey field not found in properties.ini")
#     return apiKey
