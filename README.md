# Onwello Assignemnt Project
## Project set-up
### Setting up credentials
In order to run and test the script you need to have service account with appropriate
permissions set in GCP, those permissions are:
- BigQuery Data Editor. 
- BigQuery Job User. 
- Storage Object Admin.

You need to also have correct google credentials file in order to use service account
for script to interact with GCP services.

After that place your file with credentials to path of your choice.

Next thing is to add `GOOGLE_APPLICATION_CREDENTIALS` as your environment variable.
You can do it by executing this command:

`export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service_account/credentials.json`


### Setting up venv and libraries
If you will face any problems in running `create_env.sh` script you need to add appropriate permissions like that:
`chmod +x create_venv.sh`

Then simply run it like that: `./create_venv.sh` 
and lastly active created environment using this command: `source path/to/venv/bin/activate`

## Setting up constants
Remember that you need to define values for couple of constants in order to run this project
Those are : 
* `bucket_name = "YOUR_BUCKET_ID"` <- here replace this value with your GCS bucket_id (csv files will be loaded there) 
* `dataset_name = 'YOUR_DATASET_ID'` <- here replace this value with your BigQuery dataset_id (tables will be loaded there) 

## Running the script
In order to run main.py script simply execute following command:

`python main.py`

## Using views in your project
In `sql/` folder you can find 3 queries (which normally were saved as views in my BigQuery project).

You can use this views to run them and to see results based on created tables.

Remember to replace `PROJECT_ID` and `DATASET_ID` with your own project and dataset before executing them.
