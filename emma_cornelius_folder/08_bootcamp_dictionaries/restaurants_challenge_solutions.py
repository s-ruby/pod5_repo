print("Challenge: Favourite Restaurants")

print()

print("Question 1")

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp. 

Go through the dictionary and print out the following 3 pieces of information about the restaurant: 
1. The latitude and longitude of Four Barrel Coffee 
2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code. 
3. The website of Four Barrel Coffee
'''


restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}


# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
# TODO: Write code to print the URL of the website of Four Barrel Coffee.

print(f'Latitude of Four Barrel Coffee: {restaurant["latitude"]}\nLongitude of Four Barrel Coffee: {restaurant["longitude"]}')

print(f'The complete address of Four Barrel Coffee is {restaurant["address1"]}, {restaurant["city"]}, {restaurant["state"]} {restaurant["country"]} {restaurant["zip_code"]}')

print(f'Website of Four Barrel Coffee: {restaurant["url"]}')


print()




print("Question 2")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)

# TODO: Print each dictionary

# The dictionary for each restaurant should look something like this

'''
restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich" }
'''

restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich"
    }

restaurant_2 = {
    "name": "Pisticci",
    "address" : "125 La Salle St, New York, NY 10027",
    "favourite_dish" : "Ravioli"
    }


restaurant_3  = {
    "name": "Awadh",
    "address" : "2588 Broadway, New York, NY 10025",
    "favourite_dish" : "Paneer Tikka Masala"}


print(restaurant_1)
print(restaurant_2)
print(restaurant_3)




print("Question 3")
'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there. 
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants

restaurant_1.pop('favourite_dish')

# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant

print(restaurant_1)

print("Question 4")
'''
Imagine that another one of your most favourite restaurants modified its address. 
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant 

restaurant_3['address'] = '101 Amsterdam Avenue, New York, NY, 10029'

# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary

print(restaurant_3['address'])

# TODO: Print the updated dictionary.

print(restaurant_3)
