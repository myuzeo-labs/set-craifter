import os
from google.cloud import aiplatform
from google.oauth2 import service_account

# Path to the service account key file
service_account_key_path = 'set-crafter-sa-key.json'

# Authenticate and create a Vertex AI client
credentials = service_account.Credentials.from_service_account_file(
    service_account_key_path
)
aiplatform.init(project='set-crafter', location='us-central1', credentials=credentials)

# Function to create a dataset in Vertex AI
def create_vertex_ai_dataset(dataset_display_name, gcs_source):
    dataset = aiplatform.TabularDataset.create(
        display_name=dataset_display_name,
        gcs_source=aiplatform.types.GcsSource(uris=['gs://set_crafter_bucket/features.csv'])
    )
    return dataset

# Function to train a model using Vertex AI
def train_model_on_vertex_ai(dataset, model_display_name, target_column):
    training_pipeline = aiplatform.AutoMLTabularTrainingJob(
        display_name=model_display_name,
        optimization_prediction_type='classification',
        
    )
    model = training_pipeline.run(
        dataset=dataset,
        model_display_name=model_display_name,
        target_column=target_column
    )
    return model

# Function to deploy a model for prediction in Vertex AI
def deploy_model_on_vertex_ai(model, deployed_model_display_name):
    endpoint = model.deploy(
        deployed_model_display_name=deployed_model_display_name
    )
    return endpoint

# Train a model using the created Vertex AI dataset
# Retrieve the created Vertex AI dataset
dataset = aiplatform.TabularDataset('projects/189973823689/locations/us-central1/datasets/1458666001477402624')

# Train a model using the created Vertex AI dataset
model = train_model_on_vertex_ai(dataset, 'set_crafter_model', 'target_column_name')
print(f'Model training started: {model.display_name}')
