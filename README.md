# Data Entry App

This is a simple web application built with **Streamlit** and **SQLAlchemy**, allowing users to insert and view messages from a PostgreSQL database. The project is containerized using Docker, making it easy to run in any environment.

## Docker Setup

### Prerequisites

Before you begin, ensure you have the following installed:

- Docker

### Running the Application

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/cmpbj/data-entry-app.git
   cd data-entry-app
   ```

2. **Build and Start Containers**

   Using Docker Compose, you can easily build and start all necessary services (PostgreSQL, PgAdmin, and the app):

   ```bash
   docker-compose up --build
   ```

   This will:
   - Build the app service
   - Start PostgreSQL database (`postgres`)
   - Start PgAdmin for database management (`pgadmin`)
   - Start the Streamlit app (`app`)

   The app will be available at `http://localhost:8501`, and PgAdmin at `http://localhost:8080`.

3. **Accessing the Application**

   - The Streamlit app should now be running at `http://localhost:8501`.
   - PgAdmin is available at `http://localhost:8080`. The login credentials are:
     - **Email:** `user@domain.com`
     - **Password:** `adminpassword`
   
4. **Database Configuration**

   The PostgreSQL service is set up with the following environment variables:

   - **POSTGRES_USER**: `myuser`
   - **POSTGRES_PASSWORD**: `mypassword`
   - **POSTGRES_DB**: `mydatabase`

   These credentials are used by the application to connect to the database.

### Docker Compose Services

- **postgres**: A PostgreSQL container running on port 5432.
- **pgadmin**: A PgAdmin container for managing the database via a web interface.
- **app**: The Streamlit app, which allows users to input messages into the database.

## Application Overview

The application consists of two main parts:
- **Streamlit**: Provides the user interface where users can insert and view messages.
- **SQLAlchemy**: Handles database interaction with PostgreSQL to store and retrieve messages.

The app allows users to input messages, which are stored in a PostgreSQL database. Users can view the submitted messages in the app.

## Docker Compose File (`docker-compose.yml`)

```yaml
version: '3.12'

services:
  postgres:
    image: postgres
    volumes: 
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: mydatabase
    ports:
      - "5432:5432"
    networks:
      - mynetwork
  
  pgadmin:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: user@domain.com
      PGADMIN_DEFAULT_PASSWORD: adminpassword
    ports:
      - "8080:80"
    depends_on:
      - postgres
    networks:
      - mynetwork
  
  app:
    build: .
    ports:
      - "8501:8501"
    environment:
      DB_NAME: mydatabase
      DB_USER: myuser
      DB_PASS: mypassword
    depends_on:
      - postgres
    networks:
      - mynetwork
    
networks:
  mynetwork:

volumes:
  postgres_data:
```