import pathway as pw

# Define schema matching your Travel.csv columns
class TravelSchema(pw.Schema):
    CustomerID: int
    ProdTaken: int
    Age: int
    TypeofContact: str
    CityTier: int
    DurationOfPitch: int
    Occupation: str
    Gender: str
    NumberOfPersonVisiting: int
    NumberOfFollowups: int
    ProductPitched: str
    PreferredPropertyStar: int
    MaritalStatus: str
    NumberOfTrips: int
    Passport: int
    PitchSatisfactionScore: int
    OwnCar: int
    NumberOfChildrenVisiting: int
    Designation: str
    MonthlyIncome: int

# Read data from CSV file
data = pw.io.csv.read('./input/', schema=TravelSchema)

# Write output with a filename
pw.io.csv.write(data, './output/result.csv')

# Run the pipeline
pw.run()