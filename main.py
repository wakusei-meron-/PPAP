import urllib2, sys
import json
import BingImageClient
import GCSImageClient

from json import JSONEncoder
class MyEncoder(JSONEncoder):
  def default(self, o):
    return o.__dict__

def main():
  bingImgs = BingImageClient.find('hoge')
  GCSImgs = GCSImageClient.find('hoge')
  imgs = bingImgs + GCSImgs

  print(MyEncoder().encode(imgs))
  # term = sys.argv[1]
  # location = sys.argv[2]
  # params = search_params(term, location)
  # response = get_restaurants(params)
  # restaurants_info = response["businesses"]
  # restaurant_names = []
  # for restaurant_info in restaurants_info:
  #   restaurant_name = restaurant_info["name"]
  #   print restaurant_name
  #
if __name__ == "__main__":
  main()
