---
layout: post
status: publish
published: true
title: 'Text My Bus: Transit Info for Detroiters'
author: Alicia Rouault
author_login: alicia
author_email: alicia@codeforamerica.org
wordpress_id: 16663
wordpress_url: http://codeforamerica.org/?p=16663
date: 2012-09-11 14:21:42.000000000 +00:00
categories:
- News
- 2012 fellows
- Detroit
tags: []
---
<a href="http://codeforamerica.org/wp-content/uploads/2012/09/2012-09-04_DDOTLaunch_Detroit.jpg"><img class="alignright size-medium wp-image-16683" title="2012-09-04_DDOTLaunch_Detroit" src="http://codeforamerica.org/wp-content/uploads/2012/09/2012-09-04_DDOTLaunch_Detroit-300x224.jpg" alt="" width="300" height="224" /></a>Last week, on the first day of the new school year in Detroit, the CfA Detroit team launched a new service with the <a href="http://www.ci.detroit.mi.us/DepartmentsandAgencies/DetroitDepartmentofTransportation.aspx" target="_blank">Detroit Department of Transportation</a> (DDOT) called <a href="http://www.detroitmi.gov/Portals/0/docs/deptoftransportation/pdfs/TextMyBusBroch2_5_3.pdf" target="_blank">TextMyBus</a>. TextMyBus provides a simple text messaging service to relay real time transit information to riders. In an environment where Detroiters are faced with cold winters, dangerous street corners, and broken street lights, TextMyBus provides critical information to anyone with a phone that has text messaging capability. DDOT riders simply text in their closest intersection or street address to <strong>50464</strong> and receive a list of routes that service nearby bus stops. Riders then select the route they’d like and find out the live arrival-time predictions.

<strong>Our Strategy</strong>
Over the past six months we’ve worked hand-in-hand with the Mayor’s Office and DDOT to expose the internally-tracked data. Although they have been regularly publishing static schedule GTFS data, they had no external interface for real-time information. In a landmark move, the City of Detroit opted to publish real-time transit data, which is <a href="http://appsfordetroit.org/ddot.html" target="_blank">now available</a> to developers to build on top of. We decided to build a demonstration app on this data: the text messaging service riders use today.

From there we co-hosted an apps contest called <a href="http://appsfordetroit.org/" target="_blank">Apps for Detroit</a>, calling on Detroit-based web developers to build innovative tools on top of the city's newly-opened datasets. In just two weeks we received 15 submissions, three of which were transit-related apps. One of the challenge winners called <a href="http://DDotinfo.com/" target="_blank">DDOTInfo</a> actually developed a low-cost solar-powered screen to display real-time arrival data at stops or local businesses built with <a href="http://www.raspberrypi.org/faqs" target="_blank">Raspberry Pi computers</a>.

<strong>Partners
</strong>This project was a success because we had a broad set of invaluable partners in the city and at the federal level. We worked most closely with DDOT and the Mayor's Office to open the transit data. But this project would not have happened without support from the White House Initiative: <a href="http://www.whitehouse.gov/blog/2012/06/19/white-house-council-strong-cities-strong-communities-announces-new-executive-directo" target="_blank">Strong Cities, Strong Communities</a> (SC2), who were critical to negotiating a budget with the Federal Transit Administration to make this project and other transit improvements possible at DDOT. We additionally partnered with the Detroit Police Department as well as the Detroit Public School system around the launch to get the word out. Detroit's most vulnerable populations are often those who rely most on the bus system. In support of the Safe Routes to School initiative, we distributed information and hosted students to try out the new service on their first day of school.

<strong>The Technology
</strong>We've exposed the scheduled and live data (routes, stops, arrivals, etc.) through the OneBusAway interface. Developers can use that to build phone apps, live maps, live signage, or whatever else they think of. We use the exact same interface to build the text messaging service, which is our way of quickly reaching a broad set of riders. Providing the live data in a usable way helps ensure that the experience can become richer in the future without a reliance on any one organization to develop new technology.
