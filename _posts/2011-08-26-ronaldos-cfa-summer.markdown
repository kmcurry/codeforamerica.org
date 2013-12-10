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
wordpress_html: true
wordpress_permalink: http://www.codeforamerica.org/2011/08/26/ronaldos-cfa-summer/
---

<p>As one of the first interns at CfA, I am pleased with my experience with both <a href="http://codeforamerica.org" title="Code For America">CFA</a> and <a href="http://socghop.appspot.com/gsoc/homepage/google/gsoc2011" title="GSOC 2011">Google Summer of Code</a>. This summer I was assigned to develop PHP libraries on existing government related projects.</p>
<p>Much of my work has focused on v2 of the Open311 API spec, National Health Library API’s, creating a API base class, and implementing continuous integration strategies using <a href="http://www.simpletest.org/" title="Simple Test">SimpleTest</a> and <a href="http://jenkins-ci.org/" title="Jenkins">Jenkins</a>. With the <a href="https://github.com/codeforamerica/PHP-API-Template" title="PHP Base Class">new</a> base class, I was quickly able to create the following libraries :</p>
<ul>
<li><a href="https://github.com/codeforamerica/product_recall_php" title="PHP Product Recall API Library">product_recall_php</a> – Search known Federal Product Recall data.</li>
<li><a href="https://github.com/codeforamerica/usa_spending_php" title="USA Spending">usa_spending_php</a> – Search databases that track USA spending.</li>
<li><a href="https://github.com/codeforamerica/faa_php" title="Faa">faa_php</a> – Query FAA for Airport delays/updates.</li>
<li><a href="https://github.com/codeforamerica/chronicling-america-php" title="Chronicling America">chronicling-america-php</a> – Search American periodicals.</li>
<li><a href="https://github.com/codeforamerica/world_bank_php" title="World Bank">world_bank_php</a> – Search database with World Bank statistics.</li>
<li><a href="https://github.com/codeforamerica/open311_php" title="Open311">open311_php</a> – For interacting with municipal based help-ticket system; updated for v2.</li>
<li><em>National Health Library API’s</em></li>
<li><a href="https://github.com/codeforamerica/rxNorm_php" title="RxNorm"> RxNorm</a> – Semantic Medications Tool.</li>
<li><a href="https://github.com/codeforamerica/ndfRT_php" title="NDF-RT"> NDF-rt</a> – Searches drug interactions.</li>
<li><a href="https://github.com/codeforamerica/toxnet_php" title="Toxnet">Toxnet</a> – Searches known toxin databases.</li>
<li><a href="https://github.com/codeforamerica/pillbox_php" title="Pillbox">Pillbox</a> – Search drugs based on physical pill descriptions.</li>
</ul>
<p>Of these API’s I was able to quickly put together a small web App <a href="http://rxnix.com">RXNix</a> for the RxNorm API which was recently created this summer. This <a href="https://github.com/codeforamerica/rxNormRef_php" title="rxNormRef_php">App</a> interfaces with a database created by <a href="http://www.nlm.nih.gov/" title="National Library of Health">the National Library of Health</a> to give healthcare professionals a single location to convert a variety of existing medical codes (for concepts, drugs, ingredients and related) to the new Unified Medical Language System.</p>
<p><a href="http://codeforamerica.org/wp-content/uploads/2011/08/rxnix_ss.jpg"><img alt="" class="aligncenter size-full wp-image-8160" src="http://codeforamerica.org/wp-content/uploads/2011/08/rxnix_ss.jpg" title="rxnix_ss" width="610"/></a></p>
<p>(Editor’s Note: <em>Over the summer of 2011, over a dozen students interned with Code for America. They brought great energy, passion, and skills to bear on our projects and our mission to make government more open and efficient. Over the next week, we’ll be posting their summaries of their work and learnings, in addition to an overview of the summer.</em>)</p>
