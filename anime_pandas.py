import pandas as pd

# my_anime_list = {{'Title': '7 seeds'}: [{'Status': 'currently watching'}, {'Genres': ['adventure', 'drama', 'mystery', 'romance', 'sci-fi']}], 
# {'Title': 'Bakemonogatari'}: [{'Status': 'currently watching'}, {'Genres': ['mystery', 'romance', 'supernatural']}], {'Title': 'Banana Fish'}: [{'Status': 'currently watching'}, {'Genres': ['action', 'adventure', 'drama']}],
# {'Title': 'Black Clover'}: [{'Status': 'currently watching'}, {'Genres': ['action', 'comedy', 'fantasy']}], {'Title': 'Bleach'}: [{'Status': 'currently watching'}, {'Genres': ['action', 'adventure', 'fantasy']}],
# {'Title': 'Cannon Busters'}: [{'Status': 'on hold'}, {'Genres': ['action', 'adventure', 'fantasy', 'sci-fi']}], {'Title': 'Fairy Tail'}: [{'Status': 'on hold'}, {'Genres': ['action', 'adventure', 'fantasy']}],
# {'Title': 'High School DxD'}: [{'Status': 'on hold'}, {'Genres': ['comedy', 'romance', 'ecchi']}], {'Title':'Mnemosyne'}: [{'Status': 'on hold'}, {'Genres': ['action', 'girls love', 'horror', 'sci-fi', 'supernatural']}],
# {'Title': 'Nana'}: [{'Status': 'on hold'}, {'Genres': ['drama', 'romance', 'slice of life']}], {'Title': 'Abenobashi Mahou Shoutengai'}: [{'Status': 'plan to watch'}, {'Genres': ['comedy', 'fantasy', 'ecchi']}],
# {'Title': 'Adachi to Shimamura'}: [{'Status':'plan to watch'}, {'Genres': ['girls love', 'romance', 'slice of life']}], {'Title': 'Air Gear'}: [{'Status': 'plan to watch'}, {'Genres': ['action', 'comedy', 'sports', 'ecchi']}],
# {'Title': 'Akibas Trip'}: [{'Status': 'plan to watch'}, {'Genres': ['action', 'comedy', 'supernatural', 'ecchi']}], {'Title': 'Aldnoah.Zero'}: [{'Status': 'plan to watch'}, {'Genres': ['action', 'sci-fi']}]}

anime = ['7 seeds', 'Bakemonogatari', 'Banana Fish', 'Black Clover', 'Bleach', 
'Cannon Busters', 'Fairy Tail', 'High School DxD', 'Mnemosyne', 'Nana', 'Abenobashi Mahou Shoutengai',
'Adachi to Shimamura', 'Air Gear', 'Aldnoah.Zero', 'Akibas Trip']

choices = pd.Series(anime, dtype='category')

print(choices)