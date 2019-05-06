
temperatures =[]
my_date = []

class Temperature():
    def __init__(self):
        self.year = raw_input("Enter the year: ")
        self.month = raw_input("Enter the month: ")
        self.day = raw_input("Enter the day: ")

    def getDate(self):
        year = raw_input("Enter the year: ")
        month = raw_input("Enter the month: ")
        day = raw_input("Enter the day: ")
        my_date.append(year)
        my_date.append(month) 
        my_date.append(day)
        return my_date
        

    def getTemperatures(self):
        for temp in range(3):
            temp = float(input("Enter the temperatures: "))
            temperatures.append(temp)
            result=input("Type C for convert to Celsius and F for Fahrenheit:")
            if result == 'C':
                convert_to_fahren= (9*temp+32*5)/5
                print convert_to_fahren
            elif result == 'F':
                convert_to_celcius = (5 * temp - 32 * 5) / 9
                print convert_to_celcius

    def min_max_average(self):
        choice_list=[1,2,3]
        for user_input in range(3):
            user_input=int(input("enter your choice: "))
            if(user_input==choice_list[0]):
                return max(temperatures)
            elif(user_input==choice_list[1]):
                return min(temperatures)
            elif(user_input==choice_list[2]):
                average = (temperatures[0]+ temperatures[1]+temperatures[2])/3
                return ("Average is %d degree temperature for the day" %average)
                

    
        
if __name__ == "__main__":
    t = Temperature()
    print t.getDate()
    t.getTemperatures()
    print t.min_max_average()




