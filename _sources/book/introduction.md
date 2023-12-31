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

An abundance of data available and it is increasingly geo-located. While some argue that spatial is not special and can be simply considered as an additional attribute or field, it is clear to practitioners that spatial data often requires specific domain knowledge and experience. As an example, the seemingly simple task of finding and using a spatial dataset is a process that is often fraught with additional challenges that must be overcome including: geo-file format, coordinate reference systems, spatial granularity, temporalities, privacy, to name a few. This is in addition to the more general challenges applicable to any data of discovery, access, quality, and usability.

The purpose of this project is to document and critically analyse the challenges of finding, accessing, and utilising a geospatial dataset using the FAIR (Findability, Accessibility, Interoperability and Reusability) data principles {cite}`wilkinson_fair_2016`. Further, the project will assess the platform hosting the geospatial dataset in terms of which tier of spatial data infrastructure (SDI) it belongs to. Finally, the project will detail options and tools around integrating the geospatial dataset with other datasets in the future.

A side goal of this project is to utilise a series of modern tools and techniques that are gaining increased usage among the geospatial data science community. In pursuit of this aim, I established a development environment tailored for the collection, analysis, and visualization of geospatial data that can be used to document future (open) data collection efforts. This environment is anchored by the use of GitHub CodeSpaces, selected for its versatility, shareability, and accessibility through any web browser. The project's documentation and presentation are adeptly managed through the Jupyter Book tool {cite}`executable_books_community_2021`, while Jupyter Notebooks {cite}`soton403913` provide a platform for effective data collection and visualisation.

## FAIR Data Principles
The FAIR data principles were developed to provide a framework for scientific knowledge sharing and reuse. The principles that form the acronym (FAIR) itself explicitly attempt to enumerate a set of rules to enhance the findability, accessibility, interoperability, and reusability of digital assets. 

The principles are applicable to any digital asset, including geospatial data and are available online {cite}`gofair2023fair`. The principles can be summarised as follows:

- **Findable**: Data and metadata are easily locatable and identifiable through unique identifiers and rich, searchable metadata.
- **Accessible**: Data and metadata can be reliably and securely retrieved using standardised techniques, with metadata remaining available even if the data is not.
- **Interoperable**: Data and metadata are structured using common standards and languages, enabling seamless integration and use across various platforms and applications.
- **Reusable**: Data and metadata are thoroughly documented and adhere to community standards, ensuring they can be effectively reused in different contexts and for various purposes.

One criticism of these guidelines is that, while they are inclusive of specific and useful criteria such as the use of persistent identifiers, they offer only vauge and general guidance and offer no specific reference implementation. This makes them somewhat difficult to implement in practice as evidenced by {cite}`martorana2022aligning` who conducted a study to discover methods and approaches to operationalise the FAIR principles as related to restricted research data. While this study may be misconstruing the purpose of the FAIR principles, in that the FAIR principles do not necessarily imply that data should be open or in other words the FAIR principles are distinct to open data practices, it does highlight the need for more specific guidance and reference implementations.

## Spatial Data Infrastructure
Spatial data infrastructure (SDI) is a framework of technologies, policies, and institutional arrangements that facilitate the availability of and access to spatial data {cite}`su1040946`. The concept of SDI is not new, with the term first being coined in the 1990s {cite}`goodchild1997interoperating` and has since expanded to include the notion of a spatial data ecosystem, which is a more holistic view of the spatial data landscape that includes the people, processes, and technologies that interact with spatial data. {cite}`fernandeza2008spatial` introduced the concept of SDI maturity levels, from local and regional to national as the focus was on official government SDIs.

More recently, given the increasing availability of spatial data from non-governmental sources such as that from volunteered geographic information and private companies the levels have been redefined as tiers by the Open Geospatial Consortium (OGC) and International Organization for Standardization (ISO) {cite}`guide_standards_geospatial_2018`, whereby each tier represents a level of maturity in terms of the availability and accessibility of spatial data and services.

```{figure} images/sdi-tiers.png
---
name: sdi-tiers-fig
---
Spatial Data Infrastructure Tiers {cite}`guide_standards_geospatial_2018`
```