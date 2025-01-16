---
title: How I built Geolocator DP using open source code
description: New standard and software for geolocator data was inspired by tools developed by the Open science lab of biodiversity.
background:
  img: https://raw.githubusercontent.com/Rafnuss/GeoLocator-DP/refs/heads/main/assets/home.png
  by: Raphaël Nussbaumer
  href: https://raphaelnussbaumer.com/GeoLocator-DP/
author: Raphaël Nussbaumer
tags: [software, R]
---


{:.alert .alert-info}
This is a guest post written by [Raphaël Nussbaumer](https://github.com/rafnuss).

Geolocators are essential tools for studying bird movement, enabling researchers to gain insights into migration and behavior. However, managing and sharing geolocator data consistently remains challenging. To address this, I developed the [Geolocator Data Package (Geolocator DP)](https://raphaelnussbaumer.com/GeoLocator-DP/), an extension of the **Data Package** standard, designed specifically for geolocator data.

The development of Geolocator DP was greatly facilitated by the **Camera Trap Data Package (Camtrap DP)**, which is also build upon the Data Package standard. Camtrap DP provided a robust foundation that I could adapt to the needs of geolocator data. I was also inspired by the Camtrap DP website to create a Geolocator DP website, reusing the same free **Petridish** theme.

To further enhance usability, I developed the R package [GeoLocatoR](https://raphaelnussbaumer.com/GeoLocatoR/). Just like the R package **camtrapdp**, it makes use of the R package **frictionless** to read and manipulate data. GeoLocatoR allows researchers to seamlessly create, manage, and validate geolocator data packages. It is designed to work in tandem with the geolocator analysis R package [GeoPressureR](https://raphaelnussbaumer.com/GeoPressureR/), which retrieves bird locations by combining light, activity, and pressure measurements. Together, GeoPressureR and GeoLocatoR provide a cohesive pipeline for analyzing geolocator data and publishing findings in movement ecology research.

I extend my gratitude to the individuals and teams behind the tools that made this work possible. In particular, we want to thanks the Research Institute for Nature and Forest ([INBO](https://github.com/inbo)), [Frictionless Data](https://github.com/frictionlessdata), and Biodiversity Information Standards ([TDWG](https://github.com/tdwg)) for releasing their software as open source. Diving into source code is a really useful way to learn how functionality can be implemented and build upon. I also wish to express our gratitude to [Peter Desmet](https://github.com/peterdesmet), whose advice and contributions have been instrumental.

These efforts exemplify the power of open science and collaboration, enabling researchers to address data challenges effectively and advance movement ecology research.

## Tools used

Name | What | I used this for
--- | --- | ---
[Camtrap DP](https://github.com/tdwg/camtrap-dp) | Standard co-maintained by [Oscibio](/) | Geolocator DP
[Data Package](https://github.com/frictionlessdata/datapackage) | Standard co-maintained by Oscibio | Geolocator DP
[camtrapdp](https://github.com/inbo/camtrapdp) | R package maintained by Oscibio | GeoLocatoR
[frictionless](https://github.com/frictionlessdata/frictionless-r) | R package maintained by Oscibio | GeoLocatoR
[petridish](https://github.com/peterdesmet/petridish) | Website theme maintained by Peter Desmet | [Geolocator DP website](https://raphaelnussbaumer.com/GeoLocator-DP/)
