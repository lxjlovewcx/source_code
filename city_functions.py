def city_function(City,Country,population = ""):
    if population:
        city_country = City + ", " + Country + " - population " + population
    else:
        city_country = City + ", " + Country
    return city_country

