import settings

def width_pct(percentage):
    return (settings.WIDTH/100) * percentage

def height_pct(percentage):
    return (settings.HEIGHT/100) * percentage

#tkinter button size is not pixel so it is dose not use

# def cell_width(percentage):
#     return int(width_pct(percentage)/ settings.GRID_SIZE)

# def cell_height(percentage):
#     return int(height_pct(percentage) / settings.GRID_SIZE)