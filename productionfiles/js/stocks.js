var nameFilter = document.getElementById("name-filter");
var priceFilter = document.getElementById("price-filter");
var typeFilter = document.getElementById("type-filter");
var sizeFilter = document.getElementById("size-filter");
var fabricFilter = document.getElementById("fabric-filter");
var stocks = document.querySelectorAll(".stock-detail");

function applyFilters() {
    var nameValue = nameFilter.value.toLowerCase();
    var priceValue = parseFloat(priceFilter.value);
    var typeValue = typeFilter.value.toLowerCase();
    var sizeValue = sizeFilter.value.toLowerCase();
    var fabricValue = fabricFilter.value.toLowerCase();

    stocks.forEach(function(stock) {
        var stockName = stock.querySelector(".product-title").textContent.toLowerCase();
        var stockPrice = parseFloat(stock.querySelector(".product-price").textContent.replace("$", ""));
        var stockType = stock.querySelector(".product-type").textContent.toLowerCase();
        var stockSize = stock.querySelector(".product-size").textContent.toLowerCase();
        var stockFabric = stock.querySelector(".product-fabric").textContent.toLowerCase();

        var nameMatch = stockName.includes(nameValue);
        var priceMatch = isNaN(priceValue) || stockPrice <= priceValue;
        var typeMatch = typeValue === "" || stockType.includes(typeValue);
        var sizeMatch = sizeValue === "" || stockSize.includes(sizeValue);
        var fabricMatch = fabricValue === "" || stockFabric.includes(fabricValue);

        if (nameMatch && priceMatch && typeMatch && sizeMatch && fabricMatch) {
            stock.style.display = "block";
        } else {
            stock.style.display = "none";
        }
    });
}

nameFilter.addEventListener("input", applyFilters);
priceFilter.addEventListener("input", applyFilters);
typeFilter.addEventListener("change", applyFilters);
sizeFilter.addEventListener("change", applyFilters);
fabricFilter.addEventListener("change", applyFilters);