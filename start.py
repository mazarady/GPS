#classes
import datetime

class directions:
       '''directions for steps'''
       def stuff(self, json_results: 'json') -> None:
              
              for steps in json_results['route']['legs']:
                     
                     print(steps['origNarrative'])
                     
                     for element in steps['maneuvers']:
                            
                            print(element['narrative'])
                            
class where:
       '''finds the lat/long''' #done
       def stuff(self,json_results: 'json') -> None:
              for lat_long in json_results['route']['locations']:
                     
                            if lat_long['latLng']['lat'] < 0:
                                   lng = abs(lat_long['latLng']['lat'])
                                   print(round(lng,2), 'N', end = ' ')
                                   
                            elif lat_long['latLng']['lat'] > 0:
                                   lng = abs(lat_long['latLng']['lat'])
                                   print(round(lng,2), 'S', end = ' ')
                                   
                            if lat_long['latLng']['lng'] < 0:
                                   lat = abs(lat_long['latLng']['lng'])
                                   print(round(lat,2), 'E')
                            
                            elif lat_long['latLng']['lng'] > 0:
                                   lat = abs(lat_long['latLng']['lng'])
                                   print(round(lat,2), 'W')
                                   
class elevation:
       '''elevation'''
       def urlinfo(self, json_results) -> None:
              to_return = ''
              for lat_long in json_results['route']['locations']:                    
                     to_return += str(lat_long['latLng']['lat']) + ','
                     to_return += str(lat_long['latLng']['lng']) + ','
              return to_return[:-1]
       def stuff(self, json_results) ->None:
              for x in json_results['elevationProfile']:                     
                     print(round(abs(x['height'])))
                     
 
class distance:
       '''distance total'''
                                  
       def stuff(self,json_results: 'json') -> None:
              
              '''finds the total distance''' #done
              total = 0
              for steps in json_results['route']['legs']:
                            for distance in steps['maneuvers']:
                                   miles = distance['distance']
                                   total += miles
              print(round(total,2), 'miles')
                            
class dime:
       
       '''time add'''
              
       def stuff(self,json_results: 'json') -> None:
              
              '''finds the time''' #done
              total = 0
                                                    
              for time in json_results['route']['legs']:
                     for formatted_time in time['maneuvers']:
                            int_total = formatted_time['time']
                            int_total = int(int_total)
                            total += int_total
                            format_time = datetime.timedelta(seconds = total)
                            
              print(format_time)


       
