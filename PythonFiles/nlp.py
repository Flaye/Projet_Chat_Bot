from wit import Wit
from data_import import *
import os

def extractEntity(nlp, entityOrIntent):
    print(entityOrIntent,"\n", nlp)
    if entityOrIntent == "intents":
        if (len(nlp['intents']) != 0):
            if (nlp['intents'][0]['confidence'] >= 0.8):
                return nlp['intents'][0]
    else:
        if ((entityOrIntent in nlp['entities']) and nlp['entities'][entityOrIntent][0]['confidence'] >= 0.8):
            for i in range(len(nlp['entities'][entityOrIntent])):
                if nlp['entities'][entityOrIntent][i]['value'] != "Where" and nlp['entities'][entityOrIntent][i]['value'] != "in":
                    return nlp['entities'][entityOrIntent][i]['value']
    return None


def NLP(msg):
    client = Wit(os.getenv('WIT_TOKEN'))
    nlp = client.message(msg)
    intent = extractEntity(nlp, 'intents')

    if intent:
        if intent['name'] == "find_by_type": #Looking for french food
            try:
                typefood = extractEntity(nlp, 'TypeFood:TypeFood')
                all_placeId = chefmozcuisine.loc[chefmozcuisine['Rcuisine'].str.lower().str.contains(typefood.lower())]
                if(len(all_placeId) != 0):
                    list_restaurant = geoplaces2.loc[geoplaces2["placeID"].isin(all_placeId["placeID"])] #Get all rows where id is in list of id :all_placeId
                    print(list_restaurant)
                    if(len(list_restaurant)!=0):
                        n = 5 if len(list_restaurant) >= 5 else len(list_restaurant)
                        list_five = list_restaurant.sample(n)
                        dict_place = []
                        for index, row in list_five.iterrows():
                            val = {'txt':":fork_knife_plate: Name : {}\nAddress : {}\nCity : {}\nPrice : ".format(row["name"],row["address"],row["city"],row["price"]), "link":"https://www.google.com/maps/place/{},{}".format(row["latitude"],row["longitude"])}
                            dict_place.append(val)
                        return dict_place
                return [{'txt': "Sorry, no restaurant found !", "link":None}]
            except:
                print("Erreur ligne 39")
                return [{'txt': ":pensive: Sorry, something went wrong !", "link": None}]
        elif intent['name'] == "get_info": #Info for the restaurant <name of restaurant>
            try:
                restaurant = extractEntity(nlp, 'restaurant:restaurant')
            except:
                print("Erreur ligne 45")
                return [{'txt': ":pensive: Sorry, something went wrong !", "link": None}]

            city = None
            try: #Maybe in a specific city
                city = extractEntity(nlp, 'Localisation:City')
                print(city)
            except:
                print("No specific city in the request, ligne 53")

            copy_geoplaces2 = geoplaces2.copy()
            copy_geoplaces2["name"] = copy_geoplaces2["name"].str.lower()
            rest_info = copy_geoplaces2.loc[copy_geoplaces2["name"].str.contains(restaurant.lower())]
            if(city != None):
                rest_info = rest_info.loc[rest_info["city"].str.lower() == city.lower()]
            if(len(rest_info) != 0):
                dict_place = []
                for index, row in rest_info.iterrows():
                    val = {'txt': ":fork_knife_plate: Name : {}\nAddress : {}\nCity : {}\nPrice : ".format(row["name"], row["address"],
                                                                                        row["city"], row["price"]),
                           "link": "https://www.google.com/maps/place/{},{}".format(row["latitude"],
                                                                                    row["longitude"])}
                    dict_place.append(val)
                return dict_place
            return [{'txt': ":pensive: Sorry, no restaurant found !", "link":None}]

        elif intent['name'] == "find_by_city": #Give the 5 best restaurant in the city
            city = extractEntity(nlp, "Localisation:City")
            print(city)
            list_restaurant = geoplaces2.loc[geoplaces2['city'].str.lower() == city.lower()]

            typefood = None
            try:  # Give the best for a specific type of food
                typefood = extractEntity(nlp, 'TypeFood:TypeFood')
            except:
                print("No specific type of food")
            print(typefood)
            try:
                if(typefood != None):
                    all_placeId = chefmozcuisine.index[chefmozcuisine['Rcuisine'].str.lower() == typefood.lower()]
                    list_restaurant = list_restaurant.index[list_restaurant.index.isin(all_placeId)]

                if (len(list_restaurant) != 0):
                    list_five = list_restaurant.sample(n=5)
                    dict_place = []
                    for index, row in list_five.iterrows():
                        val = {'txt': ":fork_knife_plate: Name : {}\nAddress : {}\nCity : {}\nPrice : ".format(row["name"], row["address"],
                                                                                            row["city"], row["price"]),
                               "link": "https://www.google.com/maps/place/{},{}".format(row["latitude"],
                                                                                        row["longitude"])}
                        dict_place.append(val)
                    return dict_place
                return [{'txt': ":pensive: Sorry, no restaurant found !", "link": None}]
            except:
                return [{'txt': ":pensive: Sorry, something went wrong !", "link": None}]
        return [{'txt': ":face_with_monocle: Could you ask again ?", 'link': None}]
    else:
        return [{'txt': ":face_with_monocle: Could you ask again ?", 'link': None}]