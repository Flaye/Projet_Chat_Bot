from wit import Wit
from data_import import *
import os

def extractEntity(nlp, entityOrIntent):
    if entityOrIntent == "intents":
        if (len(nlp['intents']) != 0):
            if (nlp['intents'][0]['confidence'] >= 0.8):
                return nlp['intents'][0]
    else:
        if (nlp['entities'][entityOrIntent][0]['confidence'] >= 0.8):
            return nlp['entities'][entityOrIntent][0]['value']
    return None


def NLP(msg):
    client = Wit(os.getenv('WIT_TOKEN'))
    nlp = client.message(msg)
    intent = extractEntity(nlp, 'intents')

    if intent:
        if intent['name'] == "find_by_type": #Looking for french food
            typefood = extractEntity(nlp, 'TypeFood:TypeFood')
            all_placeId = chefmozcuisine.index[chefmozcuisine['Rcuisine'].str.lower() == typefood.lower()]
            if(len(all_placeId) != 0):
                print(all_placeId)
                list_restaurant = geoplaces2.loc[geoplaces2.index.isin(all_placeId)] #Get all rows where id is in list of id :all_placeId
                if(len(list_restaurant)!=0):
                    list_five = list_restaurant.sample(n = 3)
                    dict_place = []
                    for index, row in list_five.iterrows():
                        val = {'txt':"Name : {}\nAddress : {}\nCity : {}\nPrice : ".format(row["name"],row["address"],row["city"],row["price"]), "link":"https://www.google.com/maps/place/{},{}".format(row["latitude"],row["longitude"])}
                        dict_place.append(val)
                    return dict_place
            return [{'txt': "Sorry, no restaurant found !", "link":None}]

        elif intent['name'] == "get_info": #Info for the restaurant <name of restaurant>
            restaurant = extractEntity(nlp, 'restaurant:restaurant')
            city = None
            try: #Maybe in a specific city
                city = extractEntity(nlp, 'Localisation:City')
                print(city)
            except:
                print("No specific city in the request")
        elif intent['name'] == "find_by_city": #Give the 5 best restaurant in the city
            city = extractEntity(nlp, "Localisation:City")
            typefood = None
            try: #Give the best for a specific type of food
                typefood = extractEntity(nlp, 'TypeFood:TypeFood')
            except:
                print("No specific type of food")

        # return {txt:messageWithBDD, link:google.com/maps/place}
        return [{'txt': "Wait for the data", 'link': "https://www.google.com/maps/place/22.14958,-100.999557"}]
    else:
        return [{'txt': "Could you ask again ?", 'link': None}]
    # rep = client.message(msg)
    # return rep