// products/js/product_detail.js

document.addEventListener('DOMContentLoaded', function () {
    const sizeDropdown = document.getElementById('id_product_size');
    const stockDisplay = document.getElementById('stock-display');
    const stockList = document.getElementById('stock-list');

    if (sizeDropdown) {
        // Trigger stock display update for default size
        updateStockDisplay();

        sizeDropdown.addEventListener('change', updateStockDisplay);

        // Function to update stock display based on the selected size
        function updateStockDisplay() {
            const selectedSize = sizeDropdown.value;
            const stockItems = stockList.querySelectorAll('li');
            let stockLevel = 0;

            if (!selectedSize) {
                stockDisplay.textContent = "Select a size to view stock status.";
                return;
            }

            
            stockItems.forEach(item => {
                const size = item.getAttribute('data-size');
                const stock = item.getAttribute('data-stock');
                if (size === selectedSize) {
                    stockLevel = stock;
                }
            });

            // Display the stock level
            if (stockLevel > 0) {
                stockDisplay.textContent = `Stock for ${selectedSize}: ${stockLevel} items available`;
            } else {
                stockDisplay.textContent = `Sorry, the ${selectedSize} size is out of stock.`;
            }
        }

        // Initial call to update the stock display when the page loads
        updateStockDisplay();
    }
});
