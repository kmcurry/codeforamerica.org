---
layout: post
status: publish
published: true
title: WufooPress
author: Abhi Nemani
author_login: Abhi
author_email: abhi@codeforamerica.org
wordpress_id: 7890
wordpress_url: http://codeforamerica.org/?p=7890
date: 2011-08-02 15:49:40.000000000 +00:00
categories:
- CfA Labs
tags:
- labs
wordpress_html: true
wordpress_permalink: http://www.codeforamerica.org/2011/08/02/wufoopress/
---

<p>Last year, we got through 362 applications for the fellowship without printing out one application. (And yes, that was also because last year, at this point, we didn’t own a printer that could have handled that; still don’t actually.) This year, we’ve gotten even more applications, and to handle them, we decided to automate the process a little.</p>
<p><a href="http://codeforamerica.org/wp-content/uploads/2011/08/wufoo.jpeg"><img alt="" class="alignright size-medium wp-image-7896" height="177" src="http://codeforamerica.org/wp-content/uploads/2011/08/wufoo-300x177.jpg" title="wufoo" width="300"/></a>We handle applications online through the popular and effective form software, <a href="http://wufoo.com">Wufoo</a>, which allows for a straightforward data entry mechanism. To get those applications into a useful format for our <a href="http://codeforamerica.org/2011/04/13/2012-fellow-selection-committee/">selection committee</a> to review, however, we designed a custom separate site for display, commenting, and sorting (aptly named, The Sorting Hat), which was built on top of WordPress (<a href="http://codeforamerica.org/2010/09/09/getting-to-23-our-attempt-at-a-more-modern-selection-process/">more details here</a>). This system has proven rather useful for our reviewers. But there was one problem for us: connecting Wufoo and WordPress. In the past, this had to be handled manually with a data export from Wufoo, data manipulation locally on (gasp) Excel, and then finally an import into WordPress through a plugin. And yet, efficiency is one of our values… Enter the hack.</p>
<p>Fortunately, Wufoo has a <a href="http://wufoo.com/docs/api/v3/">well-documented API</a>, which allows you to call all the entries attached to a form, and WordPress has programatic post-creation functionality through its API through the <a href="http://codex.wordpress.org/XML-RPC_Support">XML-RPC protocol</a>. I was able to connect the two together with a little PHP script that when run will first check for the last entry already in WordPress, see if there are new submissions in Wufoo, and then publish them as new posts in WordPress. Basically, it’ll let you keep an up-to-date Worpress site with your Wufoo entries. Hence the name, <a href="https://github.com/codeforamerica/Wufoopress">WufooPress</a>.</p>
<p>The script is fairly simple (I’m not much of a hacker) and could use some cleaning up and additional functionality. (It’d be great to automate the checking and posting process, or even hash this out as a proper WordPress plugin.) Code is on <a href="https://github.com/codeforamerica/Wufoopress">github</a> if there are any takers. For now, I thought it might be of some use to other people who both love and use Wufoo and WordPress — like we do here at Code for America.</p>
