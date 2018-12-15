from math import sqrt

def findDistance(lon1, lat1, lon2, lat2):
    """
    find distance for one offer
    """
    res = round(sqrt((lat1-lat2)**2 +(lon1-lon2)**2) * 10000)/100
    return res

def searchDistance(res, latitude, longitude):
    """
    sort by distance
    add length, lat of user, long of user in json
    """
    for i in range(len(res)):
        r = findDistance(longitude, latitude, res[i]['longitude'], res[i]['latitude'])
        res[i]['length'] = r
        res[i]['lat'] = latitude
        res[i]['long'] = longitude
        # print("distance = {}, my({},{}) your({},{}) " .format(r, longitude, latitude, res[i]['longitude'],  res[i]['latitude']))
    res.sort(key=lambda row: row['length'])  # sort by priority
    # print("New sorted")
    # for i in res:
    #     print("distance = {}, my({},{}) your({},{}) place {} length {} ".format(r, longitude, latitude, i['longitude'],
    #                                                          i['latitude'],i['place_id'], i['length']))

    return res
