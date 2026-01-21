flowchart TD
    A[Log Sources<br/>SSH / Auth Logs]
    B[Log Ingestion<br/>Python Parsers]
    C[Detection Engine<br/>Rules + Thresholds]
    D[Alert Manager<br/>JSON Alerts]
    E[Automated Response<br/>IP Block / Actions]
    F[Alerts Storage<br/>alerts.json]
    G[Flask Dashboard<br/>SOC View]

    A --> B
    B --> C
    C -->|MITRE T1110| D
    D --> E
    D --> F
    F --> G

