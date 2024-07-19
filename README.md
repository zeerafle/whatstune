# Last.fm Weekly Top Track to WhatsApp Story

This project automatically updates your WhatsApp status with your current top track from Last.fm every week. It utilizes
Digital Ocean Functions for scheduling, the Last.fm API for fetching the top track, and a WhatsApp API for updating the status.

## Features

- Fetches the top track of a user from Last.fm for the current week.
- Checks if the current top track is different from the last one saved.
- Updates the WhatsApp status with the current top track details, including the album cover image resized to 770x770
  pixels.
- Utilizes Azure Functions for periodic execution.

## Prerequisites

- Python 3.8 or higher
- [doctl](https://docs.digitalocean.com/reference/doctl/how-to/install/)
- A Last.fm API account
- Access to a [Whapi](https://whapi.cloud)
