var nameFilter = document.getElementById("name-filter");
// Get the stocks list
var stocksList = document.getElementsByClassName("stocks-list")[0];
// Add event listener to handle name filtering
nameFilter.addEventListener("input", function() {
    var filterValue = nameFilter.value.toLowerCase();
    var stocks = stocksList.getElementsByTagName("li");
    // Loop through each stock and hide/show based on the filter value
    for (var i = 0; i < stocks.length; i++) {
        var stockName = stocks[i].querySelector(".stock-name").textContent.toLowerCase();
        if (stockName.includes(filterValue)) {
            stocks[i].style.display = "block";
        } else {
            stocks[i].style.display = "none";
        }
    }
});