# CrewAI Powered Movie Recommender

## Project Overview
This project uses CrewAI to create ai agents with the task of making movie recommendations.\
It uses OpenAI's gpt 4o mini as the generative AI.\
It additionally uses SerperAPI for google searches, and a movie database API.\
The crew works as such:
- The analyst takes in the user's input and from that determines the type of movie that the user enjoys
- Then this analysis is given to the consultant, who uses the movie db api to search for movies of that genre
- Then the movies that the consultant comes up with are given to the searcher, who searches for which movies are being played near the user
- Finally the summarizer takes everything and returns it to the user.

## Workflow

```mermaid
graph TD
    real_user([Real User])
    movie_recommendation_system[Movie Recommendation System]
    movie_db[Movie Database]
    serper_search_tool[Serper Search Tool]

    subgraph AI_Recommender_Crew["AI Recommender Crew"]
        direction TB
        analyst[AI Input Analyst]
        consultant[AI Movie Consultant]
        searcher[AI Movie Searcher]
        summarizer[AI Summarizer]
    end

    real_user -->|1.Natural Language Input| analyst
    analyst -->|2.Forward movie details| consultant
    consultant -->|3.Make API call| movie_db
    movie_db -->|4.Return relevant movies| consultant
    consultant -->|5.Send movies to searcher| searcher
    searcher -->|6.Search for movies near user| serper_search_tool
    serper_search_tool -->|7.Return with search results| searcher
    searcher -->|8.Forward results to summarizer| summarizer
    summarizer -->|9.Present user with finished report| real_user


```

## Programmable Chain of Thought

```mermaid
sequenceDiagram
    box AI_Scanner_System
    participant scanner as AI Receipt Scanner
    participant merchant_finder as AI Merchant Finder
    participant decider as AI Policy Decider
    end
    box CrewAI Tools
    participant vision as Vision Tool
    participant search as Google Search Tool
    end

    scanner->>vision: Send receipt image
    vision->>scanner: Extract receipt details (merchant, time, amount)

    scanner->>merchant_finder: Request merchant identification
    merchant_finder->>search: Query merchant information
    search->>merchant_finder: Provide merchant details (category, location)
    merchant_finder->>decider: Forward merchant profile (category, location) and Rceipt Details
```

## User cases

```mermaid
sequenceDiagram
    participant real_user as Real User
    participant ai_scanner_system as AI Scanner System
    participant expense_claim_system as Expense Claim System

    real_user->>ai_scanner_system: Send receipt image
    alt Processed
        ai_scanner_system->>expense_claim_system: Process expense claim
        expense_claim_system->>ai_scanner_system: Confirm claim submission
        ai_scanner_system->>real_user: Notify claim approval
    else Rejected
        ai_scanner_system->>real_user: Communicate rejection rationale
    else Additional Information Required
        ai_scanner_system->>real_user: Request supplementary receipt details
        real_user->>ai_scanner_system: Provide additional receipt information
        ai_scanner_system->>expense_claim_system: Process expense claim
        expense_claim_system->>ai_scanner_system: Confirm claim submission
        ai_scanner_system->>real_user: Notify claim approval
    end
```