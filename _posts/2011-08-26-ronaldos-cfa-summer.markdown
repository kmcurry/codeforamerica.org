---
layout: post
status: publish
published: true
title: Ronaldo's CfA Summer
author: Ronaldo Barbachano
author_login: ronaldo
author_email: ronaldo@codeforamerica.org
wordpress_id: 8159
wordpress_url: http://codeforamerica.org/?p=8159
date: 2011-08-26 09:57:31.000000000 +00:00
categories:
- CfA Labs
- 2011 Interns
tags: []
---
As one of the first interns at CfA, I am pleased with my experience with both <a title="Code For America" href="http://codeforamerica.org">CFA</a> and <a title="GSOC 2011" href="http://socghop.appspot.com/gsoc/homepage/google/gsoc2011">Google Summer of Code</a>. This summer I was assigned to develop PHP libraries on existing government related projects.

Much of my work has focused on v2 of the Open311 API spec, National Health Library API's, creating a API base class, and implementing continuous integration strategies using <a title="Simple Test" href="http://www.simpletest.org/">SimpleTest</a> and <a title="Jenkins" href="http://jenkins-ci.org/">Jenkins</a>. With the <a title="PHP Base Class" href="https://github.com/codeforamerica/PHP-API-Template">new</a> base class, I was quickly able to create the following libraries :
<ul>
	<li><a title="PHP Product Recall API Library" href="https://github.com/codeforamerica/product_recall_php">product_recall_php</a> - Search known Federal Product Recall data.</li>
	<li><a title="USA Spending" href="https://github.com/codeforamerica/usa_spending_php">usa_spending_php</a> - Search databases that track USA spending.</li>
	<li><a title="Faa" href="https://github.com/codeforamerica/faa_php">faa_php</a> - Query FAA for Airport delays/updates.</li>
	<li><a title="Chronicling America" href="https://github.com/codeforamerica/chronicling-america-php">chronicling-america-php</a> - Search American periodicals.</li>
	<li><a title="World Bank" href="https://github.com/codeforamerica/world_bank_php">world_bank_php</a> - Search database with World Bank statistics.</li>
	<li><a title="Open311" href="https://github.com/codeforamerica/open311_php">open311_php</a> - For interacting with municipal based help-ticket system; updated for v2.</li>
	<li><em>National Health Library API's</em></li>
	<li><a title="RxNorm" href="https://github.com/codeforamerica/rxNorm_php"> RxNorm</a> - Semantic Medications Tool.</li>
	<li><a title="NDF-RT" href="https://github.com/codeforamerica/ndfRT_php"> NDF-rt</a> - Searches drug interactions.</li>
	<li><a title="Toxnet" href="https://github.com/codeforamerica/toxnet_php">Toxnet</a> - Searches known toxin databases.</li>
	<li><a title="Pillbox" href="https://github.com/codeforamerica/pillbox_php">Pillbox</a> - Search drugs based on physical pill descriptions.</li>
</ul>
Of these API's I was able to quickly put together a small web App <a href="http://rxnix.com">RXNix</a> for the RxNorm API which was recently created this summer. This <a title="rxNormRef_php" href="https://github.com/codeforamerica/rxNormRef_php">App</a> interfaces with a database created by <a title="National Library of Health" href="http://www.nlm.nih.gov/">the National Library of Health</a> to give healthcare professionals a single location to convert a variety of existing medical codes (for concepts, drugs, ingredients and related) to the new Unified Medical Language System.

<a href="http://codeforamerica.org/wp-content/uploads/2011/08/rxnix_ss.jpg"><img class="aligncenter size-full wp-image-8160" title="rxnix_ss" src="http://codeforamerica.org/wp-content/uploads/2011/08/rxnix_ss.jpg" alt="" width="610" /></a>

(Editor's Note: <em>Over the summer of 2011, over a dozen students interned with Code for America. They brought great energy, passion, and skills to bear on our projects and our mission to make government more open and efficient. Over the next week, we'll be posting their summaries of their work and learnings, in addition to an overview of the summer.</em>)
