$('#sort-selector').change(function () {
    let selector = $(this);
    let currentUrl = new URL(window.location);
    let selectedValue = selector.val();

    console.log('Selected Value:', selectedValue);
    console.log('Current URL:', currentUrl);

    if (selectedValue != 'reset') {
        let filterParam = selectedValue.split('_');

        console.log('Filter Params:', filterParam);

        currentUrl.searchParams.set('sort', filterParam[0]);
        currentUrl.searchParams.set('direction', filterParam[1]);
        window.location.href = currentUrl; // Use href instead of replace for back navigation
    } else {
        currentUrl.searchParams.delete('sort');
        currentUrl.searchParams.delete('direction');
        window.location.href = currentUrl; // Redirect after removing params
    }
});
