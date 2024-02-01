
$("button").click(function() {
    // WRITE YOUR jQuery CODE HERE
    function calculateTotal(){
        var total=0;
        $("#example tbody tr").each(function(){
            var salary=parseFloat($(this).find("td:nth-child(6)").text());
            total+=isNaN(salary)?0:salary;
        });
        $("#para1").text("Total Salary Paid: Rs. "+total);
    }
    calculateTotal();
});