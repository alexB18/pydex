if __name__ == "__main__":
    from ascii_magic import AsciiArt

    my_art = AsciiArt.from_image('images/moon.jpg')
    my_art.to_terminal()