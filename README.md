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
    searcher -->|6.Search for play times near user| serper_search_tool
    serper_search_tool -->|7.Return with search results| searcher
    searcher -->|8.Forward results to summarizer| summarizer
    summarizer -->|9.Present user with finished report| real_user


```

## Programmable Chain of Thought

```mermaid
sequenceDiagram
    box AI_Scanner_System
    participant analyst as Input Analyst
    participant consultant as Movie Consultant
    participant searcher as Movie Searcher
    participant summarizer as Summarizer
    end
    box CrewAI Tools
    participant search as Serper Search Tool
    end
    box External APIs
    participant moviedb as Movie Database
    end

    analyst->>consultant: Send Movie Preference Data
    consultant->>moviedb: Make API call to database for relevant movies
    moviedb->>consultant: Return with relevant movies
    consultant->>searcher: Send movies to searcher
    searcher->>search: Search for play times
    search->>searcher: Return with play times
    searcher->>summarizer: Send results to summarizer
```

<!-- ## User cases -->

<!-- ```mermaid
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
``` -->