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

# Introduction

An abundance of data is available and is increasingly geographically referenced, while some argue that spatial is not special effectively working with spatial data requires domain knowledge, experience, and often specialised tools. Working with geospatial data in a reproducible and transparent manner raises additional challenges, simply finding and using a spatial dataset can be fraught with additional complexity. From coordinate reference systems, spatial granularity, temporalities, privacy, and file formats to general data challenges such as discovery, access, quality, and usability.

This project aims to document and review the challenges of finding, accessing, and utilising a geospatial dataset through the lens of the FAIR (Findability, Accessibility, Interoperability and Reusability) data principles {cite}`wilkinson_fair_2016` and also assessing the platform hosting the geospatial dataset through the spatial data infrastructure (SDI) framework. Further, a development environment tailored for the collection, analysis, and visualisation of geospatial data that can be used in future (open) data collection efforts is developed. This environment is anchored by the use of GitHub CodeSpaces, selected for its accessibility through any web browser, while documentation and presentation use the Jupyter Book tool {cite}`executable_books_community_2021`, Python and Jupyter Notebooks {cite}`soton403913` provide the platform for actual data collection.

## FAIR Data Principles
The FAIR data principles were developed to provide a framework for scientific knowledge sharing and reuse. The principles apply to any digital asset including geospatial data and are available online {cite}`gofair2023fair`, in summary, data and metadata should be:

- Findable: easily locatable and identifiable through unique identifiers and rich, searchable metadata.

- Accessible: reliably and securely retrieved using standardised techniques, with metadata remaining available even if underlying data is not.

- Interoperable: structured using common standards and languages, enabling seamless integration and use across various platforms and applications.

- Reusable: licensed, documented, and adhere to community standards, ensuring they can be effectively reused.

A key criticism, while inclusive of specific criteria such as the use of persistent identifiers, the principles offer only vague and general guidance thus making them difficult to implement in practice. {cite}`martorana2022aligning` studied methods to operationalise the FAIR principles for restricted data, and while the study may misconstrue the purpose of the FAIR principles, in that they do not necessarily imply that data should be open-access and seems to conflate FAIR with open-data practices, it does highlight the need for specific guidance and reference implementations.

## Spatial Data Infrastructure

Spatial data infrastructure (SDI) is a framework of technologies, policies, and institutional arrangements that facilitate the availability of and access to spatial data {cite}`su1040946`. The concept of SDI is not new, with the term first being coined in the late-90s {cite}`goodchild1997interoperating` and having since expanded to include the notion of a spatial data ecosystem, which is a holistic view of the spatial data landscape including people, processes, and technologies. 

{cite}`fernandeza2008spatial` introduced the concept of SDI maturity levels, from local and regional to national levels, this arose as the focus was on official government SDIs. More recently, as spatial data is increasingly available from non-governmental sources and private companies, these levels have been redefined as tiers by the Open Geospatial Consortium (OGC) and International Organization for Standardization (ISO) {cite}`guide_standards_geospatial_2018`, whereby each tier represents a level of maturity in terms of the availability and accessibility. The tiers are as follows:

```{figure} images/sdi-tiers.png
---
name: sdi-tiers-fig
---
Spatial Data Infrastructure Tiers {cite}`guide_standards_geospatial_2018`
```
