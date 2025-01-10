# ODSC-CRS-ODA-comp
Comparison analysis of IATI to CRS ODA for ODSC

## Installation

```
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running
```
python3 download_crs.py
```

## Outputs
- `output/crs_aggregated_2014_2023.csv`: OECD DAC CRS disbursement flows from 2014-2023, in millions of current USD, grouped by year, donor, and category (flow type).

## Extras
- `iati_donor_mapping_20241101.csv`: A many-to-one mapping from IATI organisation reference codes to OECD donor codes, last updated November 2024.