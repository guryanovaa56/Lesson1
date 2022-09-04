city_dict = {"city": "Москва", "temperature": "20"}
print(city_dict["city"])
city_dict["temperature"] = int(city_dict["temperature"])-5
print(city_dict)
print(city_dict.get("country", "Россия"))
city_dict["date"] = "27.05.2019"
print(len(city_dict))