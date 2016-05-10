import urllib.parse
import urllib.request
import json
import UI
import start


def build_search_url(list_of_places: list) -> None:
       '''Builds url'''
       query_parameters = [
              ('key', UI.MAP),('from', list_of_places[0])
              ]
       
       for address in list_of_places[1:]:

              query_parameters.append(('to', str(address)))

       
       return UI.BASE_URL + '?' + urllib.parse.urlencode(query_parameters)



def get_url(final_url: str) -> 'json':
       '''get url and decodes it'''
       res = None
       try:
              res = urllib.request.urlopen(final_url)
              json_text = res.read().decode(encoding = 'utf-8')
              
              return json.loads(json_text)
       finally:
              if res != None:
                     res.close()


def build_elevation_url(json_results) -> None:

       string_lat_long = '' 

       lat_long = start.elevation()
       string_lat_long += str(lat_long.urlinfo(json_results))
       
       return UI.ELEVATION_URL + '?key=' + UI.MAP + '&shapeFormat=raw&unit=f&latLngCollection=' + string_lat_long

       
def get_elevation_url(elevation_url: str) -> 'json':
       response = None
       json_elev_text = None
       try:
              response = urllib.request.urlopen(elevation_url)
              json_elev_text = response.read().decode(encoding = 'utf-8')
              if json_elev_text:
                     return json.loads(json_elev_text)


       finally:
              if response != None:
                     response.close()
              else:
                     print('Waria')


       
