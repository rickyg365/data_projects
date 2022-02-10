"""


"""
import sqlite3
from typing import List, Dict
from model import AnimeEntry


class DatabaseHandler:
    def __init__(self, database_name:str="test_database.db"):
        self.name = database_name
        # Connect to database
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

        # Keep Track of tables
        self.tables = []
        self.complete_tables = {}

        self.primary_key = "rank"

    def __str__(self) -> str:
        txt = f"[ {self.name} ]:\n"
        for _, table in enumerate(self.tables):
            txt += f" {_+1}. {table}\n"
        return txt

    # Create Table
    def create_table(self, table_name:str="main", attributes:Dict[str, str]=None):
        self.tables.append(table_name)
        self.complete_tables[table_name] = attributes

        sql_text = ""

        first = True
        for key_name, key_type in attributes.items():
            if first:
                first = False
            else:
                sql_text += ",\n"
            sql_text += f"            {key_name} {key_type}"
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
{sql_text}
        )""")

    def get_all(self, table_name:str) -> List[AnimeEntry]:
        self.cursor.execute(f"select * from {table_name}")
        results = self.cursor.fetchall()
        objects = []
        for result in results:
            objects.append(AnimeEntry(*result))
        return objects

    # Add to Table
    def insert_data_point(self, table_attrs:Dict[str, str], table_name:str):
        values = ""
        val_dict = {}
        
        first = True
        
        for key_name, key_val in table_attrs.items():
            if first:
                first = False
            else:
                values += ", "
            values += f":{key_name}"
            val_dict[key_name] = key_val
        
        with self.conn:
            self.cursor.execute(f"INSERT INTO {table_name} VALUES ({values})",
            val_dict)

        return True

    # Edit Table

    # Delete from Table
    def delete_data_point(self, key, table_name):
        with self.conn:
            self.cursor.execute(f"DELETE from {table_name} WHERE {self.primary_key}=:key", {'key': key})


if __name__ == "__main__":
    db = DatabaseHandler()

    anime_entry_attrs = {
        "rank": "integer",
        "name": "text",
        "japanese_name": "text",
        "type": "text",
        "episodes": "integer",
        "studio": "text",
        "release_season": "text",
        "tags": "text",
        "rating": "integer",
        "release_year": "integer",
        "end_year": "integer",
        "description": "text",
        "content_warning": "text",
        "related_manga": "text",
        "related_anime": "text",
        "voice_actors": "text",
        "staff": "text"
    }

    db.create_table("animes", anime_entry_attrs)

    anime_entry = {
        "rank": 0,
        "name": "text",
        "japanese_name": "text",
        "type": "text",
        "episodes": 1,
        "studio": "text",
        "release_season": "text",
        "tags": "text",
        "rating": 5,
        "release_year": 2020,
        "end_year": 2021,
        "description": "text",
        "content_warning": "text",
        "related_manga": "text",
        "related_anime": "text",
        "voice_actors": "text",
        "staff": "text"
    }
    db.insert_data_point(anime_entry, "animes")

    print(db.get_all("animes"))
    print("")
    print(db)



