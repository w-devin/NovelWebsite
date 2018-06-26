/*
    include the necessary tools function to handle str etc.
*/


// 计算字符串长度
function strlen(str){
    var len = 0;
    for (var i=0; i<str.length; i++) {
     var c = str.charCodeAt(i);
    //单字节加1
     if ((c >= 0x0001 && c <= 0x007e) || (0xff60<=c && c<=0xff9f)) {
       len++;
     }
     else {
      len+=2;
     }
    }
    return len;
}

// 处理书籍的description, 将过长的信息截取并添加省略号
function handle_des(des){
    ws = "                    ";
    if(strlen(des) > 10){
        des = des.substring(0, 20) + "......";
    }else{
        des = des + ws;
        des = des.substring(0, 20) + "......";
    }
    return des;
}
//
//// 处理书籍的name, 将较短的信息添加一行
//function handle_name(name){
//    ws = "         ";
//    if(name.length < 10){
//        name = name + ws;
//        name = name.substring(0, 20);
//    }
//    return name;
//}