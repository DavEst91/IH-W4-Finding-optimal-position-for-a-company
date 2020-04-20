# IH-W4-Finding optimal position for a company

A Gaming company has been recenty created. As data engineers, we have been tasked with finding the optimal location for our new company. We have been asking all the employees about their preferences and those are the requisites we found.

- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
- 30% of the company have at least 1 child, so childcare centers nearby will be appreciated.
- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Executives like Starbucks A LOT. Ensure there's a starbucks not to far.
- Account managers need to travel a lot
- All people in the company have between 25 and 40 years, give them some place to go to party.
- Nobody in the company likes to have companies with more than 10 years in a radius of 2 KM.
- The CEO is Vegan.

For our porpuse, we have been provided with [Crunchbase Data](https://data.crunchbase.com/docs), a database with information about companies from the US, its activitys and its offices.

Locations of the airports have been found using [Amadeus API](https://developers.amadeus.com/) and its Python implemented library [amadeus](https://github.com/amadeus4dev/amadeus-python).

Social requeriments have been checked using [Foursquare places API](https://developer.foursquare.com/docs/places-api/).

Maps have been represented in jupyter notebooks using [folium library](https://python-visualization.github.io/folium/).

Other requeriment we have made ourselves is:

-New office must be located in the US (which is the origin of the company) and in the East Coast (to facility connections to Europe).

Instructions:

-You must copy the file companies.json from [Crunchbase Data](https://data.crunchbase.com/docs) on an input folder located in parent directory.

-You must get API access to from Foursquare and Amadeus and save them in the .env file as: AMADEUS_APIKEY, AMADEUS_APISECRET, FOURSQUARE_CLIENTID and FOURSQUARE_CLIENTSECRET.

-Sometimes a map from folium takes up to 30 second to be loaded. Please, be patient.
