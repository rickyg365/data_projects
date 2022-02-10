
from model import AnimeEntry
from handler import DatabaseHandler

def main():
    file_name = "frontend_database"
    db = DatabaseHandler(file_name)
    
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

    # Handle data Insert 
    """ key_name:data_type key_value """
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
    print(db)

if __name__ == "__main__":
    main()

