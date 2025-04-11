---
title:  Omop
created: Tuesday 14th January 2025 20:08
aliases: 
tags: Omop
---
*The Observational Medical Outcomes Partnership* (OMOP) Common Data Model (CDM) is an open community data standard, designed to standardize the structure and content of observational data and to enable efficient analyses that can produce reliable evidence. A central component of the OMOP CDM is the OHDSI standardized vocabularies. The OHDSI vocabularies allow organization and standardization of medical terms to be used across the various clinical domains of the OMOP common data model and enable standardized analytics that leverage the knowledge base when constructing exposure and outcome phenotypes and other features within characterization, population-level effect estimation, and patient-level prediction studies.

OMOP is compatible with many [[RDBMS]], but some tools and extensions may work better with specific ones (e.g., [[PostgreSQL]] for OHDSI tools).

| Tool                                                          | Description                                                        |
| ------------------------------------------------------------- | ------------------------------------------------------------------ |
| [Broadsea-Atlasdb](https://github.com/OHDSI/Broadsea-Atlasdb) | A Postgresql database in a Docker container for OHDSI Atlas/WebAPI |
| [CDM](https://github.com/OHDSI/CommonDataModel)               | Definition and DDLs for the OMOP Common Data Model (CDM)           |
Here’s a brief overview of its core components:

- **Concepts.** Basic building blocks represent entities such as drugs, diseases, procedures, and observations.
- **Vocabulary tables.** Provide standardised terminology and classification for concepts, including drug names, disease classifications, and measurement units.
- **Person table.** Contains demographic information about patients, such as age, gender, and ethnicity.
- **Observation period table.** Tracks the time period during which each person’s data is collected.
- **Condition table.** Records diagnoses and medical conditions observed in the data.
- **Drug exposure table.** Details the medications and treatments patients have received.
- **Procedure table.** Captures information about medical procedures and interventions.
- **Measurement table.** Includes data from clinical measurements and laboratory tests.
- **Visit the occurrence table.** Logs the healthcare visits and encounters.