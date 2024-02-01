function show_value(x) {
    document.getElementById("demo").innerHTML = x;
}

function costCalculation() {
    // fill javascript code here - do not use let keyword for variable initialization; instead use var.
    var noOfTickets = parseInt(document.getElementById("noOfTickets").value);
    var ticketType = document.getElementById("ticketType").value;
    var couponCode = document.getElementById("couponCode").checked;
    var refreshment = document.getElementById("refreshment").checked;
    var basePrice = (ticketType === "Floor") ? 400 : 500;
    var total = noOfTickets * basePrice;
    var discount = 0;

    if (noOfTickets > 20) {
        total *= 0.9;
    }

    if (couponCode) {
        discount = noOfTickets * basePrice * 0.02;
        total -= discount;
    }

    if (refreshment) {
        total += 100;
    }

    total = Math.round(total);
    document.getElementById("result").innerHTML = "Your ticket charge is Rs. " + total;
    return false;
}