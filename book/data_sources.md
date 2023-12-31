---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Dataset & Source

The 2021 Output Area Classification (OAC) {cite}`OAC2021`, a residential-based area classification that divides the UK into 7 Supergroups, 21 Groups, and 52 Subgroups based on the characteristics of the population living in each Output Area (OA) and made available by the Consumer Data Research Centre (CDRC).

The OAC dataset was chosen as it is a valuable resource for a wide range of applications and is a useful tool to understand demographic patterns across the United Kingdom (noting the current absence of data for Scotland and Northern Ireland due to a decision by the Scottish Government to delay the 2021 census to 2022 {cite}`scotland_census_2020` and a delay in publication respectively).

A second dataset, residential mobility at local authority level {cite}`cdrc_residential_mobility_index_2020`, was collected to demonstrate the reusability of the code developed to automate acquisition from the CDRC platform. This reusability meets the additional goal of this project, which was to develop a framework for future data collection efforts. This is important in the context of the CDRC which [has a wealth of open data available](../data_collection/todo.md), as well as several restricted datasets requiring a formalised application process (currently in progress).

## How the Data Was Found

### Online Search and Discovery

Discovering the OAC dataset began with a Google search, which led to the Office for National Statistics (ONS) website and a dedicated page for the 2021 version ([ONS Area Classifications](https://www.ons.gov.uk/methodology/geography/geographicalproducts/areaclassifications/2021residentialbasedareaclassifications)). Notably, while the 2011 OAC dataset was available for download directly from the ONS website, the 2021 dataset links directly to the CDRC platform, this may be because the 2021 dataset does not yet wholly cover the UK.

### Geoportals

The ONS data and geoportal, in addition to providing a link to the CDRC, is an invaluable asset for accessing a broad array of geographic data and will be a significant source for future projects, it is likely a Tier 2 SDI hosting both data and metadata and provides web mapping tools.

The CDRC hosts data and metadata directly, although the metadata is rich in detail, it is not available for download. It is available and presented in a standardised HTML table so extractable and usefully includes created and updated dates.
