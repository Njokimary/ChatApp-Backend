import pandas as pd
from flask_seeder import Seeder
from app import create_app, db, Message  
from datetime import datetime

class MessageSeeder(Seeder):
    def run(self):
        # Read data from the CSV file using pandas
        data = pd.read_csv('/home/njoki/Downloads/GeneralistRails_Project_MessageData.csv')

        # Iterate over the rows and insert data into the database
        for index, row in data.iterrows():
            timestamp = datetime.strptime(row['Timestamp (UTC)'], '%Y-%m-%d %H:%M:%S')
            message = Message(
                user_id=row['User ID'],
                timestamp=timestamp,
                body=row['Message Body']
            )
            db.session.add(message)

       
        db.session.commit()

# Create application context
app = create_app()

# Run the seeder within the application context
with app.app_context():
   
    db.create_all()

    MessageSeeder().run()
