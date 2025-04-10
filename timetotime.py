from datetime import datetime

date_time_str = input("Enter time in 'HH:MM:SS' format: ")

date_time_obj = datetime.strptime(date_time_str, '%H:%M:%S')


print ("The type of the date is now",  type(date_time_obj))
print ("The date is", date_time_obj)
