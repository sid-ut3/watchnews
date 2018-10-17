// LC, SD, TR, FGD
/* 
THEME JS PAGE
SERIGNE DIAW, LUCAS CLOCHARD AND THOMAS ROY
WATCH NEWS PROJECT 2017/2018
*/

/**/
function start() {
	request_number_article_theme();
	request_word_trend();
	request_word_cloud_theme();
}

/* Calling json data for graphing (bar chart of the number of articles by theme) */
function request_number_article_theme() {
	$.ajax({
		//url:'http://130.120.8.250:5000/newspaper_by_label',
		url:'http://127.0.0.1:5000/newspaper_by_label',
		type: 'GET',
		dataType: 'json',
		success: draw_number_article_theme,
		error: ajax_failed,
	});
}

/* Calling json data for graphing (most associated table of words (verb, noun, adjective) and their tendency) */
function request_word_trend() {
	$( ".radio" ).click(function() {
		var theme = $(this).attr('id');
		$.ajax({
			//url:'http://130.120.8.250:5000/link_by_tagging/'+theme,
			url:'http://127.0.0.1:5000/link_by_tagging/'+theme,
			type: 'GET',
			dataType: 'json',
			success: draw_word_trend,
			error: ajax_failed,
		});
	});
}
/* Calling json data for graphing (draw the word cloud of the most represented words by theme
									and specifies the color according to their trend) */
function request_word_cloud_theme() {
	$( ".radio" ).click(function() {
		var theme = $(this).attr('id');
		$.ajax({
			//url:'http://130.120.8.250:5000/link_by_label'+theme,
			url:'http://127.0.0.1:5000/link_by_label/'+theme,
			type: 'GET',
			dataType: 'json',
			success: draw_word_cloud_trend,
			error: ajax_failed,
		});
	});
}

/* parameterized function of making bar chart graph using google chart: 
   this function takes as input a json variable and then transforms it 
   into a table according to the inputs of the google chart functions
   Remarqs : This is valid for the above functions
 */
function draw_number_article_theme(data_json_most_treated_themes) {
	$("#3_main_words_article_theme").hide();
	google.charts.load('visualization', '1', {packages: ['corechart']});
	google.charts.setOnLoadCallback(function(){
		// Data table creation with the json file received
    	var tab = new Array(['Theme','Effectif']);
		for (var i = 1; i <=Object.keys(data_json_most_treated_themes).length; i++) {
			tab[i] = [data_json_most_treated_themes[i].label, data_json_most_treated_themes[i].number_article];
		}
		var data = new google.visualization.arrayToDataTable(tab);
		var options = {   
        	hAxis : {
          	minValue: 0
        	},
        	bar: {groupWidth: "95%"},
        	legend: { position: "none" },
        	backgroundColor: {fill: 'transparent'}
		};
		// Conversion of the table into a horizontal bar graph
		var chart = new google.visualization.BarChart(document.getElementById("series_chart_theme"));
		chart.draw(data, options);
		// Adaptation of the graph size depending on the window size
		$(window).resize(function(){
			chart.draw(data, options);
		});
	});
	$("#most_treated_theme_article_theme").show();
}

/* parameterized function of making the table of the most associated words graph using google chart */
function draw_word_trend(data_json_trend_themes) {
	$("#most_treated_theme_article_theme").hide();
	google.charts.load('visualization', '1', {packages: ['table']});
	google.charts.setOnLoadCallback(function(){
    	var options = {
      		width: '100%',
      		height: '100%',
      		backgroundColor: {fill: 'transparent'}
    	};
    	// Specification off words trend whom will be written in the table
    	var trend_translated = {
  			'Strongly_increasing_trend': 'En très forte hausse',
  			'Increasing_trend': 'En hausse',
  			'No_trend': 'Stagnante',
  			'Decreasing_trend': 'En baisse',
  			'Strongly_decreasing_trend': 'En très forte baisse'
		};
		// Table created with json data
    	var tab = new Array(['Mots liés au thème',  'Tendance']);
		for (var i = 1; i <=Object.keys(data_json_trend_themes).length; i++) {
			var json_trend = data_json_trend_themes[i].trend;
			tab[i] = [data_json_trend_themes[i].text, trend_translated[json_trend]];
		}
    	var data = google.visualization.arrayToDataTable(tab);
    	var table = new google.visualization.Table(document.getElementById('table_div'));
    	table.draw(data, options);
    	// Adaptation of the table size depending on the window size
    	$(window).resize(function(){
			table.draw(data, options);
		});
	});
	$("#3_main_words_article_theme").show();
}

/* parameterized function of making the word cloud */
function draw_word_cloud_trend(some_words) {
	$("div.modal-bg").removeClass("hide");
	$("#most_treated_theme_article_theme").hide();
	// Table created with json data
	var tab = [];
	for (var i = 1; i <Object.keys(some_words).length+1; i++) {
		tab = tab.concat(some_words[i]);
	}
	// Add colors legend for the word cloud tendency
	var trend_colors = {
  		'Strongly_increasing_trend': '#32CD32',
  		'Increasing_trend': '#7FFF00',
  		'No_trend': '#FFD700',
  		'Decreasing_trend': '#FF4500',
  		'Strongly_decreasing_trend': '#B22222'
	};
	// Replace the trend color in our table data by its associated color
	var colored_tab = [];
	for (var i = 0;i<7;i++){
  		var color = tab[i].trend;
  		colored_tab = colored_tab.concat({text : tab[i].text, weight : tab[i].weight, color : trend_colors[color]});
	}
	$(".world_cloud_div_theme").jQCloud(colored_tab, {
		autoResize: true
	});
	$(document).ready(function() {
		// Printing of the word cloud with trend colors
		$(".world_cloud_div_theme").jQCloud('update', colored_tab, {
			autoResize: true
		});
		var obj = $(".world_cloud_div_theme").data("jqcloud");
    	var data = obj.word_array;
    	for (var i in data) {
        	$("#" + data[i]["attr"]["id"]).css("color", data[i]["color"]);
    	}
    	// Adaptation of the word cloud size depending on the window size
		$(window).on('resize',function(){
			$(".world_cloud_div_theme").jQCloud('update', colored_tab, {
				autoResize: true
			});
			var obj = $(".world_cloud_div_theme").data("jqcloud");
    		var data = obj.word_array;
    		for (var i in data) {
        		$("#" + data[i]["attr"]["id"]).css("color", data[i]["color"]);
    		}
		});
	});
	$('#most_treated_word_article_theme').show();
}

/* Failed error message */
function ajax_failed() {
	alert('erreur');
}
