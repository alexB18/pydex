if __name__ == "__main__":
    from ascii_magic import AsciiArt
    import pokebase as pb

    # prompt user for pokemon ID number
    pokenumber = int(input('Enter pokemon number:\n'))
    print("loading pokemon data...")

    # load pokemon data into memory
    pokemon = pb.pokemon(pokenumber)
    
    # display sprite and basic info
    sprite = pb.SpriteResource('pokemon', pokenumber)
    displayed_art = AsciiArt.from_url(sprite.url)
    displayed_art.to_terminal()
    ## print basic info
    print("Name: " + pokemon.name)
    print("ID: " + str(pokenumber) + "\n")
    
    ## print flavor text
    #TODO: make it so pydex looks for newest, *English* description in database.
    #       > could be fun to give user the ability to choose preferred language
    print(pb.pokemon_species(pokenumber).flavor_text_entries[15].flavor_text)