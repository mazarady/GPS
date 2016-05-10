#MAAZ MUNIR 22602418
# Project 3
# Consumer Key: bJF0CU3Of6wtGXigb7BAtNjW9I6wQiTp
# Consumer Secret: dANFz9EHdnBzmCnT
import start
import url

MAP = 'bJF0CU3Of6wtGXigb7BAtNjW9I6wQiTp'

BASE_URL = 'http://open.mapquestapi.com/directions/v2/route'

ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile'

def user_input() -> list:
       '''user input'''
       
       while True:

              location_number = int(input('Enter Number Of Locations: '))
              # The number of locations you're visiting, including the one
              # you're traveling from
              list_of_places = []
              
              count = 0
             
              for count in range(int(location_number)):
                     locations = input('Location: ')
                     # The Location, can input city, address
                     if count == 0:
                            list_of_places.append((locations))
                            count +=1
                     else:
                            list_of_places.append((locations))
                            count +=1
 
              location_types = int(input('Enter Number of Location Types: '))
              #Type of Locations, so for instance, DIRECTIONS, STEPS, TOTALDISTANCE
              # TOTALTIME, ELEVATION

              list_of_types = []

              for x in range(location_types):
                     types = input("Location Type: STEPS, TOTALTIME, TOTALDISTANCE, ELEVATION, LATLONG:  ")
                     #Enter the location type: DIRECTIONS, STEPS, TOTALDISTANCE, TOTALTIME, ELEVATION
                     list_of_types.append(types)
                     
              return list_of_places, list_of_types
       
              break
       

if __name__ == '__main__':
       '''main'''
       list1,list2 =user_input()
       result = url.get_url(url.build_search_url(list1))
       
       elevation_url = url.build_elevation_url(result)
       elevationjson = url.get_elevation_url(elevation_url)
       
       

       for entered in list2:
                     
              if entered == 'STEPS':
                     print()
                     print('DIRECTIONS')
                     steps = start.directions()
                     steps = steps.stuff(result)
                     print()
        
              elif entered == 'TOTALTIME':
                     print()
                     print('TOTAL TIME')
                     time = start.dime()
                     time = time.stuff(result)
                     print()
                     
              elif entered == 'TOTALDISTANCE':
                     print()
                     print('TOTAL DISTANCE')
                     distance = start.distance()
                     distance = distance.stuff(result)
                     print()

              elif entered == 'LATLONG':
                     print()
                     print('LATLONGS')
                     lat_longs = start.where()
                     lat_longs = lat_longs.stuff(result)
                     print()
                     
              elif entered == 'ELEVATION':
                     print()
                     print('ELEVATIONS')
                     elevation = start.elevation()
                     elevation = elevation.stuff(elevationjson)
                     print()
                     
                     



                     


