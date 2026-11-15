```mermaid
%%{init: {"theme": "base", "flowchart": {"nodeSpacing": 8, "rankSpacing": 8, "diagramPadding": 4}, "themeVariables": {"background": "#000000", "primaryTextColor": "#ffffff", "lineColor": "#aaaaaa", "fontFamily": "Arial"}}}%%

flowchart TB
    Controller["Controller<br/>Application logic and coordination"]

    subgraph Layers[" "]
        direction LR
        UI["UI Layer<br/>User interface"]
        Data["Data Layer<br/>Data operations"]
    end

    Database["Database<br/>Data storage (SQLite)"]

    Controller ~~~ UI
    Controller ~~~ Data
    Data --> Database

    style Controller fill:#000000,stroke:#1689d4,color:#ffffff
    style UI fill:#00101f,stroke:#00101f,color:#ffffff
    style Data fill:#001409,stroke:#001409,color:#ffffff
    style Database fill:#000000,stroke:#444444,color:#ffffff
    style Layers fill:none,stroke:none
```

# 1. Controller Overview
The Controller is the central component responsible for the application's logic and for coordinating interactions between the UI Layer and the Data Layer.

Its
