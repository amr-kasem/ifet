import os
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.models import *
from app.schema import *
from app.utils import run_migrations



DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

engine = create_engine(DATABASE_URL)
run_migrations(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
app = FastAPI()

# Dependency to get the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

projectRouter = SQLAlchemyCRUDRouter(
    schema=ProjectSchema,
    create_schema=ProjectCreateSchema, 
    db_model=Project,
    db=get_db
)
app.include_router(projectRouter)

staticTestRouter = SQLAlchemyCRUDRouter(
    schema=StaticTestSchema,
    create_schema=StaticTestCreateSchema, 
    db_model=StaticTest,
    db=get_db
)
app.include_router(staticTestRouter)

deflectionRouter = SQLAlchemyCRUDRouter(
    schema=DeflectionSchema,
    create_schema=DeflectionCreateSchema, 
    db_model=Deflection,
    db=get_db
)
app.include_router(deflectionRouter)


infiltrationTestRouter = SQLAlchemyCRUDRouter(
    schema=InfiltrationTestSchema,
    create_schema=InfiltrationTestCreateSchema, 
    db_model=InfiltrationTest,
    db=get_db
)
app.include_router(infiltrationTestRouter)


missileImpactTestRouter = SQLAlchemyCRUDRouter(
    schema=MissileImpactTestSchema,
    create_schema=MissileImpactTestCreateSchema, 
    db_model=MissileImpactTest,
    db=get_db
)
app.include_router(missileImpactTestRouter)


shotRouter = SQLAlchemyCRUDRouter(
    schema=ShotSchema,
    create_schema=ShotCreateSchema, 
    db_model=Shot,
    db=get_db
)
app.include_router(shotRouter)


cyclicTestRouter = SQLAlchemyCRUDRouter(
    schema=CyclicTestSchema,
    create_schema=CyclicTestCreateSchema, 
    db_model=CyclicTest,
    db=get_db
)
app.include_router(cyclicTestRouter)
