# Python-PostGreSQL

A Python project demonstrating database connectivity and operations using PostgreSQL.

## Overview

This repository contains Python scripts and examples for connecting to and interacting with PostgreSQL databases. It's designed to help developers learn how to establish connections, execute queries, and manage database operations using Python.

## Prerequisites

Before you get started, ensure you have the following installed:

- **Python 3.x** - [Download here](https://www.python.org/downloads/)
- **PostgreSQL** - [Download here](https://www.postgresql.org/download/)
- **psycopg2** - Python adapter for PostgreSQL

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/riteshp1584/Python-PostGreSQL.git
cd Python-PostGreSQL
```

### 2. Install Dependencies

Install the required Python package using pip:

```bash
pip install psycopg2-binary
```

Alternatively, if you prefer the compiled version:

```bash
pip install psycopg2
```

### 3. Configure Database Connection

Before running the scripts, you need to configure your PostgreSQL connection details:

- **Database Name:** postgres (default)
- **User:** postgres (default)
- **Password:** Your PostgreSQL password
- **Host:** localhost (default)
- **Port:** 5432 (default)

Update the connection parameters in the script files to match your PostgreSQL setup.

## Project Structure

```
Python-PostGreSQL/
├── 25012025_P1.py         # Python script demonstrating PostgreSQL connection
└── README.md              # This file
```

## Usage

### Basic Connection Example

The `25012025_P1.py` script demonstrates how to establish a connection to PostgreSQL:

```python
import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="your_password_here",
    host="localhost",
    port="5432"
)

print("Connected to PostgreSQL")
conn.close()
```

### Running the Script

```bash
python 25012025_P1.py
```

## Features

- Simple PostgreSQL connection setup
- Connection verification and error handling examples
- Ready-to-use templates for database operations

## Security Note

⚠️ **Important:** Never commit passwords directly to your code. Use environment variables or configuration files instead:

```python
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)
```

Create a `.env` file (add to `.gitignore`):

```
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=5432
```

## Resources

- [psycopg2 Documentation](https://www.psycopg.org/documentation/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Python Database API Specification](https://www.python.org/dev/peps/pep-0249/)

## Troubleshooting

### Connection Refused Error

- Ensure PostgreSQL server is running
- Verify host and port settings
- Check that the database credentials are correct

### Module Not Found Error

```bash
pip install psycopg2-binary
```

### Permission Denied

- Verify your PostgreSQL user permissions
- Ensure the user has access to the specified database

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests with improvements or new examples.

## License

This project is open source and available under the MIT License.

## Contact

For questions or suggestions, please reach out to [riteshp1584](https://github.com/riteshp1584).

---

**Happy coding!** 🎉
