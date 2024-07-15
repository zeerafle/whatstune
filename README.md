# Last.fm Weekly Top Track to WhatsApp Status

This project automatically updates your WhatsApp status with your current top track from Last.fm every week. It utilizes
Azure Functions for scheduling, the Last.fm API for fetching the top track, and a WhatsApp API for updating the status.

## Features

- Fetches the top track of a user from Last.fm for the current week.
- Checks if the current top track is different from the last one saved.
- Updates the WhatsApp status with the current top track details, including the album cover image resized to 770x770
  pixels.
- Utilizes Azure Functions for periodic execution.

## Prerequisites

- Python 3.8 or higher
- Azure Functions Core
  Tools ([guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Cnon-http-trigger%2Ccontainer-apps&pivots=programming-language-python))
- A Last.fm API account
- Access to a [Whapi](https://whapi.cloud)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/zeerafle/whatstune.git
   ```
2. Navigate to the project directory:
   ```
   cd whatstune
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
4. Activate the virtual environment:
   ```
   .venv\Scripts\activate
   ```

## Configuration

1. Initialize the Azure Function:
   ```
   func init
   ``` 
2. Fill in your Last.fm API key and secret, and your Whapi URL and token in the `local.settings.json` file inside Values key.

## Run locally

1. Run the Azure Function locally:
   ```
   func start
   ```
2. Make a POST request to `http://localhost:7071/admin/functions/StoryUpdate` to trigger the function manually. 

## Deployment

1. Deploy the Azure Function:
   ```
   func azure functionapp publish <YourFunctionAppName>
   ```
2. Ensure your function app is running and the timer trigger is set correctly in `function_app.py`.

## Usage

The Azure Function will automatically trigger every week, fetching your top track from Last.fm and updating your WhatsApp status if the track has changed.
