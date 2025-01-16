---
title: Introducing Geolocator DP: A Data Standard for Geolocator Research
description: We released a new version of our R package frictionless.
background: https://images.unsplash.com/photo-1696778083008-cf105a901e30?q=80&w=2370&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
author: Raphaël Nussbaumer
tags: [software, R]
---

Geolocators are essential tools for studying bird movement, enabling researchers to gain insights into migration and behavior. However, managing and sharing geolocator data consistently remains challenging. To address this, we developed the [Geolocator Data Package (Geolocator DP)](https://github.com/Rafnuss/GeoLocatoR)—an extension of the [Data Package](https://datapackage.org/) standard designed specifically for geolocator data.

The development of Geolocator DP was greatly facilitated by the [Camtrap Data Package (Camtrap DP)](https://camtrap-dp.tdwg.org/), an extension of the Data Package standard for camera trap datasets. Camtrap DP provided a robust foundation that we could adapt to the needs of geolocator data. Its use of [Petridish](https://peterdesmet.com/petridish) for documentation made it easy to create a comprehensive and accessible website for Geolocator DP.

To further enhance usability, we developed [GeoLocatoR](https://raphaelnussbaumer.com/GeoLocatoR/), an R package built on the frictionless R package, similar to how [camtrapdp](https://inbo.github.io/camtrapdp/) operates for camera trap data. GeoLocatoR allows researchers to seamlessly create, manage, and validate geolocator data packages. It is designed to work in tandem with the geolocator analysis R package [GeoPressureR](https://raphaelnussbaumer.com/GeoPressureR/), which retrieves bird locations by combining light, activity, and pressure measurements. Together, GeoPressureR and GeoLocatoR provide a cohesive pipeline for analyzing geolocator data and publishing findings in movement ecology research.

We extend our gratitude to the individuals and teams behind the tools that made this work possible. In particular, we want to thanks the Research Institute for Nature and Forest (INBO) ([GitHub](https://github.com/inbo/)), Frictionless Data ([GitHub](https://github.com/frictionlessdata)), and Biodiversity Information Standards (TDWG) ([GitHub](https://github.com/tdwg)). We also wish to express our gratitude to Peter Desmet ([GitHub](https://github.com/peterdesmet)), whose advice and contributions have been instrumental. These efforts exemplify the power of open science and collaboration, enabling researchers to address data challenges effectively and advance movement ecology research.
