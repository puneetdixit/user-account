
import settings
from src.database_manager import Database
import src.models

database = Database()

if settings.DROP_TABLES:
    print("Going to Drop tables...")
    database.db.drop_tables((src.models.Users,))
    print("Tables dropped successfully")
print("Going to migrate database")
database.db.create_tables((src.models.Users,))
print("Database migrated successfully")