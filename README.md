# IEUK26
## Engineering Sector Project

## Artefact 1: Data Processing

This repository contains an anomaly detector for turbine telemetry data.
The script reads `data/telemetry_data.csv`, computes average turbine temperature and maximum vibration, and flags turbines that require urgent maintenance.

### Files

- `anomaly_detector.py` — Python script that detects anomalous turbines.
- `data/telemetry_data.csv` — sample turbine telemetry input data.
- `requirements.txt` — Python dependency list for the script.
- `Dockerfile` — container recipe for packaging the script in a Docker image.

### Run the script locally

1. Install Python 3.8+.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the detector:
   ```bash
   python anomaly_detector.py
   ```

The script prints a list of turbine IDs that fail the anomaly rules:
- average temperature above `85.0°C`
- vibration spikes above `15.0 mm/s`

## Artefact 2: Containerisation

### Run inside Docker

1. Build the Docker image:
   ```bash
   docker build -t turbine-anomaly-detector .
   ```
2. Run the container:
   ```bash
   docker run --rm turbine-anomaly-detector
   ```

This packages the script, Python runtime, and dependencies so it runs consistently in any compatible Docker host.

### Notes

- The Dockerfile uses `python:3.12-slim` as the base image.
- The container command runs `python anomaly_detector.py` by default.
- If you update dependencies, also update `requirements.txt`.