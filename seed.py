# seed.py
import pandas as pd
from app import create_app, db, Message
from datetime import datetime

class MessageSeeder:
    def run(self):
        app = create_app()

        with app.app_context():
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

if __name__ == "__main__":
    MessageSeeder().run()
