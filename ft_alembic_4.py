import alchemy

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")

    print("Testing create_air:", alchemy.create_air())
    try:
        print("Testing the hidden create_earth:", alchemy.create_earth())
    except AttributeError as e:
        print(e)
