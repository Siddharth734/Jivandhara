from settings import *
from csv import reader

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
    
def import_folder(*path):
     surf_list = []
     for file_path,_,file_names in walk(join(*path)): 
         for file_name in file_names:
             full_path = join(file_path,file_name)
             image_surf = pygame.image.load(full_path).convert_alpha()
             surf_list.append(image_surf)
     return(surf_list)          