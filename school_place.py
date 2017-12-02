import requests
import csv
foldername = 'reg_data'
api_key = 'AIzaSyCz4Kk0_XJ6BcfYFPQfpUnsqNPwgajxvds'
data = []
error = []
with open(foldername + '/schools.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            print(row["name"])
            payload = {'input': row["name"], 'types': 'geocode',
                       'language': 'zh_TW', 'key': api_key}
            r = requests.get(
                "https://maps.googleapis.com/maps/api/place/queryautocomplete/json", params=payload)
            res = r.json()
            # 
            if res['status'] == "ZERO_RESULTS":
                payload = {'input': row["name"].replace('高中','中學'), 'types': 'geocode',
                           'language': 'zh_TW', 'key': api_key}
                r = requests.get(
                    "https://maps.googleapis.com/maps/api/place/queryautocomplete/json", params=payload)
                res = r.json()
            pid = res['predictions'][0]['place_id']
            
            payload1 = {'placeid': pid, 'key': api_key, 'language': 'zh_TW'}
            r1 = requests.get(
                "https://maps.googleapis.com/maps/api/place/details/json", params=payload1)
            res1 = r1.json()
            res1 = res1['result']
            temp = [row["name"],res1['name'], res1['formatted_address'],
                    res1['geometry']['location']['lat'], res1['geometry']['location']['lng']]
            data.append(temp)
        except :
            error.append(row["name"])
        
print(error)
with open(foldername + '/school_place.csv', 'w', newline='') as csvfile:
        fieldnames = ['school','name','formatted_address', 'lat', 'lng']
        writer1 = csv.writer(csvfile)
        writer1.writerow(fieldnames)
        for dg in data:
            print(dg)
            writer1.writerow(dg)

        
