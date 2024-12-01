document.addEventListener('DOMContentLoaded', function () {
    // Define the updateStockDisplay function here
    function updateStockDisplay() {
        const selectedSize = document.getElementById('id_product_size').value;
        const stockList = document.querySelectorAll('#stock-list li');
        const stockDisplay = document.getElementById('stock-display');
        const addToBagButton = document.querySelector('input[type="submit"]');

        let stockAmount = 0;
        let sizeSelected = false;

        stockList.forEach(item => {
            const size = item.getAttribute('data-size');
            const stock = item.getAttribute('data-stock');

            if (size === selectedSize) {
                stockAmount = parseInt(stock, 10);
                sizeSelected = true;

                if (stockAmount > 0) {
                    stockDisplay.innerHTML = `<span class="text-white">In Stock: ${stockAmount}</span>`;
                    addToBagButton.disabled = false;  // Enable the button
                    addToBagButton.classList.remove("btn-not-allowed");
                    addToBagButton.classList.add("btn-cordovan");  // Change button color to cordovan
                } else {
                    stockDisplay.innerHTML = `<span class="text-white">Out of Stock</span>`;
                    addToBagButton.disabled = true;   // Disable the button
                    addToBagButton.classList.remove("btn-cordovan");
                    addToBagButton.classList.add("btn-not-allowed");  // Revert button color to disabled state
                }
            }
        });

        // If no size is selected, show the "Select a size" message
        if (!sizeSelected) {
            stockDisplay.innerHTML = `<span class="text-muted">Select a size to view stock.</span>`;
        }
    }

    // Attach the function to the 'onchange' event of the size dropdown
    const sizeDropdown = document.getElementById('id_product_size');
    if (sizeDropdown) {
        sizeDropdown.addEventListener('change', updateStockDisplay);
    }

    // Call the function once on page load to handle initial stock display
    updateStockDisplay();
});
