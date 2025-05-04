---
config:
  layout: fixed
---
flowchart LR
 subgraph FE["<u>Front End</u>"]
        A["Donor"]
        B["Recipient/Volunteer"]
        R["React + React-Leaflet"]
        M["OSM Integration"]
  end
 subgraph BE["<u>Backend</u>"]
        AL["Authentication Layer"]
        F["Flask API"]
        ML["Donor Matching Logic <br> <i> ML Model Integration</i>"]
        DB[("PostgreSQL DB")]
  end
 subgraph AWS["<u><b><i>System Architecture</i></b></u>"]
    direction TB
        FE
        BE
        BI["BI Tool<br>Data Analytics"]
  end
    R -- Data/Map Tiles --> M
    A -- Requests --> AL
    B -- Requests --> AL
    AL -- Auth Pass --> F
    F -- CRUD Ops --> DB
    F -- Invokes --> ML
    A -- UI/UX --> R
    B -- UI/UX --> R
    R -- API Calls --> F
    BI -- Reads Data --> DB
     A:::donor
     B:::recipient
     R:::reactleaflet
     M:::osm
     AL:::auth
     F:::flask
     ML:::matching
     DB:::database
     BI:::bi
    classDef donor fill:#E6F7FF,stroke:#007BFF,stroke-width:1px,color:#000
    classDef recipient fill:#FFF9E6,stroke:#FFC107,stroke-width:1px,color:#000
    classDef reactleaflet fill:#EBF3FC,stroke:#61DAFB,stroke-width:1px,color:#000
    classDef osm fill:#C8E6C9,stroke:#4CAF50,stroke-width:1px,color:#000
    classDef auth fill:#FDEDEC,stroke:#E74C3C,stroke-width:1px,color:#000
    classDef flask fill:#FFF2E0,stroke:#FF851B,stroke-width:1px,color:#000
    classDef matching fill:#F5F5F5,stroke:#555,stroke-width:1px,color:#000
    classDef database fill:#E0F2F1,stroke:#009688,stroke-width:1px,color:#000
    classDef bi fill:#E1BEE7,stroke:#9C27B0,stroke-width:1px,color:#000
    style BE fill:#424242
    style AWS fill:#E1BEE7
