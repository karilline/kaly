<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            padding: 0px;
            margin: 0px;
            background: cornsilk;
        }
        #all{
            height: 400px;
        }
        /* div position脱离文档流，给父亲div设置高度 */
        #container{
            position: relative;
            top: 20px;
            left: 600px;
        }
        table{
            border: 2px solid red;
            color: blueviolet;
            text-align: center;
        }
        .button{
            float: left;
           
        }
        #beginButton,#stopButton{
            width: 100px;
        }
        .clear{
            clear: both;
        }
    </style>
</head>
<body>
    <!-- 所有名字 -->
    <div id="all">
        <div id="container">
            <table>
            
            </table>
        </div>
    </div>
        
    <!-- 开始按钮 -->
    <div class="button">
        <input type="submit" id="beginButton" value="开始" onclick="begin()">
    </div>
    <!-- 关闭按钮 -->
    <div class="button" id="stopDiv">
        <input type="submit" id="stopButton" value="停止" onclick="stop()">
    </div>
    <!-- 显示名字 -->
    <div class="clear"></div>
    <hr>
    <span style="color: darkturquoise; font-size: x-large;">抽到的学生名字为:</span>
    <h1 id="sign"></h1>
    
    <script>
    // ========================================================== 
        var names = ["谢霆锋","张柏芝","李希","黄晓明","杨颖","杨幂","张靓颖","黄子韬","张艺兴","吴希凡",
                     "唐僧","猪八戒","如来","观音","白骨精","白龙马","刘备","关羽","张飞","我","你"];
        var table = document.getElementsByTagName("table")[0];
        var tr;
        var td;
        for(var i = 0; i < names.length; i++){
            if(i%5==0){
                tr = document.createElement("tr");
                table.append(tr);
            }
            td = document.createElement("td");
            td.innerHTML = "<span class='stu'>"+names[i]+"</span>";
            tr.append(td);
        }
        var tds = document.getElementsByTagName("td");
        for(var j = 0; j<names.length; j++){
            tds[j].style.border="1px solid red";
            tds[j].style.padding="10px";
        }
// =================================================================
        var tdName;
        var spans = document.getElementsByClassName("stu");
        var sign = document.getElementById("sign");
        //随机获取索引值
        var index = 0;
        var stopDiv = document.getElementById("stopDiv");
        var mySelect;
        var flag = false;
        //开始按钮
        function begin(){
            sign.innerHTML = null;
            mySelect = setInterval(function(){
            index = Math.floor(Math.random()*names.length);
            tdName = spans[index].parentNode;
            tdName.style.background = "green";
            setTimeout(function(){
                tdName.style.background = "";
            },50);
          },60);
       }
       //停止按钮
       function stop(){
        clearInterval(mySelect);
        //显示名字
        sign.innerHTML=names[index];
        sign.style.color="red";
       }
    </script>
</body>
</html>
