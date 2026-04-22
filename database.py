import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        # Create ilanlar table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ilanlar (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            date_posted DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')

        # Create takip_listesi table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS takip_listesi (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            ilan_id INTEGER NOT NULL,
            FOREIGN KEY (ilan_id) REFERENCES ilanlar (id)
        )''')

        # Create teklif_gecmisi table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS teklif_gecmisi (
            id INTEGER PRIMARY KEY,
            ilan_id INTEGER NOT NULL,
            offer_amount REAL NOT NULL,
            date_offered DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (ilan_id) REFERENCES ilanlar (id)
        )''')

        # Create fiyat_degisim table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS fiyat_degisim (
            id INTEGER PRIMARY KEY,
            ilan_id INTEGER NOT NULL,
            old_price REAL NOT NULL,
            new_price REAL NOT NULL,
            change_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (ilan_id) REFERENCES ilanlar (id)
        )''')

        self.connection.commit()

    def close(self):
        self.connection.close()

# Usage:
# db = Database('your_database.db')
# db.create_tables()