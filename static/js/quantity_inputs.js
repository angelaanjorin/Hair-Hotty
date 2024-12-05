document.addEventListener('DOMContentLoaded', function () {
    const sizeDropdown = document.getElementById('id_product_size');
    const quantityInputs = document.querySelectorAll('.qty_input');
    
    // Functionality for Product Detail Page (includes size dropdown)
    if (sizeDropdown) {
        sizeDropdown.addEventListener('change', updateStockDisplay);

        function updateStockDisplay() {
            const stockList = document.querySelectorAll('#stock-list li');
            const stockDisplay = document.getElementById('stock-display');
            const addToBagButton = document.querySelector('input[type="submit"]');

            let stockAmount = 0;
            let sizeSelected = false;
            stockList.forEach(item => {
                if (item.getAttribute('data-size') === sizeDropdown.value) {
                    stockAmount = parseInt(item.getAttribute('data-stock'), 10);
                    sizeSelected = true;

                    if (stockAmount > 0) {
                        stockDisplay.innerHTML = `IN STOCK: ${stockAmount}`;
                        addToBagButton.disabled = false;
                    } else {
                        stockDisplay.innerHTML = `OUT OF STOCK`;
                        addToBagButton.disabled = true;
                    }
                }
            });

            if (!sizeSelected) {
                stockDisplay.innerHTML = `Select a size to view stock.`;
            }
        }

        updateStockDisplay(); // Call once on load
    }

    // Functionality for both Product Detail and Bag Pages (quantity inputs)
    quantityInputs.forEach(input => {
        const itemId = input.dataset.item_id;
        const size = input.dataset.size;
        
        // Handle enabling/disabling the increment and decrement buttons
        function handleEnableDisable() {
            const decrementButton = document.querySelector(`.decrement-qty_${itemId}`);
            const incrementButton = document.querySelector(`.increment-qty_${itemId}`);
            const currentValue = parseInt(input.value);

            // Disable buttons if quantity is at min or max
            decrementButton.disabled = currentValue <= 1;
            incrementButton.disabled = currentValue >= 99; // Assuming max quantity is 99
        }

        // Attach event listeners to the quantity input and buttons
        input.addEventListener('input', () => {
            handleEnableDisable();
        });

        document.querySelector(`.decrement-qty_${itemId}`).addEventListener('click', e => {
            e.preventDefault();
            if (input.value > 1) input.value--;
            handleEnableDisable();
        });

        document.querySelector(`.increment-qty_${itemId}`).addEventListener('click', e => {
            e.preventDefault();
            if (input.value < 99) input.value++;
            handleEnableDisable();
        });

        // Initial check to disable buttons as necessary
        handleEnableDisable();
    });
});
