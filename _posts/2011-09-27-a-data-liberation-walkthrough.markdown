---
layout: post
status: publish
published: true
title: A Data Liberation Walkthrough
author: John Mertens
author_login: john
author_email: john@codeforamerica.org
author_url: http://mertonium.com
wordpress_id: 8782
wordpress_url: http://codeforamerica.org/?p=8782
date: 2011-09-27 16:57:24.000000000 +00:00
categories:
- CfA Labs
- Boston
tags: []
---
Last time I wrote about how to build a <a title="Farmers’ Market API" href="http://codeforamerica.org/2011/08/08/farmers-market-api/">US-wide farmers' market API</a> in under an hour. Today, I want to walk through a larger challenge to highlight some of the tools &amp; techniques we are using at Code for America to create APIs for public data (and an example of a web app that uses the API). For this example we're going to use the <a href="http://www.publicartboston.com">City of Boston's Public Art website</a>. I really like this site; they have a great map interface and a bunch of good content. The one missing piece is an API so that other developers can build on this data. That's what we'll build today (and just to be extra productive, we'll setup a mobile web app that runs off the data). Also, Boston is a 2011 Code for America city and they are already taking steps to provide an API for this data, so I figure they won't mind if we do this :) (<a href="#tldr">tl;dr version</a>)

<strong>UPDATE</strong> <em>The API I just mentioned is now live and can be accessed <a href="http://datacouch.com/api/couch/dca42ee329dce8b97ccd706c5815002067/_all_docs?include_docs=true">via DataCouch.com</a>. </em>

<em></em>Before we dive into this specific case, I want to point out some of the tools that all data liberators should be familiar with, along with how we are going to use them.
<ul>
	<li><a href="http://code.google.com/p/google-refine/">Google Refine</a> - we only use it as a scraper, but if you're not familiar with Refine, follow the link and watch the video.</li>
	<li><a href="https://github.com/maxogden/recline">Recline</a> - as a data manager for couch documents.</li>
	<li><a title="GeoCouch Utils on GitHub" href="https://github.com/vmx/geocouch-utils" target="_blank">GeoCouch-Utils</a> - adds geospatial api, default map.</li>
	<li><a href="https://github.com/codeforamerica/public_art_finder/tree/master/viewer_couchapp">viewer</a> - example of drop in CouchApp...with a poor name.</li>
</ul>
<a name="getdata"></a>
<h2>1. Getting the data</h2>
In many cases, this can be the hardest step. Fortunately, the City of Boston <a href="http://www.publicartboston.com">has a website</a> with geolocated data for over 250 pieces of public art. We are going to look at the source code for their map and find all the juicy data. If you want to skip straight to the data (or if the website changes formatting) I've posted a <a title="boston_public_art.json" href="https://gist.github.com/1190109" target="_blank">copy of the file I used on GitHub</a>. <em>Be aware that this method of getting data is not a best practice and should be used only when needed (and legal).</em>

Go to the <a title="Public Art Boston map" href="http://publicartboston.com/map/node" target="_blank">Public Art Boston map</a> and view the source code for the page. Copy the "markers" array from the javascript source into a file called <em>boston_public_art.json</em>.

<a href="http://codeforamerica.org/wp-content/uploads/2011/09/view-source.png"><img class="size-large wp-image-8784  alignnone" title="view-source" src="http://codeforamerica.org/wp-content/uploads/2011/09/view-source-1024x331.png" alt="source code with all the data" width="640" height="206" /></a>
<h3>Tidy the data in Refine</h3>
Open <em>boston_public_art.json</em> in Google Refine.

<a href="http://codeforamerica.org/wp-content/uploads/2011/09/in-refine-1.png"><img class="size-large wp-image-8787 alignleft" title="in-refine-1" src="http://codeforamerica.org/wp-content/uploads/2011/09/in-refine-1-1024x428.png" alt="Refine Screenshot" width="640" height="267" /></a>

Remove the 'text' column - we don't need it

<a href="http://codeforamerica.org/wp-content/uploads/2011/09/remove-column.png"><img class="size-full wp-image-8789 alignleft" title="remove-column" src="http://codeforamerica.org/wp-content/uploads/2011/09/remove-column.png" alt="Deleting a column in Google Refine" width="725" height="501" /></a>

Clean up the column names (rmt, latitude, longitude, markername, title)

[caption id="attachment_8790" align="alignleft" width="874" caption="Column headings: before"]<a href="http://codeforamerica.org/wp-content/uploads/2011/09/titles-before.png"><img class="size-full wp-image-8790" title="titles-before" src="http://codeforamerica.org/wp-content/uploads/2011/09/titles-before.png" alt="column titles: before" width="874" height="28" /></a>[/caption]

[caption id="attachment_8791" align="alignleft" width="443" caption="Column headers: after"]<a href="http://codeforamerica.org/wp-content/uploads/2011/09/titles-after.png"><img class="size-full wp-image-8791" title="titles-after" src="http://codeforamerica.org/wp-content/uploads/2011/09/titles-after.png" alt="column titles: after" width="443" height="26" /></a>[/caption]
<h3>Transform the <em>rmt</em> column</h3>
I'm not sure what 'rmt' stands for, but it looks like an ID to me (except for all the '/0's). Let's go on that hunch for now and remove all of the '/0's so we are left with just the IDs. We'll do that using the Transform functionality in Refine. Transforming a cell involves running a small piece of javascript-esque code on each cell in the column. Transforms use the <a href="http://code.google.com/p/google-refine/wiki/GRELFunctions">Google Refine Expression Language</a> (GREL). Transforms are a powerful way to programmatically clean poorly formatted data. Our current situation, however, only requires a slight string manipulation using the <a href="http://code.google.com/p/google-refine/wiki/GRELStringFunctions#replace(string_s,_string_f,_string_r">replace</a> method.

<a href="http://codeforamerica.org/wp-content/uploads/2011/09/transform.png"><img class="size-full wp-image-8792 alignnone" title="transform" src="http://codeforamerica.org/wp-content/uploads/2011/09/transform.png" alt="google refine transform menu" width="546" height="316" /></a>

<a href="http://codeforamerica.org/wp-content/uploads/2011/09/transform-dialog.png"><img class="size-full wp-image-8793 alignnone" title="transform-dialog" src="http://codeforamerica.org/wp-content/uploads/2011/09/transform-dialog.png" alt="Transform using GREL" width="704" height="523" /></a>
<h3>Scrape more data</h3>
I want to pause for a minute and do a little recon. Let's use one of our IDs and see where it leads us. We'll take the first ID (276) and build a standard, out of the box, Drupal url: <a title="http://www.publicartboston.com/node/276" href="http://www.publicartboston.com/node/276" target="_blank">http://www.publicartboston.com/node/276</a> (it was pretty trivial to figure out this was a Drupal site). This looks like a page full of awesome data! Taking a look at the source code, we see that the data is in some sort of structured form - good news. Extracting the data from the page looks like a simple problem for a javascript framework like jQuery.

<a href="http://codeforamerica.org/wp-content/uploads/2011/09/art-details-html.png"><img class="size-large wp-image-8797 alignnone" title="art-details-html" src="http://codeforamerica.org/wp-content/uploads/2011/09/art-details-html-1024x613.png" alt="Screenshot of the structure of the page with all the data" width="640" height="383" /></a>

We now find ourselves in a position where we have a list of IDs which lead to webpages containing great public art data. The next question is, how do we mash all this together? Luckily, Refine has a function to help us out. Its called "Add column by fetching URLs...". In many cases of data clean-up, this function is used to <a href="http://www.journalismgis.com/2010/11/using-google-refine-to-geocode-addresses/">geocode addresses</a>, but today we will be using it to pull the HTML from a webpage into our DB.

<a href="http://codeforamerica.org/wp-content/uploads/2011/09/fetch-url.png"><img class="size-full wp-image-8798 alignnone" title="fetch-url" src="http://codeforamerica.org/wp-content/uploads/2011/09/fetch-url.png" alt="Fetch url on the menu" width="535" height="364" /></a>

<a href="http://codeforamerica.org/wp-content/uploads/2011/09/fetch-url-dialog.png"><img class="size-full wp-image-8799 alignnone" title="fetch-url-dialog" src="http://codeforamerica.org/wp-content/uploads/2011/09/fetch-url-dialog.png" alt="Fetch from URL dialog" width="699" height="541" /></a>

<a href="http://codeforamerica.org/wp-content/uploads/2011/09/fetch-url-result.png"><img class="size-full wp-image-8800 alignnone" title="fetch-url-result" src="http://codeforamerica.org/wp-content/uploads/2011/09/fetch-url-result.png" alt="Data fetched from the url" width="833" height="617" /></a>

Great, its done! Now we have a column called 'full_html' with an entire webpage jammed into it. It may look awful, but it is exactly what we want. At this point, I would say that we've successfully acquired the data. Now let's clean it up and make it more useful.

<strong>Note</strong> <em>Google Refine is a powerful tool and we've barely scratched the surface of what it can do. I would definitely recommend exploring it more. If you've got an old CSV of poorly structured data, dump it into Refine and see how easily you can clean/normalize it.</em>
<a name="cleandata"></a>
<h2>2. Clean the data</h2>
Now that we have our raw data, we can put it into our database. We are going to use CouchDB as our database (and later as our application server). I chose <a title="The Apache CouchDB Project" href="http://couchdb.apache.org/" target="_blank">CouchDB</a> to leverage its geo-spatial component (<a title="GeoCouch on GitHub" href="https://github.com/couchbase/geocouch" target="_blank">GeoCouch</a>), to use it's out-of-the-box REST API, and because of its schema-less document structure, it will handle data of different shapes. Another benefit of using CouchDB is that we can use CouchApps to easily add frontend interfaces to the data (i.e. Recline, Geojson-utils &amp; the Viewer app used below). For development, I would highly recommend using the <a href="http://www.couchbase.org/get/couchbase-single/current">Couchbase Single Server</a>. Just download, and install it. You will know it worked when you can go to <a title="Is CouchDB running locally?" href="http://localhost:5984/_utils" target="_blank">http://localhost:5984/_utils</a> and see Futon, CouchDB's web-based administration console.
<h3>Setup the DB</h3>
From the Futon homepage, create a new database and call it "boston_public<em>_</em>art".

<a href="http://codeforamerica.org/wp-content/uploads/2011/09/create-database.png"><img class="size-full wp-image-8801 alignnone" title="create-database" src="http://codeforamerica.org/wp-content/uploads/2011/09/create-database.png" alt="Creating a DB in Couch" width="452" height="185" /></a>
<h3>Install Recline</h3>
<a title="Recline on GitHub" href="https://github.com/maxogden/recline" target="_blank"> Recline</a> is a cleverly named CouchApp built by <a title="Max on Twitter" href="http://twitter.com/#!/maxogden" target="_blank">Max Ogden</a>. It provides a Refine-ish interface to data in a couch. My favorite part is that transformation functions are written in javascript (as opposed to GREL in Refine). Also, we can access the jQuery object in our transformations, which will come in handy for us. The easiest way to install Recline is via the command line.
<pre>curl -X POST http://localhost:5984/_replicate -d '{"source":"http://max.iriscouch.com/apps","target":"boston_public_art", "doc_ids":["_design/recline"]}' -H "Content-type: application/json"</pre>
Alternately, if you are familiar with CouchApps, you can <a href="https://github.com/maxogden/recline">download the code from GitHub</a> and install it yourself. Once installed, go to <a title="Your local Recline instance" href="http://127.0.0.1:5984/boston_public_art/_design/recline/_rewrite/" target="_blank">http://127.0.0.1:5984/boston_public_art/_design/recline/_rewrite/</a>. You will see it in an interface which resembles a minimalist version of Refine.

[caption id="attachment_8812" align="alignnone" width="640" caption="Fresh install of Recline"]<a href="http://codeforamerica.org/wp-content/uploads/2011/09/recline-empty.png"><img class="size-large wp-image-8812 " title="recline-empty" src="http://codeforamerica.org/wp-content/uploads/2011/09/recline-empty-1024x367.png" alt="Screenshot of a fresh Recline install" width="640" height="229" /></a>[/caption]

Lets put some data in it.
<h3>Upload the data to a Couch[DB]</h3>
Now that the couch is ready, we need to move our data into it from Refine. We'll use the Refine export templating engine to create a JSON object that can be accepted by the native <a href="http://wiki.apache.org/couchdb/HTTP_Bulk_Document_API#Modify_Multiple_Documents_With_a_Single_Request">CouchDB bulk documents API</a> as illustrated below.

[caption id="attachment_8813" align="alignnone" width="901" caption="Template for exporting the data in a format _bulk_docs can receive"]<a href="http://codeforamerica.org/wp-content/uploads/2011/09/bulk-docs-templating.png"><img class="size-full wp-image-8813 " title="bulk-docs-templating" src="http://codeforamerica.org/wp-content/uploads/2011/09/bulk-docs-templating.png" alt="screenshot of refine export templating engine" width="901" height="609" /></a>[/caption]

Clicking "Export" will download the JSON object as a file named boston-public-art.txt. We switch to our terminal and navigate to the folder where the file was downloaded (I use ~/Downloads/ on my machine). The following command will insert all of our data into the couch (each object in our "docs" array will become one document in the couch).
<pre>curl -X POST http://127.0.0.1:5984/boston_public_art/_bulk_docs -d@boston-public-art.txt -H "Content-type: application/json"</pre>
[caption id="attachment_8814" align="alignnone" width="640" caption="Viewing out imported data via Recline"]<a href="http://codeforamerica.org/wp-content/uploads/2011/09/after-recline-import.png"><img class="size-large wp-image-8814 " title="after-recline-import" src="http://codeforamerica.org/wp-content/uploads/2011/09/after-recline-import-1024x585.png" alt="Screenshot of recline after a the import" width="640" height="365" /></a>[/caption]

<strong>Note</strong> <em>There is another way to upload the data from Refine to CouchDB. You will need to download and install Max Ogden's <a href="https://github.com/maxogden/refine-uploader">Google Refine Uploader Extension</a>. It allows you to export data from Refine directly into a couch - basically automating the steps above.</em>

[caption id="attachment_8815" align="alignnone" width="272" caption="After installing Refine Uploader, this option will appear in the &quot;Export&quot; menu"]<a href="http://codeforamerica.org/wp-content/uploads/2011/09/refine-uploader.png"><img class="size-full wp-image-8815 " title="refine-uploader" src="http://codeforamerica.org/wp-content/uploads/2011/09/refine-uploader.png" alt="Screenshot of Refine Uploader" width="272" height="277" /></a>[/caption]

[caption id="attachment_8816" align="alignnone" width="901" caption="Enter the path to your database, followed by &quot;_bulk_docs&quot;"]<a href="http://codeforamerica.org/wp-content/uploads/2011/09/refine-uploader-dialog.png"><img class="size-full wp-image-8816 " title="refine-uploader-dialog" src="http://codeforamerica.org/wp-content/uploads/2011/09/refine-uploader-dialog.png" alt="Screenshot of Refine Uploader dialog box" width="901" height="295" /></a>[/caption]
<h3>Use jQuery to extract the data</h3>
I may be getting ahead of myself.  Before we can use jQuery to pull the data out of the scraped page and into the correct fields of our DB, we need to know what pieces of information we are looking for.  I know that in order to use the Viewer CouchApp we need to have the following pieces of data:
<ul>
	<li>_id - a unique ID for each document. The auto-generated CouchDB IDs will be fine for this.</li>
	<li>title - the title of the piece of art</li>
	<li>artist - name of the artist(s)</li>
	<li>description - description of the work, artist statement, notes, etc.</li>
	<li>discipline - preferably one of the following: sculpture, painting, photography, ceramics, fiber, architectural integration, mural, fountain, other</li>
	<li>location_description - a human readable location for the piece</li>
	<li>full_address - full street address, w/ city, state, zip if possible</li>
	<li>geometry - longitude/latitude in <a title="GeoJSON Spec" href="http://geojson.org/geojson-spec.html#id2" target="_blank">geojson point format</a></li>
	<li>image_urls - a comma delimited list (array) of urls to remote images.</li>
	<li>data_source - the source of the data. (i.e. 'Boston Art Commission')</li>
	<li>doc_type - this field is used by the Viewer CouchApp and should always be set to 'artwork'</li>
</ul>
All of these bits of data are present in our scraped HTML, as well as a few others. The Viewer CouchApp we are going to setup only requires the fields above, but in the interest of building a richer API we should include all of the data available. Our additional fields will include:
<ul>
	<li>audio_description</li>
	<li>collection</li>
	<li>funders</li>
	<li>medium</li>
	<li>neighborhood</li>
	<li>year</li>
</ul>
Now that we've planned out what information we want, it is time to go about collecting it. A simple way to do this is to run a transform function that uses jQuery to pull the data out of our full_html field. Select "Transform" from the menu at the top of any column. <a href="http://codeforamerica.org/wp-content/uploads/2011/09/recline-transform.png"><img class="alignnone size-full wp-image-8841" title="recline-transform" src="http://codeforamerica.org/wp-content/uploads/2011/09/recline-transform.png" alt="Screenshot of transform link on Recline" width="397" height="254" /></a>This should all look very similar to Refine so you won't be surprised by the dialog box that opens next.  The main difference from Refine is that now we can use any javascript functionality within our transform. The default transform function (for the '_id' column) looks like this:
<pre>function(doc) {             // doc is an object representing the document (or row)
  doc['_id'] = doc['_id'];  // Do any transformations you'd like
  return doc;               // Return the transformed document
}</pre>
This process makes it easy to add new fields to your documents; just assign a value to doc['newFieldName'] and it will be added to the document. We are going to get crazy and add all of our fields at once. Here is our finished transformation function:
<pre>function(doc) {
  doc['artist'] = $(doc['full_html']).find('h3:contains(Artist)').next('div').text();
  doc['description'] = $(doc['full_html']).find('h3:contains(Description:)').filter(':first').next('div').text();
  doc['discipline'] = $(doc['full_html']).find('h3:contains(Type:)').next('div').text();
  doc['location_description'] = $(doc['full_html']).find('span.fn').text();
  doc['full_address'] = $(doc['full_html']).find('span.fn').text() +', Boston, MA';
  doc['geometry'] = { type: "Point", coordinates: [parseFloat(doc['longitude'], 10), parseFloat(doc['latitude'], 10)] };
  var temp = [];
  $(doc['full_html']).find('.node_images img').each(function(idx, el){ temp.push(el.src) });
  doc['image_urls'] = temp;
  doc['data_source'] = 'Boston Art Commission';
  doc['doc_type'] = 'artwork';
  doc['audio_description'] = $(doc['full_html']).find('h3:contains(Audio Description:)').next('div').find('a').attr('href');
  doc['collection'] = $(doc['full_html']).find('h3:contains(Collection:)').next('div').text();
  doc['funders'] = $(doc['full_html']).find('h3:contains(Funders:)').next('div').text();
  doc['medium'] = $(doc['full_html']).find('h3:contains(Medium:)').next('div').text();
  doc['neighborhood'] = $(doc['full_html']).find('h3:contains(Neighborhood:)').next('div').text();
  doc['year'] = $(doc['full_html']).find('h3:contains(Year:)').next('div').text();
  return doc;
}</pre>
Yes, a bit of refactoring would make this function a bit more efficient, but I want to be clear on where each new field value is coming from. Run the transform. Once it is finished, our data will be clean (almost). One last piece of housekeeping we should do is delete the full_html column. To do that we simply use the "Delete this column" command on the menu for the full_html column. <a href="http://codeforamerica.org/wp-content/uploads/2011/09/recline-delete-column.png"><img class="alignnone size-full wp-image-8842" title="recline-delete-column" src="http://codeforamerica.org/wp-content/uploads/2011/09/recline-delete-column.png" alt="delete this column screenshot" width="500" height="261" /></a>
<a name="addgeo"></a>
<h2>3. Add Geo-spatial support</h2>
Earlier, we made sure that each document in our Couch had a geojson-formatted 'geometry' field. In order to utilize this field for geospatial queries we are going to install another CouchApp, <a title="GeoCouch-Utils on GitHub" href="https://github.com/vmx/geocouch-utils" target="_blank">GeoCouch-Utils</a>. Just like the Recline CouchApp, you can either download the source from GitHub, and install it via the CouchApp command line interface, or replicate it from someone else's couch via cURL.
<pre>curl -X POST http://localhost:5984/_replicate -d '{"source":"http://max.iriscouch.com/apps","target":"boston_public_art", "doc_ids":["_design/geo"]}' -H "Content-type: application/json"</pre>
To make sure that everything went well, point your browser at the map that comes with GeoCouch-Utils which is located at <a title="Link to the GeoCouch-utils map" href="http://127.0.0.1:5984/boston_public_art/_design/geo/_rewrite/" target="_blank">http://127.0.0.1:5984/boston_public_art/_design/geo/_rewrite/</a>.  You should see a bunch of dots on a map of Boston like this: <a href="http://codeforamerica.org/wp-content/uploads/2011/09/GeoCouch-utils-map.png"><img class="alignnone size-full wp-image-8871" title="GeoCouch-utils-map" src="http://codeforamerica.org/wp-content/uploads/2011/09/GeoCouch-utils-map.png" alt="GeoCouch-utils out of the box map" width="773" height="663" /></a>We can now give the API a bounding box of longitude/latitude coordinates and we will get a list of all the pieces of art within that box.  For example, if we wanted all of the art in/around Boston Common, we would hit the following URL:
<pre>http://localhost:5984/boston_public_art/_design/geo/_spatial/_list/geojson/full?bbox=-71.07114,42.3519,-71.0631,42.3577</pre>
At this point we have a Geospatially-enabled REST API for all city-sanctioned public art in Boston, huzzah!
<a name="setupapp"></a>
<h2>4. Setup the mobile app</h2>
I am a huge advocate for organizations (cities included) to open up their data via APIs, but I've found that many times the decision makers need an example of what can be built on the API. This is why I built a CouchApp with a crappy name: <a title="Viewer CouchApp on GitHub" href="https://github.com/codeforamerica/public_art_finder" target="_blank">viewer</a>. It is basically a CouchApp version of the <a title="MuralApp website" href="http://muralapp.mobi/" target="_blank">MuralApp mobile website</a> that <a title="Aaron on Twitter" href="http://twitter.com/#!/atogle" target="_blank">Aaron Ogle</a>&amp; I built for the Open Data Philly Hackathon. Once again, you can install it manually by downloading the code from GitHub and pushing it to your couch with the CouchApp CLI, or you can just enter this command in your terminal:
<pre>curl -X POST http://user:pass@YOURCOUCH/_replicate -d '{"source":"http://mertonium.iriscouch.com/apps","target":"YOURDB", "doc_ids":["_design/viewer"]}' -H "Content-type: application/json"</pre>
Now that the viewer CouchApp is installed, you should be able to see the app live at <a title="Link to your local Public Art App" href="http://localhost:5984/boston_public_art/_design/viewer/index.html" target="_blank">http://localhost:5984/boston_public_art/_design/viewer/index.html</a> and it should look something like this:

<a href="http://codeforamerica.org/wp-content/uploads/2011/09/mobile-viewer-app.png"><img class="alignnone size-full wp-image-8876" title="mobile-viewer-app" src="http://codeforamerica.org/wp-content/uploads/2011/09/mobile-viewer-app.png" alt="Screenshot of Public Art mobile website" width="776" height="666" /></a>

Hey, look at us, we just built a mobile website for exploring and discovering public art in Boston! Awesome.
<a name="shareit"></a>
<h2>5. Make it public</h2>
Developing locally is great, but we need to close the circle and share what we've made with the world. Luckily, we can make use of CouchDB's replication feature to easily move our app &amp; data to a [free] host.

Two of the big names in free CouchDb hosting are <a title="Iriscouch Free CouchDB hosting" href="http://iriscouch.com" target="_blank">Iriscouch</a> (which I use regularly) and <a title="Cloudant Free CouchDb hosting" href="https://cloudant.com/#!/solutions/cloud" target="_blank">Cloudant</a>.

Once you've set up an account, create a database called boston_public_art. Then, all you need to do it replicate your local boston_public_art database to the one you just created via the replicator in Futon (you could also do it from the command line, but beginners usually find Futon more approachable).

<a href="http://codeforamerica.org/wp-content/uploads/2011/09/Futon-Replicator.png"><img class="alignnone size-full wp-image-8877" title="Futon-Replicator" src="http://codeforamerica.org/wp-content/uploads/2011/09/Futon-Replicator.png" alt="Screenshot of Futon replicator" width="950" height="295" /></a>

&nbsp;

After the replication you should be able to access the mobile app with the same url as before, but with your hosted domain instead of localhost:5984. For example, I've got the app setup at <a title="Live version of the viewer app" href="http://mertonium.iriscouch.com/boston_public_art/_design/viewer/index.html" target="_blank">http://mertonium.iriscouch.com/boston_public_art/_design/viewer/index.html</a> (Be sure to check it out on a mobile device too).
<h2>What's next?</h2>
This is the point where I challenge you to go forth and liberate data with the tools and techniques listed in this post, but I do want to add one key point: data liberation is not a smash &amp; grab process.  If the data is not kept up to date, then it will lose its value and all of your hard work will be for naught.  To guard against this, work with the people and organizations who hold the data.  You may need to scrape data at first, but your end-game should be to come up with a system where updates are pulled into the couch automatically (or help the data-holders build an API directly into their current system).

This is what is now happening in Boston, hence my earlier disclaimer that the API we built is not obsolete.
<h2>More information</h2>
<ul>
	<li><a href="http://www.voiceingov.org/blog/?p=2334">Operation Data Liberation</a> by Mark Headd</li>
	<li><a href="http://maxogden.com/#blog/diy-open-data-catalog">DIY Open Data</a> by Max Ogden</li>
</ul>
<a name="tldr"></a>
<h2>tl;dr version</h2>
<ul>
	<li><a href="#getdata">Get data anyway you can.</a></li>
	<li><a href="#cleandata">Use Refine &amp; Recline to clean it up and put it in a couch.</a></li>
	<li><a href="#addgeo">Add geospatial support.</a></li>
	<li><a href="#setupapp">Build an app on your new API</a> (optional).</li>
	<li><a href="#shareit">Share it with the world.</a></li>
</ul>
