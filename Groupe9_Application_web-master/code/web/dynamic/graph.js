// MV, VF, MD, FGD
var compt=0;

function start() {
	request_top_10();
    request_word_cloud();
    request_top_theme();
    request_gauge();
}

function request_top_10() {
	$('#top10_sources').hide();
    	$.ajax({
        	//url:'http://130.120.8.250:5000/newspaper_by_article/',
        	url:'http://localhost:5000/newspaper_by_article',
        	type: 'GET',
        	dataType: 'json',
        	success: drawBasic,
        	error: ajax_failed,
	});
}

function request_word_cloud() {
    $('#word_cloud_cover').hide();
    $.ajax({
        //url:'http://130.120.8.250:5000/Top10_pertinent',
        url:'http://localhost:5000/test1',
        type: 'GET',
        dataType: 'json',
        success: draw_cloud,
        error: ajax_failed,
    });
}

function request_top_theme() {
    $('#most_popular_theme').hide();
    $.ajax({
        //url:'http://130.120.8.250:5000/best_label_week',
        url:'http://localhost:5000/best_label_week',
        type: 'GET',
        dataType: 'json',
        success: top_theme,
        error: ajax_failed,
    });
}

function request_gauge() {
    $.ajax({
        //url:'/top_3_rate_feeling',
        url:'http://localhost:5000/top_3_rate_feeling',
        type: 'GET',
        dataType: 'json',
        success: draw_gauge,
        error: ajax_failed,
    });
}


function drawBasic(data_json) {
	google.charts.load('visualization', '1', {packages: ['corechart', 'bar']});
	google.charts.setOnLoadCallback(function(){
		var data = new google.visualization.DataTable();
		data.addColumn("string", "sources");
    		data.addColumn("number", "nombres d'articles");
    		for (var i = 1; i <=10; i++) {
    			data.addRow([data_json[i].newspaper,data_json[i].number_article]);
		}
		var options = {
    		hAxis: {
        		title: 'sources',
        		format: 'string',
			},
        	vAxis: {
        		title: "nombres d'articles par source"
			},
			backgroundColor: 'transparent'
		};
		var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
		$('#top10_sources').show();
		chart.draw(data, options);
		$(window).resize(function(){
			chart.draw(data, options);
		});
	});
	draw_table(data_json);
}

function draw_table(data_json) {
   var length = data_json.length;
   for (var i = 1; i <=Object.keys(data_json).length; i++) {
       document.getElementById('table_source_body').insertAdjacentHTML("beforeEnd",'<tr><td>'+data_json[i].newspaper+'</td> <td>'+data_json[i].number_article+'</td></tr>');
   }
}

function draw_cloud(some_words) {
	  $('#word_cloud_cover').show();
    var tab = [];
    for (var i = 1; i <Object.keys(some_words).length+1; i++) {
        tab = tab.concat(some_words[i]);
    }
		var trend_colors = {
	  		'Strongly_increasing_trend': '#32CD32',
	  		'Increasing_trend': '#7FFF00',
	  		'No_trend': '#FFD700',
	  		'Decreasing_trend': '#FF4500',
	  		'Strongly_decreasing_trend': '#B22222'
		};
    var colored_tab = [];
    for (var i = 0;i<7;i++){
        var color = tab[i].trend;
        colored_tab = colored_tab.concat({text : tab[i].text, weight : tab[i].weight, color : trend_colors[color]});
    }
    $(".word_cloud_row_graph").jQCloud(colored_tab);
    $(document).ready(function() {
        setTimeout(function () {
            var obj = $(".word_cloud_row_graph").data("jqcloud");
            var data = obj.word_array;
            for (var i in data) {
                $("#" + data[i]["attr"]["id"]).css("color", data[i]["color"]);
            }
        });
    });
}

function top_theme(theme_pourcent) {
    $('#most_popular_theme').show();
    document.getElementById("most_popular_theme_pourcentage").textContent = theme_pourcent[1].ratio_article;
    document.getElementById("most_popular_theme_name").textContent = theme_pourcent[1].label;
}

function draw_gauge(data_gauge) {
	var title1 = data_gauge[1].feeling;
	var title2 = data_gauge[2].feeling;
	var title3 = data_gauge[3].feeling;
	var pourcent1 = data_gauge[1].rate*100;
	var pourcent2 = data_gauge[2].rate*100;
	var pourcent3 = data_gauge[3].rate*100;
	gauge(title1,title2,title3,pourcent1,pourcent2,pourcent3);
}

function gauge(title1,title2,title3,pourcent1,pourcent2,pourcent3) {
    var g1 = new JustGage({
        id: "g1",
        value: pourcent1,
        min: 0,
        max: 100,
        title: title1,
        label: "%"
    });

    var g2 = new JustGage({
        id: "g2",
        value: pourcent2,
        min: 0,
        max: 100,
        title: title2,
        label: "%"
    });

    var g3 = new JustGage({
        id: "g3",
        value: pourcent3,
        min: 0,
        max: 100,
        title: title3,
        label: "%"
    });
}

function ajax_failed() {
    compt+=1;
    if ( compt == 3){
        alert('erreur')
    };
}
