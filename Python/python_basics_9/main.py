class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, hours):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.hours = hours

    def describe_restaurant(self):
        print('Moja restauracja nazywa się ' + self.restaurant_name.title())
        print('Moja restauracja zajmuje się kuchnią: ' + str(self.cuisine_type.title()))


    def open_restaurant(self):
        print('restauracja jest otwarta o godzinie: ' + self.hours)


my_restaurant = Restaurant('grecka', 'regionalna', '')
open_hour = Restaurant('', '', '12:00')
yours_restaurant = Restaurant('slaska', 'wojewodzka', '')
open_hour_yours = Restaurant('', '', '14:00')
his_restaurant = Restaurant('podkarpacka', 'inna', '')
open_hour_his = Restaurant('', '', '16:00')

print(my_restaurant.restaurant_name.title())
print(my_restaurant.cuisine_type.title())
print(open_hour.hours)
print(yours_restaurant.restaurant_name.title())
print(yours_restaurant.cuisine_type.title())
print(open_hour_yours.hours)
print(his_restaurant.restaurant_name.title())
print(his_restaurant.cuisine_type.title())
print(open_hour_his.hours)

