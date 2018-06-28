

  $(document)
    .ready(function() {
        var page = 1;
        var table = $("tbody")[0];


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
                $.get('author/select/author/'+ page, function(data){
                    var res = data.res;
                    for(var i=0;i<res.length;i++){
                      var info = JSON.parse(res[i]);
                      console.log(info);
                      var _this = $(this);
                      var authorname=info.authorname;
                      var id=info.id;
                      var nickname=info.nick_name;
                      var pass=info.authorpass;
                      var des=info.description;
                      var authorclass=info.author_class;
                      var check_state=info.check;
                      if(check_state=="1")
                        var sss="通过";
                      else
                        var sss="不通过"
                      var $tr="<tr>"+"<td>"+id+"</td>"+"<td>"+authorname+"</td>"+"<td>"+nickname+"</td>"
                        +"<td>"+pass+"</td>"+"<td>"+des+"</td>"+"<td>"+authorclass+"</td>"+"<td>"+sss+"</td>"
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

                            var returnval = window.confirm("是否要删除该作者？","标题");
                            if(returnval){
                                $.post('author/delete',{'id': id}, function(data){

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

                $.get('author/select/author/'+ page, function(data){
                    var res = data.res;
                    for(var i=0;i<res.length;i++){
                      var info = JSON.parse(res[i]);
                      console.log(info);
                      var _this = $(this);
                      var authorname=info.authorname;
                      var id=info.id;
                      var nickname=info.nick_name;
                      var pass=info.authorpass;
                      var des=info.description;
                      var authorclass=info.author_class;
                      var check_state=info.check;
                      if(check_state=="1")
                        var sss="通过";
                      else
                        var sss="不通过"
                      var $tr="<tr>"+"<td>"+id+"</td>"+"<td>"+authorname+"</td>"+"<td>"+nickname+"</td>"
                        +"<td>"+pass+"</td>"+"<td>"+des+"</td>"+"<td>"+authorclass+"</td>"+"<td>"+sss+"</td>"
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

                            var returnval = window.confirm("是否要删除该作者？","标题");
                            if(returnval){
                                $.post('author/delete',{'id': id}, function(data){

                                });
                                console.log(returnval);
                                window.location.reload();
                                }
                        });

                        ///////////////////////////////////////////////////////////////////////
                         $("tbody tr td button.update").on('click',function (){

                          var _this = $(this);
                          console.log(_this);
                          var myid = _this.attr('data');

                          console.log(myid);

                        });
          ///////////////////////////////////////////////////////////////////
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
        table.innerHTML = "";
          page = page + 1;
          $('#page_num').val(page);
          _this.attr('data', page);
          $('#last_page').attr('data', page);

                $.get('author/select/author/'+ page, function(data){
                    var res = data.res;
                    for(var i=0;i<res.length;i++){
                      var info = JSON.parse(res[i]);
                      console.log(info);
                      var _this = $(this);
                      var authorname=info.authorname;
                      var id=info.id;
                      var nickname=info.nick_name;
                      var pass=info.authorpass;
                      var des=info.description;
                      var authorclass=info.author_class;
                      var check_state=info.check;
                      if(check_state=="1")
                        var sss="通过";
                      else
                        var sss="不通过"
                      var $tr="<tr>"+"<td>"+id+"</td>"+"<td>"+authorname+"</td>"+"<td>"+nickname+"</td>"
                        +"<td>"+pass+"</td>"+"<td>"+des+"</td>"+"<td>"+authorclass+"</td>"+"<td>"+sss+"</td>"
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

                            var returnval = window.confirm("是否要删除该作者？","标题");
                            if(returnval){
                                $.post('author/delete',{'id': id}, function(data){

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

      $.get('author/select/author/'+ page, function(data){
            table.innerHTML = "";
                var res = data.res;
                for(var i=0;i<res.length;i++){
                  var info = JSON.parse(res[i]);
                  console.log(info);
                  var _this = $(this);
                  var authorname=info.authorname;
                  var id=info.id;
                  var nickname=info.nick_name;
                  var pass=info.authorpass;
                  var des=info.description;
                  var authorclass=info.author_class;
                  var check_state=info.check;
                  if(check_state=="1")
                    var sss="通过";
                  else
                    var sss="不通过"
                  var $tr="<tr>"+"<td>"+id+"</td>"+"<td>"+authorname+"</td>"+"<td>"+nickname+"</td>"
                        +"<td>"+pass+"</td>"+"<td>"+des+"</td>"+"<td>"+authorclass+"</td>"+"<td>"+sss+"</td>"
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

                        var returnval = window.confirm("是否要删除该作者？","标题");
                        if(returnval){
                            $.post('author/delete',{'id': id}, function(data){

                            });
                            console.log(returnval);
                            window.location.reload();
                            }
                    });


      ///////////////////////////////////////////////////////////////////
                }
    });
 /////////////////////////////////////////////////////////////////////////////////////////////////////////////
 //新事件，查询
 $('#Mysearch').on('click', function(){
        var txt=$("#text").val();
        var kind=$('input[name="frequency"]:checked').val();

        if(kind=="id")
        var txt=Number(txt);
        console.log(txt);
        console.log(kind);

        if(kind=="id"){
        $.get('select/author/id/'+txt, function(data){
                table.innerHTML = "";
                var res = data.res;
                for(var i=0;i<res.length;i++){
                  var info = JSON.parse(res[i]);
                  console.log(info);
                  var _this = $(this);
                  var authorname=info.authorname;
                  var id=info.id;
                  var nickname=info.nick_name;
                  var pass=info.authorpass;
                  var des=info.description;
                  var authorclass=info.author_class;
                  var check_state=info.check;
                  if(check_state=="1")
                    var sss="通过";
                  else
                    var sss="不通过"
                  var $tr="<tr>"+"<td>"+id+"</td>"+"<td>"+authorname+"</td>"+"<td>"+nickname+"</td>"
                        +"<td>"+pass+"</td>"+"<td>"+des+"</td>"+"<td>"+authorclass+"</td>"+"<td>"+sss+"</td>"
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

                        var returnval = window.confirm("是否要删除该作者？","标题");
                        if(returnval){
                            $.post('author/delete',{'id': id}, function(data){

                            });
                            console.log(returnval);
                            window.location.reload();
                            }
                    });
      ///////////////////////////////////////////////////////////////////
                }
        });
        }
        else{
                $.get('select/author/author/'+txt, function(data){
                table.innerHTML = "";
                var res = data.res;
                for(var i=0;i<res.length;i++){
                  var info = JSON.parse(res[i]);
                  console.log(info);
                  var _this = $(this);
                  var authorname=info.authorname;
                  var id=info.id;
                  var nickname=info.nick_name;
                  var pass=info.authorpass;
                  var des=info.description;
                  var authorclass=info.author_class;
                  var check_state=info.check;
                  if(check_state=="1")
                    var sss="通过";
                  else
                    var sss="不通过"
                  var $tr="<tr>"+"<td>"+id+"</td>"+"<td>"+authorname+"</td>"+"<td>"+nickname+"</td>"
                        +"<td>"+pass+"</td>"+"<td>"+des+"</td>"+"<td>"+authorclass+"</td>"+"<td>"+sss+"</td>"
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

                        var returnval = window.confirm("是否要删除该作者？","标题");
                        if(returnval){
                            $.post('author/delete',{'id': id}, function(data){

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
 ////////////////////////////////////////////////////////////////////////////////////////////
    })