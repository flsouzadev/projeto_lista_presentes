function limitCheckboxSelection() {
    var checkboxes = document.querySelectorAll('input[type="radio"]');
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            checkboxes.forEach(function(cb) {
                if (cb.name !== checkbox.name) {
                    cb.checked = false;
                }
            });
        });
    });
}
window.addEventListener('load', limitCheckboxSelection);