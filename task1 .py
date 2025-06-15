#API of DOGS
import json
import requests
import matplotlib.pyplot as plt
breed=input("enter a dog breed:").lower()
api_url=f"https://dog.ceo/api/breed/{breed}/images/random"
get_server_information=requests.get(api_url)
data=get_server_information.json()
print("Random Image of", breed, ":", data['message'])

#data visualization
plt.style.use('classic')
breeds_name= ["pug", "husky", "labrador"]
breeds_count=[5,7,3]


plt.bar(breeds_name,breeds_count)
plt.xlabel("breed")
plt.ylabel("count")
plt.title("Dogs breed")
plt.show()
