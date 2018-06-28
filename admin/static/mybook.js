

  $(document)
    .ready(function() {
        var page = 1;
        var table = $("tbody")[0];

      $.get('book/select/book/'+page, function(data){
                table.innerHTML = "";
                var res = data.res;
                for(var i=0;i<res.length;i++){
                  var info = JSON.parse(res[i]);
                  console.log(info);
                  var _this = $(this);
                  var author=info.author;
                  var id=info.id;
                  var name=info.bookname;
                  var catalog=info.catalog;
                  var current_state=info.current_state;
                  var recent_update_time=info.recent_update_time;
                  var check_state=info.check;
                  if(check_state=="1")
                    var sss="通过";
                  else
                    var sss="不通过"
                 var $tr="<tr>"+"<td>"+id+"</td>"+"<td>"+name+"</td>"+"<td>"+author+"</td>"
                            +"<td>"+catalog+"</td>"+"<td>"+current_state+"</td>"+"<td>"+recent_update_time+"</td>"+"<td>"+sss+"</td>"
                            +"<td>"+"<button type='button' class='ui button' data='" + id +"'>删除</button>"+"</td>"+"</tr>"

                    ///////////////////////////////////////////////////////////////////
                  console.log($tr);
                  table.innerHTML += $tr;
                  ///////////////////////////////////////////////////////////////////
                  $("tbody tr td button.ui.button").on('click',function (){

                        var _this = $(this);
                        console.log(_this);
                        var id = _this.attr('data');
                        console.log(id);

                        var returnval = window.confirm("是否要删除该小说？","标题");
                        if(returnval){
                            $.post('book/delete',{'id': id}, function(data){

                            });
                            console.log(returnval);
                            window.location.reload();
                            }
                    });


        ///////////////////////////////////////////////////////////////////
                }
            });
/////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////
        console.log(table);
        $('#last_page').on('click', function(){
        var _this = $($(this)[0]);
        var page = Number(_this.attr('data'));
        var mark = $('#redirect_page').attr('data');
        if(page == 1)
            return;
        else{
          table.innerHTML = "";
          page = page - 1;
          $('#page_num').val(page);
          _this.attr('data', page);
         $('#next_page').attr('data', page);
                $.get('book/select/book/'+ page, function(data){
                    var res = data.res;
                    for(var i=0;i<res.length;i++){
                      var info = JSON.parse(res[i]);
                      console.log(info);
                      var _this = $(this);
                      var author=info.author;
                      var id=info.id;
                      var name=info.bookname;
                      var catalog=info.catalog;
                      var current_state=info.current_state;
                      var recent_update_time=info.recent_update_time;
                      var check_state=info.check;
                      if(check_state=="1")
                        var sss="通过";
                      else
                        var sss="不通过"
                      var $tr="<tr>"+"<td>"+id+"</td>"+"<td>"+name+"</td>"+"<td>"+author+"</td>"
                            +"<td>"+catalog+"</td>"+"<td>"+current_state+"</td>"+"<td>"+recent_update_time+"</td>"+"<td>"+sss+"</td>"
                            +"<td>"+"<button type='button' class='ui button' data='" + id +"'>删除</button>"+"</td>"+"</tr>"

                        ///////////////////////////////////////////////////////////////////
                      console.log($tr);
                      table.innerHTML += $tr;
                      ///////////////////////////////////////////////////////////////////
                      $("tbody tr td button.ui.button").on('click',function (){

                            var _this = $(this);
                            console.log(_this);
                            var id = _this.attr('data');
                            console.log(id);

                            var returnval = window.confirm("是否要删除该小说？","标题");
                            if(returnval){
                                $.post('book/delete',{'id': id}, function(data){

                                });
                                console.log(returnval);
                                window.location.reload();
                                }
                        });


          ///////////////////////////////////////////////////////////////////
                    }
        });
        }
    });
    ////////////////////////////////////////////////////////////////////
    // 跳转
      $('#redirect_page').on('click', function(){
        var _this = $($(this)[0]);
        var mark = _this.attr('data');
        var page = $('#page_num').val();
        if(page == "" || page < 1){
            return;
        }else{
        table.innerHTML = "";
          _this.attr('data', page);
          if(mark == 'all'){
          $.get('book/select/book/'+page, function(data){
                var res = data.res;
                for(var i=0;i<res.length;i++){
                  var info = JSON.parse(res[i]);
                  console.log(info);
                  var _this = $(this);
                  var author=info.author;
                  var id=info.id;
                  var name=info.bookname;
                  var catalog=info.catalog;
                  var current_state=info.current_state;
                  var recent_update_time=info.recent_update_time;
                  var check_state=info.check;
                  if(check_state=="1")
                    var sss="通过";
                  else
                    var sss="不通过"
                 var $tr="<tr>"+"<td>"+id+"</td>"+"<td>"+name+"</td>"+"<td>"+author+"</td>"
                            +"<td>"+catalog+"</td>"+"<td>"+current_state+"</td>"+"<td>"+recent_update_time+"</td>"+"<td>"+sss+"</td>"
                            +"<td>"+"<button type='button' class='ui button' data='" + id +"'>删除</button>"+"</td>"+"</tr>"

                    ///////////////////////////////////////////////////////////////////
                  console.log($tr);
                  table.innerHTML += $tr;
                  ///////////////////////////////////////////////////////////////////
                  $("tbody tr td button.ui.button").on('click',function (){

                        var _this = $(this);
                        console.log(_this);
                        var id = _this.attr('data');
                        console.log(id);

                        var returnval = window.confirm("是否要删除该小说？","标题");
                        if(returnval){
                            $.post('book/delete',{'id': id}, function(data){

                            });
                            console.log(returnval);
                            window.location.reload();
                            }
                    });


                }
            });
          }
          }
          });
      //////////////////////////////////////////////////////////////////////////////////
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
          $.get('book/select/book/'+page, function(data){
                table.innerHTML = "";
                var res = data.res;
                for(var i=0;i<res.length;i++){
                  var info = JSON.parse(res[i]);
                  console.log(info);
                  var _this = $(this);
                  var author=info.author;
                  var id=info.id;
                  var name=info.bookname;
                  var catalog=info.catalog;
                  var current_state=info.current_state;
                  var recent_update_time=info.recent_update_time;
                  var check_state=info.check;
                  if(check_state=="1")
                    var sss="通过";
                  else
                    var sss="不通过"
                 var $tr="<tr>"+"<td>"+id+"</td>"+"<td>"+name+"</td>"+"<td>"+author+"</td>"
                            +"<td>"+catalog+"</td>"+"<td>"+current_state+"</td>"+"<td>"+recent_update_time+"</td>"+"<td>"+sss+"</td>"
                            +"<td>"+"<button type='button' class='ui button' data='" + id +"'>删除</button>"+"</td>"+"</tr>"

                    ///////////////////////////////////////////////////////////////////
                  console.log($tr);
                  table.innerHTML += $tr;
                  ///////////////////////////////////////////////////////////////////
                  $("tbody tr td button.ui.button").on('click',function (){

                        var _this = $(this);
                        console.log(_this);
                        var id = _this.attr('data');
                        console.log(id);

                        var returnval = window.confirm("是否要删除该小说？","标题");
                        if(returnval){
                            $.post('book/delete',{'id': id}, function(data){

                            });
                            console.log(returnval);
                            window.location.reload();
                            }
                    });


        ///////////////////////////////////////////////////////////////////
                }
            });
            }
           });
        //////////////////////////////////////////////////////////////////////////
//新事件，查询
 $('#Mysearch').on('click', function(){
        var txt=$("#text").val();
        var kind=$('input[name="frequency"]:checked').val();

        if(kind=="id")
        var txt=Number(txt);
        console.log(txt);
        console.log(kind);

        if(kind=="id"){
        $.get('book/select/book/id/'+txt, function(data){
                table.innerHTML = "";
                var res = data.res;
                for(var i=0;i<res.length;i++){
                  var info = JSON.parse(res[i]);
                  console.log(info);
                  var _this = $(this);
                  var author=info.author;
                  var id=info.id;
                  var name=info.bookname;
                  var catalog=info.catalog;
                  var current_state=info.current_state;
                  var recent_update_time=info.recent_update_time;
                  var check_state=info.check;
                  if(check_state=="1")
                    var sss="通过";
                  else
                    var sss="不通过"
                 var $tr="<tr>"+"<td>"+id+"</td>"+"<td>"+name+"</td>"+"<td>"+author+"</td>"
                            +"<td>"+catalog+"</td>"+"<td>"+current_state+"</td>"+"<td>"+recent_update_time+"</td>"+"<td>"+sss+"</td>"
                            +"<td>"+"<button type='button' class='ui button' data='" + id +"'>删除</button>"+"</td>"+"</tr>"
 ///////////////////////////////////////////////////////////////////
                  console.log($tr);
                  table.innerHTML += $tr;
                  ///////////////////////////////////////////////////////////////////
                  $("tbody tr td button.ui.button").on('click',function (){

                        var _this = $(this);
                        console.log(_this);
                        var id = _this.attr('data');
                        console.log(id);

                        var returnval = window.confirm("是否要删除该读者？","标题");
                        if(returnval){
                            $.post('reader/delete',{'id': id}, function(data){

                            });
                            console.log(returnval);
                            window.location.reload();
                            }
                    });
                }
            });
                }


        else if(kind == "author"){
                $.get('book/select/book/author/'+txt, function(data){
                table.innerHTML = "";
                var res = data.res;
                for(var i=0;i<res.length;i++){
                  var info = JSON.parse(res[i]);
                  console.log(info);
                  var _this = $(this);
                  var author=info.author;
                  var id=info.id;
                  var name=info.bookname;
                  var catalog=info.catalog;
                  var current_state=info.current_state;
                  var recent_update_time=info.recent_update_time;
                  var check_state=info.check;
                  if(check_state=="1")
                    var sss="通过";
                  else
                    var sss="不通过"
                 var $tr="<tr>"+"<td>"+id+"</td>"+"<td>"+name+"</td>"+"<td>"+author+"</td>"
                            +"<td>"+catalog+"</td>"+"<td>"+current_state+"</td>"+"<td>"+recent_update_time+"</td>"+"<td>"+sss+"</td>"
                            +"<td>"+"<button type='button' class='ui button' data='" + id +"'>删除</button>"+"</td>"+"</tr>"
///////////////////////////////////////////////////////////////////
                  console.log($tr);
                  table.innerHTML += $tr;
                  ///////////////////////////////////////////////////////////////////
                  $("tbody tr td button.ui.button").on('click',function (){

                        var _this = $(this);
                        console.log(_this);
                        var id = _this.attr('data');
                        console.log(id);

                        var returnval = window.confirm("是否要删除该读者？","标题");
                        if(returnval){
                            $.post('reader/delete',{'id': id}, function(data){

                            });
                            console.log(returnval);
                            window.location.reload();
                            }
                    });
                }
            });
                }
                else
                    $.get('book/select/book/bookname/'+txt, function(data){
                        table.innerHTML = "";
                        var res = data.res;
                        for(var i=0;i<res.length;i++){
                          var info = JSON.parse(res[i]);
                          console.log(info);
                          var _this = $(this);
                          var author=info.author;
                          var id=info.id;
                          var name=info.bookname;
                          var catalog=info.catalog;
                          var current_state=info.current_state;
                          var recent_update_time=info.recent_update_time;
                          var check_state=info.check;
                          if(check_state=="1")
                            var sss="通过";
                          else
                            var sss="不通过"
                         var $tr="<tr>"+"<td>"+id+"</td>"+"<td>"+name+"</td>"+"<td>"+author+"</td>"
                                    +"<td>"+catalog+"</td>"+"<td>"+current_state+"</td>"+"<td>"+recent_update_time+"</td>"+"<td>"+sss+"</td>"
                                    +"<td>"+"<button type='button' class='ui button' data='" + id +"'>删除</button>"+"</td>"+"</tr>"
        ///////////////////////////////////////////////////////////////////
                          console.log($tr);
                          table.innerHTML += $tr;
                          ///////////////////////////////////////////////////////////////////
                          $("tbody tr td button.ui.button").on('click',function (){

                                var _this = $(this);
                                console.log(_this);
                                var id = _this.attr('data');
                                console.log(id);

                                var returnval = window.confirm("是否要删除该读者？","标题");
                                if(returnval){
                                    $.post('reader/delete',{'id': id}, function(data){

                                    });
                                    console.log(returnval);
                                    window.location.reload();
                                    }
                            });
                        }
                    });
        });
 /////////////////////////////////////////////////////////////////////////////////////////////
        $('#book_update').on('click', function(){
                var txt=$("#myupdate").val();
                var id=Number(txt);
                console.log(txt);
                console.log(id);
                $.get('book/select/book/id/'+txt, function(data){
                table.innerHTML = "";
                var res = data.res;
                for(var i=0;i<res.length;i++){
                  var info = JSON.parse(res[i]);
                  console.log(info);
                  var _this = $(this);
                  var author=info.author;
                  var id=info.id;
                  var name=info.bookname;
                  var catalog=info.catalog;
                  var current_state=info.current_state;
                  var recent_update_time=info.recent_update_time;
                  var check_state=info.check;
                  if(check_state=="1")
                    var sss="通过";
                  else
                    var sss="不通过"
                 var $tr="<tr>"+"<td>"+id+"</td>"+"<td>"+name+"</td>"+"<td>"+author+"</td>"
                            +"<td>"+"<input type='text' id = 'newcatalog' value ='"+catalog+"'></input>"+"</td>"
                            +"<td>"+"<input type='text' id = 'newcurrent' value ='"+current_state+"'></input>"+"</td>"
                            +"<td>"+ recent_update_time+ "</td>"+"<td>"+"<input type='text' id = 'newcheck' value ='"+sss+"'></input>"+"</td>"
                            +"<td>"+"<button type='button' class='ui button' data='" + id +"' id = 'sure'>确认</button>"
                            +"<button type='button' class='ui button' data='" + id +"' id = 'undo'>取消</button>"+"</td>"+"</tr>"
 ///////////////////////////////////////////////////////////////////
                  console.log($tr);
                  table.innerHTML += $tr;
                  ///////////////////////////////////////////////////////////////////
                  $("#sure").on('click',function (){

                        var _this = $(this);
                        console.log(_this);
                        var id = _this.attr('data');
                        console.log(id);

                        var catalog=$("#newcatalog").val();
                        var current=$("#newcurrent").val();
                        var new_check=$("#newcheck").val();
                        console.log(catalog);
                        console.log(current);
                        console.log(new_check);

                        if(new_check!="通过")
                        var new_check=0;


                        var returnval = window.confirm("是否要更改该小说？","标题");
                        if(returnval){
                            $.post('book/update',{'id': id,'catalog':catalog,'current':current,'new_check':new_check}, function(data){

                            });
                            console.log(returnval);
                            window.location.reload();
                            }
                    });

                    $("#undo").on('click',function (){
                    console.log("undo");
                    window.location.reload();
                    })

                })
            });

        });
 /////////////////////////////////////////////////////////////////////////////////////////////////////////////
    })