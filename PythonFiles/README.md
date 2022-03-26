# Find Your Restaurant - DIA4

## Members
- Tom PAYET 1
- Anthony PACINI 2
- Elie OBADIA 3

## Description
The idea is to find a restaurant depending on what you want to eat, the type of food and the place. We can also ask for details of a specific restaurant.
## Bot Info
- Chatbot platform: Discord
- [Join discord server](https://discord.gg/eqTCAPsDmV)
- [Working video of this bot](https://youtu.be/xqNw6YzTu8k)
- [Github](https://github.com/Flaye/Projet_Chat_Bot)
### Used Dataset
We used an existing dataset
[link](https://data.world/uci/restaurant-consumer-data/workspace)

## Language Processing

Video from the trained texts on wit.ai. [Video](https://youtu.be/t5w2BEErJyc)



### Intents and Entities

| Intent       | Entities                                                  |
|--------------|-----------------------------------------------------------|
|  get_info    | localisation, city, typefood, restaurant, restaurant_name |
| find_by_city | localisation, city, typefood                              |
| find_by_type | localisation, city, typefood                              |

## Scenarios

### scenario 1:
| User    | Bot                                                             |
|---------|-----------------------------------------------------------------|
| Hi      | Hi ! Welcome to the chatBot of Where could I eat ?              |
| Hello   | You are looking for a restaurant ?                              |
| Chatbot | Just ask : Tell me more about <The name of the restaurant>      |
|         | You know what you would like to eat, but you don't know where ? |
|         | Just ask : I would like to eat <The type of food> (for example: French food !)|
### scenario 2:
| User                        | Bot                          |
|-----------------------------|------------------------------|
| Where can I eat Mexican ?   | Restaurant 1                 |
|                             | Restaurant 2                 |
|                             | ...                          |
|                             | Restaurant 5                 |
| I would like to eat chinese | Restaurant 1                 |
|                             | Restaurant 2                 |
|                             | ...                          |
|                             | Restaurant 5                 |
| I would like to eat a Hot dogs | Sorry, no restaurant found ! |




### scenario 3:

| User                     | Bot                           |
|--------------------------|-------------------------------|                      
| Where is the restaurant Restaurante 75 ? | Restaurante 75 caracteristics |
| Where is the restaurant El Herradero Restaurante and Bar ? | El Herradero Restaurante and Bar caracteristics|
| What could you tell me about Restaurante la Gran Via | Restaurante la Gran Via caracteristics|





