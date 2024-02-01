//WRITE YOUR jQUERY CODE HERE
$(".add-row").click(function(){
    var name=$("#name").val();
    var data="<tr><td><input type='checkbox' name='record'></td><td>"+name+"</td></tr>";
   if (name!==""){
       $("table tbody").append(data);
       $("#name").val("");
    }
 });
 
 $(".delete-row").click(function(){
     $("table tbody input[name='record']:checked").parents("tr").remove();
 });
 