function updateStockDisplay() {
    const sizeDropdown = document.getElementById('id_product_size');
    const stockList = document.querySelectorAll('#stock-list li');
    const stockDisplay = document.getElementById('stock-display');
    const addToBagButton = document.querySelector('input[type="submit"]');
    const bagQuantity = parseInt(document.getElementById('id_quantity').value) || 0;

    let sizeSelected = false;

    stockList.forEach(item => {
        const size = item.getAttribute('data-size');
        const stock = parseInt(item.getAttribute('data-stock'), 10);

        if (sizeDropdown && sizeDropdown.value === size) {
            sizeSelected = true;
            const virtualStock = stock - bagQuantity;

            if (virtualStock > 0) {
                stockDisplay.innerHTML = `<span class="in-stock-label text-dark">IN STOCK: ${virtualStock}</span>`;
                addToBagButton.disabled = false;
            } else {
                stockDisplay.innerHTML = `<span class="out-of-stock-label text-dark">OUT OF STOCK</span>`;
                addToBagButton.disabled = true;
            }
        }
    });

    if (!sizeSelected) {
        stockDisplay.innerHTML = `<span class="text-muted">Select a size to view stock.</span>`;
    }
}
