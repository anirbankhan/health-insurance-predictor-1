from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities,tier_2_cities


# pydantic model to validate incoming data
class UserInput(BaseModel):
    age: Annotated[int, Field(...,gt=0,lt=120,description='Enter the age')]
    height: Annotated[float, Field(...,gt=0,description='Enter the height')]
    weight: Annotated[float, Field(...,gt=0,description='Enter the weight')]
    income_lpa: Annotated[float, Field(...,gt=0,description='Enter the lpa income')]
    smoker: Annotated[bool, Field(...,description='Is a smoker')]
    city: Annotated[str, Field(...,description='Enter the city belongs to')]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(...,description='Occupation of the user')]
    
    @computed_field
    @property
    def bmi(self) -> float:
      return self.weight/(self.height**2)

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.bmi > 30 and self.smoker:
            return "high"
        elif self.bmi > 20 and self.smoker:
            return "medium"
        return "low"
        
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        if self.age < 45:
            return "adult"
        if self.age < 60:
            return "mid_aged"
        return "senior" 

    @field_validator('city')
    @classmethod  
    def normalize_city(cls, v: str) -> str:
        v = v.strip().title()
        return v