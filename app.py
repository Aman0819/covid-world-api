from flask import Flask
from flask_restful import Resource, Api
from api import dataProcessor


app = Flask(__name__)
api = Api(app)

class Global_data(Resource):
    
    def get(self):
    
       self.datum=dataProcessor().globalwise()
       return self.datum

class Country_data(Resource):
    
    def get(self,country):
        self.country=country
        self.datum=dataProcessor().countrywise()
        try:
            for i in self.datum:
                if i['Country/other']== self.country:
                    self.countr_y=i
                    break
            return self.countr_y
        except:
            return "Make sure to enter proper input and its method"

class Continent_data(Resource):
    
    def get(self,continent):
        self.continent=continent
        self.datum=dataProcessor().continentwise()
        try:
            for i in self.datum:
                if i['Country/other']== self.continent:
                    self.cont_y=i
                    break
            return self.cont_y
        except:
            return "Make sure to enter proper input and its method"

#endpoints of the api
api.add_resource(Global_data, '/')
api.add_resource(Country_data,'/country=<string:country>')
api.add_resource(Continent_data,'/continent=<string:continent>')

if __name__ == '__main__':
   app.run(debug=True)
