/*
    Render the book's information to the page
*/

  $(document)
    .ready(function() {

      /*搜索图书Button的响应*/
      $('#search').on('click', function(){
        var key = $('#key').val();
        window.location.href = 'search?keyword=' + key;
      });

      /*获取所有图书的信息并进行渲染*/
      $.get('book/all', function(data){
        var res = data.res;
        $('#all_book div.ui.segment div.item')
            .each(function(i){
                var info = JSON.parse(res[i]);
                var _this = $(this);
                _this.find('img')[0].src = info.cover;
//                _this.find('a')[0].innerHTML = info.name;
                _this.find('a')[0].innerHTML = info.name;
                _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                _this.find('.description')[0].innerHTML = '简介: ' + handle_des(info.description);
                _this.find('.button')[0].innerHTML = "<a href='" + info.link + "'>点击阅读</a>";
            })
          ;
        })
      ;

      /*获取每种类型图书排名前12的图书的信息并进行渲染*/
      var catagory_array = ["科幻灵异", "玄幻奇幻", "网游竞技", "武侠仙侠", "都市言情", "历史军事", "同人小说", "女生频道"];
      // 提前渲染一开始可见的部分
      $.get('book/order/1', function(data){
        var res = data.res;
        $('#order_book div.ui.segment div.item')
            .each(function(i){
                var info = JSON.parse(res[i]);
                var _this = $(this);
                _this.find('img')[0].src = info.cover;
                _this.find('a')[0].innerHTML = info.name;
                _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                _this.find('.description')[0].innerHTML = '简介: ' + info.description;
                _this.find('.button')[0].innerHTML = "<a href='" + info.link + "'>点击阅读</a>";
            })
          ;
        })
      ;
      $('.ui.container .ui.menu a.item')
        .on('click', function() {
          $(this)
            .addClass('active')
            .siblings()
            .removeClass('active')
          ;
          var _this = $(this)[0];
          var catagory = _this.innerHTML;
          var pos = $.inArray(catagory,catagory_array);
          if(pos!=-1){
            var index = pos + 1;
              $.get('book/order/' + index, function(data){
                var res = data.res;
                $('#order_book div.ui.segment div.item')
                    .each(function(i){
                        var info = JSON.parse(res[i]);
                        var _this = $(this);
                        _this.find('img')[0].src = info.cover;
        //                _this.find('a')[0].innerHTML = info.name;
                        _this.find('a')[0].innerHTML = info.name;
                        _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                        _this.find('.description')[0].innerHTML = '简介: ' + info.description;
                        _this.find('.button')[0].innerHTML = "<a href='" + info.link + "'>点击阅读</a>";
                    })
                  ;
                })
              ;
          }
        })
      ;

      /*获取完本图书的信息并进行渲染*/
      $.get('book/finished', function(data){
        var res = data.res;
        $('#finished_book div.ui.segment div.item')
            .each(function(i){
                var info = JSON.parse(res[i]);
                var _this = $(this);
                _this.find('img')[0].src = info.cover;
//                _this.find('a')[0].innerHTML = info.name;
                _this.find('a')[0].innerHTML = info.name;
                _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                _this.find('.description')[0].innerHTML = '简介: ' + info.description;
                _this.find('.button')[0].innerHTML = "<a href='" + info.link + "'>点击阅读</a>";
            })
          ;
        })
      ;
    })
  ;



