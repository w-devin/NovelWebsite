/*
    Render the book's information to the page
*/

  $(document)
    .ready(function() {
      var catagory_array = ["科幻灵异", "玄幻奇幻", "网游竞技", "武侠仙侠", "都市言情", "历史军事", "同人小说", "女生频道", "全部小说"];

      /* 返回主页*/
      $('#return_index').on('click', function(){
        window.location.href = "/";
      });
      /*
        页面跳转
      */
      // 上一页
      $('#last_page').on('click', function(){
        var _this = $($(this)[0]);
        var page = Number(_this.attr('data'));
        var mark = $('#redirect_page').attr('data');
        if(page == 1)
            return;
        else{
          page = page - 1;
          $('#page_num').val(page);
          _this.attr('data', page);
          $('#next_page').attr('data', page);
          if(mark == 'all'){
            /*获取所有图书的信息并进行渲染*/
              $.get('book/all/' + page, function(data){
                var res = data.res;
                if(res.length < 12){
                    return;
                }
                $('#all_book div.ui.segment div.item')
                    .each(function(i){
                        var info = JSON.parse(res[i]);
                        var _this = $(this);
                        if(info.cover == null){
                            info.cover = "https://www.qu.la/BookFiles/BookImages/zhongshengzhiguiwangguilai.jpg";
                        }
                        if(info.link == null){
                            info.link = "book/";
                        }
                        if(info.description == null){
                            info.description = "暂无";
                        }
                        _this.find('img')[0].src = info.cover;
        //                _this.find('a')[0].innerHTML = info.name;
                        _this.find('a')[0].innerHTML = info.name;
                        _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                        _this.find('.description')[0].innerHTML = '简介: ' + handle_des(info.description);
                        _this.find('.button')[0].innerHTML = "<a href='read/" + info.link + "'>点击阅读</a>";
                    })
                  ;
                })
              ;
            }else{
              /*获取完本图书的信息并进行渲染*/
              $.get('book/finished/' + page, function(data){
                var res = data.res;
                if(res.length < 12){
                    return;
                }
                $('#finished_book div.ui.segment div.item')
                    .each(function(i){
                        var info = JSON.parse(res[i]);
                        var _this = $(this);
                        if(info.cover == null){
                            info.cover = "https://www.qu.la/BookFiles/BookImages/zhongshengzhiguiwangguilai.jpg";
                        }
                        if(info.link == null){
                            info.link = "book/";
                        }
                        if(info.description == null){
                            info.description = "暂无";
                        }
                        _this.find('img')[0].src = info.cover;
        //                _this.find('a')[0].innerHTML = info.name;
                        _this.find('a')[0].innerHTML = info.name;
                        _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                        _this.find('.description')[0].innerHTML = '简介: ' + handle_des(info.description);
                        _this.find('.button')[0].innerHTML = "<a href='read" + info.link + "'>点击阅读</a>";
                    })
                  ;
                })
              ;
            }
        }
      });
      // 跳转
      $('#redirect_page').on('click', function(){
        var _this = $($(this)[0]);
        var mark = _this.attr('data');
        var page = $('#page_num').val();
        if(page == "" || page < 1){
            return;
        }else{
          _this.attr('data', page);
          if(mark == 'all'){
            /*获取所有图书的信息并进行渲染*/
              $.get('book/all/' + page, function(data){
                var res = data.res;
                if(res.length < 12){
                    return;
                }
                $('#last_page').attr('data', page);
                $('#next_page').attr('data', page);
                $('#all_book div.ui.segment div.item')
                    .each(function(i){
                        var info = JSON.parse(res[i]);
                        var _this = $(this);
                        if(info.cover == null){
                            info.cover = "https://www.qu.la/BookFiles/BookImages/zhongshengzhiguiwangguilai.jpg";
                        }
                        if(info.link == null){
                            info.link = "book/";
                        }
                        if(info.description == null){
                            info.description = "暂无";
                        }
                        _this.find('img')[0].src = info.cover;
        //                _this.find('a')[0].innerHTML = info.name;
                        _this.find('a')[0].innerHTML = info.name;
                        _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                        _this.find('.description')[0].innerHTML = '简介: ' + handle_des(info.description);
                        _this.find('.button')[0].innerHTML = "<a href='read" + info.link + "'>点击阅读</a>";
                    })
                  ;
                })
              ;
            }else{
              /*获取完本图书的信息并进行渲染*/
              $.get('book/finished/' + page, function(data){
                var res = data.res;
                if(res.length < 12){
                    return;
                }
                $('#finished_book div.ui.segment div.item')
                    .each(function(i){
                        var info = JSON.parse(res[i]);
                        var _this = $(this);
                        $('#last_page').attr('data', page);
                        $('#next_page').attr('data', page);
                        if(info.cover == null){
                            info.cover = "https://www.qu.la/BookFiles/BookImages/zhongshengzhiguiwangguilai.jpg";
                        }
                        if(info.link == null){
                            info.link = "book/";
                        }
                        if(info.description == null){
                            info.description = "暂无";
                        }
                        _this.find('img')[0].src = info.cover;
        //                _this.find('a')[0].innerHTML = info.name;
                        _this.find('a')[0].innerHTML = info.name;
                        _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                        _this.find('.description')[0].innerHTML = '简介: ' + handle_des(info.description);
                        _this.find('.button')[0].innerHTML = "<a href='read" + info.link + "'>点击阅读</a>";
                    })
                  ;
                })
              ;
            }
        }
      });
      // 下一页
      $('#next_page').on('click', function(){
        var _this = $($(this)[0]);
        var page = Number(_this.attr('data'));
        var mark = $('#redirect_page').attr('data');
        console.log(mark);
        if(page > 100000)
            return;
        else{
          page = page + 1;
          $('#page_num').val(page);
          _this.attr('data', page);
          $('#last_page').attr('data', page);
          if(mark == 'all'){
            /*获取所有图书的信息并进行渲染*/
              $.get('book/all/' + page, function(data){
                var res = data.res;
                if(res.length < 12){
                    return;
                }
                $('#all_book div.ui.segment div.item')
                    .each(function(i){
                        var info = JSON.parse(res[i]);
                        var _this = $(this);
                        if(info.cover == null){
                            info.cover = "https://www.qu.la/BookFiles/BookImages/zhongshengzhiguiwangguilai.jpg";
                        }
                        if(info.link == null){
                            info.link = "book/";
                        }
                        if(info.description == null){
                            info.description = "暂无";
                        }
                        _this.find('img')[0].src = info.cover;
                        _this.find('a')[0].innerHTML = info.name;
                        _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                        _this.find('.description')[0].innerHTML = '简介: ' + handle_des(info.description);
                        _this.find('.button')[0].innerHTML = "<a href='read" + info.link + "'>点击阅读</a>";
                    })
                  ;
                })
              ;
            }else{
              /*获取完本图书的信息并进行渲染*/
              $.get('book/finished/' + page, function(data){
                var res = data.res;
                if(res.length < 12){
                    return;
                }
                $('#finished_book div.ui.segment div.item')
                    .each(function(i){
                        var info = JSON.parse(res[i]);
                        var _this = $(this);
                        if(info.cover == null){
                            info.cover = "https://www.qu.la/BookFiles/BookImages/zhongshengzhiguiwangguilai.jpg";
                        }
                        if(info.link == null){
                            info.link = "book/";
                        }
                        if(info.description == null){
                            info.description = "暂无";
                        }
                        _this.find('img')[0].src = info.cover;
        //                _this.find('a')[0].innerHTML = info.name;
                        _this.find('a')[0].innerHTML = info.name;
                        _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                        _this.find('.description')[0].innerHTML = '简介: ' + handle_des(info.description);
                        _this.find('.button')[0].innerHTML = "<a href='read" + info.link + "'>点击阅读</a>";
                    })
                  ;
                })
              ;
            }
        }
      });


      /*搜索图书下拉框的响应*/
      $('#search').on('click', function(){
        var key = $('#key').val();
        window.location.href = 'search?keyword=' + key;
      });

      /*图书分类的下拉菜单的响应*/
      $('#catagory_menu div.item').on('click', function(){
          $('#all_index').trigger("click");
          var _this = $(this)[0];
          var catagory = _this.innerHTML;
          var pos = $.inArray(catagory,catagory_array);
          if(catagory == '全部小说')
            pos = 8;
          if(pos!=-1){
            var index = pos;
              $.get('book/catagory/' + index + "/" + $('#page_num').val(), function(data){
                var res = data.res;
                if(res.length < 12){
                    return;
                }
                $('#all_book div.ui.segment div.item')
                    .each(function(i){
                        var info = res[i];
                        var _this = $(this);
                        if(info.cover == null){
                            info.cover = "https://www.qu.la/BookFiles/BookImages/zhongshengzhiguiwangguilai.jpg";
                        }
                        if(info.link == null){
                            info.link = "book/";
                        }
                        if(info.description == null){
                            info.description = "暂无";
                        }
                        _this.find('img')[0].src = info.cover;
        //                _this.find('a')[0].innerHTML = info.name;
                        _this.find('a')[0].innerHTML = info.name;
                        _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                        _this.find('.description')[0].innerHTML = '简介: ' + handle_des(info.description);
                        _this.find('.button')[0].innerHTML = "<a href='read" + info.link + "'>点击阅读</a>";
                    })
                  ;
                })
              ;
          }
      });

      /*获取所有图书的信息并进行渲染*/
      $.get('book/all/1', function(data){
        var res = data.res;
        $('#all_book div.ui.segment div.item')
            .each(function(i){
                var info = JSON.parse(res[i]);
                var _this = $(this);
                if(info.cover == null){
                    info.cover = "https://www.qu.la/BookFiles/BookImages/zhongshengzhiguiwangguilai.jpg";
                }
                if(info.link == null){
                    info.link = "book/";
                }
                if(info.description == null){
                    info.description = "暂无";
                }
                _this.find('img')[0].src = info.cover;
//                _this.find('a')[0].innerHTML = info.name;
                _this.find('a')[0].innerHTML = info.name;
                _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                _this.find('.description')[0].innerHTML = '简介: ' + handle_des(info.description);
                _this.find('.button')[0].innerHTML = "<a href='read" + info.link + "'>点击阅读</a>";
            })
          ;
        })
      ;

      /*获取每种类型图书排名前12的图书的信息并进行渲染*/
      // 提前渲染一开始可见的部分
      $.get('book/order/1', function(data){
        var res = data.res;
        $('#order_book div.ui.segment div.item')
            .each(function(i){
                var info = JSON.parse(res[i]);
                var _this = $(this);
                if(info.cover == null){
                    info.cover = "https://www.qu.la/BookFiles/BookImages/zhongshengzhiguiwangguilai.jpg";
                }
                if(info.link == null){
                    info.link = "book/";
                }
                if(info.description == null){
                    info.description = "暂无";
                }
                _this.find('img')[0].src = info.cover;
                _this.find('a')[0].innerHTML = info.name;
                _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                _this.find('.description')[0].innerHTML = '简介: ' + handle_des(info.description);
                _this.find('.button')[0].innerHTML = "<a href='read" + info.link + "'>点击阅读</a>";
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
                        if(info.cover == null){
                            info.cover = "https://www.qu.la/BookFiles/BookImages/zhongshengzhiguiwangguilai.jpg";
                        }
                        if(info.link == null){
                            info.link = "book/";
                        }
                        if(info.description == null){
                            info.description = "暂无";
                        }
                        _this.find('img')[0].src = info.cover;
        //                _this.find('a')[0].innerHTML = info.name;
                        _this.find('a')[0].innerHTML = info.name;
                        _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                        _this.find('.description')[0].innerHTML = '简介: ' + handle_des(info.description);
                        _this.find('.button')[0].innerHTML = "<a href='read" + info.link + "'>点击阅读</a>";
                    })
                  ;
                })
              ;
          }
        })
      ;

      /*获取完本图书的信息并进行渲染*/
      $.get('book/finished/1', function(data){
        var res = data.res;
        $('#finished_book div.ui.segment div.item')
            .each(function(i){
                var info = JSON.parse(res[i]);
                var _this = $(this);
                if(info.cover == null){
                    info.cover = "https://www.qu.la/BookFiles/BookImages/zhongshengzhiguiwangguilai.jpg";
                }
                if(info.link == null){
                    info.link = "book/";
                }
                if(info.description == null){
                    info.description = "暂无";
                }
                _this.find('img')[0].src = info.cover;
//                _this.find('a')[0].innerHTML = info.name;
                _this.find('a')[0].innerHTML = info.name;
                _this.find('.meta')[0].innerHTML = '作者: ' + info.author;
                _this.find('.description')[0].innerHTML = '简介: ' + handle_des(info.description);
                _this.find('.button')[0].innerHTML = "<a href='read" + info.link + "'>点击阅读</a>";
            })
          ;
        })
      ;
    })
  ;



