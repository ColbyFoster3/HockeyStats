from dotenv import load_dotenv
import os
# seed.py
from app.models.team import Team
from app.core.database import Base, engine, SessionLocal

load_dotenv()

if os.environ.get("ENV") == "development":
    print("Seeding database...")
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()

    # Deleting Existing Data
    session.query(Team).delete()
    session.commit()

    # Seed data
    session.add_all([
        Team(id=1, name="Test", city="Test", abbreviation="TCT"),
    ])

    session.commit()
    session.close()
    print("Seeding complete.")
else:
    print("Seeding is only allowed in development environment.")