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

# Data Access
The CDRC site involves navigating a web user interface (UI) to find datasets, selecting desired formats, and downloading. One barrier to access is the requirement for users to register and log-in, even for open data.

As with any UI, it requires a manual and difficult-to-automate process. An application programming interface (API) is available, however, does not provide access to the majority of datasets. Besides completeness, the API suffers from a sub-optimal design as there are no endpoints to list datasets or geographical granularity making it difficult to programmatically use. Further, each API endpoint is on a per dataset and geography basis. A better design would likely have fewer endpoints and more parameters to specify the required dataset and geography, this would mean that new datasets would be easier to implement for both the CDRC (as no additional API endpoint would be needed) and users.

## Spatial Data Infrastructure

The CDRC platform falls into either the [second or third tier of the SDI maturity model](sdi-tiers-fig), as although organised around the topic of Consumer Data it offers several thematic datasets including Population and Mobility, Retail Futures, and Transport. Furthermore, while it is not wholly spatially enabling national UK data, it is notably linked to national UK SDI through at least the ONS.

## Data Openness

The CDRC seems to provide most if not all open data under the UK Open Government License, which is a permissive license allowing use, reuse, and redistribution with minimal restrictions. Given the sensitive nature, some datasets are restricted and require a formal application process which entails both an initial application and a formal application to the data owner.

## Data Formats

The OAC dataset was available in CSV, Shapefile, and GPKG formats and was accompanied by a PDF file that included information about each Supergroup, Group, and Subgroup and also linked to a detailed methodology paper.
