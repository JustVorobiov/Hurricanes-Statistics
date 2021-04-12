# names of hurricanes
from collections import defaultdict

names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']
# scale by damage in M$
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
# Scale by death rate
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# write your update damages function here:
conversion = {"M": 1000000,
              "B": 1000000000}


def updated_damages(list_of_damages: list, conv_rate: dict) -> list:
    """Function that convert string of damages to float and returns updated list"""
    updated_list_of_damages = []
    for damage in list_of_damages:
        if damage == "Damages not recorded":
            updated_list_of_damages.append(damage)
        elif damage[-1] == "M":
            new_value = float(damage[:-1]) * conv_rate["M"]
            updated_list_of_damages.append(new_value)
        else:
            new_value = float(damage[:-1]) * conv_rate["B"]
            updated_list_of_damages.append(new_value)
    return updated_list_of_damages


update_damages = updated_damages(damages, conversion)


# write your construct hurricane dictionary function here:
def construct_hurricane_dictionary(name: list, month: list, year: list, max_sustained_wind: list, area_affected: list,
                                   damage: list, death: list) -> dict:
    """Function which creates a new dictionary of hurricanes with key: valued pairs"""
    hurricanes = {}
    for x in range(34):
        hurricanes.update({
            name[x]: {
                "Name": name[x],
                "Month": month[x],
                "Year": year[x],
                "Max Sustained Wind": max_sustained_wind[x],
                "Areas Affected": area_affected[x],
                "Damage": damage[x],
                "Deaths": death[x]
            }
        })
    return hurricanes


hur_dict = construct_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, update_damages,
                                          deaths)


# write your construct hurricane by year dictionary function here:
def yearly_hurricanes_dict(dict_of_hurricanes: dict, year: int) -> dict:
    """Function that takes dictionary and year, and creates new dictionary where key is a year,
    value - all information about hurricane"""
    hurricane_by_year_dictionary = {}
    list_of_hurricane_info = []
    for information in dict_of_hurricanes.values():
        if information["Year"] == year:
            list_of_hurricane_info.append(information)
            hurricane_by_year_dictionary.update({
                information["Year"]:
                    list_of_hurricane_info
            })

    return hurricane_by_year_dictionary


hurricane_by_year = yearly_hurricanes_dict(hur_dict, 1932)
print(hurricane_by_year)


# write your find most affected area function here:
def areas_affected_count(dict_of_hurricanes: dict) -> dict:
    """Function that takes dictionary and return new dictionary of damaged area and number of hurricanes there"""
    d = defaultdict(int)
    for information in dict_of_hurricanes:
        for area in dict_of_hurricanes.get(information, {}).get('Areas Affected'):
            d[area] += 1
    return dict(d.items())


areas_damaged = areas_affected_count(hur_dict)
print(areas_damaged)


def most_affected_area(affected_areas_dict: dict) -> str:
    """Function which takes dictionary of affected areas and return string with name and number of times of the most
    affected region """
    max_area = ""
    counter = 0
    for area in affected_areas_dict.items():
        if area[1] > counter:
            max_area = area[0]
            counter = area[1]
    return max_area + " " + str(counter)


most_affected_region = most_affected_area(areas_damaged)
print(most_affected_region)


# write your greatest number of deaths function here:
def most_deaths(hurricane_dictionary: dict) -> str:
    """Function which takes a hurricane dictionary and returns new string with the most deaths in 'Hurricane_name
    death_number' format """
    max_area = ""
    counter = 0
    for hurricane in hurricane_dictionary.values():
        if hurricane.get("Deaths") > counter:
            max_area = hurricane.get("Name")
            counter = hurricane.get("Deaths")
    return max_area + " " + str(counter)


most_deaths_by_hurricane = most_deaths(hur_dict)
print(most_deaths_by_hurricane)


# write your categorize by mortality function here:

def categorize_by_death_hurricanes(hurricane_dictionary: dict, scale: dict) -> dict:
    """Function create a new dictionary with 5 categories of hurricane power and push all hurricane as list to its own
    category depends on its death rate lvl"""
    dictionary_of_categorized_hurricanes = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    for hurricane in hurricane_dictionary.values():
        if hurricane.get("Deaths") < scale[0]:
            dictionary_of_categorized_hurricanes[0].append(hurricane)
        elif hurricane.get("Deaths") < scale[1]:
            dictionary_of_categorized_hurricanes[1].append(hurricane)
        elif hurricane.get("Deaths") < scale[2]:
            dictionary_of_categorized_hurricanes[2].append(hurricane)
        elif hurricane.get("Deaths") < scale[3]:
            dictionary_of_categorized_hurricanes[3].append(hurricane)
        elif hurricane.get("Deaths") < scale[4]:
            dictionary_of_categorized_hurricanes[4].append(hurricane)
        else:
            dictionary_of_categorized_hurricanes[5].append(hurricane)

    return dictionary_of_categorized_hurricanes


print(categorize_by_death_hurricanes(hur_dict, mortality_scale))


# write your greatest damage function here:
def biggest_damage(hurricane_dictionary: dict) -> str:
    max_damage = 0
    name = ""
    for hurricane in hurricane_dictionary.values():
        if isinstance(hurricane.get("Damage"), float):
            if float(hurricane.get("Damage")) > max_damage:
                max_damage = hurricane.get("Damage")
                name = hurricane.get("Name")
    return name + " $" + str(max_damage)


biggest_damage_hurricane = biggest_damage(hur_dict)
print(biggest_damage_hurricane)


# write your catgeorize by damage function here:

def categorize_by_damage_hurricanes(hurricane_dictionary: dict, scale: dict) -> dict:
    """Function which categorized hurricanes by damage from 0 to 5, where key0 is 'Not Recorded damage' or damage < 10kk
    and other key is growing damage"""
    dictionary_of_categorized_by_damage_hurricanes = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in hurricane_dictionary.values():
        if isinstance(hurricane.get("Damage"), float):
            if hurricane.get("Damage") < scale[0]:
                dictionary_of_categorized_by_damage_hurricanes[0].append(hurricane)
            elif hurricane.get("Damage") < scale[1]:
                dictionary_of_categorized_by_damage_hurricanes[1].append(hurricane)
            elif hurricane.get("Damage") < scale[2]:
                dictionary_of_categorized_by_damage_hurricanes[2].append(hurricane)
            elif hurricane.get("Damage") < scale[3]:
                dictionary_of_categorized_by_damage_hurricanes[3].append(hurricane)
            elif hurricane.get("Damage") < scale[4]:
                dictionary_of_categorized_by_damage_hurricanes[4].append(hurricane)
            else:
                dictionary_of_categorized_by_damage_hurricanes[5].append(hurricane)
        else:
            dictionary_of_categorized_by_damage_hurricanes[0].append(hurricane)
    return dictionary_of_categorized_by_damage_hurricanes


print(categorize_by_damage_hurricanes(hur_dict, damage_scale))
