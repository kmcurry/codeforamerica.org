---
layout: post
status: publish
published: true
title: 'Justin''s CfA Summer: Ruby & World Bank Data'
author: Justin Stoller
author_login: justins
author_email: justin@codeforamerica.org
wordpress_id: 8455
wordpress_url: http://codeforamerica.org/?p=8455
date: 2011-09-08 11:25:49.000000000 +00:00
categories:
- CfA Labs
- 2011 Interns
tags:
- labs
- cfalabs
---
When the summer started off, we broke into teams of two or three and worked on to build out developer tools for our chosen datasets, though soon enough we were constantly conferring and getting advice from each other. (We literally all worked side by side at what quickly became the "Interns' Table".)

I choose with my usual foolishness the largest, most complicated API we had on the table, the <a href="http://data.worldbank.org/indicator">World Bank's Development Indicators</a>. I didn't just choose this API for the challenge, but also because it, though global in scope, represented to my one of the most important data sets we had to work with. The World Bank's Catalog of Development Indicators is over 7,000 strong, holding metrics from the percentage of women who receive prenatal care, to percentage of land occupied by forest, to industry by industry rates of pollution, as well as all things economic. This data represents the humanity's best attempt to measure the health of the world, economically, environmentally, and socially, country by country for the last half a century.

I began this task, honestly, having never written either a Ruby gem or an API wrapper before. In another life I had been a geeky construction worker and manager and quit only a little while ago to follow what a career in what truly interested me. I had, however, written scripts to consume different API's. Having this experience left we wanting to mimic or learn how to program in a style of some of the best Ruby API wrappers. I sat, pouring over the source code for the Twitter gem on Github for hours. How could I make the World Bank's wealth of information as accessible as Twitter's?

To start with I created the a list of aliases for each country, so a developer needn't remember that the two letter country code for Algeria is 'DZ'.<sup><a href="#f1">1</a></sup> If you know the codes perfect, otherwise typing in 'algeria' will return the same information to you (and misspelling will raise an error with an error that suggests possible countries you meant). Then I began looking into the simple chaining of methods on a “query” object. This would allow you to programatically build your query in several steps instead of passing one long gargantuan parameter list into the API in the same manner that Rails and Jquery ease searching. (You can read an excellent tutorial on doing this by the original author of the Twitter gem <a href="http://railstips.org/blog/archives/2010/10/24/the-chain-gang/">here</a>.) 

Finally I created the ability to receive from and pass into the API native Ruby objects. When you searched for “featured indicators” you can receive either a simple array of data hashes or you can receive back an array of “Indicator” objects. These instead of having to parse to find their ID and return that string back to a new query for information within that data set, you can simply pass that Indicator object into the query and it will submit its ID to the query when you send in the request.

For an example, if I wanted to look at a list of “featured” indicators I can call <sup><a href="#f2">2</a></sup>:

<blockquote>WorldBank::Indicator.featured.cycle
</blockquote>

Sorting through the returned array I can inspect the names, note, organization that supplies the information, and what topic it falls under. After some sorting I pull the “Forested Area (% of total land)” Indicator and save it in a variable called '@forests'.

If in some other part of my program I was working with Ruby Date objects, say my birthday as the variable '@birth' and the present date as the variable '@now', and I wanted to know the percentage of land occupied by forest in Brazil and how it's changed during my life time I can submit a query like this:

<blockquote>WorldBank::Data.country( 'brazil' ).indicator( @forests ).dates( @birth...@now ).fetch
</blockquote>

This is far from a final solution to the challenge of accessing all of the World Bank's information, but it is my humble attempt. I hope that it helps ease the process of working with what I believe is one of the world's most important datasets. A dataset that we can use to compare exactly how our economic, environmental, and social goals are progressing as a planet.

Of course, if you do have an issue of any kind I plan to continue to maintain and work on this gem. Don't hesitate to contact me through the <a href="https://github.com/codeforamerica/world_bank_ruby">project's Github page</a> or my own <a href="https://github.com/justinstoller">personal Github page</a>.

<h3>Notes</h3>

<a name="f1">1</a> To geek out on you for a minute: the World Bank's API allows you to sort through its information using a number of parameters, it also allows you to inspect its information on the parameters you can pass to filter data. It has a number of global options for any query, and the terms it uses to sort data and to inspect those parameters is of course the same. Depending on how the terms are placed within the search path, however, you could, say, get back Syria's Agricultural datasets, or instead, a list of meta information about the Agricultural datasets that are on record for Syria. Obviously this distinction is a footnote in the actual documentation and you cannot actually refer to 'Syria' in a request or sort by 'Agricultural Data'. You must use one of the World Bank's partial implementations of either the country's two letter or three letter country code, refer to topics by ID, and pull out information using the Indicator's ID (percentage of forested land in a country is listed by 'AG.LND.FRST.ZS', naturally...).
// end geek out

<a name="f2">2</a> The cycle method will repeat the request for each successive page of results – the 'short' featured list is 7 pages long!

(Editor’s Note: Over the summer of 2011, over a dozen students interned with Code for America. They brought great energy, passion, and skills to bear on our projects and our mission to make government more open and efficient. Over the next week, we’ll be posting their <a href="http://codeforamerica.org/category/interns/">summaries of their work and learnings</a>, in addition to an overview of the summer.)
