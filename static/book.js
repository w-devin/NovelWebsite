/*
    Render the book's information to the page
*/

  $(document)
    .ready(function() {
      $.get('book/all', function(data){
        var res = data.res;
        $('#all_book div.ui.segment div.item')
            .each(function(i){
                var info = JSON.parse(res[i]);
                var _this = $(this);
                _this.find('img')[0].src = info.cover;
//                _this.find('a')[0].innerHTML = info.name;
                _this.find('a')[0].innerHTML = '书名: ' + info.name;
                _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                _this.find('.description')[0].innerHTML = '简介: ' + info.description;
                _this.find('.button')[0].innerHTML = "<a href='" + info.link + "'>点击阅读</a>";
            })
          ;
        })
      ;
      $.get('book/finished', function(data){
        var res = data.res;
        $('#finished_book div.ui.segment div.item')
            .each(function(i){
                var info = JSON.parse(res[i]);
                var _this = $(this);
                _this.find('img')[0].src = info.cover;
//                _this.find('a')[0].innerHTML = info.name;
                _this.find('a')[0].innerHTML = '书名: ' + info.name;
                _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                _this.find('.description')[0].innerHTML = '简介: ' + info.description;
                _this.find('.button')[0].innerHTML = "<a href='" + info.link + "'>点击阅读</a>";
            })
          ;
        })
      ;
    })
  ;



