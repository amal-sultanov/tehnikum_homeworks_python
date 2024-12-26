from typing import List, Dict, Optional

from pydantic import BaseModel


class Player(BaseModel):
    player_name: str
    player_deposit: int
    player_items: List[Dict[str, int]]
    player_friends: List[str] = []
    player_souvenir: Optional[str]


# player1 = Player(player_name="Bob", player_deposit=1000,
#                  player_items=[{'shvabra': 1}], player_souvenir=None)
# print(vars(player1))


# class Bank(BaseModel):
#     name: str
#     money_amount: int
#     currency: str
#
#
# bank_client = {'name': 'Bob', 'money_amount': 10000, 'currency': 'sum'}
# client = Bank(**bank_client)
# print(vars(client))
#
#
# class User(BaseModel):
#     name: str
#     followers: int
#     posts: int
#
#
# class Comment(BaseModel):
#     user: User
#     comment: str
#     likes: int = 0


class User(BaseModel):
    username: str
    mail: str
    language: str


class Artist(BaseModel):
    artist_name: str
    artist_followers: List[User]


class Song(BaseModel):
    artist: Artist
    song_name: str
    date_of_publishing: str


class Playlist(BaseModel):
    user: User
    songs: List[Song]
    likes: int = 0
