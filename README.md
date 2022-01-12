# recipefinder_backend
This project served as backend service to application created at https://github.com/Harshetamahajan/recipefinder.git (Front end)

# Description
This is backend application treated as middleware for recipe finder. This project is based on Python with application hosted on Flask. Its integrated with Postgres as database where recipe data is stored.

# Run the service
Pre-requisites before running the service; 

   * pip install flask, flask_restful, flask_cors
   * pip install psycopg2 (Used to for connection with postgres database)

To run this service, we need to simply run following command; 

   * python app.py

# Working Flow

Once flask application is in running state, user can hit the service with endpoint method
"api/search?query=paneer" where search item such paneer will be queried against database(postgres) and then upon parsing the response, its output will be return to the frontend in the JSON format.

# Database details
For database, we have used postgres where table structure looks as follows ; 
   * id
   * item
   * value (Recipe details are stored here including ingredients details and image)
