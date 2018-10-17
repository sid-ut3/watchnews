// KB, PSB, FGD
/*Lien Wiki*/
function wiki(word){
	$.ajax({
      url:'http://localhost:5000/found_word' + '/' + word,
    //url:'http://130.120.8.250:5000/found_word' + '/' + word,
      type: 'GET',
      dataType: 'json',
      success: function(code_html, statut){
      	if (Object.keys(code_html).length==1){
      	var text = '<a id=wiki_a_research href="'+code_html[1].link+'"><img id=wiki_img_research src="https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png" width="50" height="50">'+code_html[1].word+'</img></a>';
      	$('#wiki').html(text);}},
      error: ajax_failed,
    });
} 


/*Boites des dates*/

function verification(word,start,end){
d1=formattedDate(start,'mmddyyyy');
d2=formattedDate(end,'mmddyyyy');
if (d1==false || d2==false){
  alert('date impossible,réessayez')
  }else{
    d1=new Date(d1)
    d2=new Date(d2)
    if (word=='' ||  d2<d1){
      if (word==''){
        alert('Il faut absolument rentrer un mot')
      }else{                
        alert('Il faut absolument que la première date soit inférieur ou égale à la deuxième')      
      }
      return false
    }else{
      return true
    }
  }
}

function formattedDate(date,type) {
  var day="";var month="";var year="";
  if (date.substring(2,3)=='/' && date.substring(5,6)=='/'){day=date.substring(0,2); month=date.substring(3,5); year=date.substring(6,10)}
  if (date.substring(2,3)=='/' && date.substring(4,5)=='/'){day=date.substring(0,2); month=date.substring(3,4); year=date.substring(5,9)}
  if (date.substring(1,2)=='/' && date.substring(3,4)=='/'){day=date.substring(0,1); month=date.substring(2,3); year=date.substring(4,8)}
  if (date.substring(1,2)=='/' && date.substring(4,5)=='/'){day=date.substring(0,1); month=date.substring(2,4); year=date.substring(5,9)}
  if (day!="" && month!="" && year!=""){
    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;
    if (day<=31 && month<=12 && type=='mmddyyyy'){
      return `${month}/${day}/${year}`;
    }else if (day<=31 && month<=12 && type=='yyyymmdd'){
      return `${year}-${month}-${day}`;
    }else{
      return false;
    }
  }else{
    return false
  }
}



/*Auto-completion*/
/*var countries = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.whitespace,
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  prefetch: 'code/web/countries.json'
});
$('#prefetch .typeahead').typeahead(null, {
  name: 'countries',
  source: countries
});*/



/*Boutton de recherche*/
$("#buttonResearch_input_research").click(function() {
 var valueSearchBar = $("#searchBar_input_research").val();
 var start_date = $("#startDate_input_research").val();
 var end_date = $("#endDate_input_research").val();

 for (var i = 0; i<valueSearchBar.length; i++) {
   if (valueSearchBar.substr(i)==' '){
     valueSearchBar =valueSearchBar.replace(" ", "_")
   }
 }});

$("#buttonResearch_input_research").click(function() {
  var valueSearchBar = $("#searchBar_input_research").val();
  var start_date = $("#startDate_input_research").val();
  var end_date = $("#endDate_input_research").val();

  if (verification(valueSearchBar,start_date,end_date)==true){
    document.getElementById("wiki").innerHTML = wiki(valueSearchBar);
    var start_date_ajax = formattedDate(start_date,'yyyymmdd') ;
    var end_date_ajax = formattedDate(end_date,'yyyymmdd');

    document.getElementById("title1").innerHTML = recupTitle1(valueSearchBar,start_date,end_date);
    $.ajax({
      //url:'http://130.120.8.250:5000/article_per_day_source' + '/' + valueSearchBar + '/' + start_date_ajax + '/' + end_date_ajax,
      url:'http://localhost:5000/article_per_day_source' + '/' + valueSearchBar + '/' + start_date_ajax + '/' + end_date_ajax,
      type: 'GET',
      dataType: 'json',
      success: Graph1,
      error: ajax_failed,
    });
    document.getElementById("title2").innerHTML = recupTitle2(valueSearchBar,start_date,end_date);
    $.ajax({
      //url:'http://130.120.8.250:5000/article_per_day_label' + '/' + valueSearchBar + '/' + start_date_ajax + '/' + end_date_ajax,
      url:'http://localhost:5000/article_per_day_label' + '/' + valueSearchBar + '/' + start_date_ajax + '/' + end_date_ajax,
      type: 'GET',
      dataType: 'json',
      success: Graph2,
      error: ajax_failed,
    });
    document.getElementById("title3").innerHTML = recupTitle3(valueSearchBar,start_date,end_date);
    $.ajax({
      //url:'http://130.120.8.250:5000/article_per_source' + '/' + valueSearchBar + '/' + start_date_ajax + '/' + end_date_ajax,
      url:'http://localhost:5000/article_per_source' + '/' + valueSearchBar + '/' + start_date_ajax + '/' + end_date_ajax,
      type: 'GET',
      dataType: 'json',
      success: Graph3,
      error: ajax_failed,
    });
    document.getElementById("title4").innerHTML = recupTitle4(valueSearchBar,start_date,end_date);
    $.ajax({
      //url:'http://130.120.8.250:5000/article_per_label' + '/' + valueSearchBar + '/' + start_date_ajax + '/' + end_date_ajax,
      url:'http://localhost:5000/article_per_label' + '/' + valueSearchBar + '/' + start_date_ajax + '/' + end_date_ajax,
      type: 'GET',
      dataType: 'json',
      success: Graph4,
      error: ajax_failed,
    });
    document.getElementById("title5").innerHTML = recupTitle5(valueSearchBar,start_date,end_date);
    $.ajax({
      //url:'http://130.120.8.250:5000/article_per_day' + '/' + valueSearchBar + '/' + start_date_ajax + '/' + end_date_ajax,
      url:'http://localhost:5000/article_per_day' + '/' + valueSearchBar + '/' + start_date_ajax + '/' + end_date_ajax,
      type: 'GET',
      dataType: 'json',
      success: Graph5,
      error: ajax_failed,
    });
    document.getElementById("title6").innerHTML = recupTitle6(valueSearchBar,start_date,end_date);
    $.ajax({
      //url:'http://130.120.8.250:5000/positivity_per_newspaper' + '/' + valueSearchBar + '/' + start_date_ajax + '/' + end_date_ajax,
      url:'http://localhost:5000/positivity_per_newspaper' + '/' + valueSearchBar + '/' + start_date_ajax + '/' + end_date_ajax,
      type: 'GET',
      dataType: 'json',
      success: Graph6,
      error: ajax_failed,
    });
  }
});



/*Création des titres*/
function recupTitle1(word,start,end){  return "Evolution du nombre d'article utilisant le mot " + word + " par jour et par sources entre le " + start + " et le " + end;}
function recupTitle2(word,start,end){  return "Evolution du nombre d'article utilisant le mot " + word + " par jour et par thèmes entre le " + start + " et le " + end;}
function recupTitle3(word,start,end){  return "Nombre d'utilisation du mot " + word + " par sources entre le " + start + " et le " + end;}
function recupTitle4(word,start,end){  return "Nombre d'utilisation du mot " + word + " par thèmes entre le " + start + " et le " + end;}
function recupTitle5(word,start,end){  return "Evolution du nombre d'article utilisant le mot " + word + " par jour entre le " + start + " et le " + end;}
function recupTitle6(word,start,end){  return "Score de polarité du mot " + word + " par sources par jour entre le " + start + " et le " + end;}


/*Création des graphiques*/
function Graph1(json_graph1) {
  google.charts.load('visualization', '1', {'packages':['corechart']});
  google.charts.setOnLoadCallback(function(){
    var data = new google.visualization.DataTable();    
    var week=json_graph1[1].date;
    var col=0;
    data.addColumn('string', 'source');
    for (var g = 1; g <=Object.keys(json_graph1).length; g++) {
      if (json_graph1[g].date==week){
        data.addColumn('number', json_graph1[g].newspaper); //add every distinct sources present in the Json into column
        col=col+1;
      }
    }
    for (var i = 1; i <=Object.keys(json_graph1).length; i+=col) {
      var tab = [json_graph1[i].date];
      for (var j = 0; j < col; j++) { //create a table proportional to the number of sources selected
        tab.splice(j+1, 0, json_graph1[j+i].number_article);
      }
     data.addRow(tab); //add the table to generate the lines
    }
    var options = {
      curveType: 'function',
      backgroundColor: 'transparent',
      legend: { position: 'bottom' }};
    var chart = new google.visualization.LineChart(document.getElementById('chart1_div_research'));
    $("#chart1_div_research").show();
    chart.draw(data,options);
      $(window).resize(function(){ //make the graphics responsive
        chart.draw(data,options);
     });
  });
}

function Graph2(json_graph2) {
  google.charts.load('visualization', '1', {'packages':['corechart']});
  google.charts.setOnLoadCallback(function(){
    var data = new google.visualization.DataTable();    
    var week=json_graph2[1].date;
    var col=0;
    data.addColumn('string', 'theme');
    for (var g = 1; g <=Object.keys(json_graph2).length; g++) {
      if (json_graph2[g].date==week){
        data.addColumn('number', json_graph2[g].label); //add every distinct sources present in the Json into column
        col=col+1;
      }
    }
    for (var i = 1; i <=Object.keys(json_graph2).length; i+=col) {
      var tab = [json_graph2[i].date];
      for (var j = 0; j < col; j++) { //create a table proportional to the number of sources selected
        tab.splice(j+1, 0, json_graph2[j+i].number_article);
      }
     data.addRow(tab); //add the table to generate the lines
    }
    var options = {
      curveType: 'function',
      backgroundColor: 'transparent',
      legend: { position: 'bottom' }};
    var chart = new google.visualization.LineChart(document.getElementById('chart2_div_research'));
    $("#chart2_div_research").show();
    chart.draw(data,options);
      $(window).resize(function(){ //make the graphics responsive
        chart.draw(data,options);
     });
  });
}


function Graph3(json_graph3){
  google.charts.load('current', {packages: ['corechart', 'bar']});
  google.charts.setOnLoadCallback(function(){
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'source');
    data.addColumn('number', "nombre");
    for (var i = 1; i <Object.keys(json_graph3).length; i++) {
    data.addRow([json_graph3[i].newspaper,json_graph3[i].number_article ]);
    }
    var options = {
      backgroundColor: 'transparent',
      legend: {position: 'none'}};
    var chart = new google.visualization.ColumnChart(
    document.getElementById('chart3_div_research'));
    chart.draw(data,options);
    $(window).resize(function(){ //make the graphics responsive
      chart.draw(data,options);
    });
    $("#chart3_div_research").show();
  });
}

function Graph4(json_graph4){
  google.charts.load('current', {packages: ['corechart', 'bar']});
  google.charts.setOnLoadCallback(function(){
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'theme');
    data.addColumn('number', "nombre");
    for (var i = 1; i <Object.keys(json_graph4).length; i++) {
    data.addRow([json_graph4[i].label,json_graph4[i].number_article ]);
    }
    var options = {
      backgroundColor: 'transparent',
      legend: {position: 'none'}};
    var chart = new google.visualization.ColumnChart(
    document.getElementById('chart4_div_research'));
    chart.draw(data,options);
    $(window).resize(function(){ //make the graphics responsive
      chart.draw(data,options);
    });
    $("#chart4_div_research").show();
  });
}

function Graph5(json_graph5) {
  google.charts.load('visualization', '1', {'packages':['corechart']});
  google.charts.setOnLoadCallback(function(){
    var data = new google.visualization.DataTable();    
    data.addColumn('string', 'periode');
    data.addColumn('number', "nombre");
    for (var i = 1; i <= Object.keys(json_graph5).length; i++) {
    data.addRow([json_graph5[i].date,json_graph5[i].number_article ]);
    }
    var options = {
      curveType: 'function',
      backgroundColor: 'transparent',
      legend: { position: 'bottom' }};
    var chart = new google.visualization.LineChart(document.getElementById('chart5_div_research'));
    $("#chart5_div_research").show();
    chart.draw(data,options);
      $(window).resize(function(){ //make the graphics responsive
        chart.draw(data,options);
     });
  });
}

function Graph6(json_graph6){
  google.charts.load('current', {packages: ['corechart', 'bar']});
  google.charts.setOnLoadCallback(function(){
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'source');
    data.addColumn('number', "polarite");
    for (var i = 1; i < Object.keys(json_graph6).length; i++) {
    	data.addRow([json_graph6[i].source,json_graph6[i].polarite]);
    }
    var options = {
      backgroundColor: 'transparent',
      legend: {position: 'none'}};
    var chart = new google.visualization.ColumnChart(
    document.getElementById('chart6_div_research'));
    chart.draw(data,options);
    $(window).resize(function(){ //make the graphics responsive
      chart.draw(data,options);
    });
    $("#chart6_div_research").show();
  });
}


function ajax_failed() {
    alert('Essayez un autre mot');
}
