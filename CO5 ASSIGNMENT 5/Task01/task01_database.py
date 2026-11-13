import sqlite3
con=sqlite3.connect("air_quality.db")
con.executescript("""
CREATE TABLE IF NOT EXISTS stations(station_id INTEGER PRIMARY KEY, station_name TEXT UNIQUE NOT NULL);
CREATE TABLE IF NOT EXISTS readings(reading_id INTEGER PRIMARY KEY, station_id INTEGER NOT NULL,
 reading_date TEXT NOT NULL, hour INTEGER NOT NULL, pm25 REAL, pm10 REAL, no_value REAL,
 temperature_c REAL, UNIQUE(station_id,reading_date,hour),
 FOREIGN KEY(station_id) REFERENCES stations(station_id));
CREATE INDEX IF NOT EXISTS idx_station_date ON readings(station_id,reading_date);
""")
con.commit()
print("Station and readings tables created.")
con.close()
