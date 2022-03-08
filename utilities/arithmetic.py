from math import ceil

def title_start(title, width):
    return int((width // 2) - (len(title) // 2) - len(title) % 2) #I forgot how I came to this equation, but it perfectly centers the title. 