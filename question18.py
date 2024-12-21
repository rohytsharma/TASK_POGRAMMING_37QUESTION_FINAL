""""
Accept any city from the user and display monument of that city.
City Monument
Delhi Red Fort
Agra Taj Mahal
Jaipur Jal Mahal"""
city_data = input("Enter the name of a city: ").lower()

monuments_data = {
    "delhi": "Red Fort",
    "agra": "Taj Mahal",
    "jaipur": "Jal Mahal"
}
if city_data in monuments_data:
    print(f"The monument in {city_data.capitalize()} is {monuments_data[city_data]}.")
else:
    print("Sorry, no information available for that city.")