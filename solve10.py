class WeatherAdviceSystem:
    def __init__(self):
        self.preferences = {
            'temperature': None,
            'precipitation': None
        }

    def set_preference(self, category, value):
        if category in self.preferences:
            self.preferences[category] = value
        else:
            print(f"Invalid preference category: {category}")

    def get_advice(self):
        if self.preferences['temperature'] is None or self.preferences['precipitation'] is None:
            print("Please set both temperature and precipitation preferences.")
            return

        temperature = self.preferences['temperature']
        precipitation = self.preferences['precipitation']

        
        if temperature > 30:
            if precipitation == 'rain':
                return 'It\'s hot and raining. Bring an umbrella!'
            else:
                return 'It\'s hot and dry. Stay hydrated!'
        elif 20 <= temperature <= 30:
            if precipitation == 'rain':
                return 'It\'s moderate and raining. Don\'t forget your umbrella!'
            else:
                return 'The weather is pleasant. Enjoy your day!'
        else:
            if precipitation == 'snow':
                return 'It\'s cold and snowy. Bundle up!'
            else:
                return 'It\'s cold and dry. Dress warmly!'

if __name__ == "__main__":
    weather_system = WeatherAdviceSystem()

   
    weather_system.set_preference('temperature', 25)
    weather_system.set_preference('precipitation', 'rain')

    
    advice = weather_system.get_advice()
    print("Weather Advice:", advice)
