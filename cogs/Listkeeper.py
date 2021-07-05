# Cog to keep track of lists made by users

# import discord
# from discord.ext import commands
import asyncio
import os
import json

from typing import Union, Dict, List


# ## CLASS DEFS ##
# class ColxItem():

#     def __init__(self, parent_collection: List, label:str, note:str="") -> None:
#         self.label: str = label
#         self.note: str = note
#         self.parent_collection: List[self] = parent_collection


#     def __repr__(self) -> str:
#         return f"(Item) {self.label}"


#     def set_label(self, label:str) -> None:
#         self.label = label
#         Collection.update_selected(self.parent_collection)


#     def set_note(self, note:str) -> None:
#         self.note = note
#         Collection.update_selected(self.parent_collection)

#     def printout(self) -> str:
#         return f"{self.label}: {self.note}"



# class Collection():

#     master: List[ColxItem] = []
#     selected_list: Union[List[ColxItem], None] = None

#     def __init__(self, name, desc) -> None:
#         self.name: str = name
#         self.desc: str = desc
#         self.contents: List[ColxItem] = []

#         Collection.master.append(self)
#         Collection.selected_list = self


#     def __repr__(self) -> str:
#         return f"(Collection Object) {self.name}: {self.desc}"


#     @classmethod
#     def update_selected(self, collection: Union[List[ColxItem], None]) -> None:
#         self.selected_list = collection


#     def delete_self(self) -> None:
#         print(f'Removing {self.name} from Listkeeper!')
#         Collection.master.remove(self)
#         if Collection.selected_list == self:
#             Collection.update_selected(None)
#         save_to_file()


#     def add_item(self, label:str, note:str="") -> None: #
#         for item in self.contents:
#             if item.label == label:
#                 print("ERROR: Label already in use!")
#                 return

#         item: ColxItem = ColxItem(self, label, note) # self here is ColxItem(parent_collection) parameter
#         self.contents.append(item)
#         Collection.update_selected(self)
#         save_to_file()


#     def delete_item(self, label:str) -> None:
#         for item in self.contents:
#             if item.label == label:
#                 print("removing", item.label)
#                 self.contents.remove(item)

#         Collection.update_selected(self)



# ## HELPER FUNCTIONS ##
# def read_from_file() -> str: # I think this will return the file contents as str, maybe not
#     pass


# def save_to_file() -> None:
#     pass


# ## MAIN COG ##
# class ListKeeper(commands.cog):

#     save_dir_initialized: Dict[int, bool] = 

#     def __init__(self, bot) -> None:
#         self.bot = bot


#     def dir_init(self, ctx) -> None:
#         # check for directory exists
#         # if os.path.isdir(str(ctx.message.guild.id)):
#         #   ctx.channel.send('All set up!')
#         # else:
#         #   ctx.channel.send('Setting up folder!')
#         #   make folder
#         pass


#     @commands.command()
#     def list(self, ctx, colx_name=None) -> None:
#         # if not colx_name: return [self.name for name in List.master]
#         # else: 1)Find where List.master.name == colx_name and return that obj; 2)Return that obj info
#         pass