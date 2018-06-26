

  $(document)
    .ready(function() {
        var table = $("tbody")[0];
        console.log(table);
        $.get('select/book', function(data){
            var res = data.res;
            for(var i=0;i<res.length;i++){
              var info = JSON.parse(res[i]);
              console.log(info);
              var _this = $(this);
              var author=info.author;
              var name=info.bookname;
              var $tr="<tr>"+"<td>"+author+"</td>"+"<td>"+"</td>"+"<td>"+"</td>"
                    +"<td>"+"</td>"+"<td>"+"</td>"+"<td>"+"</td>"+"<td>"+"</td>"+"</tr>"
              console.log($tr);
              table.innerHTML += $tr;
            }
//            _this.find('.button')[0].innerHTML = "<a href='" + info.link + "'>点击阅读</a>";
        })
      ;
    })