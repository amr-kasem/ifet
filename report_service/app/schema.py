from typing import List
from pydantic import BaseModel

class DeflectionCreateSchema(BaseModel):
    deflection_gauge: int
    max_deflection: float
    permanent_deflection: float
    recovery: float

class DeflectionSchema(DeflectionCreateSchema):
    id: int
    class Config:
        orm_mode = True

class StaticTestCreateSchema(BaseModel):
    pressure_factor: float
    pressure: float
class StaticTestSchema(StaticTestCreateSchema):
    id: int
    deflections: List[DeflectionSchema]
    class Config:
        orm_mode = True
        
class InfiltrationTestCreateSchema(BaseModel):
    type: str
    pressure: float
class InfiltrationTestSchema(InfiltrationTestCreateSchema):
    id: int
    duration: float
    leakage: float

    class Config:
        orm_mode = True

class ShotCreateSchema(BaseModel):
    area: float
    velocity: float
    result: bool
    note: str
    
class ShotSchema(ShotCreateSchema):
    id: int

    class Config:
        orm_mode = True

class MissileImpactTestCreateSchema(BaseModel):
    missile: str
    missile_weight: float
    
class MissileImpactTestSchema(MissileImpactTestCreateSchema):
    id: int
    shots: List[ShotSchema]

    class Config:
        orm_mode = True



class CyclicTestCreateSchema(BaseModel):
    type: str
    cycles: int
    low_pressure: float
    high_pressure: float
    
class CyclicTestSchema(CyclicTestCreateSchema):
    id: int
    deflection: float
    permanent_set: float
    result: bool
    note: str

    class Config:
        orm_mode = True

class ProjectCreateSchema(BaseModel):
    name: str
    device_id: int  # New field added

        
class ProjectSchema(ProjectCreateSchema):
    id: int
    static_tests: List[StaticTestSchema]
    infiltration_tests: List[InfiltrationTestSchema]
    missile_impact_tests: List[MissileImpactTestSchema]
    cyclic_tests: List[CyclicTestSchema]

    class Config:
        orm_mode = True
