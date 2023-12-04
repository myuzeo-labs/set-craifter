# SetCraifter 

## Introduction

SetCrafter AI is a tentative project designed to revolutionize the way DJs organize and curate their music libraries. By employing AI-driven categorization and leveraging Spotify's API, SetCrafter AI aims to automate the sorting of large and unorganized DJ libraries into cohesive sets.

## Features

- **Automated Categorization:** Sorts tracks based on where they fit within an hour-long set using seven different categories with 10-minute increments.
- **AI-Driven Classification:** Utilizes nearest-neighbor classification techniques to sort tracks with reasonable accuracy.
- **Integration with Spotify's API:** Enriches metadata with additional data such as energy, acoustics, and danceability.
- **Set Curation:** If successful, a second AI will be developed to curate sets based on unique time categories, BPM, key, and other factors.

## Getting Started

### Prerequisites

- Python (version 3.x or higher)
- Spotify Developer Account (for API access)

### Installation

1. Clone the repository:
2. Navigate to the project directory and install the required packages:
3. Configure the Spotify API credentials in the configuration file.

### Usage

Run the main script to start categorizing and curating your DJ library:
## Contribution

We welcome contributions to SetCrafter AI. Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute.

## Alternative Solutions

- Deep learning models could be explored instead of nearest-neighbor techniques for more sophisticated classification.
- Collaborations with music experts for labeling the training data might increase accuracy.

## License

SetCrafter AI is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Contact

For any inquiries or feedback, please reach out to [username@email.com](mailto:username@email.com).

## Acknowledgments

Special thanks to the music community for inspiring this innovative approach to DJ library organization.



=======
# Set Crafter Tool

Set Crafter is a tool designed to assist DJs in crafting their music sets with the help of AI-driven recommendations and data analysis.

## Features

- Spotify integration for downloading and analyzing track data
- Data preprocessing for AI model consumption
- AI models for track categorization and set curation
- Streamlit-based user interface for easy interaction

## Modules

### Data Preprocessing Module
- `DJLibraryDataExtractor`: Extracts data from a DJ's music library
- `DataPreprocessor`: Processes the data for AI model consumption
- `SpotifyDataDownloader`: Downloads track data from Spotify

### AI Models Module
- `TrackCategorizer`: Categorizes tracks based on their features
- `SetCurator`: Curates music sets based on the categorized tracks
- `ModelTrainingDataBuilder`: Prepares datasets for training AI models

### Main Application Module
- `SetCrafterApp`: Coordinates modules and provides the user interface

## Libraries
- spotipy
- pandas
- scikit-learn
- flask
- streamlit

## Backend Development
- Endpoints for Spotify authentication and track downloading

## Frontend Development
- Implemented using Streamlit for a user-friendly interface

## Security and Error Handling
- OAuth 2.0 implementation for secure Spotify authentication
- Robust error handling and logging mechanisms

## Testing and Deployment
- Comprehensive testing of backend and frontend components
- Deployment strategies for the Flask and Streamlit applications

## Getting Started

Instructions on how to set up and run Set Crafter will be provided here.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

