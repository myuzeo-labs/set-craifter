import os
from google.cloud import aiplatform
from google.oauth2 import service_account

# Authenticate and create a Vertex AI client using environment variable
credentials = service_account.Credentials.from_service_account_info(
    os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
)
aiplatform.init(project="set-crafter", location="us-central1", credentials=credentials)


# Function to create a dataset in Vertex AI
def create_vertex_ai_dataset(dataset_display_name, gcs_source):
    dataset = aiplatform.TabularDataset.create(
        display_name=dataset_display_name,
        gcs_source=aiplatform.types.GcsSource(uris=[gcs_source]),
    )
    return dataset


# Function to train a model using Vertex AI
def train_model(dataset_id, model_display_name, target_column):
    job = aiplatform.CustomJob.from_local_script(
        script_path="train_script.py",
        container_uri="gcr.io/cloud-aiplatform/training/tf-cpu.2-2:latest",
        display_name=model_display_name,
        dataset=dataset_id,
        model_serving_container_image_uri="gcr.io/cloud-aiplatform/prediction/tf2-cpu.2-2:latest",
        requirements=["tensorflow>=2.2", "scikit-learn"],
    )
    model = job.run(sync=True)
    return model
