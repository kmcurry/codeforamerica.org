---
layout: post
status: publish
published: true
title: Transparency? We need more Middleware!
author: Dan Melton
author_login: dan
author_email: dan@codeforamerica.org
excerpt: 'Over the past month, we''ve been traveling from coast-to-coast to meet with
  our cities. Part of the process included interviewing dozens of key staff and stakeholders
  to get a stronger sense of the culture, IT environment and problems our cities are
  facing. Every city is unique. They have different histories, budgets, political
  structures, priorities and even dress codes. Despite their unique cultures, Alissa
  and I heard the same interesting themes over and over again. Here are a few themes
  that cut across every city:'
wordpress_id: 1377
wordpress_url: http://codeforamerica.org/?p=1377
date: 2010-09-13 13:56:27.000000000 +00:00
categories:
- Commentary
tags: []
---
Over the past month, we've been traveling from coast-to-coast to meet with our cities. Part of the process included interviewing dozens of key staff and stakeholders to get a stronger sense of the culture, IT environment and problems our cities are facing. Every city is unique. They have different histories, budgets, political structures, priorities and even dress codes. Despite their unique cultures, Alissa and I heard the same interesting themes over and over again. Here are a few themes that cut across every city:<a id="more"></a><a id="more-1377"></a>

<strong>Different Decades, Different Systems</strong>
From green screens to white-labeled software-as-a-service solutions, every city has a tough time connecting the disparate data systems. Depending on the decade, that solution runs on legacy Windows environments or uses older database connections that don't sync up in the modern IT infrastructure. This poses problems when trying to connect data about citizens in one place. Building permits run on Oracle; Licensing on PostGres; Payroll is in the cloud. The uniqueness costs money and time. Each new software system has to build in legacy connectors, but the knowledge to do so often rests outside city IT departments.

<strong>Double Entry</strong>
When the price is too high (either time or money) to build in cross-compatibility, cities turn to double entry.  One of our cities requires staff to enter time sheets in excel, print them out and fax into a central department. Once there, the sheets are keyed into an older legacy system. I couldn't imagine sitting on the receiving end of that fax machine. A simple web form could take care of the problem, if, and only if, some one could connect the web form to the human resources system. Along this line, two of our cities use web forms for licensing or permits. The completed form is emailed (and some times printed) to a staff member and rekeyed into another system. Again, the answer is double entry, frustrating staff members and creating hidden costs that add up across departments. The lack of little connectors between systems cost cities big money.

<strong>People Management</strong>
From 1800 people in Boulder to over 30,000 in Philadelphia, people management through integrated software is a huge need. Cities buy separate software packages to manage payroll, cell phones, access cards, website passwords, GIS access, health benefits, and email, to name just a few critical areas. Often, each software solution is located in a different department purchased years apart in different programming or database languages.  Different systems makes it super difficult to manage costs. How many cell phones are currently active versus being used? How many licenses have we bought versus actually need? Out of 30,000 employees, who knows the answer to this citizen's question?  These questions should be easier to answer, but the decision support tools are lacking.

<strong>Middleware Spawns Transparency</strong>
What struck me the most out of our visits is the reliance of transparency on middleware. Take any really simple transparent topic. How many building permits were given in my neighborhood? In order to answer that question, the building permit database in Department of Planning has to be queried by the IT Department GIS database and delivered to a citizen through a secure, nonwriteable web interface. The building permit database is geo-coded by street, but the GIS database is geo-coded by polygon boundaries. That requires a wrapper.  So does the web to GIS system and the web to building permit system. These little things are the core of making government transparent. Without the little connectors between systems, evaluating our IT-driven governments is nearly impossible.

We need more middleware!
