

  $(document)
    .ready(function() {
        $.get('/select/book', function(data){
                var res = data.res;
                for(var i=0;i<res.length;i++)
                {
                var info = JSON.parse(res[i]);
                var _this = $(this);

                var $table = $("ui celled table")
                $("#ui celled table  tr:not(:first)").html("");
                    var id=info.id;
                    var name=info.name;
                    var $tr=$("<tr>"+"<td>"+id+"</td>"+"<td>"+"</td>"+"<td>"+"</td>"
                    +"<td>"+"</td>"+"<td>"+"</td>"+"<td>"+"</td>"+"<td>"+"</td>"+"</tr>")
                    $table.append($tr);
                   }
                _this.find('.button')[0].innerHTML = "<a href='" + info.link + "'>点击阅读</a>";
            })
          ;
        })
      ;


    })