if __name__ == "__main__":
    from ascii_magic import AsciiArt
    import pokebase as pb

    pokenumber = int(input('Enter pokemon number:\n'))

    sprite = pb.SpriteResource('pokemon', pokenumber)
    displayed_art = AsciiArt.from_url(sprite.url)
    displayed_art.to_terminal()