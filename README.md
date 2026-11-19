# GeoBIM: Automated IDS-Validated IFC 4 to CityGML 3.0 Framework

> **Status:** Active Research — Professional Master in BIM Thesis  
> **Approach:** 100% Open Standards & Open-Source Tooling (Zero Proprietary Middleware)

## Overview

Building Information Modeling (BIM) and Geographic Information Systems (GIS) operate under fundamentally different coordinate systems, geometric paradigms, and semantic structures. In practice, standard **Revit → IFC 4** exports suffer from weak georeferencing (`LoGeoRef20`), inconsistent spatial hierarchies, and missing properties—causing positional drift and semantic loss when integrated into 3D urban GIS environments.

This repository hosts a reproducible, vendor-neutral **openBIM-to-GIS integration pipeline** that introduces an automated pre-conversion quality gate (**buildingSMART IDS 1.0** + **LoGeoRef50**) before transforming multi-story **IFC 4** building models into **OGC CityGML 3.0**, storing them in **3DCityDB v5**, and integrating them into **QGIS** for smart-city urban analysis.

---

## Core Objectives

1. **Baseline Loss Audit:** Quantify coordinate drift, geometric issues, and attribute loss in unvalidated ("dirty") Revit-to-IFC 4 → CityGML 3.0 conversions.
2. **Upstream Quality Gate:** Author a machine-readable **GeoBIM Readiness IDS (`.ids`)** specification and automated Python (`IfcOpenShell` / `IfcTester`) validation workflow enforcing `LoGeoRef50` georeferencing and required semantic properties.
3. **Open-Source Integration:** Execute reproducible IFC 4 → CityGML 3.0 schema transformation and multi-scale ingestion into **3DCityDB v5 (PostgreSQL/PostGIS)** alongside surrounding neighborhood context.
4. **Urban Analytical Validation:** Demonstrate end-to-end indoor-to-outdoor spatial continuity (e.g., emergency evacuation routing) with quantitative **Before vs. After** KPIs.

---

## Open-Source Technology Stack

| Pipeline Stage | Open Standard | Open-Source Tooling |
| :--- | :--- | :--- |
| **BIM Inspection & Georeferencing** | IFC 4 (ISO 16739-1) | Bonsai (BlenderBIM), FZKViewer |
| **Automated QA/QC Gate** | buildingSMART IDS 1.0 | Python, IfcOpenShell, IfcTester |
| **Schema Transformation** | IFC 4 → CityGML 3.0 | TUM `ifc-to-citygml3`, IDIBAU `ifc2citygml` |
| **3D Spatial Database** | OGC CityGML 3.0 | Docker, PostgreSQL + PostGIS, 3DCityDB v5 |
| **GIS & Urban Analysis** | OGC Simple Features / EPSG | QGIS (LTR), OpenStreetMap |

---

## Planned Repository Structure

* **`01_ids_rules/`** — Machine-readable GeoBIM Readiness IDS XML rules and IFC 4 ↔ CityGML 3.0 mapping tables.
* **`02_scripts/`** — Python automation scripts (`IfcOpenShell` inspection, `IfcTester` compliance checks, and KPI evaluation).
* **`03_database_docker/`** — Reproducible Docker setup for 3DCityDB v5 (PostgreSQL/PostGIS).
* **`04_qgis_analysis/`** — Spatial queries, layer styles, and indoor–outdoor analysis workflows.
* **`05_sample_data/`** — Lightweight open test models and external dataset links.
* **`docs/`** — Architecture diagrams, validation screenshots, and HTML IDS compliance reports.

---

## Validation Metrics (To Be Populated)

| KPI | Baseline (Dirty Export) | Validated (IDS + LoGeoRef50) |
| :--- | :--- | :--- |
| **Horizontal Positional Drift ($\Delta XY$)** | *Pending baseline test* | *Target: < 0.05 m* |
| **Semantic Attribute Retention (%)** | *Pending baseline test* | *Target: > 95%* |
| **Entity Mapping Completeness (%)** | *Pending baseline test* | *Pending validation* |
| **Compliance Audit Time** | *Manual inspection* | *Automated (< 30 sec)* |

---

## License

This repository is released under the **MIT License** — see the `LICENSE` file for details. Open standards, open code, reproducible research.
