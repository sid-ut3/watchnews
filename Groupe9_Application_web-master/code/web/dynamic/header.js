// KB, PSB, FGD
/*fonction servant a inserer le header dans l'ensemble des pages du site. Permet d'actualiser tous les headers en meme temps.*/
/*utilise le lien vers bootstrap de chaque page */

document.body.insertAdjacentHTML("afterBegin",
  '<header>'+
    '<nav class="navbar navbar-default">'+ 

    /*Navigation bar*/    
      '<div id = "navBar" class="container">'+
        '<div class="navbar-header">'+
          '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#codebrainery-toggle-nav" aria-expanded="false">'+
            '<span class="sr-only">Toggle navigation </span>'+
            '<span class="icon-bar"></span>'+
            '<span class="icon-bar"></span>'+
            '<span class="icon-bar"></span>'+
          '</button>'+
        '<img src="https://raw.githubusercontent.com/ProjetSID2018/Groupe10_Qualite_communication/master/Logos/bleu1.png" class="navbar-brand"></img>'+
        '</div>'+
        '<div class="collapse navbar-collapse" id="codebrainery-toggle-nav">'+
          '<ul class="nav navbar-nav navbar-right">'+
            '<li class="item"><a class="a.a-nav" href="index.html">Accueil</a></li>'+
            '<li class="item"><a class="a.a-nav" href="theme.html">Thèmes</a></li>'+
            '<li class="item"><a class="a.a-nav" href="search_page.html">Recherche</a></li>'+
          '</ul>'+
        '</div>'+
      '</div>'+

    /*Search bar*/
      '<div id ="searchBar" class="container">'+
        '<div class="navbar-header">'+
          '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#codebrainery-toggle-search" aria-expanded="false">'+
            '<span class="glyphicon glyphicon-search"></span>'+
          '</button>' +
          '<div id="codebrainery-toggle-search" class="collapse navbar-collapse">' +
            '<div class="col-lg-offset-3">'+
            // '<div>'+
              '<div class="row">' +
                '<div id="prefetch" class="col-xs-offset-4 col-xs-8 col-sm-offset-4 col-sm-8 col-md-offset-4 col-md-8 col-lg-offset-4 col-lg-8">' +
                  '<input id="searchBar_input_research" type="text" class="typeahead" placeholder="Recherche">' +
                '</div>' +
              '</div>'+

              '<div class="row">' +
                '<div class="col-xs-4 col-sm-4 col-md-4 col-lg-4">' +
                  '<div class="form-group">' +
                    '<div class="input-group date" >' +
                      '<input type="text" class="form-control" id="startDate_input_research" style="cursor: pointer" onclick="new calendar(this);" value="Du :">' +
                      '<span class="input-group-addon">' +
                        '<span class="glyphicon glyphicon-calendar"></span>' +
                      '</span>' +
                    '</div>' +
                  '</div>' +    
                '</div>' +
                '<div class="col-xs-4 col-sm-4 col-md-4 col-lg-4">' +
                  '<div class="form-group">' +
                    '<div class="input-group date" >' +
                      '<input type="text" class="form-control" id="endDate_input_research" style="cursor: pointer" onclick="new calendar(this);" value="Au :">' +
                      '<span class="input-group-addon">' +
                        '<span class="glyphicon glyphicon-calendar"></span>' +
                      '</span>' +
                    '</div>' +
                  '</div>' +    
                '</div>' +
                '<div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">' +
                  '<button id="buttonCancel_input_research" type="submit" class="btn btn-primary" onclick="window.location.relo2d(false)">Réinitialiser</button>'+
                '</div>' +
                '<div class="col-xs-2 col-sm-2 col-md-2 col-lg-2">' +
                  '<button id="buttonResearch_input_research" type="submit" class="btn btn-primary">Valider</button>' +
                '</div>'  +
              '</div>' +
            '</div>'+
          '</div>'+   
        '</div>'+
      '</div>' +

    /*Theme choice*/ 

      '<div id = "themeBar" class = "container">' +
        '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#codebrainery-toggle-theme" aria-expanded="false">'+
          '<span class="glyphicon glyphicon-search"></span>'+
        '</button>' +
        '<div id="codebrainery-toggle-theme" class="collapse navbar-collapse">' +
          '<div class="navbar-header" id="container2_div_theme">' +
            '<h5>' +
              'Choisissez votre theme' +
            '</h5>' +
            '<div id="list_theme_div_theme" class="row">' +
              '<form>' +
                '<div class="col-sm-2" + id="_international" value="_international">' +
                  '<label><input id="_international" class="radio" type="radio" name="optradio">International</label>' +
                '</div>' +
                '<div class="col-sm-2" id="_france">' +
                  '<label><input id="_france" class="radio" type="radio" name="optradio">France</label>' +
                '</div>' +
                '<div class="col-sm-2" id="_economie">' +
                  '<label><input id="_economie" class="radio" type="radio" name="optradio">&Eacute;conomie</label>' +
                '</div>' +
                '<div class="col-sm-2" id="_sciences_high_tech">' +
                  '<label><input id="_sciences_high_tech" class="radio" type="radio" name="optradio">Science/High-tech</label>' +
                '</div>' +
                '<div class="col-sm-2" id="_arts_et_culture">' +
                  '<label><input id="_arts_et_culture" class="radio" type="radio" name="optradio">Art et Culture</label>' +
                '</div>' +
                '<div class="col-sm-1" id="_sports">' +
                  '<label><input id="_sports" class="radio" type="radio" name="optradio">Sports</label>' +
                '</div>'+
                '<div class="col-sm-1" id="_sante">' +
                   '<label><input id="_sante" class="radio" type="radio" name="optradio">Sant&eacute;</label>' +
                '</div>' +
              '</form>' +
            '</div>' +
          '</div>' +
        '</div>' +
      '</div>' +
      
    '</nav>'+
  '</header>');
