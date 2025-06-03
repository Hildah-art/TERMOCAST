TermoCast CLI 🌤

TermoCast is a lightweight Command Line Interface (CLI) weather application built with Python. It uses SQLAlchemy for managing weather data storage in a local SQLite database and Click for a beautiful and user-friendly CLI.


🚀 Features

 Add weather entries for a city with temperature and description.
 View all stored weather logs.
 Filter weather data by city.
 Update or delete weather records.
 Clean and simple terminal interface.



🛠 Tech Stack

 *Python
 *SQLAlchemy for ORM
 *SQLite as the databse




 📁 Project Structure
.
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── __pycache__
    │   ├── main.cpython-38.pyc
    │   └── models.cpython-38.pyc
    ├── alembic
    │   ├── README
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions
    │       └── 7193ea3509ea_added_data_in_the_tables.py
    ├── alembic.ini
    ├── cli.py
    ├── main.py
    ├── models.py
    ├── seed.py
    └── weather.db

 🧑‍💻 Installation



git clone https://github.com/your-username/termocast-cli.git
cd termocast-cli

2. Create a Virtual Environment (Optional but Recommended)
pipenv shell

3. Install Dependencies

pipenv install


⚙ Usage

Add a new weather entry

python cli.py add --city "Nairobi" --temperature 26 --description "Sunny"

List all entries

python cli.py list

Filter by city

python cli.py filter --city "Nairobi"

Update a record

python cli.py update --id 1 --temperature 28

Delete a record

python cli.py delete --id 1


📌 Notes

All data is stored locally in database.db.

Tables are auto-created on first run.




📝 License

The project is licensed under the Apache License 2.0



Made with ❤ by Hildah Njaga
