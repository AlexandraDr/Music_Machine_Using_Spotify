# Billboard to Spotify Playlist Automation

A Python integration project that combines web scraping with the Spotify API to automatically create a playlist based on the Billboard Hot 100 for a user-selected historical date.

## Workflow

User selects date
→ Billboard page retrieved
→ Song titles extracted
→ Spotify API search
→ Track URIs collected
→ Private playlist created
→ Available tracks added

## Technologies

- Python
- BeautifulSoup
- Requests
- Spotify Web API
- Spotipy
- OAuth
- HTML parsing
- Environment variables

## What This Project Demonstrates

- Web scraping
- HTML data extraction
- API integration
- OAuth authentication
- Data transformation between systems
- Handling missing API search results
- Automated resource creation
- End-to-end integration workflows

## Error Handling

Not every Billboard track is necessarily available through Spotify search. The application handles missing results by skipping unavailable tracks while continuing the workflow.

## Project Context

Learning and portfolio project demonstrating how information retrieved from one external system can be transformed and passed into another through an authenticated API.
