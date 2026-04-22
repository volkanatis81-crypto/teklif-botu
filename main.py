# Update main.py to initialize database on startup

def main():
    # Existing main function code...

    # Initialize database
    create_tables()  # Call to create_tables() on startup

if __name__ == '__main__':
    main()