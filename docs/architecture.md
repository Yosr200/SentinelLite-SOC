flowchart LR
    A[Log Sources<br/>SSH / Auth Logs]
    B[Log Ingestion]
    C[Detection Engine]
    D[Alert Manager]
    E[Incident Response]
    F[Dashboard / Reports]

    A --> B
    B --> C
    C -->|Suspicious Activity| D
    D --> E
    D --> F
