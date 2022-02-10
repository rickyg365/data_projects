
from typing import List
from dataclasses import dataclass, field


@dataclass
class AnimeEntry:
    rank:int
    name:str
    japanese_name:str
    type:str
    episodes:float
    studio:str
    release_season:str
    tags:List[str]
    rating:float
    release_year:int
    end_year:int
    description:str
    content_warning:str
    related_manga:List[str]
    related_anime:List[str]
    voice_actors:List[str]
    staff:List[str]



