# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again."
# }


# programming_dictionary["Loop"] = "The action of doing something over and over again."



# empty_dictionary = {}

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }

# #Nesting Dictionary in Dictionary

# travel_log = {
#     "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits":12}
# }
# print(travel_log["France"]["cities_visited"][2])


# #Nesting Dictionary in List

# travel_log = [
#     {"country": "France", 
#      "cities_visited": ["Paris", "Lille", "Dijon"],
#      "total_visits": 12
#     },
#     {"country": "Germany",
#      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
#      "total_visits": 5
#     }
# ]

# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# # Do NOT change the code above 👆

# # TODO: Write the function that will allow new countries
# # to be added to the travel_log. 

# def add_new_country(user_country, user_visits, user_list):
#   new_country = {}
#   new_country["country"] =  user_country
#   new_country["visits"] = user_visits
#   new_country["cities"] = user_list
#   travel_log.append(new_country)

# # Do not change the code below 👇
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")



