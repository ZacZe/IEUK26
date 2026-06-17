#!/usr/bin/env python3
"""Detect anomalous turbines from telemetry data.

The script reads data/telemetry_data.csv and checks each turbine for:
  - average temperature above 85.0*C
  - vibration spikes above 15.0 mm/s

As a result, it prints a report of anomalous turbines and their metrics. 
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parent / "data" / "telemetry_data.csv"


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Telemetry file not found: {DATA_PATH}\n"
            "Please ensure the telemetry CSV is located at data/telemetry_data.csv!!!!!"
        )

    df = pd.read_csv(DATA_PATH)
    summary = (
        df.groupby("turbine_id", sort=True)
        .agg(
            average_temperature_c=("temperature_c", "mean"),
            max_vibration_mm_s=("vibration_mm_s", "max"),
        )
        .reset_index()
    )

    anomalies = summary[
        (summary["average_temperature_c"] > 85.0)
        | (summary["max_vibration_mm_s"] > 15.0)
    ]

    print("Turbine Anomaly Report")
    print("======================")

    if anomalies.empty:
        print("No turbines currently fail the anomaly rules.")
        return

    print("Turbines requiring URGENT MAINTENANCE:")
    for _, row in anomalies.iterrows():
        reasons = []
        if row["average_temperature_c"] > 85.0:
            reasons.append(
                f"average temperature {row['average_temperature_c']:.1f}°C > 85.0°C"
            )
        if row["max_vibration_mm_s"] > 15.0:
            reasons.append(
                f"vibration spike {row['max_vibration_mm_s']:.1f} mm/s > 15.0 mm/s"
            )
        print(f"- {row['turbine_id']}: {', '.join(reasons)}")

    print("\nDetailed metrics:")
    for _, row in anomalies.iterrows():
        print(
            f"  {row['turbine_id']}: avg temp={row['average_temperature_c']:.1f}°C, "
            f"max vibration={row['max_vibration_mm_s']:.1f} mm/s"
        )


if __name__ == "__main__":
    main()
